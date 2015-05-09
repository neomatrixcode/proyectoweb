from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,ListView,FormView
from .models import Boleta1, Tarea, Personal, Alumno, Tutor, Grupo
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import UserForm,UseraForm 

# Create your views here.
#@login_required()
class registrarcalificaciones (CreateView):
	template_name = 'calificaciones/registrarcalificaciones.html'
	model= Boleta1
	success_url= reverse_lazy('calificaciones') #una vez que se ha registrado el 
								#formulario en la bd decide a donde 
								#te mandara

class registrarpersonal(FormView):
	template_name = 'calificaciones/registrarpersonal.html'
	form_class = UserForm
	success_url= reverse_lazy('personal') 

	def form_valid(self, form):
		perfil = Personal()
		perfil.nombre = form.cleaned_data['nombre']
		perfil.apellidop = form.cleaned_data['apellidop']
		perfil.apellidom = form.cleaned_data['apellidom']
		perfil.clavepresupuestal = form.cleaned_data['clavepresupuestal']
		perfil.telefono = form.cleaned_data['telefono']
		perfil.direccion = form.cleaned_data['direccion']
		perfil.correo = form.cleaned_data['correo']
		perfil.curp = form.cleaned_data['curp']
		perfil.aingresep = form.cleaned_data['aingresep']
		perfil.aingreescuela = form.cleaned_data['aingreescuela']
		perfil.aingrezona = form.cleaned_data['aingrezona']
		perfil.fechanacimiento = form.cleaned_data['fechanacimiento']
		perfil.rfc = form.cleaned_data['rfc']
		perfil.cargo = form.cleaned_data['cargo']

		user = form.save()
		perfil.usuario  = user
  		perfil.save()
		return super(registrarpersonal, self).form_valid(form)


class registraralumno(FormView):
	template_name = 'calificaciones/registraralumnos.html'
	form_class = UseraForm
	success_url= reverse_lazy('alumno') 

	def form_valid(self, form):
		perfila = Alumno()
		perfila.nombrea = form.cleaned_data['nombrea']
		perfila.apellidoPa = form.cleaned_data['apellidoPa']
		perfila.apellidoMa = form.cleaned_data['apellidoMa']
		perfila.sexo = form.cleaned_data['sexo']
		perfila.correo = form.cleaned_data['correo']
		perfila.curp = form.cleaned_data['curp']
		perfila.fechanacimiento = form.cleaned_data['fechanacimiento']
		perfila.rh = form.cleaned_data['rh']
		perfila.tutor1 = form.cleaned_data['tutor1']
		perfila.idgrupo = form.cleaned_data['idgrupo']
		usera = form.save()
		perfila.usuario  = usera
  		perfila.save()
		return super(registraralumno, self).form_valid(form)


class registrartutor (CreateView):
	template_name = 'calificaciones/registrartutor.html'
	model= Tutor
	success_url= reverse_lazy('registraralumno')

class tutor(ListView):
	template_name = 'calificaciones/tutor.html'
	model= Tutor
	context_object_name = 'tutores'

class registrargrupo(CreateView):
	template_name = 'calificaciones/registrargrupo.html'
	model= Grupo
	success_url= reverse_lazy('grupo')

class grupo(ListView):
	template_name = 'calificaciones/grupo.html'
	model= Grupo
	context_object_name = 'grupos'

class calificaciones(ListView):
	template_name = 'calificaciones/calificaciones.html'
	model= Boleta1
	context_object_name = 'calificaciones'
####aqui mismose pueden crear la cantida de vistas que uno quiera

class alumno(ListView):
	template_name = 'calificaciones/alumnos.html'
	model= Alumno
	context_object_name = 'alumnos'

class personal(ListView):
	template_name = 'calificaciones/personal.html'
	model= Personal
	context_object_name = 'personal'

class creartareas (CreateView):
	template_name = 'calificaciones/registrartareas.html'
	model= Tarea
	success_url= reverse_lazy('tareas') #una vez que se ha registrado el 
								#formulario en la bd decide a donde 
								#te mandara

class tareas(ListView):
	template_name = 'calificaciones/tareas.html'
	model= Tarea
	context_object_name = 'tareas'
