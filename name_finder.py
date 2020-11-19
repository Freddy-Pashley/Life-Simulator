
import random


__title__ = 'Life Simulator'
__version__ = '0.0.1'
__author__ = 'Freddy Pashley'
__license__ = 'MIT'
__notes__ = 'This is a script used for Life Simulator.'



def get_name(filename1=None, filename2=None):
	if filename1 == None or filename2 == None:
		return 'You must provide valid paths to the documents you want to scan for names'
	else:
		lines = 0
		try:
			with open(filename1) as f:
				f.close()
			try:
				lines = open(filename1).read().splitlines()
				if lines == []:
					return '{0} is empty'.format(filename1)
				else:
					result = str(random.choice(lines))
					lines = 0
					try:
						with open(filename2) as f:
							f.close()
						try:
							lines = open(filename2).read().splitlines()
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
		return 'You must provide a valid path to the document you want to scan for names'
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
		return 'You must provide a valid path to the document you want to scan for names'
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
	
	