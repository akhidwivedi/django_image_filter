from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
from .forms import ImageForm
from .models import Category

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST or None, request.FILES or None)
        if form.is_valid:
            form.save()
        return render(request,'home.html',{'form':form})
    else:
        form = ImageForm()
    return render(request,'home.html',{'form':form})
    
def index(request):
    image = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        image = Image.get_all_images_by_id(categoryID)
    else:
        image = Image.get_all_images()
    data = {}
    data['image'] = image
    data['categories'] = categories
    
    return render(request,'index.html',data)