from django.urls import path
from student import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name='home'),
    path('search/',views.search,name='search'),
    path('detail/<int:stud_id>/',views.detail,name='detail'),
    path('not_Reg/',views.not_Reg,name='not_Reg'),
    path('reg_stud/',views.reg_stud,name='reg_stud'),
    path('result/',views.result,name='result'),
    path('department/',views.department,name='department'),
    path('download-csv/',views.download_csv, name='download_csv'),
    path('edit/<int:stud_id>/',views.edit,name='edit'),
    path('edit_stud',views.edit_stud,name='edit_stud'),
    path('login/',views.log_in,name='login'),
    path('logout/',views.log_out,name='logout'),
    path('register/',views.register, name='register'),
    path('contact/',views.contact,name='contact'),
]