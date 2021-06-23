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
    event_id = request.GET.get('id')
    data = {}
    if event_id:
        data['event'] = Event.objects.get(id=event_id)
    return render(request, 'evento.html', data)


@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        tittle = request.POST.get('titulo')
        event_date = request.POST.get('data_evento')
        description = request.POST.get('descricao')
        user = request.user
        event_id = request.POST.get('event_id')
        if event_id:
            event = Event.objects.get(id=event_id)
            if event.user == user:
                event.tittle = tittle
                event.description = description
                event.event_date = event_date
                event.save()
            # Event.objects.filter(id=event_id).update(tittle=tittle,
            #                                          event_date=event_date,
            #                                          description=description)
        else:
            Event.objects.create(tittle=tittle,
                                 event_date=event_date,
                                 description=description,
                                 user=user)
    return redirect('/')


@login_required(login_url='/login/')
def delete_event(request, event_id):
    usuario = request.user
    event = Event.objects.get(id=event_id)
    if usuario == event.user:
        event.delete()
    return redirect('/')
