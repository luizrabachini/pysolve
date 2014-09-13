#!/usr/bin/python


class CoinDeterminerSolver:
	'''
	Solver of Coin Determiner Problem
	'''

	COIN_VALUES = [11, 9, 7, 5, 1]


	def __init__(self, min_value=1, max_value=250):
		'''
		Class constructor

		:Parameters:
			- `min_value`: Minimum value to calculate least number of coins
			- `max_value`: Maximum value to calculate least number of coins
		'''

		self.min_value = min_value
		self.max_value = max_value


	def coin_determiner(self, num):
		'''
		Calculate least number of coins.

		:Parameters:
			- `num`: Value to calculate least number of coins (must be an integer).

		:Returns:
			Original input, number of coins and array with combination of values.
			If process fail, None is returned.
	 
		:Returns Type:
			(int, int, array), if process success, or None, if process fail.
		'''

		result = []		# Result array
		rest_num = num 	# Rest number

		# Non integer, negative and maximum value check.
		if not isinstance(num, int) or num < self.min_value or num > self.max_value:
			return None

		# Find a maximal coin for subtract from num up to 0.
		while rest_num > 0:
			for cur_coin in self.COIN_VALUES:
				if cur_coin <= rest_num:
					result.append(cur_coin)
					rest_num -= cur_coin
					break
		
		return num, len(result), result


	def coin_determiner_file(self, file_reader):
		'''
		Calculate least number of coins from input file stream.

		:Parameters:
			- `file_reader`: Text file stream of values to calculate coins (must be a file).

		:Returns:
			Array of tuples containing original input, number of coins and array with combination of values.
	 
		:Returns Type:
			array.
		'''

		result = []		# Result array

		for line in file_reader:
			# Prevent non integer input
			try:
				num = int(line)
				result.append(self.coin_determiner(num))
			except:
				result.append(None)

		return result

	def coin_determiner_file_path(self, file_path):
		'''
		Calculate least number of coins from input file (based in path).

		:Parameters:
			- `file_path`: Text file of values to calculate coins (must be a string).

		:Returns:
			See returns of coin_determiner_file method.
		'''

		with open(file_path, 'r') as file_reader:
			return self.coin_determiner_file(file_reader)


if __name__ == '__main__':
	'''
	Command line resource
	'''

	import sys, getopt


	help_message = '\nUsage: core.py --h --v --q --n <num_to_convert> --i <input_file>\n'
	argv = sys.argv[1:]

	verbose = False 		# Show all information about coins: number, least of coins and combination
	quiet = False 			# Disable prints of result
	input_file = None 		# Text file to proccess
	num_to_convert = None 	# Number to convert

	solver = CoinDeterminerSolver()

	# Parse input options
	try:
		opts, args = getopt.getopt(argv, 'hni', ['help', 'verbose', 'quiet', 'num=', 'input='])
	except getopt.GetoptError:
		print help_message
		sys.exit(2)

	# Configure execution
	for opt, arg in opts:
		if opt in ('--i', '--input'):
			input_file = arg
		elif opt in ('--v', '--verbose'):
			verbose = True
		elif opt in ('--q', '--quiet'):
			quiet = True
		elif opt in ('--n', '--num'):
			num_to_convert = arg
		else:
			print help_message
			sys.exit()

	# Call process
	if input_file:
		result = solver.coin_determiner_file_path(input_file)
		if not quiet:
			for entry in result:
				# Print according with verbose (and verify none result)
				print entry if verbose or not entry else entry[1]
	elif num_to_convert:
		num = int(num_to_convert)
		result = solver.coin_determiner(num)
		if not quiet:
			# Print according with verbose (and verify none result)
			print result if verbose or not result else result[1]


# Text file generator for tests
# with open('input_test.txt', 'w') as file_writer:
# 	for value in range(1, 251):
# 		file_writer.write('%d\n' % value)