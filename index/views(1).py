from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from .forms import ItemForm
from .models import Item

def Item_list(request):    
    items=Item.objects.all()
    return render(request,'item_list.html',{'items':items})

def upload_item(request):
    if request.method =='POST':
        form=ItemForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('items/')
    else:
        form=ItemForm()
    return render(request,'upload_item.html',{'form':form})

def delete_item(request, pk):
    if request.method=='POST':
        item=Item.objects.get(pk=pk)
        item.delete()
    return redirect('items/')
