from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Task, Quote
import datetime
import random
from .forms import LoginForm, SignupForm, TaskToAddForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index_view(request):
    if request.user.is_authenticated:
        logged_in = True
        all_tasks = request.user.task_set.filter(date=datetime.date.today()).order_by('-id')
        task_history = request.user.task_set.order_by('-date')
        completed_tasks = request.user.task_set.filter(completed=1, date=datetime.date.today()).order_by('-id')
        uncompleted_tasks = request.user.task_set.filter(completed=0, date=datetime.date.today()).order_by('-id')
    else:
        logged_in = False
        all_tasks = []
        task_history = []
        completed_tasks = []
        uncompleted_tasks = []

    form = TaskToAddForm()
    random_quote_id = random.randint(1, len(Quote.objects.all()))
    quote = Quote.objects.get(id=random_quote_id)
    context = {
        'all_tasks': all_tasks,
        'completed_tasks': completed_tasks,
        'uncompleted_tasks': uncompleted_tasks,
        'task_history': task_history,
        'quote': quote,
        'form': form,
        'logged_in': logged_in,
    }
    return render(request, 'myplanner/index.html', context)


def add_task(request):
    form = TaskToAddForm(request.POST)
    if form.is_valid():
        task_name = form.cleaned_data['task_to_add']
    if task_name:
        if request.user.is_authenticated:
            new_task = Task(user=request.user, task_name=task_name)
            new_task.save()
            return HttpResponseRedirect(reverse('myplanner:index'))
        else:
            return HttpResponseRedirect(reverse('myplanner:index'))
    else:
        return HttpResponseRedirect(reverse('myplanner:index'))


def add_to_completed(request):
    try:
        task = Task.objects.get(id=request.POST['task'])

    except(KeyError, Task.DoesNotExist):

        return HttpResponseRedirect(reverse('myplanner:index'))

    else:
        if "add_to_completed" in request.POST:
            task.completed = 1
            task.save()
        elif "delete_task" in request.POST:
            task.delete()
        return HttpResponseRedirect(reverse('myplanner:index'))


def auth_view(request):
    if request.method == "POST":
        if "submit-sign-in-form" in request.POST:
            sign_in_form = LoginForm(request.POST)
            if sign_in_form.is_valid():
                username = sign_in_form.cleaned_data['Email_or_Username']
                password = sign_in_form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('myplanner:index'))
                else:
                    return HttpResponseRedirect(reverse('myplanner:auth'))

        elif "submit-sign-up-form" in request.POST:
            sign_up_form = SignupForm(request.POST)
            if sign_up_form.is_valid():
                username = sign_up_form.cleaned_data['Username']
                email = sign_up_form.cleaned_data['Email']
                password = sign_up_form.cleaned_data['Password']
                try:
                    User.objects.get(username=username)
                except User.DoesNotExist:
                    User.objects.create_user(username=username, email=email, password=password)
                else:
                    print("User exists")
                return HttpResponseRedirect(reverse('myplanner:index'))
    else:
        sign_in_form = LoginForm()
        sign_up_form = SignupForm()
        context = {
            'sign_in_form': sign_in_form,
            'sign_up_form': sign_up_form
        }
        return render(request, 'myplanner/auth.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('myplanner:index'))
