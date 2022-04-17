from django.urls import path
from api import views

urlpatterns = [
    path('table/', views.TableView.as_view(), name='table_list'),
    path('table/<int:id>/', views.TableView.as_view(), name='table_detail'),
    
    path('last_session/', views.LastSessionView.as_view(), name='last_session_list'),
    path('last_session/<int:id>/', views.LastSessionView.as_view(), name='last_session_detail'),
    
    path('history/', views.HistoryView.as_view(), name='history_list'),
    path('history/<int:id>/', views.HistoryView.as_view(), name='history_detail'),
    
    path('file/', views.FileView.as_view(), name='file_list'),
    path('file/<int:id>/', views.FileView.as_view(), name='file_detail'),
]