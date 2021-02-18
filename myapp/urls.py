from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('role',views.RoleView)
router.register('user',views.UserView)


urlpatterns=[
    path('', include(router.urls)),
    # path('role/', views.RoleView.as_view({'post':'create'}), name="role"),


]