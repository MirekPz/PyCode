def uppercase_decorator(txt_func):
    def nested():
        txt = txt_func()  # say_hello() --> hello
        txt = txt.upper() # --> HELLO
        return txt
    return nested


@uppercase_decorator
def say_hello():
    return "hello"


@uppercase_decorator
def say_hi():
    return "hihihi"


print(say_hello())
print(say_hi())

# uppercased_text = uppercase_decorator(say_hello)
# print(uppercased_text())

# uppercased_text = uppercase_decorator(say_hi)
# print(uppercased_text())
