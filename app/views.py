from django.shortcuts import render,redirect

from .models import Task
# Create your views here.
def index(request):
     data=Task.objects.all()
     print(data)
     context={"data":data}
     return render(request,"index.html",context)

def insertdata(request):
   
    if request.method=="POST":
        title=request.POST.get('title')
        description=request.POST.get('description')
        status=request.POST.get('status')
        duedate=request.POST.get('duedate')
        print(title,description,status,duedate)
        query=Task(title=title,description=description,status=status,duedate=duedate)
        query.save()
    return render(request,"index.html")

def updateData(request,id):
     if request.method=="POST":
        title=request.POST.get('title')
        description=request.POST.get('description')
        status=request.POST.get('status')
        duedate=request.POST.get('duedate')

        edit=Task.objects.get(id=id)
        edit.title=title
        edit.description=description
        edit.status=status
        edit.duedate=duedate
        edit.save()
        return redirect("/")

     d=Task.objects.get(id=id)
     context={"d":d}

     return render(request,"edit.html",context)

def deleteData(request,id):
    d=Task.objects.get(id=id)
    d.delete()
    return redirect("/")

    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")
