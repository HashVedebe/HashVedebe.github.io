from django import forms
from django.shortcuts import render

tasks = ["foo", "bar", "baz"]
# Create your views here.

class NewTaskForm(forms.Form):
    FOR_WHO_CHOICES = [
        ('option1','Ivo'),
        ('option2','Joris'),
        ('option3','Victor'),
        ('option4','Hilde')
    ]
    
    for_who = forms.ChoiceField(
        choices=FOR_WHO_CHOICES,
        widget=forms.RadioSelect,
        label="Voor wie?"
    )
    
    task = forms.CharField(label="Nieuwe taak")
    priority = forms.IntegerField(label="Prioriteit", min_value=1, max_value=5)
    

def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
    
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })    
            
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })