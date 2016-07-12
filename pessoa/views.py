from django.shortcuts import render
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate
from .models import Pessoa

def register(request):
    form = PessoaForm()
    return render(request, 'core/register.html', {'form': form})
#Page for register pessoa
class Register(CreateView):
    template_name = 'register.html'
    fields = ['nome', 'email', 'senha']
    model = Pessoa
    success_url = reverse_lazy('list')