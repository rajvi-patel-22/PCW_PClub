from django.shortcuts import render
from .models import Announcement ,Event,Winner,Gallery ,Resource,Tag,AboutUs,PostImage,UserBlog
from django.contrib import messages
from pymsgbox import *


# Create your views here.
def home(request):
    ans = Announcement.objects.all()
    blog = UserBlog.objects.filter().order_by('-uploaded_at')[0:2]
    return render(request,'1_HomePage.html',{'ans' : ans,'blog':blog})

def events(request):
    event = Event.objects.all()
    winner=Winner.objects.all()
    return render(request,'2_Events.html',{'event' : event,'winner':winner})


def resources(request):
    event = Event.objects.all()
    resource = Resource.objects.all()    
    tag = Tag.objects.all()
    photos=PostImage.objects.all()
    temp=resource
    
    if request.method == 'POST':
        query = request.POST['select2']
        if(query != 'Show all'):
          sorted_tag=Resource.objects.filter(tag__name=query)
        else:
          sorted_tag=temp
        resource=sorted_tag
        return render(request,'3_Resources.html',{'resource' : resource,'tag' : tag,'event':event,'photos':photos})
    
    resource=temp
    return render(request,'3_Resources.html',{'resource' : resource,'tag' : tag,'event':event,'photos':photos})
    
def aboutus(request):
    pics = Gallery.objects.all()
    detail =AboutUs.objects.all()
    return render(request,'4_AboutUs.html',{'pics' : pics,'detail' :detail})

def blog(request):
    blog = UserBlog.objects.filter().order_by('-uploaded_at')
    return render(request,'5_Blog.html',{'blog' : blog})

def addblog(request):
        
    if request.method == 'POST':
        user_name = request.POST['user_name']
        user_emailId = request.POST['user_emailId']
        Enrollment_No = request.POST['Enrollment_ID']
        BlogTitle = request.POST['BlogTitle']
        BlogDesc = request.POST['BlogDesc']
       
        storeInTable = UserBlog(user_name=user_name,user_emailId=user_emailId,Enrollment_No=Enrollment_No,BlogTitle=BlogTitle,BlogDesc=BlogDesc)
        storeInTable.save()
      
        messages.info(request,'Thank you , Blog Added Successfully')
        alert(text='', title='Thank you , Blog Added Successfully')
        return render(request,'5_Blog.html')
      
    return render(request,'5_Blog.html')
