from django.http import HttpResponse
from django.template import loader
from .models import Logins, Worker
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from scripts.table_manager import TableManager
from scripts.check_data import CheckData


def user_is_logged_in(view_func):
    def wrapper(request, *args, **kwargs):
        object = CheckData(Logins)
        status = object.check_user_exists(request.session.get('user_login'),
                                          request.session.get('user_password'))
        if status == 1:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrapper


def main(request):
    template = loader.get_template('main_page.html')
    return HttpResponse(template.render())


def login(request):
    if request.method == 'POST':
        userLogin = request.POST['login']
        userPassword = request.POST['password']
        object = CheckData(Logins)
        status = object.check_user_exists(userLogin, userPassword)
        if status == 1:
            request.session['user_login'] = userLogin
            request.session['user_password'] = userPassword
            return redirect('workers')
        elif status == 2:
            messages.error(request, 'Such login does not exist')
        elif status == 0:
            messages.error(request, 'Password incorrect')
    return render(request, 'login_page.html')


def user_is_logged_in(view_func):
    def wrapper(request, *args, **kwargs):
        object = CheckData(Logins)
        status = object.check_user_exists(request.session.get('user_login'),
                                          request.session.get('user_password'))
        if status == 1:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrapper


def register(request):
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']
        repeatedPassword = request.POST['repeatedPassword']
        loginsList = Logins.objects.values_list('login', flat=True)
        list(loginsList)

        if login not in loginsList:
            if password == repeatedPassword:
                tableManager = TableManager(Logins)
                tableManager.add_login(login, password)
                return redirect('login')
            else:
                messages.error(request, 'Repeated password is not the same!')
        else:
            messages.error(request, 'Such a login already exists!')

    return render(request, 'register_page.html')


@user_is_logged_in
def workers(request):
    template = loader.get_template('workers_list.html')
    workerList = Worker.objects.all().values()
    context = {
        'workerList': workerList,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    template = loader.get_template('worker_details.html')
    workerList = Worker.objects.get(id=id)
    context = {
        'workerList': workerList,
    }
    return HttpResponse(template.render(context, request))

def delete(request, id):
    record = Worker.objects.get(id=id)
    record.delete()
    return redirect('workers')

def add_worker(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        profession = request.POST['profession']
        birth_date = request.POST['birth_date']
        phone_number = request.POST['phone_number']
        email = request.POST['email']

        worker = Worker.objects.create(firstname=firstname,
                                       lastname=lastname,
                                       profession=profession,
                                       birth_date=birth_date,
                                       phone_number=phone_number,
                                       email=email)
        worker.save()
        return redirect('workers')
    return render(request, 'add_worker.html')

def edit_worker(request, id):
    if request.method == 'POST':
        worker = Worker.objects.get(id=id)
        worker.firstname = request.POST['firstname']
        worker.lastname = request.POST['lastname']
        worker.profession = request.POST['profession']
        worker.birth_date = request.POST['birth_date']
        worker.phone_number = request.POST['phone_number']
        worker.email = request.POST['email']
        worker.save()
        return redirect('details', id=id)
    return render(request, 'edit_worker.html')
