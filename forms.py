from django import forms


class ContactForm(forms.Form):
	sujet = forms.CharField(max_length = 100)
	message = forms.CharField(widget = forms.Textarea)
	envoyeur = forms.EmailField(label = 'Votre adresse e-mail')
	renvoi = forms.BooleanField(help_text = 'Cocher si vous voulez recevoir une copie de ce mail', required = False)
