from django.urls import path
from api import views

urlpatterns = [
    # Rutas GETs
    # * Consultar la lista de historiales
    path('getHistoryList/', views.searchHistoryListView.as_view(), name='get_history_list'),
    # * Consultar los detalles de un historial
    path('getHistoryDetail/<str:historyID>/', views.searchHistoryDetailView.as_view(), name='get_history_detail'),
    # * Consultar los detalles de la ultima sesion de un usuario
    path('getLastSession/<str:userID>/', views.searchLastSessionView.as_view(), name='get_last_session'),
    # * Crear un nuevo registro de una sesion y devuelve el userID
    path('getUserID/<str:historyID>/', views.searchUserIDView.as_view(), name='get_user_id'),
    
    # Rutas PUTs
    # * Actualizar los detalles del historial de un usuario
    path('putHistory/<str:userID>/', views.updateHistoryView.as_view(), name='put_last_session'),
    
    # ToDo: Rutas POSTs
    # * Crear un nuevo historial
    # ? Eliminar ?
    path('postHistory/<str:userID>/', views.insertToHistoryView.as_view(), name='post_history'),
    
    # Rutas DELETEs
    # * Eliminar una sesion
    path('deleteLastSession/<str:userID>/', views.deleteLastSessionView.as_view(), name='delete_last_session'),

    # Rutas de la subida de archivos
    path('upload_file/', views.FileUploadView.as_view(), name='upload_file')
]