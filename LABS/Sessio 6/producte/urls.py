from django.urls import path
from . import views

urlpatterns = [
    # ex: /producte/
    path('', views.index, name='index'),
    # ex: /producte/5/
    path('<int:producte_id>/', views.producte, name='producte'),
]