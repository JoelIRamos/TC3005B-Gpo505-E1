from django.urls import path
from api import views

urlpatterns = [
    # Endpoints GETs
    # * Consultar la lista de historiales
    path('getHistoryList/', views.searchHistoryListView.as_view(), name='get_history_list'),
    # * Consultar los detalles de un historial
    path('getHistoryDetail/<int:historyID>/', views.searchHistoryDetailView.as_view(), name='get_history_detail'),
    # * Consultar los detalles de la ultima sesion de un usuario
    path('getLastSession/<int:userID>/', views.searchLastSessionView.as_view(), name='get_last_session'),
    
    # Endpoints PUTs
    # * Actualizar los detalles de la ultima sesion de un usuario
    path('putLastSession/<int:userID>/', views.updateLastSessionView.as_view(), name='put_last_session'),
    
    # Endpoints POSTs
    # * Crear un nuevo historial
    path('postHistory/<int:userID>/', views.insertToHistoryView.as_view(), name='post_history'),
    # * Crear un nuevo registro de una sesion
    path('postLastSession/<int:userID>/<historyID>/', views.insertLastSessionView.as_view(), name='post_last_session'),
    
    # Endpoints DELETEs
    # * Eliminar una sesion
    path('deleteLastSession/<int:userID>/', views.deleteLastSessionView.as_view(), name='delete_last_session'),
]