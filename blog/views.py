from django.shortcuts import render, redirect
from blog.models import Post
from datetime import datetime
from django.http import  Http404, HttpResponse

# Create your views here.
def homepage(request):
    return render(request,'blog.html', {'posts': Post.objects.filter(show=True)})

def faq(request):
    return render(request,'faq.html', {})

def post_details(request,pk):
    try: 
        post=Post.objects.get(pk=pk)
        if post.show== True:
            return render(request, 'post_details.html', {'post':post })
        elif post.author== request.user:
            return render(request, 'post_details.html', {'post':post })
        else:
            raise Http404
        
    except:
        raise Http404
    
def new_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title= request.POST['title']
            text= request.POST['text']
            author=request.user 
            date=datetime.now()
            new_post= Post.objects.create (
                title=title,
                text=text,
                date=date,
                author=author,
            )
            new_post.save()
            return redirect('post_details', pk=new_post.pk)
    
        else:
            return render(request, 'new_post.html', {})
    else:
        return redirect('homepage')

