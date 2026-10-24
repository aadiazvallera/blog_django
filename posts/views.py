from django.shortcuts import render
from .models import Post


def inicio(request):
    """Muestra la página de inicio."""
    return render(request, 'posts/inicio.html')


def acerca(request):
    """Muestra la página 'Acerca de'."""
    return render(request, 'posts/acerca.html')


def lista_posts(request):
    """Muestra los posts publicados, del más nuevo al más viejo."""
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
    context = {
        "posts": posts
    }
    return render(request, 'posts/lista_posts.html', context)