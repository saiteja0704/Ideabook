from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Student,CommentIdea
from .forms import *
import datetime
# Create your views here.
def index(request):
	return render(request,'index.html')

def login(request):
	return render(request,'studentlogin.html')	  
def faclogin(request):
	return render(request,'facultylogin.html')	  
def register(request):
	return render(request,'sturegister.html')	   
def facregister(request):
	return render(request,'facregister.html')		
def studentSave(request):
	if request.method == 'POST':
		if request.POST.get('username') and request.POST.get('userid') and request.POST.get('password') and request.POST.get('confirmpassword'):
			student=Student()
			student.username= request.POST.get('username')
			student.userid= request.POST.get('userid')
			student.password= request.POST.get('password')
			student.confirmpassword= request.POST.get('confirmpassword')
			student.save()	
			#user_list = user.objects.all()
			#print(user_list)
			return redirect('login')
		else:
				return HttpResponse('unsuccess')	
def studentLoginCheck(request):
	if request.method == 'POST':
		userid = request.POST.get('userid')
		password = request.POST.get('password')
		request.session['userid'] = userid 
		print(userid)
		print(password)
		try:
			user_object = Student.objects.get(userid=userid,password=password)
			print(user_object)
			return redirect('studentHome')
		except:
			print('hello')
			return redirect('login')
	return render(request,'studentlogin.html') 
def studentHome(request):
	'''userid = request.session['userid']
	user_object = Student.objects.get(userid=userid)
	userid=user_object.id'''
	newidea1=NewIdea.objects.all().order_by('-id')
	d={'newidea1':newidea1}
	return render(request,'studenthome.html',d)
def profile(request):
	userid = request.session['userid']
	user_object = Student.objects.get(userid=userid)
	userid=user_object.id
	newidea1=NewIdea.objects.filter(student=userid).order_by('-id')
	d={'newidea1':newidea1}
	return render(request,'studenthome.html',d)
def newidea(request):
	form = NewIdeaForm()
	print('studenttttttttttttttttttttttt')
	return render(request,'newidea.html', {'form': form})
def newideasave(request):
	if request.method == 'POST': 
		print('helllllllllllllloooooooooooooooo')
		form = NewIdeaForm(request.POST, request.FILES) 
		if form.is_valid(): 
			form.save() 
			return HttpResponse('success') 
	else: 
		form = NewIdeaForm() 
	return render(request, 'newidea.html', {'form' : form}) 
	#return HttpResponse('success')
def nis(request):
	if request.method=='POST':
		form=NewIdeaForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			#id = form.cleaned_data[id]
			lastrecord=NewIdea.objects.all().last()
			id=lastrecord.id
			x = datetime.datetime.now()
			dt = datetime.datetime.today()
			year= dt.year
			userid = request.session['userid']
			user_object = Student.objects.get(userid=userid)
			userid=user_object.id
			newideadate=NewIdea.objects.filter(id=id).update(dateofpublish=year,dateandtime=x,student=userid)
			#newidea1=NewIdea.objects.all()
			#d={'newidea1':newidea1}
			return redirect('studentHome')
	else:
		form=NewIdeaForm()
	return HttpResponse('unsuccess')	
def comment(request,id):
	if request.method == 'POST':
		userid = request.session['userid']
		user_object = Student.objects.get(userid=userid)
		studentid=user_object.id
		stuid = get_object_or_404(Student, id=studentid)
		newideaid = get_object_or_404(NewIdea, id=id)
		commentidea=CommentIdea()
		commentidea.studentid= stuid
		commentidea.newideaid=newideaid
		commentidea.comment= request.POST.get('comment')
		commentidea.save()
		return redirect('studentHome')
	return HttpResponse('nis')
def viewcomment(request,id):
	ffds = NewIdea.objects.get(id=id)
	aa=CommentIdea.objects.filter(newideaid=ffds)
	return render(request,'viewcomment.html',{'ffs':aa})
def likes(request,pk):
	vott1,vott, neg = 0, 0, 0
	objs= NewIdea.objects.get(id=pk)
	unid = objs.id
	vot_count = NewIdea.objects.all().filter(id=unid)

	for t in vot_count:

		vott = t.votes

		vott1 = vott + 1

		obj = get_object_or_404(NewIdea, id=unid)

		obj.votes= vott1
		obj.save(update_fields=["votes"])
		return redirect('studentHome')
	return HttpResponse('unsuccess')	
	#return render(request, 'users_cqa/likes.html',{'objs':vott1})
def delete(request,id): 
	deletcomment=CommentIdea.objects.filter(newideaid=id).delete()
	deletnewidea=NewIdea.objects.filter(id=id).delete()
	return redirect('studentHome')
def updateidea(request,id):
	request.session['newideaid'] = id 
	#newideaupdate=NewIdea.objects.filter(id=7).update(name="ram")
	form = NewIdeaForm()
	return render(request,'newideaupdate.html', {'form': form})
def updateideasave(request):
	if request.method=='POST':
		newideaid = request.session['newideaid']
		updateidea = NewIdea.objects.get(pk=newideaid)
		form=NewIdeaForm(request.POST,request.FILES,instance=updateidea)
		form.save()
		#id = form.cleaned_data[id]
		'''lastrecord=NewIdea.objects.all().last()
		id=lastrecord.id
		x = datetime.datetime.now()
		dt = datetime.datetime.today()
		year= dt.year
		userid = request.session['userid']
		user_object = Student.objects.get(userid=userid)
		userid=user_object.id
		newideadate=NewIdea.objects.filter(id=id).update(dateofpublish=year,dateandtime=x,student=userid)'''
		#newidea1=NewIdea.objects.all()
		#d={'newidea1':newidea1}
		return redirect('studentHome')
	else:
		form=NewIdeaForm()
	return HttpResponse('unsuccess')
def favourite(request,id):
	userid = request.session['userid']
	user_object = Student.objects.get(userid=userid)
	studentid=user_object.id
	stuid = get_object_or_404(Student, id=studentid)
	newideaid = get_object_or_404(NewIdea, id=id)
	fovourite=Fovourite()
	fovourite.studentid= stuid
	fovourite.newideaid=newideaid
	fovourite.save()
	return redirect('studentHome')
def favouritepage(request):
	userid = request.session['userid']
	user_object = Student.objects.get(userid=userid)
	studentid=user_object.id
	stuid = get_object_or_404(Student, id=studentid)
	aa=Fovourite.objects.filter(studentid=stuid)
	return render(request,'viewfavourite.html',{'favourite':aa})
def yearstu(request,y):
	newidea1=NewIdea.objects.filter(dateofpublish=y).order_by('-id')
	d={'newidea1':newidea1}
	return render(request,'studenthome.html',d)