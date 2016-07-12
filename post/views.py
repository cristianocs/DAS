from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.views.generic import CreateView, ListView
from .models import Post
from .forms import PostForm
from django.utils import timezone

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.data_publicacao = timezone.now()
            post.save()
    else:
        form = PostForm()
    return render(request, 'core/post_edit.html', {'form': form})

class PostView(View):
	def post_list(request):
		posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('data_publicacao')
		return render(request, 'post.html', {'posts': posts})

	