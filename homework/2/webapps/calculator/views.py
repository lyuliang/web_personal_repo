from django.shortcuts import render

def calc(request):   

	context = {}
	context['display'] = '0'
	context['operator'] = ''
	context['current_status'] = 'idle'
	context['first_operand'] = '0'

	if not isValidRequest(request):

		context['current_status'] = 'error'
		context['display'] = 'Error'

	elif 'digit' in request.GET:
    
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

		if not isValidText(request.GET.get('textbox')):
			context['display'] = 'Error'
		elif request.GET.get('status') == 'after_op':
			context['display'] = request.GET['textbox']
		elif request.GET.get('textbox') == 'Error':
			context['display'] = 'Error'
		else:
			# if '+' in request.GET['prev_operator']:
			if request.GET['prev_operator'].strip('\u200b') == '+':
				context['display'] = str(int(request.GET['operand1']) + int(request.GET['textbox']))
			elif request.GET['prev_operator'].strip('\u200b') == '×':
				context['display'] = str(int(int(request.GET['operand1']) * int(request.GET['textbox'])))
			elif request.GET['prev_operator'].strip('\u200b') == '=':
				context['display'] = request.GET['textbox']
			elif request.GET['prev_operator'].strip('\u200b') == '−':
				context['display'] = str(int(request.GET['operand1']) - int(request.GET['textbox']))
			elif request.GET['prev_operator'].strip('\u200b') == '÷':
				if int(request.GET['textbox']) == 0:
					context['display'] = 'Error'
				else:
					context['display'] = str(int(request.GET['operand1']) // int(request.GET['textbox']))
		if context['display'] == 'Error':
			context['current_status'] = 'error'
		elif request.GET['operator'].strip('\u200b') == '=':
			context['current_status'] = 'after_equal'
		else:
			context['current_status'] = 'after_op'
	
		context['first_operand'] = context['display']
		context['operator'] = request.GET['operator']

	print(context['current_status'])
	return render(request, 'ui.html', context)

def isValidText(textbox):
	list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	if not textbox:
		return False
	if (not textbox[0] in list) and (textbox[0] != '-'):    
	# '-' is the right one, which is the keyboard hyphens, 
	# while '−' is wrong, which is the minus symbol http requests use.
		return False
	for c in textbox[1:]:
		if not c in list:
			return False
	return True

def isValidRequest(request):

	digitList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	operatorList = ['+', '−', '×', '÷', '=']
	statusList = ['idle', 'before_op', 'after_op', 'after_equal', 'error']

	if ((not 'digit' in request.GET) and (not 'prev_operator' in request.GET)
		and (not 'operator' in request.GET) and (not 'operand1' in request.GET)
		and (not 'textbox' in request.GET) and (not 'status' in request.GET)):
		return True
	
	if 'digit' in request.GET and 'operator' in request.GET:
		return False
	if ((not 'digit' in request.GET) and (not 'operator' in request.GET)
		and not '42' in request.GET):
		return False
	if 'digit' in request.GET and not request.GET.get('digit') in digitList:
		return False
	if 'operator' in request.GET:
		if not request.GET.get('operator').strip('\u200b') in operatorList:
			return False
	if not 'prev_operator' in request.GET:
		return False
	if not request.GET.get('prev_operator').strip('\u200b') in operatorList:
		return False
	if not request.GET.get('status') in statusList:
		return False
	if (not isValidText(request.GET.get('textbox')) 
		and request.GET.get('textbox') != 'Error'):
		return False
	if not isValidText(request.GET.get('operand1')):
		return False

	return True









