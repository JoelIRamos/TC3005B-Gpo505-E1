from django.urls import path
from api import views

urlpatterns = [
    path('getHistoryList/', views.searchHistoryListView.as_view(), name='get_history_list'),
    path('getHistoryDetail/<int:historyID>/', views.searchHistoryDetailView.as_view(), name='get_history_detail'),
    path('getLastSession/<int:userID>/', views.searchLastSessionView.as_view(), name='get_last_session'),
    path('deleteLastSession/<int:userID>/', views.deleteLastSessionView.as_view(), name='delete_last_session'),
    path('postHistory/<int:userID>/', views.insertToHistoryView.as_view(), name='post_history'),
    path('postLastSession/<int:userID>/<historyID>/', views.insertLastSessionView.as_view(), name='post_last_session'),
    path('putLastSession/<int:userID>/', views.updateLastSessionView.as_view(), name='put_last_session'),
]