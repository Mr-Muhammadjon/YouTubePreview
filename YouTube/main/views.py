from django.shortcuts import render

# Create your views here.
def index(request):
    user_link = request.POST.get()
    if user_link:
        links = user_link.split('=')
        link = links[1]
        context = {
            'link':link
        }
    return render(request,'index.html',context)