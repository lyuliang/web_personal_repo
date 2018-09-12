from django.shortcuts import render
def calc(request):
	# context = {}
	# context['person_name'] = ''
	# if 'username' in request.GET:
	# 	context['person_name'] = request.GET['username']
	# return render(request, 'calculator/hello.html', context)    

	context = {}
	context['digit'] = ''

	if 'digit' in request.GET:
		context['digit'] = request.GET['textbox'] + request.GET['digit']
	# if 'operator' in request.GET:
	# 	context['operator'] = request.GET['operator']
	return render(request, 'hello.html', context)
