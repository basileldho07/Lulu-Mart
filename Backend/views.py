from django.shortcuts import render,redirect
from Backend.models import CategoryDb,ProductDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from Frontend.models import ContactDb
from django.contrib import messages

# Create your views here.
def lulu_page(request):
    return render(request,"index.html")
def Category(request):
    return render(request,"Addcategory.html")

def Category_save(request):
    if request.method == "POST":
        x = request.POST.get("Name")
        y = request.POST.get("Description")
        img = request.FILES['image']
        obj = CategoryDb(Name=x, Description=y, ProfileImage=img)
        obj.save()
        messages.success(request,"category.saved successfully")
        return redirect(Category)

def Display_category(request):
    cat = CategoryDb.objects.all()
    return render(request,"Display_category.html",{'cat': cat})

def Edit_category(request,p_id):
    std = CategoryDb.objects.get(id=p_id)
    return render(request,"Edit_category.html",{'std':std})

def uptade_category(request,p_id):
    if request.method == "POST":
        x = request.POST.get("Name")
        y = request.POST.get("Description")
        try:
            f = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(f.name,f)
        except MultiValueDictKeyError:
            file = CategoryDb.objects.get (id=p_id).ProfileImage
        CategoryDb.objects.filter(id=p_id).update(Name=x, Description=y, ProfileImage=file)
        return redirect(Display_category)

def Product(request):
    data = CategoryDb.objects.all()
    return render(request, "Addproducts.html", {'data':data})

def Product_save(request):
    if request.method == "POST":
        x = request.POST.get("Category_Name")
        y = request.POST.get("Products_Name")
        z = request.POST.get("Price")
        m = request.POST.get("Description")
        img = request.FILES['image']
        obj = ProductDb(Category_Name=x, Products_Name=y, Price=z, Description=m, ProductImage=img)
        obj.save()
        return redirect(Product)

def Display_products(request):
    pro = ProductDb.objects.all()
    return render(request,"Display_products.html",{'pro': pro})

def Edit_products(request,c_id):
    edi = ProductDb.objects.get(id=c_id)
    return render(request,"Edit_products.html",{'edi':edi})

def uptade_products(request,c_id):
    if request.method == "POST":
        x = request.POST.get("Category_Name")
        y = request.POST.get("Products_Name")
        z = request.POST.get("Price")
        m = request.POST.get("Description")
        try:
            f = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(f.name,f)
        except MultiValueDictKeyError:
            file = ProductDb.objects.get (id=c_id).ProductImage
        ProductDb.objects.filter(id=c_id).update(Category_Name=x, Products_Name=y, Price=z, Description=m, ProductImage=file)
        return redirect(Display_products)

def Delete_products(request,c_id):
    edi = ProductDb.objects.get(id=c_id)
    edi.delete()
    return redirect(Display_products)

def Admin_login_page(request):
    return render(request,"loginpage.html")

def Adminlogin(request):
    if request.method == "POST":
        a = request.POST.get("user")
        b = request.POST.get("password")
        if User.objects.filter(username__contains=a).exists():
            x = authenticate(username=a, password=b)
            if x is not None:
                login(request, x)
                request.session['username'] = a
                request.session['password'] = b

                return redirect(lulu_page)
            else:
                return redirect(Admin_login_page)
        else:
            return redirect(Admin_login_page)




def Adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(Admin_login_page)

def Dispaly_contact(request):
    Dis = ContactDb.objects.all()
    return render(request,"display_contact.html",{'Dis':Dis})