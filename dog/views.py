from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from dog.models import Dog


from .forms import DogForms


@login_required
def index(request):
    title = {'title': 'Dog'}
    dog_list = Dog.objects.all()
    return render(request, 'index.html', {'dogs': dog_list, 'title': title})


@login_required
def create(request):
    if request.method == "POST":
        form = DogForms(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            color = form.cleaned_data['color']
            breed = form.cleaned_data['breed']

            dog = Dog(name=name, color=color, breed=breed, owner=request.user)
            dog.save()

            return redirect('index')
    else:
        form = DogForms()
        return render(request, 'create.html', {'form': form})


@login_required
def update(request, dog_id):
    if request.method == "POST":
        form = DogForms(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            color = form.cleaned_data['color']
            breed = form.cleaned_data['breed']

            dog = Dog.objects.get(pk=dog_id)
            dog.name = name
            dog.color = color
            dog.breed = breed

            dog.save()

            return redirect('index')
    else:
        try:
            instance = request.user.dog_set.get(pk=dog_id)
        except Dog.DoesNotExist:
            messages.success(request, 'You don\'t have permission to edit this.')
            return redirect('index')

        form = DogForms(instance=instance)
        return render(request, 'edit.html', {'form': form, 'dog_id': dog_id})


@login_required
def delete(request, dog_id):
    if dog_id:
        try:
            result = request.user.dog_set.get(pk=dog_id)
        except Dog.DoesNotExist:
            messages.success(request, 'You don\'t have permission to remove this.')
            return redirect('index')

        messages.success(request, 'You deleted {}'.format(result.name))
        result.delete()
        return redirect('index')
    return HttpResponse(id)
