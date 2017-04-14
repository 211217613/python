#!/usr/bin/python3

import logging
import timeit

logging.basicConfig(filename='timing.log', filemode='w',level=logging.INFO)

def make_param_list(var 1, var 2):
	pass

def test_list():
	logging.info("Test list-1: create an empty list")
	spec_string = "1<=n<=10"
	growth_factor = 2
	logging.info("Spec string {0} by factors of {1}".format(spec_string, growth_factor))

	var_list, param_list = make_param_list(spec_string, growth_factor)
	f_list = ("1",)
	run_times = []
	trials = 1000
	for D in param_list:
		t = timeit.Timer("x = list()")
		run_times.append(t.timeit(trials)*1e6/float(trials))
	fit(var_list, param_list, run_times, f_list)
	

if __name__ == '__main__':
	test_list()