from django.urls import path

from .views import VideoListView, VideoDetailView, VideoCreateView

urlpatterns = [
    path('', VideoListView.as_view(), name='video_list'),
    path('upload/', VideoCreateView.as_view(), name='video_upload'),
    path('<int:pk>/', VideoDetailView.as_view(), name='video_detail'),
]
