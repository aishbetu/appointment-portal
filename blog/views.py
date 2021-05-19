from django.shortcuts import render, get_object_or_404

from blog.models import BlogPost


def blog(request):
    qs = BlogPost.objects.all()
    context = {'object_list': qs}
    return render(request, 'blog.html', context)


def read_article(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'read_article.html'
    context = {'object': obj}
    return render(request, template_name, context)