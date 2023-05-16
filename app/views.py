from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import View
from app.forms import *
# Create your views here.


# FBV using returning A String


def FBV_string(request):
    return HttpResponse('Data Is Inserted Successfully...!!!')

# Using Class Based Views Return A String....


class CBV_string(View):
    def get(self,request):
        return HttpResponse('Data Is Inserted Successfully...!!!')
    


## Function Based Views Usin HTML Pages....


def Fun_Bas_View_Html(request):
    return render(request,'Fun_Bas_View_Html.html')



## Class Based Views Using Html Page...!!!


class Cls_Bas_View_Html(View):
    def get(self,request):
        return render(request,'Cls_Bas_View_Html.html')
    



### Function Based Views Using Model Forms....

def FBForms(request):
    LFO=TopicForm()
    S={'LFO':LFO}
    if request.method=='POST':
        list_of_function_data=TopicForm(request.POST)
        if list_of_function_data.is_valid():
            list_of_function_data.save()
            return HttpResponse('Data Is Inserted Successfully...!!!')


    return render(request,'FBForms.html',S)


### Class Based Views Using Model Forms.....


class Class_BV(View):
    def get(self,request):
        LCO=TopicForm()
        G={'LCO':LCO}
        return render(request,'Class_BV.html',G)
    

    def post(self,request):
        class_object_data=TopicForm(request.POST)
        if class_object_data.is_valid():
            class_object_data.save()
            return HttpResponse('Data bIs Inserted Successfully...!!!')
    