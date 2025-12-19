
"""
Octofit Tracker URL Configuration

REST API endpoints are available at:
    https://$CODESPACE_NAME-8000.app.github.dev/api/[component]/
where $CODESPACE_NAME is the environment variable for your codespace name.
Example: https://$CODESPACE_NAME-8000.app.github.dev/api/activities/

Do not hardcode $CODESPACE_NAME. Django will serve endpoints at /api/[component]/, and your codespace URL will route requests correctly.
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet, api_root

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root, name='api-root'),
    path('api/', include(router.urls)),  # All API endpoints are under /api/
]
