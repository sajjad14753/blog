from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'homepage.html', {})
def faq(request):
    return render(request,'faq.html', {})