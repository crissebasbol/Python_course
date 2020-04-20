from b_oop.classes.Lamp import Lamp


def run():
    lamp = Lamp(status_lamp=True)

    while True:
        command = str(input("""
            What do you want to do?
            
            [t]urn on
            [s]hut down 
            [o]ut
            
        """))

        if command == "t":
            lamp.turn_on()
        elif command == "s":
            lamp.turn_off()
        elif command == "o":
            break
        else:
            print("Command not valid")


if __name__ == "__main__":
    run()
