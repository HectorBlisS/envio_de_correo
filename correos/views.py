from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Suscriptor
from django.core.urlresolvers import reverse_lazy




class SuscriptorList(ListView):
	model = Suscriptor

class SuscriptorDetail(DetailView):
	model = Suscriptor

class SuscriptorCreation(CreateView):
	model = Suscriptor
	success_url = reverse_lazy('correos:list')
	fields = ['nombre','email']

class SuscriptorUpdate(UpdateView):
	model = Suscriptor
	success_url = reverse_lazy('correos:list')
	fields = ['nombre','email']

class SuscriptorDelete(DeleteView):
	model = Suscriptor
	success_url = reverse_lazy('correos:list')

class Spam(View):
	def get(self,request):
		template_name = 'correos/spam.html'
		correos = Suscriptor.objects.all()
		context = {
		'correos':correos,
		}
		return render(request,template_name,context)

	def post(self,request):
		asunto = request.POST.get('asunto')
		mensaje = request.POST.get('mensaje')
		victimas = request.POST.get('victims')
		try:
			enviar_spam({
				'asunto':asunto,
				'mensaje':mensaje,
				'victimas':victimas
				})
		except Exception as err:
			print(err)
		
		return redirect('correos:list')


from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage

def enviar_spam(data):
	subject = data['asunto']
	to = [data['victimas']]
	from_email = 'FixterCamp@fixter.org'
	ctx = data

	message = get_template('correos/email.html').render(Context(ctx))
	msg = EmailMessage(subject,message,to=to,from_email=from_email)
	msg.send()









