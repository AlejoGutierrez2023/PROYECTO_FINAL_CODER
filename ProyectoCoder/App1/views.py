from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from App1.models import Blog
from App1.forms import BlogForm
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import permission_required




@login_required
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})

@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog_form.html', {'form': form})

@login_required
def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.user != blog.author:
        return redirect('blog_list')
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog_form.html', {'form': form})

@login_required
def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.user != blog.author:
        return redirect('blog_detail', pk=blog.pk)
    blog.delete()
    return redirect('blog_list')



def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    html = render_to_string('blog_detail.html', {'blog': blog})
    return HttpResponse(html)



