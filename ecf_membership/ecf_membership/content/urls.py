from django.urls import path
from django.urls.resolvers import URLPattern
from .views import CourseDetailView, CourseListView, VideoDetailView


app_name = "content"


urlpatterns = [
    path("", CourseListView.as_view(), name='course-list'),
    path("<slug>", CourseDetailView.as_view(), name='course-detail'),
    path("<slug>/<video_slug>", VideoDetailView.as_view(), name='video-detail'),
]