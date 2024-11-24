from django.shortcuts import render,redirect
from .models import Donor,Recipient
from .forms import DonorForm,RecipientForm,SearchDonorForm
# Create your views here.
def Add_Donor(request):
    
    if request.method=='POST':
       form=DonorForm(request.POST)
       if form.is_valid():
          
               form.save()
               return redirect("/view_donor")
         
          
       else:
       
        form=DonorForm()     
     
    return render(request,"management/add_donor.html",{'form':form})

def view_donor(request):
    donors = Donor.objects.all()
    return render(request, 'management/view_donors.html', {'donors': donors})



def Add_Recipient(request):
    if request.method=='POST':
     form=RecipientForm(request.POST)
     if form.is_vaild():
        try:
            form.save()
            return redirect("/view_recipients")
        except:
            pass
     else:
        form=RecipientForm()
    return render(request,"management/add_recipient,html",{'form':form})

def view_recipients(request):
    recipients = Recipient.objects.all()
    return render(request, 'management/view_recipients.html', {'recipients': recipients})


def SearchDonorView(request):
    result=None
    if request.method=="POST":
        form=SearchDonorForm(request.POST)
        if form.is_valid():
           organ=form.cleaned_data['organ']
           blood_type=form.cleaned_data['blood_type']
           result=Donor.objects.filter(organ=organ,blood_type=blood_type)
    return render(request,"management/search.html",{'form':form,'result':result})
        
           
           
            


           
            
          
     