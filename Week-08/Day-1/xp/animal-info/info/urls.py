from django.urls import path
from . import views

urlpatterns = [
    path('family/<int:fam_id>', views.family, name='family')
    path('family/<int:animal_id>', views.animal, name='animal')

    # path('', views.homepage),
    # path('', views.animal_page),
]