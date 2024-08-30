# forms.py 
from django import forms 
from .models import NewIdeaFac
  
class NewIdeaFacForm(forms.ModelForm): 
  
	class Meta: 
		model = NewIdeaFac
		fields = ['title', 'uploadpic','content','videofile','faculty'] 
