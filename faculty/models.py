from django.db import models

# Create your models here.
class Faculty(models.Model):
	id=models.AutoField(primary_key=True)
	username= models.CharField(max_length=250)
	userid= models.CharField(max_length=250,unique=True)
	password= models.CharField(max_length=250)
	confirmpassword= models.CharField(max_length=250)
class NewIdeaFac(models.Model):
	id=models.AutoField(primary_key=True)
	title= models.CharField(max_length=250)
	uploadpic= models.ImageField(upload_to = 'pic_folder/')
	content= models.CharField(max_length=250)
	dateofpublish=models.CharField(max_length=4,default=u'2020')
	dateandtime=models.DateTimeField(default=u'2020-12-12 10:00:00')
	videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")
	votes = models.IntegerField(default=0)
	faculty= models.ForeignKey(Faculty,
	on_delete=models.CASCADE)
class CommentIdeaFac(models.Model):
	facultyid = models.ForeignKey(Faculty, on_delete=models.CASCADE)
	newideaid = models.ForeignKey(NewIdeaFac, on_delete=models.CASCADE)
	comment=models.CharField(max_length=500)	
class FovouriteFac(models.Model):
	facultyid = models.ForeignKey(Faculty, on_delete=models.CASCADE)
	newideaid = models.ForeignKey(NewIdeaFac, on_delete=models.CASCADE)	