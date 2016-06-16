from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.views.generic import CreateView, ListView
from .models import Post

class PostView(View):
	def post_list(request):
		posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('data_publicacao')
		return render(request, 'post.html', {'posts': posts})