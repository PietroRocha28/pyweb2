from django.shortcuts import render, redirect, get_object_or_404
from .forms  import PersonForm
from .models import Person
def home(request):
    persons = Person.objects.all()
    return render(request, 'index.html', {'persons':persons})
def form(request):
    person_form = PersonForm(request.POST or
                             None,
                             request.FILES or
                             None)
    if person_form.is_valid():
        person = person_form.save(commit=False)
        person.save()
    return render(request, 'login.html',
                  {'person_form':person_form})
def editar(request, id):
    person = get_object_or_404(Person, pk=id)
    person_form = PersonForm(request.POST or
                             None,
                             request.FILES or
                             None,
                             instance=person)
    if person_form.is_valid():
        person = person_form.save(commit=False)
        person.save()

    return render(request,
                  'login.html',
                  {"person_form":person_form})
def deletar(request, id):
    person = get_object_or_404(Person, pk=id)
    person.delete()
    return redirect("/web")
# Create your views here.
