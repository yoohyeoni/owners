from django.urls import path

from .views import Ownersview, Dogsview

urlpatterns = [
	path('', Ownersview.as_view()),
	path('/dogs', Dogsview.as_view()),
]