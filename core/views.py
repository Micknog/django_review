from django.shortcuts import render, redirect
from core.models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


# def index(request):
#     return redirect('/agenda/')
# importa o redirect no shortcuts

def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido")

    return redirect('/')


@login_required(login_url='/login/')
def list_events(request):
    usuario = request.user
    event = Event.objects.filter(user=usuario)
    # event = Event.objects.all()
    data = {'events': event}
    return render(request, 'agenda.html', data)


@login_required(login_url='/login/')
def evento(request):
    return render(request, 'evento.html')


@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        tittle = request.POST.get('titulo')
        event_date = request.POST.get('data_evento')
        description = request.POST.get('descricao')
        user = request.user
        Event.objects.create(tittle=tittle,
                             event_date=event_date,
                             description=description,
                             user=user)
    return redirect('/')
