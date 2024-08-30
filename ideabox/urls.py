"""ideabox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from django.conf.urls import url
from django.conf.urls.static import static

from ideabox import settings
from student import views as student_views
from faculty import views as faculty_views
from ideabox import settings
urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url('^$',student_views.index,name="index"),
	url('^login',student_views.login,name="login"),
	url('^faclogin',student_views.faclogin,name="faclogin"),
	url('^register',student_views.register,name="register"),
	url('^facregister',student_views.facregister,name="facregister"),
	url('^studentSave',student_views.studentSave,name="studentSave"),
	url('^studentLoginCheck',student_views.studentLoginCheck,name="studentLoginCheck"),
	url('^studentHome',student_views.studentHome,name="studentHome"),
	url('^profile',student_views.profile,name="profile"),
	url('^newidea',student_views.newidea,name="newidea"),
	url('^newideasave',student_views.newideasave,name="newideasave"),
	url('^nis',student_views.nis,name="nis"),
	url('^comment/(?P<id>\d+)/$',student_views.comment,name="comment"),
	url('^viewcomment/(?P<id>\d+)/$',student_views.viewcomment,name="viewcomment"),
	url('^likes/(?P<pk>\d+)/$',student_views.likes,name="likes"),
	url('^delete/(?P<id>\d+)/$',student_views.delete,name="delete"),
	url('^updateidea/(?P<id>\d+)/$',student_views.updateidea,name="updateidea"),
	url('^updateideasave',student_views.updateideasave,name="updateideasave"),
	url('^favourite/(?P<id>\d+)/$',student_views.favourite,name="favourite"),
	url('^favouritepage/',student_views.favouritepage,name="favouritepage"),
	url('^facultySave/',faculty_views.facultySave,name="facultySave"),  
	url('^facultyLoginCheck/',faculty_views.facultyLoginCheck,name="facultyLoginCheck"),  
	url('^facultyHome/',faculty_views.facultyHome,name="facultyHome"),           
	url('^testnewideafaculty/',faculty_views.testnewideafaculty,name="testnewideafaculty"),    
	url('^testnisfac/',faculty_views.testnisfac,name="testnisfac"),    
	#url('^test/',faculty_views.test,name="test"),    
	url('^testcomment/(?P<id>\d+)/$',faculty_views.testcomment,name="testcomment"),    
	url('^testviewcomment/(?P<id>\d+)/$',faculty_views.testviewcomment,name="testviewcomment"),    
	url('^testlike/(?P<pk>\d+)/$',faculty_views.testlike,name="testlike"),    
	url('^testdelete/(?P<id>\d+)/$',faculty_views.testdelete,name="testdelete"),    
	url('^testupdateidea/(?P<id>\d+)/$',faculty_views.testupdateidea,name="testupdateidea"),    
	url('^testupdateideasave/',faculty_views.testupdateideasave,name="testupdateideasave"),    
	url('^testfavourite/(?P<id>\d+)/$',faculty_views.testfavourite,name="testfavourite"),    
	url('^testfavouritepage/',faculty_views.testfavouritepage,name="testfavouritepage"),    
	url('^testprofile/',faculty_views.testprofile,name="testprofile"),    
	url('^studenthomefacultypage/',faculty_views.studenthomefacultypage,name="studenthomefacultypage"),    
	url('^stufaclike/(?P<pk>\d+)/$',faculty_views.stufaclike,name="stufaclike"),    
	url('^year/(?P<y>\d+)/$',faculty_views.year,name="year"),    
	url('^yearstu/(?P<y>\d+)/$',student_views.yearstu,name="yearstu"),    
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
