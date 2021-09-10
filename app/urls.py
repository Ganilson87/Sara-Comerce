from django.urls import path
from .views import *

urlpatterns = [
    path('', produtoListView, name="index"),
    path("Produto/<int:pk>/", produtoDetailView.as_view(), name="detalhes"),
    path("Checkout", checkout, name="checkout"),

    

]