from django.urls import path
from api import views

urlpatterns = [
    path('table/', views.TableView.as_view(), name='table_list'),
    path('table/<int:id>/', views.TableView.as_view(), name='table_detail'),
]