from django.shortcuts import render,redirect
from adminapp.models import*
from.models import*

# Create your views here.
def userindex(request):
    data = Branches.objects.all()
    cata = Salons.objects.all()
    cat=Services.objects.all()
    dt=Branches.objects.all()
    return render(request, 'userindex.html', {'data': data, 'cata': cata, 'cat':cat, 'dt':dt})

def contact(request):
    return render(request,'contact.html')
def login(request):
    return render(request,'login.html')
def about(request):
    return render(request,'about.html')
def branch(request):
    data=Branches.objects.all()
    return render(request,'branches.html',{'data':data})
def register(request):
    return render(request,'register.html')

def registerdata(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        password=request.POST['password']
        data=Register(name=name,phone=phone,email=email,password=password)
        data.save()
        return redirect('register')
def contactdata(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        data=Contact(name=name,email=email,message=message)
        data.save()
        return redirect('contact')
def logindata(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        data=Login(name=name,password=password)
        data.save()
        return redirect('login')
    
def publicdata(request):
    if request.method == "POST":
        email=request.POST.get('name')
        password=request.POST.get('password')
        if Register.objects.filter(email=email,password=password).exists():
           data = Register.objects.filter(email=email,password=password).values('name','phone','id').first()
           request.session['name_u'] = data['name']
           request.session['u_id'] = data['id']
           request.session['phonenumber_u'] = data['phone'] 
           request.session['email_u'] = email
           request.session['password_u'] = password
           return redirect('userindex') 
        else:
            return render(request,'login.html',{'msg':'Invalid user credentials'})
    else:
        return redirect('userindex')

def userlogout(request):
    del request.session['name_u']
    del request.session['u_id']
    del request.session['phonenumber_u']
    del request.session['email_u']
    del request.session['password_u']
    return redirect('login')

def salons(request,category):
    if(category=="all"):
        data=Salons.objects.all()
    else:
        data=Salons.objects.filter(branch=category)
        
    return render(request,'salons.html',{'data':data})

def services(request,cat):
    if(cat=="all"):
        data=Services.objects.all()
    else:
        data=Services.objects.filter(salonname=cat)
    return render(request,'services.html',{'data':data})


def single(request,id):
    data=Services.objects.filter(id=id)
    return render(request,'singleitem.html',{'data':data})
def book(request,id):
    data=Services.objects.filter(id=id)
    return render(request,'book.html',{'data':data})

def bookdata(request,id):
    if request.method=='POST':
        userid=request.session.get('u_id')
        date=request.POST.get('date')
        time=request.POST.get('time')
        data=Book(userid=Register.objects.get(id=userid),serviceid=Services.objects.get(id=id),date=date,time=time)
        data.save()
        return redirect('history')

def history(request):
    user_id=request.session.get('u_id')
    data=Book.objects.filter(userid=user_id)
    return render(request,'history.html',{'data':data})