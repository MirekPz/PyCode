def example_function():
    a = 7

    def nested_function(age):
        print('Jestem w środku zagnieżdżenia')
        return a * age

    return nested_function


new_function = example_function()
print(new_function(30))
print(new_function(20))
