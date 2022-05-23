from django.urls import path
from api import views

urlpatterns = [
    # Rutas GETs
    # * Consultar la lista de historiales
    path('getHistoryList/', views.searchHistoryListView.as_view(), name='get_history_list'),
    
    # // # * Crear un nuevo registro de una sesion y devuelve el userID
    # // path('getUserID/<str:historyID>/', views.searchUserIDView.as_view(), name='get_user_id'),
    
    # * Consultar los detalles de un historial
    path('getHistoryDetail/<str:historyID>/', views.searchHistoryDetailView.as_view(), name='get_history_detail'),
    
    # * Consultar los detalles de la ultima sesion de un usuario
    path('getHistory/<str:historyID>/', views.searchHistoryView.as_view(), name='get_history'),
    # // path('getLastSession/<str:userID>/', views.searchLastSessionView.as_view(), name='get_last_session'),
    
    # * Mandar a pedir la informacion de una sesion en formato para una grafica de Barras
    path('getBarGraph/<str:historyID>/<str:attribute>/<str:filter>/', views.searchBarGraphView.as_view(), name='get_bar_graph'),
    # // path('getBarGraph/<str:userID>/<str:attribute>/<str:filter>/', views.searchBarGraphView.as_view(), name='get_bar_graph'),
    
    # * Mandar a pedir la informacion de una sesion en formato para una grafica de Lineas
    path('getLineGraph/<str:historyID>/<str:attribute>/<str:filter>/', views.searchLineGraphView.as_view(), name='get_line_graph'),
    # // path('getLineGraph/<str:userID>/<str:attribute>/<str:filter>/', views.searchLineGraphView.as_view(), name='get_line_graph'),
    
    # * Mandar a pedir la informacion de una sesion en formato para una grafica de Burbuja
    path('getBubbleGraph/<str:historyID>/<str:attribute>/', views.searchBubbleGraphView.as_view(), name='get_bubble_graph'),
    # // path('getBubbleGraph/<str:userID>/<str:attribute>/', views.searchBubbleGraphView.as_view(), name='get_bubble_graph'),
    
    # // # Rutas DELETEs
    # // # * Eliminar una sesion del usuario
    # // path('deleteLastSession/<str:userID>/', views.deleteLastSessionView.as_view(), name='delete_last_session'),
    
    # * Eliminar una grafica del historial
    path('deleteGraph/<str:historyID>/<int:graphID>/', views.deleteGraphView.as_view(), name='delete_graph'),
    
    # * Actualizar una grafica del historial
    path('putGraph/<str:historyID>/<int:graphID>/', views.updateGraphView.as_view(), name='put_graph'),

    # Rutas POSTs
    # * Subir un archivo
    path('upload_file/', views.FileUploadView.as_view(), name='upload_file')
]