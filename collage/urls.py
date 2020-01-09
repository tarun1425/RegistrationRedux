from django.urls import path
from . import views
urlpatterns = [
    path('',views.NoticeListView.as_view()),
     path('<int:pk>',views.NoticeDetailsView.as_view()),
    
]
