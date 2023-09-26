from django.shortcuts import render

# Create your views here.

def event_list(request):
    user = request.user
    
    return render(request, 'event/event_list.html', locals())
