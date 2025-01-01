from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('adminindex',views.adminindex,name='adminindex'),
    path('addbranches',views.addbranches,name='addbranches'),
    path('addsalons',views.addsalons,name='addsalons'),
    path('addservices',views.addservices,name='addservices'),
    path('branchdata',views.branchdata,name='branchdata'),
    path('salondata',views.salondata,name='salondata'),
    path('servicedata',views.servicedata,name='servicedata'),
    path('branchtable',views.branchtable,name='branchtable'),
    path('salontable',views.salontable,name='salontable'),
    path('servicetable',views.servicetable,name='servicetable'),
    path('editb/<int:id>',views.editb,name='editb'),
    path('updateb/<int:id>',views.updateb,name='updateb'),
    path('deleteb/<int:id>',views.deleteb,name='deleteb'),
    path('editl/<int:id>',views.editl,name='editl'),
    path('updatesal/<int:id>',views.updatesal,name='updatesal'),
    path('deletel/<int:id>',views.deletel,name='deletel'),
    path('edits/<int:id>',views.edits,name='edits'),
    path('updateser/<int:id>',views.updateser,name='updateser'),
    path('deletes/<int:id>',views.deletes,name='deletes'),
    path('registertable',views.registertable,name='registertable'),
    path('contacttable',views.contacttable,name='contacttable'),
    path('logintable',views.logintable,name='logintable'),
   path('viewuser', views.viewuser, name='viewuser'),
    path('accept/<int:id>/', views.accept, name='accept'),
    path('reject/<int:id>/', views.reject, name='reject'),
    path('approvedtable',views.approvedtable,name='approvedtable'),
    path('declinedtable',views.declinedtable,name='declinedtable'),
]
