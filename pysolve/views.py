from pyramid.view import view_config
from pyramid.renderers import render_to_response
from libs.coin_determiner.solver import CoinDeterminerSolver


@view_config(route_name='home', renderer='templates/home.html')
def home_view(request):
	'''
	Home of project
	'''

	return {}


@view_config(route_name='coin_determiner', renderer='templates/coin_determiner.html')
def coin_determiner_view(request):
	'''
	Coin determiner solver
	'''

	if request.POST:
		solver = CoinDeterminerSolver()
		result = []
		message = None

		input_value = request.POST.get('input-value')
		input_value_file = request.POST.get('input-value-file')		

		# Prevent non integer input
		try:
			num = int(input_value)
			result.append(solver.coin_determiner(num))
		except ValueError:
			pass

		# Prevent non upload file input
		try:
			input_file = input_value_file.file
			result += solver.coin_determiner_file(input_file)
		except AttributeError:
			pass

		if len(result) == 0:
			message = 'Nothing to do.'

		return {'result':result, 'message':message}

	return {}

## Error page

def notfound_view(self, request):
	'''
	404 custom page
	'''

	return render_to_response('templates/404.html', {}, request=request)