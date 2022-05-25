from django.urls import path
from api import views

urlpatterns = [
    # Rutas GETs
    # * Consultar la lista de historiales
    path('getHistoryList/', views.searchHistoryListView.as_view(), name='get_history_list'),
    
    # * Consultar los detalles de un historial
    path('getHistoryDetail/<str:historyID>/', views.searchHistoryDetailView.as_view(), name='get_history_detail'),
    
    # * Consultar los detalles de la ultima sesion de un usuario
    path('getHistory/<str:historyID>/', views.searchHistoryView.as_view(), name='get_history'),
    
    # * Mandar a pedir la informacion de una sesion en formato para una grafica de Barras
    path('getBarGraph/<str:historyID>/<str:attribute>/<str:filter>/', views.searchBarGraphView.as_view(), name='get_bar_graph'),
    
    # * Mandar a pedir la informacion de una sesion en formato para una grafica de Lineas
    path('getLineGraph/<str:historyID>/<str:attribute>/<str:filter>/', views.searchLineGraphView.as_view(), name='get_line_graph'),
    
    # * Mandar a pedir la informacion de una sesion en formato para una grafica de Burbuja
    path('getBubbleGraph/<str:historyID>/<str:attribute1>/<str:attribute2>/<str:filter>/', views.searchBubbleGraphView.as_view(), name='get_bubble_graph'),
    
    # * Eliminar una grafica del historial
    path('deleteGraph/<str:historyID>/<int:graphID>/', views.deleteGraphView.as_view(), name='delete_graph'),
    
    # * Actualizar una grafica del historial
    path('putGraph/<str:historyID>/<int:graphID>/', views.updateGraphView.as_view(), name='put_graph'),

    # Rutas POSTs
    # * Subir un archivo
    path('upload_file/', views.FileUploadView.as_view(), name='upload_file')
]