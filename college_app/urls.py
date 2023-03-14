from django.urls import path
from. import views
urlpatterns =[
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('studentform',views.studentform,name='studentform'),
    path('studentform/l/',views.course_finder,name='course_selection'),

]