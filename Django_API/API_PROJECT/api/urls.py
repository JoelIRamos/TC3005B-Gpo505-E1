from django.urls import path
from api import views

urlpatterns = [
    
    # Asyncronos
    path('getHistoryList/', views.searchHistoryList),
    path('getHistoryDetail/<int:historyID>', views.searchHistoryDetail),
    path('getLastSession/<int:userID>', views.searchLastSession),
    path('deleteLastSession/<int:userID>', views.deleteLastSession),
    path('putLastSession/<int:userID>', views.updateLastSession),
    path('postHistory/<int:userID>', views.insertToHistory),
    
    
    # Rutas de la tabla de LastSession
    path('last_session/', views.LastSessionView.as_view(), name='last_session_list'),
    path('last_session/<int:id>/', views.LastSessionView.as_view(), name='last_session_detail'),
    
    # Rutas de la tabla de History
    path('history/', views.HistoryView.as_view(), name='history_list'),
    path('history/<int:id>/', views.HistoryView.as_view(), name='history_detail'),
    # str
    # Rutas de la tabla de File
    path('file/', views.FileView.as_view(), name='file_list'),
    path('file/<int:id>/', views.FileView.as_view(), name='file_detail'),
]