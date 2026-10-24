from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class AdditionView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        n1=form_data.get("num1")
        n2=form_data.get("num2")
        result=n1+n2
        print(request_body)
        data={
            
            "Result":result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class Substarction(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        n1=form_data.get("num1")
        n2=form_data.get("num2")
        result=n1-n2
        print(request_body)
        data={
            "Result":result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class MultiplicationView(View):
    def post(self,request):
        body=request.body
        form_data=loads(body)
        n1=form_data.get("number1")
        n2=form_data.get("number2")
        result=n1*n2
        print(body)
        data={
            "Result":result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class DivisionView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        n1=form_data.get("num1")
        n2=form_data.get("num2")
        result=n1/n2
        print(request_body)
        data={
            "Result":result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class ModulusView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        n1=form_data.get("num1")
        n2=form_data.get("num2")
        result=n1%n2
        print(request_body)
        data={
            "Result":result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class BMIView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        h=form_data.get("height")
        w=form_data.get("weight")
        bmi=w/(h/100)**2
        print(request_body)
        data={
            "Height":h,
            "Weight":w,
            "BMI":bmi
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class AgeView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        b=form_data.get("birth_year")
        c=form_data.get("current_year")
        age=c-b
        print(request_body)
        data={
            "BirthYear":b,
            "CurrentYear":c,
            "Age":age
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name = 'dispatch')
class PercentageView(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)
        marks = form_data.get("marks")
        total_marks = form_data.get("total_marks")
        percentage = (marks/total_marks)*100
        data = {
            "Percentage" : percentage
        }
        return JsonResponse(data)






