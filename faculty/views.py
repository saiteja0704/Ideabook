from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Faculty,CommentIdeaFac,NewIdeaFac,FovouriteFac
from student.models import NewIdea
from .forms import NewIdeaFacForm
import datetime
# Create your views here.
def facultySave(request):
	if request.method == 'POST':
		if request.POST.get('username') and request.POST.get('userid') and request.POST.get('password') and request.POST.get('confirmpassword'):
			faculty=Faculty()
			faculty.username= request.POST.get('username')
			faculty.userid= request.POST.get('userid')
			faculty.password= request.POST.get('password')
			faculty.confirmpassword= request.POST.get('confirmpassword')
			faculty.save()	
			#user_list = user.objects.all()
			#print(user_list)
			return redirect('faclogin')
		else:
				return HttpResponse('unsuccess')	
def facultyLoginCheck(request):
	if request.method == 'POST':
		userid = request.POST.get('userid')
		password = request.POST.get('password')
		request.session['userid'] = userid 
		print(userid)
		print(password)
		try:
			user_object = Faculty.objects.get(userid=userid,password=password)
			print(user_object)
			return redirect('facultyHome')
		except:
			print('hello')
			return redirect('faclogin')
	return render(request,'facultylogin.html') 
def facultyHome(request):
	userid = request.session['userid']
	user_object = Faculty.objects.get(userid=userid)
	userid=user_object.id
	newidea1=NewIdeaFac.objects.all().order_by('-id')
	d={'newidea1':newidea1}
	return render(request,'facultyhome.html',d)	   

def testnewideafaculty(request):
	form=NewIdeaFacForm()
	print('facultyyyyyyyyyyyyy')
	return render(request,'newideafac.html',{'form':form})
def testnisfac(request):
	if request.method=='POST':
		form=NewIdeaFacForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			lastrecord=NewIdeaFac.objects.all().last()
			id=lastrecord.id
			x = datetime.datetime.now()
			dt = datetime.datetime.today()
			year= dt.year
			userid = request.session['userid']
			user_object = Faculty.objects.get(userid=userid)
			userid=user_object.id
			newideadate=NewIdeaFac.objects.filter(id=id).update(dateofpublish=year,dateandtime=x,faculty=userid)
			#newidea1=NewIdea.objects.all()
			#d={'newidea1':newidea1}
			return redirect('facultyHome')
	else:
		form=NewIdeaFacForm()
	return HttpResponse('unsuccess')
def testcomment(request,id):
	if request.method=='POST':
		print('hellllllllllllllllllllll00000000000000000')
		print(id)
		userid = request.session['userid']
		user_object = Faculty.objects.get(userid=userid)
		facultyid=user_object.id
		facid = get_object_or_404(Faculty, id=facultyid)
		newideaid = get_object_or_404(NewIdeaFac, id=id)
		commentideafac=CommentIdeaFac()
		commentideafac.facultyid= facid
		commentideafac.newideaid=newideaid
		commentideafac.comment= request.POST.get('comment')
		commentideafac.save()
		return redirect('facultyHome')
	return HttpResponse('success')
def testviewcomment(request,id):
	ffds = NewIdeaFac.objects.get(id=id)
	aa=CommentIdeaFac.objects.filter(newideaid=ffds)
	return render(request,'viewcommentfac.html',{'ffs':aa})
def testlike(request,pk):
	vott1,vott, neg = 0, 0, 0
	objs= NewIdeaFac.objects.get(id=pk)
	unid = objs.id
	vot_count = NewIdeaFac.objects.all().filter(id=unid)

	for t in vot_count:

		vott = t.votes

		vott1 = vott + 1

		obj = get_object_or_404(NewIdeaFac, id=unid)

		obj.votes= vott1
		obj.save(update_fields=["votes"])
		return redirect('facultyHome')
	return HttpResponse('success')
def testdelete(request,id):
	deletcomment=CommentIdeaFac.objects.filter(newideaid=id).delete()
	deletnewidea=NewIdeaFac.objects.filter(id=id).delete()
	return redirect('studentHome')
def testupdateidea(request,id):
	request.session['newideaid'] = id 
	#newideaupdate=NewIdea.objects.filter(id=7).update(name="ram")
	form = NewIdeaFacForm()
	return render(request,'newideaupdatefac.html', {'form': form})
def testupdateideasave(request):
	if request.method=='POST':
		newideaid = request.session['newideaid']
		updateidea = NewIdeaFac.objects.get(pk=newideaid)
		form=NewIdeaFacForm(request.POST,request.FILES,instance=updateidea)
		form.save()
		return redirect('facultyHome')
	else:
		form=NewIdeaFacForm()
	return HttpResponse('unsuccess')
def testfavourite(request,id):
	userid = request.session['userid']
	user_object = Faculty.objects.get(userid=userid)
	facultyid=user_object.id
	facid = get_object_or_404(Faculty, id=facultyid)
	newideaid = get_object_or_404(NewIdeaFac, id=id)
	fovourite=FovouriteFac()
	fovourite.facultyid= facid
	fovourite.newideaid=newideaid
	fovourite.save()
	return redirect('facultyHome')
def testfavouritepage(request):
	userid = request.session['userid']
	user_object = Faculty.objects.get(userid=userid)
	facultyid=user_object.id
	facid = get_object_or_404(Faculty, id=facultyid)
	aa=FovouriteFac.objects.filter(facultyid=facid)
	return render(request,'viewfavouritefac.html',{'favourite':aa})
def testprofile(request):	 
	userid = request.session['userid']
	user_object = Faculty.objects.get(userid=userid)
	userid=user_object.id
	newidea1=NewIdeaFac.objects.filter(faculty=userid).order_by('-id')
	d={'newidea1':newidea1}
	return render(request,'facultyhome.html',d)
def studenthomefacultypage(request):
	newidea1=NewIdea.objects.all().order_by('-id')
	d={'newidea1':newidea1}
	return render(request,'studenthomefac.html',d)
def stufaclike(request,pk):	  
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
		return redirect('studenthomefacultypage')
	return HttpResponse('success')
def year(request,y):
	print(y)
	newidea1=NewIdeaFac.objects.filter(dateofpublish=y).order_by('-id')
	d={'newidea1':newidea1}
	return render(request,'facultyhome.html',d)
