from django import forms 
from .models import Donor,Recipient

class DonorForm(forms.ModelForm):
   class meta:
       model=Donor
       field="__all__"
class RecipientForm(forms.ModelForm):
    class meta:
        model=Recipient
        field="__all__"
class SearchDonorForm(forms.Form):
    organ = forms.CharField(max_length=50)
    blood_group = forms.CharField(max_length=3)
    
