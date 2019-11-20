from django.shortcuts import render

# Create your views here.
def fn_index(request):
    return render(request,'index.html')