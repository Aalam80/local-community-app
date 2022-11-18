from django.contrib import admin
from .models import services,catogary,Queries,Contact,serviceQuery,banner
from django.contrib.auth.models import Group
admin.site.site_header ='myapp admin Panel'
admin.site.site_title='custom Admin pnel'




class catogaryAdminpost(admin.ModelAdmin):
    list_display= ('name','img')
    list_per_page = 5

class contactadminpost(admin.ModelAdmin):
    list_display= ('name','email','phone','Desc')
    list_per_page = 5

class Queryadminpost(admin.ModelAdmin):
    list_display=('user','Query_detail','reply')
    list_per_page = 5

class servicesadminpost (admin.ModelAdmin):
    list_display=('service_name','service_provider','price','contact_number','catogary')
    list_per_page = 5

class serQueryadminpost(admin.ModelAdmin):
    list_display=('Query_Detail','user','parant')
    list_per_page = 5
# Register your models here.
admin.site.register(services,servicesadminpost)
admin.site.register(catogary,catogaryAdminpost)
admin.site.register(Queries,Queryadminpost)
admin.site.register(Contact,contactadminpost)
admin.site.register(serviceQuery,serQueryadminpost)
admin.site.register(banner)


admin.site.unregister(Group)