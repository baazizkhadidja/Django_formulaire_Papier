from django.views.generic import ListView, DetailView
from my_app.models import Accounts
from django.shortcuts import render
from django.shortcuts import render


class ListAccount (ListView):
	model = Accounts
	context_object_name = 'accounts'
	template_name = 'accounts_list.html'
	paginate_by = 5
	queryset = Accounts.objects.all().order_by('name')



class VoirPlus (DetailView):
	context_object_name = 'account'
	model = Accounts
	template_name = 'detail.html'
	
	def get_object(self):
		account = super(VoirPlus, self).get_object()



def javaS(request):
	return render(request, 'javas.html')

