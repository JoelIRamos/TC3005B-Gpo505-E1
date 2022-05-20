from django.urls import path
from api import views

urlpatterns = [
    # Rutas GETs
    # * Consultar la lista de historiales
    path('getHistoryList/', views.searchHistoryListView.as_view(), name='get_history_list'),
    # * Crear un nuevo registro de una sesion y devuelve el userID
    path('getUserID/<str:historyID>/', views.searchUserIDView.as_view(), name='get_user_id'),
    # * Consultar los detalles de un historial
    path('getHistoryDetail/<str:historyID>/', views.searchHistoryDetailView.as_view(), name='get_history_detail'),
    # * Consultar los detalles de la ultima sesion de un usuario
    path('getLastSession/<str:userID>/', views.searchLastSessionView.as_view(), name='get_last_session'),
    
    # * Mandar a pedir la informacion de una sesion en formato para una grafica de Barras
    path('getBarGraph/<str:userID>/<str:variable>/<str:filter>/', views.searchBarGraphView.as_view(), name='get_bar_graph_with_filter'),
    # path('getBarGraph/<str:userID>/<str:variable>/', views.searchBarGraphView.as_view(), name='get_bar_graph_without_filter'),
    # * Mandar a pedir la informacion de una sesion en formato para una grafica de Lineas
    path('getLineGraph/<str:userID>/<str:variable>/<str:filter>/', views.searchLineGraphView.as_view(), name='get_line_graph_with_filter'),
    # path('getBarGraph/<str:userID>/<str:variable>/', views.searchBarGraphView.as_view(), name='get_bar_graph_without_filter'),
    # * Mandar a pedir la informacion de una sesion en formato para una grafica de Burbuja
    path('getBubbleGraph/<str:userID>/<str:variable>/', views.searchBubbleGraphView.as_view(), name='get_bubble_graph'),
    
    
    # Rutas PUTs
    # * Insertar una grafica de una corrida
    path('putGraphs/<str:historyID>/', views.updateGraphsView.as_view(), name='put_graphs'),
    
    # Rutas DELETEs
    # * Eliminar una sesion
    path('deleteLastSession/<str:userID>/', views.deleteLastSessionView.as_view(), name='delete_last_session'),
    path('deleteGraph/<str:userID>/<int:graphID>/', views.deleteGraphView.as_view(), name='delete_graph'),

    # Rutas POSTs
    path('upload_file/', views.FileUploadView.as_view(), name='upload_file')
]