from django.urls import path
from api import views

urlpatterns = [    
    # Rutas de la tabla de LastSession
    path('last_session/', views.LastSessionView.as_view(), name='last_session_list'),
    path('last_session/<int:id>/', views.LastSessionView.as_view(), name='last_session_detail'),
    
    # Rutas de la tabla de History
    path('history/', views.HistoryView.as_view(), name='history_list'),
    path('history/<int:id>/', views.HistoryView.as_view(), name='history_detail'),
    
    # Rutas de la tabla de File
    path('file/', views.FileView.as_view(), name='file_list'),
    path('file/<int:id>/', views.FileView.as_view(), name='file_detail'),
]