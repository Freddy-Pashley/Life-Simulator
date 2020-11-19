
import random


__title__ = 'Life Simulator'
__version__ = '0.0.1'
__author__ = 'Freddy Pashley'
__license__ = 'MIT'
__notes__ = 'This is a script used for Life Simulator.'



def get_name(filename1='firstnames.txt', filename2='lastnames.txt'):
	lines = 0
	try:
		with open('./names/{0}'.format(filename1)) as f:
			f.close()
		try:
			lines = open('./names/{0}'.format(filename1)).read().splitlines()
			if lines == []:
				return '{0} and/or {0} is empty'.format(filename1, filename2)
			else:
				result = str(random.choice(lines))
				lines = 0
				try:
					with open('./names/{0}'.format(filename2)) as f:
						f.close()
					try:
						lines = open('./names/{0}'.format(filename2)).read().splitlines()
						if lines == []:
							return '{0} is empty'.format(filename2)
						else:
							result = '{0} {1}'.format(result, str(random.choice(lines)))
							return result
					except Exception as e:
						raise Exception(e)
				except:
					return '{0} not found.'.format(filename2)
		except Exception as e:
			raise Exception(e)
	except:
		return '{0} not found.'.format(filename1)


def get_firstname(filename=None):
	if filename == None:
		filename = 'firstnames.txt'
		lines = 0
		try:
			with open('./names/{0}'.format(filename)) as f:
				f.close()
			try:
				lines = open('./names/{0}'.format(filename)).read().splitlines()
				if lines == []:
					return '{0} is empty'.format(filename)
				else:
					return random.choice(lines)
			except Exception as e:
				raise Exception(e)
		except:
			return '{0} not found'.format(filename)
	else:
		lines = 0
		try:
			with open(filename) as f:
				f.close()
			try:
				lines = open(filename).read().splitlines()
				if lines == []:
					return '{0} is empty'.format(filename)
				else:
					return random.choice(lines)
			except Exception as e:
				raise Exception(e)
		except:
			return '{0} not found'.format(filename)


def get_lastname(filename=None):
	if filename == None:
		filename = 'lastnames.txt'
		lines = 0
		try:
			with open('./names/{0}'.format(filename)) as f:
				f.close()
			try:
				lines = open('./names/{0}'.format(filename)).read().splitlines()
				if lines == []:
					return '{0} is empty'.format(filename)
				else:
					return random.choice(lines)
			except Exception as e:
				raise Exception(e)
		except:
			return '{0} not found'.format(filename)
	else:
		lines = 0
		try:
			with open(filename) as f:
				f.close()
			try:
				lines = open(filename).read().splitlines()
				if lines == []:
					return '{0} is empty'.format(filename)
				else:
					return random.choice(lines)
			except Exception as e:
				raise Exception(e)
		except:
			return '{0} not found'.format(filename) 
	
		

print(get_name('lastnames.txt', 'firstnames.txt'))