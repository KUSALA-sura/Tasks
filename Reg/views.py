from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Reg(requset):
	if requset.method=='POST':
		fname=requset.POST.get('fname')
		lname=requset.POST.get('lname')
		email=requset.POST.get('email')
		gender=requset.POST.get('gender')
		address=requset.POST.get('address')
		lang=requset.POST.getlist('lang')
		data={'fname':fname,'lname':lname,'email':email,'gender':gender,'address':address,'lang':lang}
		return render(requset,'sk/display.html',data)
		#print(requset.POST)
	return render(requset,'sk/Reg.html')

def loginreg(requset):
	if requset.method=='POST':
		uname=requset.method['UserName']
		pwd=requset.method['Password']
		info=loginreg(uname=UserName,pwd=Password)
		if info is not None:
			
			return HttpResponse('Thanks')
	#return HttpResponse('HII')

	return render(requset,'sk/loginreg.html')

