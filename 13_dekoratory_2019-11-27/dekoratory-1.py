def example_function():

    def nested_function():
        print('Jestem w środku zagnieżdżenia')

    return nested_function


new_function = example_function()
print(new_function)
new_function()
