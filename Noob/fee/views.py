from django.shortcuts import render
from datetime import datetime
# Create your views here.
# from django.http  import HttpResponse

def fedj(request):
   cname = 'Python'
   fee = '2222'
   time = '2h'
   seat = '12'
   d = datetime.now()
   py_detail= { 'nm':cname,
                 'fe':fee,
                 'time':time,
                 'st': seat,
                 'dt': d
               }
   stu = {'stu1': {'name':'ram', 'roll': 303 },
          'stu2': {'name':'hari', 'roll': 202 },
          'stu3': {'name':'pawan', 'roll': 404 },   
         }
   # context = {'student' : stu}

   context = {**py_detail, 'student': stu}
   return render(request,'fee/fee1.html',context)




   # return render(request,'fee/fee1.html',context)
# def fedj1(request): 
#    stu = {'stu1': {'name':'ram', 'roll': 303 },
#           'stu2': {'name':'hari', 'roll': 202 },
#           'stu3': {'name':'pawan', 'roll': 404 },   
#          }
#    context = {'student' : stu}
#    return render(request,'fee/fee1.html',context)




       

  