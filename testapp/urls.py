from django.urls import path
from testapp import views

urlpatterns = [
    path('first_view/',views.first_view,name= 'home'),
    path('form/',views.savedata,name='form'),
    path('form2/',views.regularFormView,name='form2'),
    path('form3/',views.modelFormView,name='form3'),
    path('display/',views.retrieveData,name='display'),
    path('update/<int:data_id>/',views.updateData,name='update'),
    path('delete/<int:data_id>/',views.deleteData,name='delete'),

]
