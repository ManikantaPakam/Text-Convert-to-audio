from django.shortcuts import render, redirect
import pyttsx3

# Create your views here.

def home_view(request):
    return render(request,'app1/home.html')

def some(request):
    value=request.GET['text_audio']
    obj=pyttsx3.init()
    obj.say(value)
    obj.runAndWait()
    return redirect('/')