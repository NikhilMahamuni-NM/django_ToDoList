from django.shortcuts import render, redirect
from todoapp.models import List
from todoapp.forms import ListForm

# Create your views here.

def todolist(request):
    form = ListForm()

    if request.method == 'POST':
        form = ListForm(request.POST)

        if form.is_valid():
            form.save()
            tolist = List.objects.all
        return render(request, 'todoapp/todolist.html', {'form': form, 'tolist' : tolist})

    else:
        tolist = List.objects.all
        return render(request, 'todoapp/todolist.html',{'form': form, 'tolist' : tolist})

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    return redirect('todoapp:todolist')
