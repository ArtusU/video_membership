from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from .models import Course

'''
class CoursePermisionMixin:
    def dispatch(self, request, *args, **kwargs):
        course = get_object_or_404(Course, slug=self.kwargs['slug'])
        subscription = request.user.subscription
        pricing_tier = subscription.pricing
        if not pricing_tier in course.pricing_tiers.all():
            messages.info(request, 'You don not have access to this course.')
            return redirect("content:course-list")
        return super().dispatch(request, *args, **kwargs)
        '''