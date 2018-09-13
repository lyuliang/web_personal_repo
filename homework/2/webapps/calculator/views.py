from django.http import HttpResponse
from django.shortcuts import render
import urllib

def calc(request):   

	context = {}
	context['display'] = '0'
	context['operator'] = ''
	context['current_status'] = 'idle'
	context['first_operand'] = '0'


	if 'digit' in request.GET:
    
		context['operator'] = request.GET['prev_operator']
		context['first_operand'] = request.GET['operand1']

		if request.GET['status'] == 'idle':			
			context['display'] = request.GET['digit']
			context['current_status'] = 'before_op'

		elif request.GET['status'] == 'after_equal':
			context['current_status'] = 'before_op'
			context['display'] = request.GET['digit']

		elif request.GET['status'] == 'before_op':
			context['display'] = request.GET['textbox'] + request.GET['digit']
			context['current_status'] = 'before_op'

		elif request.GET['status'] == 'after_op':
			context['display'] = request.GET['digit']
			context['current_status'] = 'before_op'

	elif 'operator' in request.GET:
		print(len(request.GET['prev_operator']))	#
		print(ord(request.GET['prev_operator'][0])) #

		if len(request.GET['prev_operator']) == 2:
			if ord(request.GET['prev_operator'][1]) == 43:	#'+'
				context['display'] = str(int(request.GET['operand1']) + int(request.GET['textbox']))
			elif ord(request.GET['prev_operator'][1]) == 215:	#'*'
				context['display'] = str(int(int(request.GET['operand1']) * int(request.GET['textbox'])))
			elif ord(request.GET['prev_operator'][1]) == 61:	#'='
				context['display'] = request.GET['textbox']

		elif len(request.GET['prev_operator']) == 1:
			if ord(request.GET['prev_operator'][0]) == 43:	#'+'
				context['display'] = str(int(request.GET['operand1']) + int(request.GET['textbox']))
			elif ord(request.GET['prev_operator'][0]) == 8722:	#'-'
				context['display'] = str(int(request.GET['operand1']) - int(request.GET['textbox']))
			elif ord(request.GET['prev_operator'][0]) == 247:	#'/'
				context['display'] = str(int(int(request.GET['operand1']) / int(request.GET['textbox'])))

		if len(request.GET['operator']) == 2:
			if ord(request.GET['operator'][1]) == 61:
				context['current_status'] = 'after_equal'
			else:
				context['current_status'] = 'after_op'
		else:
			context['current_status'] = 'after_op'
			
		context['first_operand'] = context['display']
		context['operator'] = request.GET['operator']


	return render(request, 'hello.html', context)
