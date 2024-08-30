from django.db import models

# Create your models here.
class Student(models.Model):
	id=models.AutoField(primary_key=True)
	username= models.CharField(max_length=250)
	userid= models.CharField(max_length=250, unique=True)
	password= models.CharField(max_length=250)
	confirmpassword= models.CharField(max_length=250) 
class NewIdea(models.Model):
	id=models.AutoField(primary_key=True)
	title= models.CharField(max_length=250)
	uploadpic= models.ImageField(upload_to = 'pic_folder/')
	content= models.CharField(max_length=250)
	dateofpublish=models.CharField(max_length=4,default=u'2020')
	dateandtime=models.DateTimeField(default=u'2020-12-12 10:00:00')
	videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")
	votes = models.IntegerField(default=0)
	student= models.ForeignKey(Student,
	on_delete=models.CASCADE)
class CommentIdea(models.Model):
	studentid = models.ForeignKey(Student, on_delete=models.CASCADE)
	newideaid = models.ForeignKey(NewIdea, on_delete=models.CASCADE)
	comment=models.CharField(max_length=500)	
class Fovourite(models.Model):
	studentid = models.ForeignKey(Student, on_delete=models.CASCADE)
	newideaid = models.ForeignKey(NewIdea, on_delete=models.CASCADE)   