from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .models import *
import random

# Create your views here.

def home(request):
    context= {"categories": Category.objects.all()}
    if request.GET.get('category'):
        print(request.GET.get('category'))
        return redirect(f"/quiz/?category={request.GET.get('category')}")
    
    return render(request, 'home.html', context)


def quiz(request):
    context= {'category': request.GET.get('category')}
    return render(request,'quiz.html',context)




# api 
# Look:
# payload
# {
#     "status":True,
#     'data':[
#         {},
#     ]
# }

def quiz_api(request):
    try:
        que_objs= Question.objects.all()
        if request.GET.get('category'):
            que_objs= que_objs.filter(category__category_name__icontains= request.GET.get('category'))
        
        que_objs= list(que_objs)
        data= []
        random.shuffle(que_objs)
        for obj in que_objs:
            data.append({
                "uid" : obj.uid ,
                "category":obj.category.category_name ,
                "question":obj.question,
                "marks":obj.marks,
                "options":obj.get_options()
            })

        payload= {'status':True, 'data':data}

        return JsonResponse(payload)

    except Exception as e:
        print(e)
