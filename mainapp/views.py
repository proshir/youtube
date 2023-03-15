from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Video


class VideoListView(ListView):
    model = Video
    paginate_by = 8
    ordering = ['-uploaded_at']

class VideoDetailView(DetailView):
    model = Video

class VideoCreateView(CreateView):
    model = Video
    fields = ['topic', 'description', 'video', 'thumbnail']
    success_url = reverse_lazy('video_list')
