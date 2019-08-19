from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^gym_app$', views.gym_app, name='gym_app'),
	url(r'^includes/new_workout$', views.new_workout, name='new_workout'),
	url(r'^gym_app_done$', views.gym_app_done, name='gym_app_done'),
	url(r'^workout_stats$', views.gym_app_stats, name='workout_stats')
]
