from django.shortcuts import render
from django import forms
from my_app.models import  Accounts, Orders
from my_app.models import table_ins

def liste (request):
	accounts = Accounts.objects.all()
	return render(request, 'accounts.html', {'accounts': accounts})


class Ajout_account(forms.Form):
	name = forms.CharField(label = 'NOM', max_length = 30)
	website = forms.CharField(label = 'site', max_length = 30)


def edit(request):
	form = Ajout_account(request.POST)
	if form.is_valid():
		new_account = Accounts(
			name = form.cleaned_data['name'],
			website = form.cleaned_data['website']
		)
		new_account.save()
		message = 'Ajout réussit'
	else:
		message = "Corrigez votre ajout ! "

		
	return render(request, 'edit.html', {'context': form, 'message':message})





class Inscription_form(forms.Form):
	nom = forms.CharField(label = 'nom', max_length = 30)
	prenom = forms.CharField(label = 'prenom', max_length = 30)

def ins(request):
	forme = Inscription_form(request.POST)
	if forme.is_valid():
		nom = forme.cleaned_data['nom'],
		prenom = forme.cleaned_data['prenom']
	envoie = True
	return render(request, 'ins.html', locals())


class order_form(forms.ModelForm):
	class Meta:
		model = Orders
		fields = ('total', 'gloss_qty')

def demande(request):
	form = order_form(request.POST)
	return render(request, 'demande.html', {'form':form})

def list_order(request):
	orders = Orders.objects.all()
	return render(request, 'order.html', {'orders':orders})


from django.views.generic import TemplateView

class FAQView(TemplateView):
   template_name = "faq.html"  
