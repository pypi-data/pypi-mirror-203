from typing import List, Optional, Sequence, Set

from django.db import models
from px_pipeline import StraightPipeline

from ..models import Notification, NotificationQuerySet, Stats
from ..signals import (
    notifications_flags_changed, notifications_updated, notifications_cleared,
    stats_updated,
)
from ..utils import model_bulk_update_or_create, to_intarray, ModelDef
from ..conf import settings


__all__ = 'change_flags', 'collect_stats', 'clear',


def set_readability_flags_operation(context):
    # FIXME: Nothing works here.
    default_state = Notification.Readability.UNREAD
    states = set(x for x in Notification.Readability)
    added = context['specify'] or context['add']
    to_remove = states - added

    for notification in context['instances']:
        temporary = set(notification.flags) - set(to_remove)

        if len(temporary & states) == 0:
            temporary = [default_state]

        notification.flags = list(temporary)


def _specify_flags(queryset, flags: Set[int]) -> List[Notification]:
    flags = set(flags)
    queryset = queryset.exclude(flags=to_intarray(flags))
    instances: List[Notification] = list(queryset)

    for notification in instances:
        notification.flags = list(flags)

    return instances


def _modify_flags(
    queryset,
    add: Set[int] = set(),
    remove: Set[int] = set()
) -> List[Notification]:
    q = models.Q()

    if len(add) > 0:
        q |= ~models.Q(flags__contains=to_intarray(add))

    if len(remove) > 0:
        q |= models.Q(flags__contains=to_intarray(remove))

    queryset = queryset.filter(q)
    instances: List[Notification] = list(queryset)

    for notification in instances:
        notification.flags = list(
            (set(notification.flags) - remove) | add
        )

    return instances


def change_flags(
    queryset,
    /,
    add: Sequence[int] = [],
    remove: Sequence[int] = [],
    specify: Sequence[int] = [],
) -> List[Notification]:
    assert not (len(add) == 0 and len(remove) == 0 and len(specify) == 0), (
        'Do something. Do not run this with all lists empty.'
    )
    assert not (len(specify) > 0 and (len(add) > 0 or len(remove) > 0)), (
        'Specify parameter overrides any `add` or `remove` actions.'
    )

    instances = []
    add_set = set(add)
    remove_set = set(remove)
    specify_set = set(specify)

    if len(specify) != 0:
        instances = _specify_flags(queryset, flags=specify_set)
    else:
        instances = _modify_flags(queryset, add=add_set, remove=remove_set)

    prepared = StraightPipeline(settings.CHANGE_FLAG_PIPELINE)({
        'instances': instances,
        'add': add_set, 'remove': remove_set, 'specify': specify_set,
        'update_fields': ['flags'],
    })
    instances = prepared['instances']
    update_fields = prepared['update_fields']

    Notification.objects.bulk_update(instances, fields=update_fields)

    notifications_flags_changed.send(
        Notification, instances=instances, add=add_set, remove=remove_set,
        specify=specify_set,
    )
    notifications_updated.send(
        Notification, instances=instances, updated_fields=update_fields,
    )

    return instances


def collect_stats(recipients: Optional[Sequence[ModelDef]]) -> List[Stats]:
    qs: NotificationQuerySet = Notification.objects.all()

    if recipients is not None:
        assert len(recipients) != 0, (
            'Cant collect statistics for empty recipients list.'
        )
        qs = qs.recipients(recipients)

    flag_stats = qs.collect_flag_stats()
    total_stats = qs.collect_total_stats()

    instances = model_bulk_update_or_create(Stats, [
        (
            {
                'recipient_content_type': stat['recipient'][0],
                'recipient_object_id': stat['recipient'][1],
            },
            {
                'flags': stat['stats'],
                'total': total_stats[stat['recipient']],
            }
        )
        for stat in flag_stats
    ])

    stats_updated.send(Stats, instances=instances)

    return instances


def clear(queryset) -> int:
    instances: List[Notification] = list(queryset)
    # FIXME: Change this to be shure that we're deleting only notifications
    # That received previously.
    deleted, _ = queryset.delete()

    notifications_cleared.send(Notification, instances=instances)

    return deleted
