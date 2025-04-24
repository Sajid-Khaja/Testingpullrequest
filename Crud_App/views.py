from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Operation
from .forms import formOperation  # Import your form

def Read(request):
    data =Operation.objects.filter(Postal_code=193201)
    return render(request, 'Read.html', {'Data': data})

def Create(request):
    if request.method == 'POST':
        form = formOperation(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('Read')) #Use reverse

    else:
        form = formOperation()

    return render(request, 'Create.html', {'form': form})

def changes(request, pk):
    data = get_object_or_404(Operation, pk=pk)
    if request.method == 'POST':
        form = formOperation(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect(reverse('Read')) #Use reverse
        else:
            return render(request, 'Details.html', {'form': form})
    else:
        form = formOperation(instance=data)
        return render(request, 'Details.html', {'form': form})

def Delete_data(request, pk):  # Corrected name
    try:
        operation = get_object_or_404(Operation, pk=pk)
    except Operation.DoesNotExist:
        return render(request, 'object_not_found.html', {'message': "Operation not found"})

    if request.method == 'POST':
        operation.delete()
        return redirect(reverse('Read'))  # Use reverse
    else:
        return render(request, 'Delete.html', {'operation': operation})