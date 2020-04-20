def upper(func):
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		
		return result.upper()
		
	return wrapper

@upper
def say_my_name(name):
	return "Hola, {}".format(name)


if __name__ == "__main__":
	print(say_my_name("cristhian"))
