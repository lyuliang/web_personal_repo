from django.shortcuts import render

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

		elif request.GET['status'] == 'error':
			context['display'] = request.GET['digit']
			context['current_status'] = 'before_op'

	elif 'operator' in request.GET:

		if not isValid(request.GET.get('textbox')):
			context['display'] = 'Error'
		elif request.GET.get('status') == 'after_op':
			context['display'] = request.GET['textbox']
		elif request.GET.get('status') == 'error':
			context['display'] = 'Error'
		else:
			if '+' in request.GET['prev_operator']:
				context['display'] = str(int(request.GET['operand1']) + int(request.GET['textbox']))
			elif '×' in request.GET['prev_operator']:
				context['display'] = str(int(int(request.GET['operand1']) * int(request.GET['textbox'])))
			elif '=' in request.GET['prev_operator']:	
				context['display'] = request.GET['textbox']
			elif '−' in request.GET['prev_operator']:
				context['display'] = str(int(request.GET['operand1']) - int(request.GET['textbox']))
			elif '÷' in request.GET['prev_operator']:
				if int(request.GET['textbox']) == 0:
					context['display'] = 'Error'
				else:
					context['display'] = str(int(request.GET['operand1']) // int(request.GET['textbox']))
		if context['display'] == 'Error':
			context['current_status'] = 'error'
		elif '=' in request.GET['operator']:
			context['current_status'] = 'after_equal'
		else:
			context['current_status'] = 'after_op'
	
		context['first_operand'] = context['display']
		context['operator'] = request.GET['operator']

	return render(request, 'ui.html', context)

def isValid(textbox):
	list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	if (not textbox[0] in list) and (textbox[0] != '-'):    
	# '-' is the right one, which is the keyboard hyphens, 
	# while '−' is wrong, which is the minus symbol http requests use.
		return False
	for c in textbox[1:]:
		if not c in list:
			return False
	return True










