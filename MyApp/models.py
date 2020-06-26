from django.db import models
from django.utils import timezone
#from multiselectfield import MultiSelectField
#import django.db.models.ManyToManyField 
import datetime
datetime.date.today()  # Returns 2018-01-15

datetime.datetime.now()
MONTH_CHOICE=(
    ('January','January'),
    ('February','February'),
    ('March','March'),
    ('April','April'),
    ('May','May'),
    ('June','June'),
    ('July','July'),
    ('August','August'),
    ('September','September'),
    ('October','October'),
    ('November','November'),
    ('December','December'),
)

SYMBOL_CHOICE=(
    ('AngularJS','AngularJS'),
    ('bootstrap','bootstrap'),
    ('C#','C#'),
    ('C','C'),
    ('C++','C++'),
    ('DataBase','DataBase'),
    ('Django','Django'),
    ('Java','Java'),
    ('Node_JS','Node_JS'),
    ('Python','Python'),
    ('React_JS','React_JS'),
    ('Ruby','Ruby'),
)   

STD_YEAR_CHOICE=(
    ('1st','1st'),
    ('2nd','2nd'),
    ('3rd','3rd'),
    ('4th','4th'),
)

DATE_CHOICE= [ (i,i) for i in range(1,32)]

STUDYYEAR_CHOICE= [ (i,i) for i in range(1,5)]

CODECHEF_RATING= [ (i,i) for i in range(1,8)]

YEAR_CHOICE= [ (i,i) for i in range(2000,2031)]

class Announcement(models.Model):
    title = models.CharField(max_length=40,unique=True) 
    desc = models.TextField(max_length=200)  
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Event(models.Model):
    date = models.IntegerField(choices=DATE_CHOICE) 
    month = models.CharField(max_length=12,choices=MONTH_CHOICE)
    year = models.IntegerField(choices=YEAR_CHOICE)   
    title = models.CharField(max_length=40,unique=True) 
    desc = models.TextField()  
    pic = models.ImageField(upload_to="events_poster/")
    time = models.TimeField(default=timezone.now)
    End_time = models.DateTimeField()
    url_link = models.URLField(max_length=200,default='http://127.0.0.1:8000/events',blank=True)
    organised_by = models.CharField(max_length=50)

    winners = models.ForeignKey(
    'Winner',
    on_delete=models.CASCADE,blank=True, null=True)

    resource = models.ForeignKey(
    'Resource',
    on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.title

class Winner(models.Model):
    id_code = models.CharField(max_length=20,primary_key=True)    
    fname_1 = models.CharField(max_length=20)   
    lname_1 = models.CharField(max_length=20)  
    year_1 = models.CharField(max_length=12,choices=STD_YEAR_CHOICE)
    fname_2 = models.CharField(max_length=20)   
    lname_2 = models.CharField(max_length=20)  
    year_2 = models.CharField(max_length=12,choices=STD_YEAR_CHOICE)
    fname_3 = models.CharField(max_length=20)   
    lname_3 = models.CharField(max_length=20)  
    year_3 = models.CharField(max_length=12,choices=STD_YEAR_CHOICE)
    
    def __str__(self):
        return self.id_code

class Resource(models.Model):
    id_code = models.CharField(max_length=20,primary_key=True)   
    desc = models.TextField()  
    url_link = models.URLField(max_length=200)
    document = models.FileField(upload_to='documents/',blank=True)
    symbol = models.CharField(max_length=20,blank=True,choices=SYMBOL_CHOICE,default='default')    
    uploaded_at = models.DateTimeField(auto_now_add=True)
    tag=models.ManyToManyField ('Tag')
    #tag = models.ForeignKey(
    #'Tag',   
    #on_delete=models.CASCADE,)

    def __str__(self):
        return self.id_code

class PostImage(models.Model):
    post= models.ForeignKey(Resource,default=None, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='Resource_Gallery/')

    def __str__(self):
        return self.post.id_code
     
class Tag(models.Model):
    name = models.CharField(max_length=20,unique=True)   
    
    def __str__(self):
        return self.name

class Gallery(models.Model):
    image= models.ImageField(upload_to="gallery/")
    alternative_text = models.TextField() 
    
    def __str__(self):
        return self.alternative_text

class AboutUs(models.Model):
    fname = models.CharField(max_length=20)   
    lname = models.CharField(max_length=20)  
    position= models.CharField(max_length=20)   
    image= models.ImageField(upload_to="profile/",default='profile/withoutProfile.png')
    skills= models.CharField(max_length=40)  
    codechef_rating = models.IntegerField(choices=CODECHEF_RATING)   
    
    def __str__(self):
        return self.position
    class Meta:
        verbose_name_plural = "AboutUs"

class UserBlog(models.Model):
    user_name = models.CharField(max_length=50)
    user_emailId = models.EmailField(max_length=50)
    Enrollment_No = models.IntegerField()
    BlogTitle = models.CharField(max_length=40) 
    BlogDesc = models.TextField(max_length=300)  
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.BlogTitle