from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.


@csrf_exempt
def core(request):
	if request.method == 'POST':
		session_id = request.POST.get('sessionId')
		service_code = request.POST.get('serviceCode')
		phone_number = request.POST.get('phoneNumber')
		text = request.POST.get('text')

		response = ""

		if text == "":
			response = "CON What would want to check \n"
			response += "1. Your Phone Number"
			response += "2. Pwaveino's email"
			response += "3. Just Checking in"

		elif text == "1":
			response = f'END Your Phone Number is {phone_number} \n'

		elif text == "2":
			response = "END pwaveinoc@gmail.com \n"

		elif text == "3":
			response = "END Thank you for checking in \n"

		return HttpResponse(response)

