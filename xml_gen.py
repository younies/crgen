#!/usr/bin/python3

import csv


def get_factor(num, den):
	"""
	Return the final factor as a string
	if num/den, will give infinity number, factor will be num/den

	else, we will return decimal number.
	"""
	factor = ""
	if float(den) == 1: factor=  num
	elif float(den) % 10 == 0 : factor = float(num)/float(den)
	else:  factor = "/".join([num, den])

	return "factor='" +str(factor) + "'"


def get_offset(num, den):
	"""
	Return the final factor as a string.

	if offset equal 0, return empty string.
	"""

	offset = ""
	if float(num) == 0: return offset

	if float(den) == 1: offset = num
	else: offset = "/".join([num, den])

	return "offset='" + offset + "'"


def get_reciprocal(reciprocal):
	"""
	return empty string if reciprocal = False,
	Else, return reciprocal='TRUE'
	"""
	if reciprocal == 'F':
		return ''
	else:
		return "reciprocal='TRUE'"

with open('cr_data.csv') as cr_csv:
	cr_reader = csv.reader(cr_csv, delimiter='\t')
	line_count = 0
	for row in cr_reader:
		line_count+=1
		if(line_count == 1): continue
		if (not row[5]) : continue;
		source = 'source=\'' + row[1] +'\''
		target = 'target=\'' + row[2] +'\''

		factor_num = row[3]
		factor_den = row[4]
		factor =  get_factor(factor_num, factor_den) 

		offset_num = row[5]
		offset_den = row[6]
		offset = get_offset(offset_num, offset_den)

		reciprocal = row[7]
		reciprocal = get_reciprocal(reciprocal)

		data = ["<convertUnit" , source, target, factor, offset, reciprocal,  "/>"]
		nonempty_data = list(filter(lambda x: x, data ))
		print(" ".join(nonempty_data))


