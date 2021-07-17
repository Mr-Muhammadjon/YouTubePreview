from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    user_link = request.POST.get('link')
    if user_link:
        links = user_link.split('=')
        link = links[1]
        context = {
            'link':link
        }
        return render(request, 'index.html',context)
    else:
        print('#'*10)
    return render(request, 'index.html')