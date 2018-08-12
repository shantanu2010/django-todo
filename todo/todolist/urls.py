from django.contrib import admin
from django.urls import path
from todolist.rest_views import *
from todolist.views import *

urlpatterns = [

    path('admin/',admin.site.urls),
    path('signup/',renderForm.as_view(),name="signup"),
    path('logout/',logout_user, name="logout"),
    path('login/',renderLogin.as_view(),name="login"),
    path('cards/',CreditListView.as_view(),name="cards"),
    path('cards/add/',AddCardView.as_view(),name="card_add"),
    path('cards/<int:pk>/edit/',UpdateCardView.as_view(), name="card_update"),
    path('cards/<int:pk>/delete/',DeleteCardView.as_view(), name="card_delete"),

    #using rest api

    path('api/v1/cards/', card_list, name="rest_cards"),
    path('api/v1/cards/<int:pk>/',card_detail, name="rest_card"),


]
