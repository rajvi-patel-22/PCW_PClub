from django.contrib import admin
from .models import Announcement,Event,Winner,Resource,Tag,Gallery,AboutUs,PostImage,UserBlog
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display= ('title','id', 'date', 'month', 'year','time','desc','End_time')
    search_fields= ('id','title', 'date', 'month', 'year')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class AnnouncementAdmin(admin.ModelAdmin):
    list_display= ('title','id', 'uploaded_at', 'desc')
    search_fields= ('id','title', 'uploaded_at')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class WinnerAdmin(admin.ModelAdmin):
    list_display= ('id_code', 'fname_1','lname_1', 'year_1','fname_2', 'lname_2','year_2','fname_3','lname_3', 'year_3')
    search_fields= ('id_code', 'fname_1','lname_1', 'year_1','fname_2', 'lname_2','year_2','fname_3','lname_3', 'year_3')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class PostImageAdmin(admin.StackedInline):
    model=PostImage

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display= ( 'id_code','desc','document','uploaded_at')
    search_fields= ( 'id_code','document','uploaded_at')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    inlines=[PostImageAdmin]

    class Meta:
        model=Resource

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

class GalleryAdmin(admin.ModelAdmin):
    list_display= ('alternative_text','image','id' )
    search_fields= ('id','image', 'alternative_text')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class TagAdmin(admin.ModelAdmin):
    list_display= ('name','id')
    search_fields= ('id','name')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class AboutUsAdmin(admin.ModelAdmin):
    list_display= ('fname','position','skills')
    search_fields= ('position','fname','skills')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class UserBlogAdmin(admin.ModelAdmin):

    list_display= ('BlogTitle','Enrollment_No','user_emailId','user_name')
    search_fields=  ('BlogTitle','Enrollment_No','user_emailId','user_name')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Announcement,AnnouncementAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Winner,WinnerAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Gallery,GalleryAdmin)
admin.site.register(AboutUs,AboutUsAdmin)
admin.site.register(UserBlog,UserBlogAdmin)
