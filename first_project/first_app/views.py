from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # add some insert_me variable
    mydict = {'insert_me': "Now I'm coming from first_app/views.py"}
    return render(request, 'first_app/index.html', context=mydict)
    # old one
    # resp = "<h1>Hello World!!!</h1>"
    # news = "<p>The URL address for editing the blog posts is: <p>"
    # urlexample = "https://superapp/blog/post-number/edit/"
    # return HttpResponse(resp+news+urlexample)
