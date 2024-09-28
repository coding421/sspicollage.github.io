from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    data=tbl_notice.objects.all().order_by('-id')[0:5]
    data1=tbl_feedback.objects.all().order_by('-id')[0:4]
    sdata=tbl_slider.objects.all().order_by('-id')[0:3]
    md={"ndata":data,"fdata":data1,"sliderdata":sdata}
    return render(request,'index.html',md)

def about(request):
    return render(request,'about.html')

def alumni(request):
    data=tbl_alumni.objects.all().order_by('-id')
    md={'adata':data}
    return render(request,'alumni.html',md)

def contact(request):

    mydict={}
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('mobile')
        d=request.POST.get('subject')
        e=request.POST.get('msg')
        contactus(Name=a,Email=b,Mobile=c,Subject=d,Message=e).save()
        return HttpResponse("<script> alert('Data Saved Successfully');location.href='/contact/' </script>")

        #mydict={"name":a, "email":b, "mobile":c, "subject":d, "message":e}

    return render(request, 'contact.html', mydict)

def cources(request):
    data=tbl_cources.objects.all()
    md={'data':data}
    return render(request,'cources.html',md)
def faculty(request):
    data=tbl_faculty.objects.all().order_by('-id')
    md={'fdata':data}
    return render(request,'faculty.html',md)

def feedback(request):
    if request.method=="POST":
        Name=request.POST.get('name')
        Picture=request.FILES['fu']
        Message=request.POST.get('message')
        tbl_feedback(name=Name,feedback=Message,picture=Picture).save()
        return HttpResponse("<script>alert('Thanks for your valuable feedback..');location.href='/feedback/' </script>")
    return render(request,'feedback.html')

def gallery(request):
    data=tbl_gallery.objects.all().order_by('-id')[0:21]
    mydict={'gdata':data}
    return render(request,'gallery.html',mydict)

def infra(request):
    data=tbl_infra.objects.all().order_by('-id')
    md={"idata":data}

    return render(request,'infra.html',md)

def recruiters(request):
    data=tbl_recruiter.objects.all().order_by('-id')
    md={'gdata': data}
    return render(request,'recruiters.html',md)
def principal(request):
    return render(request,'principal.html')

def portfolio(request):
    return render(request,'myprofile.html')