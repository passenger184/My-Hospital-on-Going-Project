from django.shortcuts import render, redirect,HttpResponse
from .forms import PatientForm
from django.contrib import messages
from .models import Patient
from django.urls import reverse, NoReverseMatch

def main(request):
    context = {}
    return render(request, 'main.html')


def add(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient Record has been successfully Saved!!!')
            return redirect('/')
    
    forms = PatientForm()
   
    context = {
        'forms': forms
    }
    return render(request, 'add.html', context)


def search(request):
    if request.method == 'POST':
        try:
            id = request.POST['id']
            return redirect(reverse('update', args=id))
        except NoReverseMatch:
            return HttpResponse('<h1>Patient ID Does not exist!!!</h1>')
    return render(request, 'search.html')


def update(request, pk):
    
    if Patient.objects.filter(pk=pk).exists():
        patient = Patient.objects.get(pk=pk)
        form = PatientForm(instance=patient)
        if request.method == 'POST':
            form = PatientForm(request.POST ,instance=patient)
            if form.is_valid():
                form.save()
                messages.success(request, 'Patient Record has been successfully Updated!!!')
                return redirect('/')
        context = {
            'form': form
        }
    else:
        return HttpResponse('<h1>Patient ID Does not exist!!!</h1>')
    
    return render (request, 'update.html', context)
   

def search1(request):
    if request.method == 'POST':
        try:
            id = request.POST['id']
            return redirect(reverse('delete', args=id))
        except NoReverseMatch:
            return HttpResponse('<h1>Patient ID Does not exist!!!</h1>')
    return render(request, 'search1.html')


   
def delete(request, pk):
    if Patient.objects.filter(pk=pk).exists():
        patient = Patient.objects.get(pk=pk)
        form = PatientForm(instance=patient)
        # if request.method == 'POST':
        #     id = patient.id
        #     return redirect(reverse('confirm'))
        context = {
            'form': form,
            'id': patient.id,
        }
    else:
          return HttpResponse('<h1>Patient ID Does not exist!!!</h1>')
    return render(request, 'delete.html', context)



def confirm(request ,pk):
    patient = Patient.objects.get(pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('/')
    
    context = {
           'patient':patient
        }
    
    return render(request, 'confirm.html', context)