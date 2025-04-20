from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def students(request):
    student = [
        {"roll_no" : 63, "name" : "Rushi Borkar", "class": "2N",}
    ]
    return HttpResponse(student)
    # return HttpResponse('<h2> Jai Shri Ram </h2>')