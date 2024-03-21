from django.shortcuts import render,redirect
from Backend.models import ProductDb,CategoryDb
from Frontend.models import ContactDb,RedisterDb,CartDb,CheckoutDb


# Create your views here.
def Frontend_page(request):
    pro = ProductDb.objects.all()
    cat = CategoryDb.objects.all()
    return render(request,"Homepage.html", {'pro':pro, 'cat':cat})

def product_page(request, catname):
    pro = ProductDb.objects.filter(Category_Name=catname)
    cat = CategoryDb.objects.all()
    return render(request,"product.html",{'pro':pro,'cat':cat})

def single_product(request,proid):
    pro = ProductDb.objects.get(id=proid)
    cat = CategoryDb.objects.all()
    return render(request,"singleproduct.html",{'pro':pro, 'cat':cat})

def contact_page(request):
    return render(request,"contact_table.html")

def Contact_save(request):
    if request.method == "POST":
        x = request.POST.get("Name")
        y = request.POST.get("Email_id")
        z = request.POST.get("Subject")
        m = request.POST.get("Message")
        obj = ContactDb(Name=x, Email_id=y,Subject=z, Message=m )
        obj.save()
        return redirect(contact_page)

def Userlogin(request):
    return render(request,"userlogin.html")

def User_save(request):
    if request.method == "POST":
        x = request.POST.get("Name")
        y = request.POST.get("Email_id")
        z = request.POST.get("Password")
        obj = RedisterDb(Name=x, Email_id=y,Password=z, )
        obj.save()
        return redirect(Userlogin)

def Admin_login(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        if RedisterDb.objects.filter(Name=un,Password=pwd).exists():
            request.session['Name'] = un
            request.session['Password'] = pwd
            return redirect(Frontend_page)
        else:
            return redirect(Userlogin)
    else:
        return redirect(Userlogin)

def Cart(request):
    data = CartDb.objects.filter(Username=request.session['Name'])
    total_price = 0
    for i in data:
        total_price = total_price+i.Totalprice
    return render(request,"Cart.html",{'data':data,'total_price':total_price})

def car_save(request):
    if request.method == "POST":
        x = request.POST.get("Username")
        y = request.POST.get("Productname")
        o = request.POST.get("Quantity")
        z = request.POST.get("Price")
        m = request.POST.get("Totalprice")
        obj = CartDb(Username=x, Productname=y, Quantity=o, Price=z, Totalprice=m )
        obj.save()
        return redirect(Cart)


def Checkout(request):
    data = CartDb.objects.filter(Username=request.session['Name'])
    total_price = 0
    for i in data:
        total_price = total_price + i.Totalprice
    return render(request,"checkout.html",{'data':data, 'total_price':total_price})

def checkout_save(request):
    if request.method == "POST":
        x = request.POST.get("Name")
        y = request.POST.get("State")
        o = request.POST.get("Street_Address")
        z = request.POST.get("Town")
        m = request.POST.get("Postcode")
        n = request.POST.get("Phone")
        p = request.POST.get("Email_Address")
        obj = CheckoutDb(Name=x, State=y, Street_Address=o, Town=z, Postcode=m, Phone=n, Email_Address=p,)
        obj.save()
        return redirect(Checkout)