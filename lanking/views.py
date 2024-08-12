from django.shortcuts import render


# Create your views here.
def lanking(request):
    return render(request, 'lanking/lanking.html')
