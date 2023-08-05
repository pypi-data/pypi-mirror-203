from django.urls import path, include

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.pagination import LimitOffsetPagination
from django_filters import rest_framework as filters

from wcd_notifications.models import Notification, Stats
from wcd_notifications.utils import resolve_recipients

from .filters import NotificationsFilterSet
from .serializers import (
    FlagReadSerializer,
    NotificationReadSerializer, NotificationChangeFlagSerializer,
    NotificationClearSerializer,
    StatsReadSerializer,
)


__all__ = (
    'FlagsList',
    'NotificationsList', 'NotificationsChangeFlags',
    'StatsList',
    'flags_list_view',
    'notifications_list_view', 'notifications_change_flags_view',
    'stats_list_view',
    'make_urlpatterns',
)


class ActionApiView(GenericAPIView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_action(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_action(self, serializer):
        serializer.commit()


class RecipientsResolverMixin:
    def get_recipients(self):
        return resolve_recipients(self.request, view=self)

    def get_queryset(self):
        recipients = self.get_recipients()
        qs = super().get_queryset()

        if len(recipients) == 0:
            return qs.none()

        return qs.recipients(recipients)


class NotificationsMixin(RecipientsResolverMixin):
    queryset = (
        Notification.objects
        .select_related(
            'recipient_content_type', 'actor_content_type',
            'action_content_type', 'target_content_type',
        )
        .prefetch_related('recipient', 'actor', 'action', 'target')
    )
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = NotificationsFilterSet


class FlagsList(ListAPIView):
    serializer_class = FlagReadSerializer
    flags_registry = property(lambda self: Notification.flags_registry)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.flags_registry.values(), many=True)
        return Response(serializer.data)


class NotificationsList(NotificationsMixin, ListAPIView):
    serializer_class = NotificationReadSerializer
    pagination_class = LimitOffsetPagination


class NotificationsClear(NotificationsMixin, ActionApiView):
    serializer_class = NotificationClearSerializer

    def perform_action(self, serializer):
        queryset = self.filter_queryset(self.get_queryset())
        serializer.commit(queryset)


class NotificationsChangeFlags(NotificationsMixin, ActionApiView):
    serializer_class = NotificationChangeFlagSerializer

    def perform_action(self, serializer):
        queryset = self.filter_queryset(self.get_queryset())
        serializer.commit(queryset)


class StatsList(RecipientsResolverMixin, ListAPIView):
    serializer_class = StatsReadSerializer
    queryset = Stats.objects.all().prefetch_related('recipient')


flags_list_view = FlagsList.as_view()
notifications_list_view = NotificationsList.as_view()
notifications_change_flags_view = NotificationsChangeFlags.as_view()
notifications_clear_view = NotificationsClear.as_view()
stats_list_view = StatsList.as_view()
app_name = 'wcd_notifications'


def make_urlpatterns(
    flags_list_view=flags_list_view,
    notifications_list_view=notifications_list_view,
    notifications_change_flags_view=notifications_change_flags_view,
    notifications_clear_view=notifications_clear_view,
    stats_list_view=stats_list_view,
):
    return [
        path('flags/', include(([
            path('list/', flags_list_view, name='list'),
        ], app_name), namespace='flags')),
        path('notifications/', include(([
            path('list/', notifications_list_view, name='list'),
            path('change-flags/', notifications_change_flags_view, name='change-flags'),
            path('clear/', notifications_clear_view, name='clear'),
            path('stats/', stats_list_view, name='stats'),
        ], app_name), namespace='notifications')),
    ]
