from collections import OrderedDict


glossary = OrderedDict()
glossary['loop'] = "a sequence of instruction s that is continually repeated until a certain condition is reached",
glossary['function'] = "a named section of a program that performs a specific task",
glossary['boolean'] = "a data type that has one of two possible values (usually denoted true and false), intended to represent the two truth values of logic and Boolean algebra",
glossary['list'] = "a tool that can be used to store multiple pieces of information at once",
glossary['string'] = "a data type used in programming used to represent text",
glossary['debugging'] = "the process of finding and removing programming errors",
glossary['dictionary'] = "a mutable associative array (or dictionary) of key and value pairs",
glossary['if statement'] = "conditionally executes a block of code, along with else and elif",
glossary['PEP 8'] = "a set of recommendations how to write Python code",
glossary['variables'] = "placeholder for texts and numbers",
    

for term, definition in glossary.items():
    if term == 'PEP 8':
        print("\n" + term + ":") 
    else:
        print("\n" + term.title() + ":")
    print(definition)


