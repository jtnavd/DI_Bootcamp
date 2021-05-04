class PythonDict():
    def __init__(self, name, definition):
        self.name = name
        self.definition = definition

    def __doc__(self):
        return f'{self.name}{self.definition}'

# DICTONARY
d1 = PythonDict('abs', ': This function is used to return the absolute value of a number.')
d2 = PythonDict('int',': This function convert number to intenger' )
d3 = PythonDict('input', ': This function allow the user to print a variable')

