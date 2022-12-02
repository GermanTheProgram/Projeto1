from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UsuarioForm

def home(request):
   
    return render (request, "index.html")

def produto(request):
    return render (request, "produto.html")



'''def login(request):
    return render (request, "login.html")
'''

def novo_usuario(request):
    form=UsuarioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return home(request)

    return render (request, 'login.html', {'form': form})