from datetime import timezone
import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from . models import*
from django.core.files.storage import FileSystemStorage
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.
def home(request):
    return render(request,"home.html")





def loginpage(request):
    if request.method=="POST":
        uname=request.POST['uname']
        psw=request.POST['password']
        print(uname,psw,"=================")
        try:
            a=login.objects.get(username=uname,password=psw)
            print(a,"----------")
            if a:
                type=a.usertype
                request.session['login_id']=a.pk
                if type=='admin':
                    return HttpResponse("<script>alert('login successfull');window.location='/adminhome'</script>")
                elif type=='staff':
                    b=staff.objects.get(login_id=request.session['login_id'])
                    request.session['staff']=b.pk
                    return HttpResponse("<script>alert('login successfull');window.location='/shophome'</script>")

                        
        except:
            return HttpResponse("<script>alert('invalid');window.location='/login'</script>")
    
    return render(request,"login.html")



def adminhome(request):
    return render(request,"adminhome.html")


def manage_staffs(request):
    c=staff.objects.all()
    if'submit'in request.POST:
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        place=request.POST['place']
        district=request.POST['district']
        pincode=request.POST['pincode']
        phone_no=request.POST['phone_no']
        username=request.POST['username']
        password=request.POST['password']
        
        a=login(username=username,password=password,usertype='staff')
        a.save()
        b=staff(first_name=first_name,last_name=last_name,email=email,place=place,district=district,pincode=pincode,phone_no=phone_no,login_id=a.pk)
        b.save()
        return HttpResponse("<script>alert('STAFF REGISTRED SUCCESSFULLY');window.location='/manage_staffs'</script>")

        
    return render(request,"manage_staffs.html",{'c':c})