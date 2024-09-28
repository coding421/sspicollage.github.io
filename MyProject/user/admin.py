from django.contrib import admin
from .models import *

class contactusAdmin(admin.ModelAdmin):
    list_display = ('Name','Email','Mobile','Subject','Message')

admin.site.register(contactus,contactusAdmin)

class tbl_feedbackAdmin(admin.ModelAdmin):
    list_display = ('id','name','feedback','picture')

admin.site.register(tbl_feedback,tbl_feedbackAdmin)

class tbl_recruiterAdmin(admin.ModelAdmin):
    list_display = ('id','company_logo')

admin.site.register(tbl_recruiter,tbl_recruiterAdmin)

class tbl_galleryAdmin(admin.ModelAdmin):
    list_display = ('id','gallery_picture')

admin.site.register(tbl_gallery,tbl_galleryAdmin)

class tbl_alumniAdmin(admin.ModelAdmin):
    list_display = ('id','name','student_picture','company_name','placement_session')

admin.site.register(tbl_alumni,tbl_alumniAdmin)

class tbl_sliderAdmin(admin.ModelAdmin):
    list_display = ('id','title','description','slider_image')

admin.site.register(tbl_slider,tbl_sliderAdmin)

class tbl_infraAdmin(admin.ModelAdmin):
    list_display = ('id','title','picture')

admin.site.register(tbl_infra,tbl_infraAdmin)

class tbl_noticeAdmin(admin.ModelAdmin):
    list_display = ('id','notice','notice_link','posted_date')

admin.site.register(tbl_notice,tbl_noticeAdmin)

class tbl_facultyAdmin(admin.ModelAdmin):
    list_display = ('id','name','picture','designation','experiance','specialization','mobile','qualification')

admin.site.register(tbl_faculty,tbl_facultyAdmin)

class tbl_courcesAdmin(admin.ModelAdmin):
    list_display = ('id','department','seats','course_code','duration')

admin.site.register(tbl_cources,tbl_courcesAdmin)