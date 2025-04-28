from django.shortcuts import render,redirect
from django.urls import reverse  
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import random
import string
import json
from .models import OwnerdataBase,HosteldataBase,RoomDataBase,HostellerDataBase
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST
from .Serializers import OwnerDataSerializer,HostelDataSerializer,RoomDataSerializer,HostellerDataSerializer
# Create your views here.
otp_saver=dict()


@api_view(['POST'])
def OwnerData(request,email):
    print('ownerdata is called')
    if request.method=='POST':
        print(request.data)
        print('post method called')
        data=request.data.copy()
        id=random.randint(10001,99999)
        data['mail_id']=email
        data['owner_id']=id
        owner_serial=OwnerDataSerializer(data=data)
        print(owner_serial)
        if owner_serial.is_valid():
            print("is valid called")
            owner_serial.save()
            name=request.data['name']
            subject='Registration Succesful'
            msg=f"Dear {name},\nThank you for registering the *Hostel4U*"
            send_mail(subject=subject,message=msg,from_email=settings.EMAIL_HOST_USER,recipient_list=[email])
            return Response(owner_serial.data,status=HTTP_201_CREATED)
        else:
            print(owner_serial.errors)
            return Response(owner_serial.errors,status=HTTP_400_BAD_REQUEST)
        
        #return render(request,'OwnerApp/login.html')
    #return render(request,'OwnerApp/ownerdata.html',{'mail':email})


def Otp_genarator():
    x = ''.join(random.choices(string.ascii_uppercase, k=2))
    y=str(random.randint(101,999))
    z=''.join(random.choices(string.ascii_lowercase, k=2))
    otp=x+y+z+'H'
    return otp


@api_view(['POST'])
def Otpverify(request,email):
    if request.method == 'POST':
        rec_otp=request.data['otp']
        #print(rec_otp,email)
        if otp_saver.get(email) == rec_otp:
            gmail={
            "mailid":email
                }
            email=json.dumps(gmail)
            return Response(gmail,status=200)
            #return render(request,'OwnerApp/ownerdata.html',{'gmail':email})
            #return redirect(reverse('ownerdataurl',args=[email]))
        else:
            return Response(status=401)
            
        #return render(request,'Ownerapp/Ownerdata.html')
        
@api_view(['POST','GET'])
def OwnerSignup(request):
    if request.method=='POST':
        otp=Otp_genarator()
        to_email=request.data['mailid']       
        otp_saver[to_email]=otp
        subject='Authentication for registartion'
        msg=f"Dear User,\n Your One Time Passcode for completing your registration is {otp}.\nPlease use this Passcode  to complete your registration.\nThank you,\nHostel4U Team"
        send_mail(subject=subject,message=msg,from_email=settings.EMAIL_HOST_USER,recipient_list=[to_email])
        gmail={
            "mailid":to_email
        }
        mail=json.dumps(gmail)
        return Response(gmail,status=200)
        #print(otp,to_email,subject,msg,settings.EMAIL_HOST_USER)
        #return render(request,'Ownerapp/otp.html',{'email':to_email})
    return render(request,'OwnerApp/signup.html')

@api_view(['POST'])
def Login(request):
    try:
        user=OwnerdataBase.objects.get(mail_id=request.data['mail_id'])
    except OwnerdataBase.DoesNotExist:
        return Response(status=404)
    else:
        if user.password !=request.data['password']:
            return Response(status=401)
        else:
            print(user.owner_id)
            ownerid={
                "ownerid":user.owner_id
            }
            userid=json.dumps(ownerid)
            return Response(ownerid,status=200)
                                                
@api_view(['GET'])                                             
def Ownerportal(request,userid):
    owner=OwnerdataBase.objects.get(owner_id=userid)
    ownerdata=OwnerDataSerializer(owner)
    return Response(ownerdata.data,status=200)


def RoomCreator(id):
    obj=HosteldataBase.objects.get(hostelid=id)
    print(obj.singleshare)
    if obj.singleshare == 'yes':
        cnt=0
        for i in range(obj.singleshare_roomno_start,obj.singleshare_roomno_end+1):
            cnt=cnt+1
            data={
                "hostelid":id,
                "sharing":'one',
                "roomno":i,
                "bedid":f"{str(id)}-one-{i}", 
                "bedno":cnt 
                }
            hstldata=RoomDataSerializer(data=data)
            if hstldata.is_valid():
                hstldata.save()
            
    if obj.twoshare =='yes':
        for i in range(obj.twoshare_roomno_start,obj.twoshare_roomno_end+1):
            cnt=0
            for j in range(1,3):
                cnt=cnt+1
                data={
                "hostelid":id,
                "sharing":'two',
                "roomno":i,
                "bedid":f"{str(id)}-two-{i}-{j}",
                "bedno":cnt  
                }
                hstldata=RoomDataSerializer(data=data)
                if hstldata.is_valid():
                    hstldata.save()
                    
    if obj.threeshare == 'yes':
        for i in range(obj.threeshare_roomno_start,obj.threeshare_roomno_end+1):
            cnt=0
            for j in range(1,4):
                cnt=cnt+1
                data={
                "hostelid":id,
                "sharing":'three',
                "roomno":i,
                "bedid":f"{str(id)}-three-{i}-{j}",
                "bedno":cnt 
                  
                }
                hstldata=RoomDataSerializer(data=data)
                if hstldata.is_valid():
                    hstldata.save()
    if obj.fourshare == 'yes':
        for i in range(obj.fourshare_roomno_start,obj.fourshare_roomno_end+1):
            cnt=0
            for j in range(1,5):
                cnt=cnt+1
                data={
                "hostelid":id,
                "sharing":'four',
                "roomno":i,
                "bedid":f"{str(id)}-four-{i}-{j}",
                "bedno":cnt    
                }
                hstldata=RoomDataSerializer(data=data)
                if hstldata.is_valid():
                    hstldata.save()
                    
    if obj.fiveshare == 'yes':
        for i in range(obj.fiveshare_roomno_start,obj.fiveshare_roomno_end+1):
            cnt=0
            for j in range(1,6):
                cnt=cnt+1
                data={
                "hostelid":id,
                "sharing":'five',
                "roomno":i,
                "bedid":f"{str(id)}-five-{i}-{j}" ,
                "bedno":cnt   
                }
                hstldata=RoomDataSerializer(data=data)
                if hstldata.is_valid():
                    hstldata.save()

@api_view(['POST'])
def HostelData(request):
    data=request.data.copy()
    data=request.data.copy()
    id=random.randint(10001,99999)
    data['hostelid']=id
    hostel_serial=HostelDataSerializer(data=data)
    if hostel_serial.is_valid():
        hostel_serial.save()
        RoomCreator(id)
        return Response(status=201)
    else:
        validated_data = hostel_serial.validated_data
        print("Validation errors:", hostel_serial.errors)
        return Response(status=400)
    
@api_view(['GET'])
def Gethosteldata(request,userid):
    hostel=HosteldataBase.objects.filter(userid=userid)
    hosteldata=HostelDataSerializer(hostel,many=True)
    return Response(hosteldata.data,status=200)

@api_view(['GET']) 
def ViewHostelData(request,hostelid):
    hostel = HosteldataBase.objects.get(hostelid = hostelid)
    hosteldata = HostelDataSerializer(hostel)
    return Response(hosteldata.data,status=200)


@api_view(['GET'])
def Bedinfo(request,hostelid,roomno):
    room=RoomDataBase.objects.filter(hostelid=hostelid,roomno=roomno)
    roominfo=RoomDataSerializer(room,many=True)
    return Response(roominfo.data,status=200)

@api_view(['GET','POST'])
def Hostellerinfo(request,hostelid,roomno):
   if request.method=='POST':
       print('Hii srinu')
       student_data = HostellerDataSerializer(data=request.data)
       print(student_data)
       if student_data.is_valid():
           student_data.save()
           print('saved successfully')
           return Response(status=201)
       
       else:
           return Response(status=404)
   
   print('hosteller info is called')
   hosteller=HostellerDataBase.objects.filter(hostelid=hostelid,roomno=roomno)
   #hostellerinfo=HostellerDataSerializer(hosteller,many=True)
   return Response(hosteller,status=200)
   
    