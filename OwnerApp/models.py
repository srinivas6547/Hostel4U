from django.db import models

# Create your models here.
class OwnerdataBase(models.Model):
    owner_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    mobile_no=models.CharField(max_length=12)
    mail_id=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=20)
    
class HosteldataBase(models.Model):
    #basicinfo
    userid=models.ForeignKey(OwnerdataBase,null=True,on_delete=models.SET_NULL)
    hostelid=models.IntegerField()
    hostelname=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    contactno=models.CharField(max_length=12)
    #singleshare
    singleshare=models.CharField(max_length=10)
    singleshare_roomno_start=models.IntegerField(null=True)
    singleshare_roomno_end=models.IntegerField(null=True)
    singleshare_fee=models.IntegerField(null=True)
    #twoshare
    twoshare=models.CharField(max_length=10)
    twoshare_roomno_start=models.IntegerField(null=True)
    twoshare_roomno_end=models.IntegerField(null=True)
    twoshare_fee=models.IntegerField(null=True)
    #threeshare
    threeshare=models.CharField(max_length=10)
    threeshare_roomno_start=models.IntegerField(null=True)
    threeshare_roomno_end=models.IntegerField(null=True)
    threeshare_fee=models.IntegerField(null=True)
    #fourshare
    fourshare=models.CharField(max_length=10)
    fourshare_roomno_start=models.IntegerField(null=True)
    fourshare_roomno_end=models.IntegerField(null=True)
    fourshare_fee=models.IntegerField(null=True)
    #fiveshare
    fiveshare=models.CharField(max_length=10)
    fiveshare_roomno_start=models.IntegerField(null=True)
    fiveshare_roomno_end=models.IntegerField(null=True)
    fiveshare_fee=models.IntegerField(null=True)
    #facilities
    wifi=models.CharField(max_length=10)
    washmachine=models.CharField(max_length=10)
    minwater=models.CharField(max_length=10)
    lift=models.CharField(max_length=10)
    hotwater=models.CharField(max_length=10)
    cctv=models.CharField(max_length=10)
    lockers=models.CharField(max_length=10)
    tv=models.CharField(max_length=10)
    #menu
    monday_bf=models.CharField(max_length=50)
    monday_launch=models.CharField(max_length=50)
    monday_dinner=models.CharField(max_length=50)
    
    tuesday_bf=models.CharField(max_length=50)
    tuesday_launch=models.CharField(max_length=50)
    tuesday_dinner=models.CharField(max_length=50)
    
    wednesday_bf=models.CharField(max_length=50)
    wednesday_launch=models.CharField(max_length=50)
    wednesday_dinner=models.CharField(max_length=50)
    
    thursday_bf=models.CharField(max_length=50)
    thursday_launch=models.CharField(max_length=50)
    thursday_dinner=models.CharField(max_length=50)
    
    friday_bf=models.CharField(max_length=50)
    friday_launch=models.CharField(max_length=50)
    friday_dinner=models.CharField(max_length=50)
    
    saturday_bf=models.CharField(max_length=50)
    saturday_launch=models.CharField(max_length=50)
    saturday_dinner=models.CharField(max_length=50)
    
    sunday_bf=models.CharField(max_length=50)
    sunday_launch=models.CharField(max_length=50)
    sunday_dinner=models.CharField(max_length=50)
    
    
    class Meta:
        db_table = 'ownerapp_hosteldatabase'
        
class RoomDataBase(models.Model):
    hostelid=models.IntegerField()
    sharing=models.CharField(max_length=30)
    roomno=models.IntegerField()
    bedid=models.CharField(max_length=30)
    bedno=models.IntegerField()
    
class HostellerDataBase(models.Model):
    hostelid=models.IntegerField()
    bedid=models.CharField(max_length=30)
    roomno=models.IntegerField()
    name=models.CharField(max_length=30)
    mobile=models.CharField(max_length=12,unique=True)
    aadhar=models.CharField(max_length=14,unique=True)
    occupation=models.CharField(max_length=20)
    joindate=models.DateField()    

     
    
    
    
    
