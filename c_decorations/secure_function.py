def protected(func):

    def wrapper(password):

        if password == "platzi":
            return func()
        else:
            print("Your password is incorrect")

    return wrapper

# Al decir protected estamos decorando la función protected_fun al encapsular su comportamiento dentro del "wrapper"
# Únicamente se ejecuta la función si el password es correcto (si se rtorna la función).
@protected
def protected_fun():
    print("Your password is correct.")


def run():
    password = str(input("Input your password: "))

    protected_fun(password)


if __name__ == "__main__":
    run()
