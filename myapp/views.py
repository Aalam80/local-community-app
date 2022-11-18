
from django.shortcuts import render,redirect,get_object_or_404
from .forms import serviceform, Queryform, cntactform,Userregistrationform
from myapp.models import banner, services, catogary,Queries,Contact,serviceQuery ,banner
from django.contrib import messages



# Create your views here.
def index(request):
    return render(request,'myapp/index.html')


def all_services(request):
    services_data= catogary.objects.filter()[:3]
    # services_data[1]
    return render(request,'myapp/index.html', {'data':services_data})

def read(request,pk):
    cat=catogary.objects.get(pk=pk)
    serv=services.objects.filter(catogary=cat)
    return render(request ,'myapp/service_detail_page.html', {'cat':cat,'serv':serv})



def About_Us(request):
    return render(request,'myapp/About_Us.html')

def Contact_Us(request):
    if request.method=='POST':
        data=cntactform(request.POST)
        if data.is_valid():
            f_data=data.save()
            return redirect('Contact_Us')
    else:
        data=cntactform()
    return render(request,'myapp/Contact_Us.html',{'data':data})



def add_services(request):
    if request.method=='POST':
        data=serviceform(request.POST)
        if data.is_valid():
            f_data=data.save()
            return redirect('index')
    else:
        data=serviceform()
    return render(request,'myapp/add_services.html',{'data':data})



def service(request):
    service_data= catogary.objects.all()
    return render(request,'myapp/services.html', {'data':service_data})


def service_detail(request,pk):
    Service=get_object_or_404(services,pk=pk)
    Querypost=serviceQuery.objects.filter(Service=Service , parant=None)
    replies=serviceQuery.objects.filter(Service=Service ).exclude(parant=None)
    repdict={}
    for reply in replies:
        if reply.parant.sno not in repdict.keys():
            repdict[reply.parant.sno]=[reply]
        else:
            repdict[reply.parant.sno].append(reply)


    return render(request,'myapp/service_info.html',{'s_data':Service, 'Querypost':Querypost,'repdict':repdict})






def Queris(request):
    queris_data= Queries.objects.filter(reply=None).order_by('-id')

    Query_data=Queryform()
    
    if request.method=='POST':
        Query_data=Queryform(request.POST )
        if Query_data.is_valid:
            Query_detail=request.POST.get('Query_detail')
            reply_id=request.POST.get('Queries_id')
            Query_as=None
            if reply_id:
                Query_as=Queries.objects.get(id=reply_id)
            query=Queries.objects.create(user=request.user, Query_detail=Query_detail, reply=Query_as)
            reply=None

            query.save()
            return redirect('Queris')
    else:
        Query_data=Queryform()
    return render(request,'myapp/Queries.html',{'queris_data':queris_data,'Query_data':Query_data,})
  

def serQuery(request):
    if request.method=='POST':
      Query_Detail=request.POST.get('Query_Detail')
      print(f'Query Detail {Query_Detail}')
      user=request.user
      ServiceID=request.POST.get('ServiceID')
      Service=services.objects.get(id=ServiceID)
      parantSno=request.POST.get('parantSno')
      if parantSno =="":
        Query_Detail=serviceQuery(Query_Detail=Query_Detail,user=user,Service=Service)
        
      else:
        parant=serviceQuery.objects.get(sno=parantSno)
        Query_Detail=serviceQuery(Query_Detail=Query_Detail,user=user,Service=Service,parant=parant)
      Query_Detail.save()
      messages.success(request,'your query posted successfully')
    return redirect('/')

        



    
def register_user(request):
    if request.method=='POST':
        form =Userregistrationform (request.POST)#capturing form data
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account create succsefully for {username}')
            return redirect('/')

    else:
        form= Userregistrationform ()
    return render(request,'registration/register.html',{'form': form})




def display_imgg(request):

        # getting all the objects of hotel.
        bnner = banner.objects.all() 
        return render(request, 'myapp/index.html',{'dis_imaggg' : bnner})