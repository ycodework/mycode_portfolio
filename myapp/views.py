from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'item_form.html', {'form': form})
