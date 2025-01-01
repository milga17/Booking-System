from django.shortcuts import render,redirect
from.models import*
from bookingapp.models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def adminindex(request):
    register=Register.objects.all().count()
    branch=Branches.objects.all().count()
    salon=Salons.objects.all().count()
    service=Services.objects.all().count()
    message=Contact.objects.all().count()
    booking=Book.objects.all().count()
    accept=Book.objects.filter(status=1).count()
    reject=Book.objects.filter(status=2).count()
    wait=Book.objects.filter(status=0).count()
    return render(request,'adminindex.html',{'register':register,'branch':branch,'salon':salon,'service':service,'message':message,'booking':booking,'accept':accept,'reject':reject,'wait':wait})
   
def addbranches(request):
    return render(request,'addbranches.html')
def addsalons(request):
    data=Branches.objects.all()
    return render(request,'addsalons.html',{'data':data})
def addservices(request):
    data=Salons.objects.all()
    return render(request,'addservices.html',{'data':data})
def branchdata(request):
    if request.method=='POST':
        name=request.POST['bname']
        image=request.FILES['image']
        data=Branches(name=name,image=image)
        data.save()
    return redirect('addbranches')
def salondata(request):
    if request.method=='POST':
        name=request.POST['sname']
        branch=request.POST['branchname']
        image=request.FILES['image']
        data=Salons(name=name,branch=branch,image=image)
        data.save()
    return redirect('addsalons')
def servicedata(request):
    if request.method=='POST':
        servicename=request.POST['sename']
        salonname=request.POST['salname']
        price=request.POST['sprice']
        image=request.FILES['image']
        data=Services(servicename=servicename,salonname=salonname,price=price,image=image)
        data.save()
        return redirect('addservices')
def branchtable(request):
    data=Branches.objects.all()
    return render(request,'branchtable.html',{'data':data})
def salontable(request):
    data=Salons.objects.all()
    return render(request,'salontable.html',{'data':data})
def servicetable(request):
    data=Services.objects.all()
    return render(request,'servicetable.html',{'data':data})
def editb(request,id):
    data=Branches.objects.filter(id=id)
    return render(request,'editbran.html',{'data':data})
def deleteb(request,id):
    Branches.objects.filter(id=id).delete()
    return redirect('branchtable')
def updateb(request,id):
    if request.method=='POST':
        name=request.POST['bname']
        try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Branches.objects.get(id=id).image
        Branches.objects.filter(id=id).update(name=name,image=file)
        return redirect('branchtable')
def editl(request,id):
    data=Branches.objects.all()
    dat=Salons.objects.filter(id=id)
    return render(request,'editsalon.html',{'data':data,'dat':dat})
def deletel(request,id):
    data=Salons.objects.filter(id=id).delete()
    return redirect('salontable')
def updatesal(request,id):
    if request.method=='POST':
        name=request.POST['sname']
        branch=request.POST['branchname']
        try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Salons.objects.get(id=id).image
        Salons.objects.filter(id=id).update(name=name,branch=branch,image=file)
        return redirect('salontable')
def edits(request,id):
    cata=Salons.objects.all()
    cat=Services.objects.filter(id=id)
    return render(request,'editservice.html',{'cata':cata,'cat':cat})
def deletes(request,id):
    data=Services.objects.filter(id=id).delete()
    return redirect('servicetable')
def updateser(request,id):
    if request.method=='POST':
        servicename=request.POST['sename']
        salonname=request.POST['salname']
        price=request.POST['sprice']
        try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Services.objects.get(id=id).image
        Services.objects.filter(id=id).update(servicename=servicename,salonname=salonname,price=price,image=file)
        return redirect('servicetable')
def registertable(request):
    data=Register.objects.all()
    return render(request,'registertable.html',{'data':data})
def contacttable(request):
    data=Contact.objects.all()
    return render(request,'contacttable.html',{'data':data})
def logintable(request):
    data=Login.objects.all()
    return render(request,'logintable.html',{'data':data})
def viewuser(request):
    data=Book.objects.filter(status=0)
    return render(request,'bookingtable.html',{'data':data})
def accept(request,id):
    Book.objects.filter(id=id).update(status=1)
    return redirect('approvedtable')
def reject(request,id):
    Book.objects.filter(id=id).update(status=2)
    return redirect('declinedtable')
def approvedtable(request):
    data=Book.objects.filter(status=1)
    return render(request,'approvedtable.html',{'data':data})
def declinedtable(request):
    data=Book.objects.filter(status=2)
    return render(request,'declinedtable.html',{'data':data})
def declinedtable(request):
    data=Book.objects.filter(status=2)
    return render(request,'declinedtable.html',{'data':data})