from django.shortcuts import render, redirect
from .models import Task, Organisation, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
# from .forms import 
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.http import JsonResponse

# Create your views here.
def get_task(request):
    if request.method == "GET":
        tasks = Task.objects.filter(organisation__user__user = request.user)
        context={
            'tasks':tasks
        }
        return render(request,'project/mytask.html',context)

def end_task(request,pk):
    if request.method == "POST":
        task = Task.objects.get(id=pk)
        task.status = '1'
        task.save()
        return redirect('get_task')