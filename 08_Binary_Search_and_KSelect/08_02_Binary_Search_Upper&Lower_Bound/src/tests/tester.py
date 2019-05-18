import os
import re

def tester(problem_name, f):
	input_path = "src/tests/" + problem_name + "/input/"
	output_path = "src/tests/" + problem_name + "/output/"
	regex = re.compile(r'input(\d+).txt')
	co = 1;
	num_tests = 0
	num_wrong = 0
	for file_name in os.listdir(input_path):	
		m = regex.match(file_name)
		if not m:
			continue
		n = m.groups()[0]
		input_file_path = os.path.join(input_path, file_name)
		output_file_path = os.path.join(output_path, "output" + n + ".txt")
		if not os.path.isfile(output_file_path):
			print("output for input file " + input_file_path + "does not exist!")
			continue
		num_tests += 1
		with open(input_file_path) as input_file:
			with open(output_file_path) as output_file:
				input_params = []
				output = eval(output_file.readlines()[0])
				for line in input_file.readlines():
					input_params.append(eval(line))
				if not f(*input_params.copy()) == output:
					num_wrong += 1
	if num_wrong != 0:
		print("Your code get wrong answer in " + str(num_wrong) + " test(s) from " + str(num_tests) + " test(s).")
	else:
		print("Your code passes all " + str(num_tests) + " test(s).")
