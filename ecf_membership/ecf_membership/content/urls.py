from django.urls import path
from django.urls.resolvers import URLPattern
from .views import CourseDetailView, CourseListView


app_name = "content"


urlpatterns = [
    path("", CourseListView.as_view(), name='course-list'),
    path("<slug>", CourseDetailView.as_view(), name='course-detail')
]