from itertools import *
from random import *
'''
Returns a list of lists of what num number of numbers that sum up to summation 
'''
def sum_list_memo(summation, num):
	answer = []
	if (num <= 0):
		return []
	if (num == 1 and summation >= 10) or (summation < 0):
		return []
	if (num == 1 and summation < 10 and summation >= 0):
		return [[summation]]
	else:
		for i in range(10):
			a = sum_list_memo(summation - i, num - 1)
			for j in a:
				print(j)
				j.append(i)
				answer.append(j)
			
	return answer

def sum_list_memo_2(summation, num, r):
	if r[summation][num]:
		return r[summation][num]
	else:
		answer = []
		if (num <= 0):
			r[summation][num] = []
		if (num == 1 and summation >= 10) or (summation < 0):
			r[summation][num] = []
		if (num == 1 and summation < 10 and summation >= 0):
			r[summation][num] = [[summation]]
		else:
			for i in range(10):
				a = None
				if (summation - i < 0) or num == 0:
					a = []
				else:
					a = sum_list_memo_2(summation - i, num - 1, r)
				# print(a)
				for j in a:
					k = list(j)
					k.append(i)
					answer.append(k)
			r[summation][num] = answer
		return r[summation][num]


def sum_list(summation, num):
	r = [[None for i in range(num + 1)] for j in range(summation + 1)]
	# print(r)
	return sum_list_memo_2(summation,num,r)

def random_index():
	a = [i for i in range(80)]
	ans = []
	for i in range(32):
		k = randint(0, len(a) - 1)
		ans.append(a[k])
		a.remove(a[k])
	return ans

def random_list():
	ans = []
	a = [i for i in range(10)]
	while a:
		print(a)
		k = randint(0,len(a) - 1)
		ans.append(a[k])
		print(k)
		print(a[k])
		a.remove(a[k])
	return ans

# a = sum_list(10,8)
print(random_list())
# b = sum_list_memo(2,3)
# print(a)
# print(b)