from django.urls import path
from.import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('signup/',views.OwnerSignup,name='signupurl'),
    path('otpverify/<str:email>/',views.Otpverify,name='otpverifyurl'),
    path('ownerdata/<str:email>/',views.OwnerData,name='ownerdataurl'),
    path('login/',views.Login,name='loginurl'),
    path('ownerportal/<int:userid>/',views.Ownerportal,name='ownerportalurl'),
    path('hosteldata/',views.HostelData,name='hosteldataurl'),
    path('gethosteldata/<int:userid>/',views.Gethosteldata,name='gethosteldataurl'),
    path('viewhosteldata/<int:hostelid>/',views.ViewHostelData),
    path('bedinfo/<int:hostelid>/<int:roomno>/',views.Bedinfo),
    path('hostellerinfo/<int:hostelid>/<int:roomno>/',views.Hostellerinfo),
]