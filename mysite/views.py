from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.contrib.sessions.models import Session
import json
import string
import random
import pymongo
from django.urls import reverse
from mysite.models import userTable,userSession,usergr 



def logoff(request):
    try:
        print(request.session['username'])
        del request.session['user_key']
        del request.session['username']
        del request.session['password']
    except:
        pass
    return HttpResponseRedirect(reverse("index"))


def search(request):
    try:
        print(request.session['username'])
        s_date=request.POST['s_date']
        print(request.POST['s_date'])
        l_user = userTable.objects.get(username=request.session['username'],password=request.session['password'])
        A_db_sessions=list(userSession.objects.filter(username=request.session['username']))
        gr_data = usergr.objects.filter(username=request.session['username'], item_date=s_date)
        userData={"user_data":l_user,"active_session_data":A_db_sessions,"this_session_key":request.session['user_key'],"gr_data":gr_data}   
        print(userData)
        return render(request, "dashboard.html", context={"userData": userData,"reset_code": 3})
    except:
        return render(request, "index.html")



def addgr(request):
    try:
        print(request.session['username'])
        gr_obj=usergr()
        gr_obj.username=userTable.objects.get(username=request.session['username'])
        gr_obj.item_name=request.POST['Item_name']
        gr_obj.item_quan = request.POST['Item_quan']
        gr_obj.item_status = request.POST.get('optradio')
        gr_obj.item_date = request.POST['Item_date']
        gr_obj.save()
        return HttpResponseRedirect(reverse("login"))
    except:
        return render(request, "index.html")


def index(request):
    try:
        print(request.session['username'])
        return HttpResponseRedirect(reverse("login"))
    except:
        return render(request,"index.html")

def register(request):
    return render(request,"register.html")


def signup(request):
    print(request.POST)
    try:
        check_ex=userTable.objects.get(username=request.POST['uname'])
        return render(request, "register.html", context={"success_status": 0})
    except:
        print("i am here")
        pp=userTable()
        print(request.POST['uname'])
        pp.username=request.POST['uname']
        pp.password=request.POST['password']
        pp.fname=request.POST['fname']
        pp.lname=request.POST['lname']
        pp.save()
        return render(request, "index.html", context={"success_status": 1})

    

def login(request):
    flag=0
    try:
        del_flag = userSession.objects.get(username=request.session['username'], user_key=request.session['user_key'])
        uname=request.session['username']
        password=request.session['password']
    except:
        try:
            print(request.session['user_key'])
            del request.session['user_key']
            del request.session['username']
            del request.session['password']
            return render(request,"index.html")
        except:
            try:
                print("gotcha")
                uname = request.POST['username']
                password = request.POST['password']
                flag=1   
            except:
                return render(request, "index.html")
    print(uname,password)
    try:
        userTable.objects.get(username=uname,password=password)
        print("userFound")
        if flag==1:
            request.session['username'] = uname
            request.session['password'] = password
            sp_key=''.join(random.choice(string.ascii_uppercase + string.digits)for _ in range(20))
            try:
                db_sessions=userSession.objects.get(username=uname,user_key=sp_key)
                sp_key=''.join(random.choice(string.ascii_uppercase + string.digits)for _ in range(20))
            except:
                request.session['user_key'] = sp_key
                bb=userSession()
                bb.username=uname
                bb.password=password
                bb.user_key=sp_key
                bb.save()
        else:
            sp_key=request.session['user_key']         
        l_user = userTable.objects.get(username=uname,password=password)
        A_db_sessions=list(userSession.objects.filter(username=uname))
        gr_data=usergr.objects.filter(username=uname)
        userData={"user_data":l_user,"active_session_data":A_db_sessions,"this_session_key":sp_key,"gr_data":gr_data}   
        print(userData)
        return render(request, "dashboard.html", context={"userData": userData,"reset_code": 3})
    except:
        return render(request, "index.html")


def delgr(request):
    try:
        print(request.session['username'])
        old_data=request.POST['o_data'].split(",")
        pp=userTable.objects.get(username=request.session['username'])
        gr_obj = usergr.objects.filter(username=pp,item_quan=old_data[0],item_name=old_data[1],item_status=old_data[2],item_date=request.POST['o_date1']).delete()
        return HttpResponseRedirect(reverse("login"))
    except:
        return render(request, "index.html")





def updateGr(request):
    try:
        print(request.session['username'])
        old_data=request.POST['o_data'].split(",")
        print(request.POST['Item_date'])
        pp=userTable.objects.get(username=request.session['username'])
        gr_obj = usergr.objects.filter(username=pp,item_quan=old_data[0],item_name=old_data[1],item_status=old_data[2],item_date=request.POST['o_date1'])
        gr_obj.update(username=pp, item_quan=request.POST['Item_quan'], item_name=request.POST['Item_name'],item_status=request.POST.get('optradio'), item_date=request.POST['Item_date'])
        return HttpResponseRedirect(reverse("login"))
    except:
        return render(request, "index.html")









    
