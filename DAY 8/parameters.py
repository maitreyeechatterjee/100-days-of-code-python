# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")


#function with multiple inputs

#positional parameters

def greet_with(name,location):
    print(f"hello {name}")
    print(f"how is {location}")

greet_with("mona","india")


#keyword parameters

def my_function(month,season):
    print(f"next month is {month} ")
    print(f"{season} will be starting soon")

my_function(month ="november", season ="winter")
my_function(season ="winter", month ="november" )
