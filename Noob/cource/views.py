from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse
# def learn(request):
#     return HttpResponse('Anuj Neupane')

def fb(request):
    coursename ={'d1':'Create a New Account'}
    return render(request,'course/project1.html',coursename)


 

