from django.urls import path

from .views import QueryCourseView, StudentGroupView, GroupView, CourseView , CourseDetailView , GroupDetailView

urlpatterns = [
	path("course/",CourseView.as_view()),
	path("studentgroup/",StudentGroupView.as_view()),
	path("group/",GroupView.as_view()),
	path("querycourse/",QueryCourseView.as_view()),
	path("course/<uuid:pk>/",CourseDetailView.as_view()),
	path("group/<int:pk>/",GroupDetailView.as_view()),
]