from django.urls import path, include
from . import views
from .views import Students, StudentMarks
from rest_framework.routers import DefaultRouter,SimpleRouter

# urlpatterns = [
#     path('student/', Students.as_view()),
#     path('marks/', StudentMarks.as_view()),
# ]
router = DefaultRouter()
router.register("studentapi", views.Students, basename="student")
router.register("marksapi", views.StudentMarks, basename="student")
urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls))
]
