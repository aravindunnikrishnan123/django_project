from django.shortcuts import render

# Create your views here.
def fn_myIndex(request):
    return render(request,'index.html')

