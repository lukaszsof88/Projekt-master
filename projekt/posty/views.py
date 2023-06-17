from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Post
from django.views.generic import CreateView, ListView
from django.core.paginator import Paginator, EmptyPage



def list_of_post(request):
    post = Post.objects.all()
    template = 'posty/posty.html'
    p = Paginator(post, 2)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    context = {"post": page}
    return render(request, template, context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    template = 'posty/posty_szczegoly.html'
    context = {'post': post}
    return render(request, template, context)


class BlogSearchView(ListView):
    model = Post
    template_name = 'posty/searchbar.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(title__icontains=query)
        else:
            return Post.objects.all()


# class BlogSearchView(ListView):
#     model = Post
#     template_name = 'posty/searchbar.html'
#     # context_object_name = 'posts'
#
#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         return Post.objects.filter(title__icontains=query)
#
# # def wyszukaj(request):
# #     if request.method == 'GET':
# #         query = request.GET.get('q')
# #         post = Post.objects.filter(title__icontains=query)
# #         template = 'posty/posty.html'
# #         context = {'post': post}
# #         return render(request, template, context)
class PostCreateView(CreateView):
    template_name = 'posty/post_create.html'
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('posty')



