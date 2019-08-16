from django.contrib import admin
from testapp.models import testdata

# Register your models here.
class testdataAdmin(admin.ModelAdmin):
    list_display = ('studentName','course','age','email')
    list_filter = ('course',)


admin.site.register(testdata,testdataAdmin)
