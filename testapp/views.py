from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from testapp.forms import *
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.forms.models import model_to_dict
from graphos.sources.model import *
from graphos.renderers import gchart
from django.contrib.auth.decorators import login_required
import cv2,time
def priupdate(request,pk):
    x=prisoner.objects.get(pk=pk)
    if request.method == 'POST':
        form=prisonerform(request.POST,request.FILES,instance=x)
        if(len(request.POST['prisoner_aadhar_no'])!=12):
            messages.warning(request,'Invalid Aadhar No.')
            return redirect('addprisoner')
        if form.is_valid():
            form.save()
            messages.success(request,'Prisoner Updated Sucessfully')
            return redirect('home')
    else:
        form=prisonerform(initial=model_to_dict(x))
    return render(request,'testapp/prisoner.html',{'form': form})
def capture(request):
    video=cv2.VideoCapture(0)
    a=0
    key=None
    while(True):
        a=a+1
        check,frame=video.read()
        cv2.imshow("Capturing",frame)
        key=cv2.waitKey(1)
        if key==ord('q'):
            break
    video.release()
    cv2.destroyAllWindows
def register(request):
    if request.method == 'POST':
        form=userform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Account has been successfully created')
            return redirect('login')
    else:
        form= userform()
    return render(request,'testapp/register.html',{'form': form})
@login_required
def home(request):
    return render(request, 'testapp/home.html')
@login_required
def fir(request):
    if request.method == 'POST':
        form=firform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'F.I.R Sucessfully Added!!')
            return redirect('home')
    else:
        form=firform()
    return render(request,'testapp/fir.html',{'form': form})
@login_required
def addprisoner(request):
    if request.method == 'POST':
        form=prisonerform(request.POST,request.FILES)
        if(len(request.POST['prisoner_aadhar_no'])!=12):
            messages.warning(request,'Invalid Aadhar No.')
            return redirect('addprisoner')
        if form.is_valid():
            form.save()
            messages.success(request,'Prisoner Added Sucessfully')
            return redirect('home')
    else:
        form=prisonerform()
    return render(request,'testapp/prisoner.html',{'form': form})
@login_required
def addvisitor(request):
    if request.method == 'POST':
        form=visitorform(request.POST,request.FILES)
        if(len(request.POST['visitor_aadhar_no'])!=12 or len(request.POST['prisoner_aadhar_no'])!=12 ):
            messages.warning(request,'Invalid Aadhar No.')
            return redirect('addprisoner')
        if form.is_valid():
            form.save()
            allvisitors.objects.get_or_create(name=request.POST['name'],visitor_aadhar_no=request.POST['visitor_aadhar_no'],prisoner_aadhar_no=request.POST['prisoner_aadhar_no'],date_of_visit=request.POST['date_of_visit'],image=form.files['image'])
            messages.success(request,'Visitor Added Sucessfully')
            return redirect('home')
    else:
        form=visitorform()
    return render(request,'testapp/visitors.html',{'form': form})
@login_required
def addguard(request):
    if request.method == 'POST':
        form=guardform(request.POST,request.FILES)
        if(len(request.POST['guard_aadhar_no'])!=12):
            messages.warning(request,'Invalid Aadhar No.')
            return redirect('addguard')
        if form.is_valid():
            form.save()
            messages.success(request,'Guard Added Sucessfully')
            return redirect('home')
    else:
        form=guardform()
    return render(request,'testapp/guard.html',{'form': form})
@login_required
def graphcrime(request):
    data=[['Crime','No Of Cases']]
    a=prisoner.objects.all()
    b=a.values('crime').distinct()
    for i in b:
        q=prisoner.objects.filter(crime=i['crime'])
        lst=[]
        lst.append(str(i['crime']))
        lst.append(len(q))
        data.append(lst)
    data_source1 = SimpleDataSource(data)
    chart1 = gchart.AreaChart(data_source1,options={'title':'Crime Number Analysis'})
    return render(request,'testapp/graph2.html',{'chart1':chart1})
@login_required
def crimeinput(request):
    if request.method == 'POST':
        crime=request.POST['Crime']
        data=[['Year','No of '+crime]]
        a=prisoner.objects.all()
        year=[]
        for i in a:
            year.append(i.date_of_entry.year)
        year=list(set(year))
        year.sort()
        for i in year:
            lst=[]
            temp=prisoner.objects.filter(crime=crime,date_of_entry__year=str(i))
            lst.append(str(i))
            lst.append(len(temp))
            data.append(lst)
        data_source1 = SimpleDataSource(data)
        chart1 = gchart.ColumnChart(data_source1, options= {'isStacked': False,'legend': {'position': 'bottom'}, 'series': [{'color': '#DB4437'},{'color': '#DB4437'}]})
        return render(request,'testapp/graph.html',{'chart1':chart1})
    else:
        form=crimeform()
    return render(request,'testapp/crimeform.html',{'form': form})
@login_required
def show(request,pk):
    a=prisoner.objects.get(id=pk)
    print(a.image.url)
    return render(request,'testapp/show.html',{'a':a})
@login_required
def displaypri(request):
    a=prisoner.objects.all()
    return render(request,"testapp/displaypri.html",{'a':a})
@login_required
def displayvis(request):
    a=visitor.objects.all()
    return render(request,"testapp/displayvis.html",{'a':a})
