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

client = pymongo.MongoClient("mongodb://tushar567:tushar567@cluster0-shard-00-00.es6qd.gcp.mongodb.net:27017,cluster0-shard-00-01.es6qd.gcp.mongodb.net:27017,cluster0-shard-00-02.es6qd.gcp.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
# Create your views here.
mydb = client['Grocery']
userTable=mydb['userTable']
groceryTable=mydb['groceryTable']
userSessions=mydb['userSession']



def index(request):
    return render(request,"index.html")

def register(request):
    return render(request,"register.html")

def signup(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    uname = request.POST['uname']
    password = request.POST['password']
    x = userTable.find_one({"uname": uname})
    print(x)
    if x:
        return render(request, "register.html", context={"success_status": 0})
    else:
        userTable.insert_one(
            {"fname": fname, "lname": lname, "uname": uname, "password": password})
        return render(request, "index.html", context={"success_status": 1})
    return HttpResponse("wait")


def login(request):
    flag=0
    try:
        del_flag=userSessions.find_one({"user_key":request.session['user_key'],"username":request.session['username']})
        if del_flag==None:
            del request.session['user_key']
            del request.session['username']
            del request.session['password']
            return render(request,"index.html")
        else:
            uname=request.session['username']
            password=request.session['password']		
    except:
        try:
            uname = request.POST['username']
            password = request.POST['password']
            flag=1
        except:
            return render(request, "index.html")
    x = userTable.find_one({"uname": uname, "password": password})
    print(flag)
    if x:
        if flag==1:
            request.session['username'] = uname
            request.session['password'] = password
            sp_key=''.join(random.choice(string.ascii_uppercase + string.digits)for _ in range(20))
            db_sessions=list(userSessions.find({"username":uname},{"user_key":1}))
            while(sp_key in db_sessions):
                sp_key=''.join(random.choice(string.ascii_uppercase + string.digits))
            request.session['user_key']=sp_key
            db_dict={'username':uname,'password':password,'user_key':sp_key}
            userSessions.insert_one(db_dict)
        else:
            sp_key=request.session['user_key']         
        l_user = userTable.find_one({"uname": uname,"password":password})
        A_db_sessions=list(userSessions.find({"username":uname}))
        userData={"user_data":l_user,"active_session_data":A_db_sessions,"this_session_key":sp_key}
            
        print(userData)
        return render(request, "dashboard.html", context={"userData": userData,"reset_code": 3})
    else:
        return HttpResponse("Invalid")
