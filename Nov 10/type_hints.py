#type hints describe what datatypes are expected for parameters and return values
#They are documentation only. NOT enforced

def greet (name: str)-> str:#returns a string
    return f"Hello {name}"

def shout (name: str)-> None:#returns nothing
    print (f"Hello {name}")

def shoutShane (name: str)->str | None:#returns str OR None
    if name == "Shane":
        return f"HEY {name.upper()}!"
    else:
        return None
