def decorator(is_valid):
    def _decorator(func):
        def before_action():
            print("We are going to execute the function")

        def after_action():
            print("The function was executed")

        # Recibir n cantidad de parámetros (*args, **kargs)
		# (*args, **kargs) --> simplemente son los argumentos que tienen keaywords, es decir, que tienen nombre, por ejemplo, cuando le 
		# 	asignamos un valor default o los argumentos posicionales 
		# la estrella (*) y la doble estrella (**) es simplemente una expansión. aquí le estamos diciendo a python que estamos recibiendo 
		# una lista, yo no quiera esa lista, quiero esos parámetros tal cual son. 
		# En sí, con esto estamos evitando el problema de determinar de antemano cuales son los parámetros que requiere la función, aquí los
        def new_function(*args, **kargs):
			# aquí estamos recibiendo y estamos pasando los parámetros a la función
			result = func(*args, **kargs)
            if is_valid:
                before_action()
            after_action()
            return result

        return new_function

    return _decorator


@decorator(is_valid=True)
def regrets():
    print("Hi world")


@decorator(is_valid=False)
def add(number_1, number_2):
    return number_1 + number_2


if __name__ == "__main__":
    regrets()
    print("**********")
    print(add(90, 17))
