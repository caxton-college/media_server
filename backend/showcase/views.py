from django.shortcuts import render

# Create your views here.
def image_feed(request):
    return render(request, 'showcase/image_feed.html')