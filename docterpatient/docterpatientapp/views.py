from django.shortcuts import render

# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'signup.html', context)


def checkemailExists(request):
    return True

def signup(request):
    return True
