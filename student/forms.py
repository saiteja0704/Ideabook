# forms.py 
from django import forms 
from .models import *
  
class NewIdeaForm(forms.ModelForm): 
  
	class Meta: 
		model = NewIdea 
		fields = ['title', 'uploadpic','content','videofile','student'] 
