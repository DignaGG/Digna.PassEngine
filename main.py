from password_config import PasswordConfig
from generator import PasswordGenerator
from validator import PasswordValidator

def get_user_config():
    #Length
    value = input("Length (default 12): ")
    if not value:
        length = 12
    else:
        try:
            length = int(value)
        except:
            length = 12
            print("Invalid input. Using default value.")

    #UpperCase
    value =  input("Use uppercase? (y/n, default y): ")
    if not value:
        use_uppercase = True
    else:
        if (value == "y"):
            use_uppercase = True
        elif (value == "n"):
            use_uppercase = False
        else:
            use_uppercase = True
            print("Invalid input. Using default value.")

    #LowerCase
    value =  input("Use lowercase? (y/n, default y): ")
    if not value:
        use_lowercase = True
    else:
        if (value == "y"):
            use_lowercase = True
        elif (value == "n"):
            use_lowercase = False
        else:
            use_lowercase = True
            print("Invalid input. Using default value.")

    #Digits
    value =  input("Use digits? (y/n, default y): ")
    if not value:
        use_digits = True
    else:
        if (value == "y"):
            use_digits = True
        elif (value == "n"):
            use_digits = False
        else:
            use_digits = True
            print("Invalid input. Using default value.")

    #Symbols
    value =  input("Use symbols? (y/n, default n): ")
    if not value:
        use_symbols = False
    else:
        if (value == "y"):
            use_symbols = True
        elif (value == "n"):
            use_symbols = False
        else:
            use_symbols = False
            print("Invalid input. Using default value.")

    #ExcludeAmbiguous
    value =  input("Exclude ambiguous characters? (y/n, default y): ")
    if not value:
        exclude_ambiguous = True
    else:
        if (value == "y"):
            exclude_ambiguous = True
        elif (value == "n"):
            exclude_ambiguous = False
        else:
            exclude_ambiguous = True
            print("Invalid input. Using default value.")

    config = PasswordConfig(length, use_uppercase, use_lowercase, use_digits, use_symbols, exclude_ambiguous)
    return config

def main():
    while True:
        config = get_user_config()
        validator = PasswordValidator(config)
        generator = PasswordGenerator(config, validator)

        password = generator.generate()
        print(f"\nGenerated password: {password}\n")

        again = input("Generate another? (y/n): ").lower()
        if again != "y":
            print("GoodBye!")
            break

if __name__ == "__main__":
    main()