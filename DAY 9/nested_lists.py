#PROGRAM 1 - nested list
#print out "Lille" from the nested List called

# travel_log = {
#     "France": ["Paris", "Lille","Dijon"], #this list[] is the value for france key
#     "Germany" : ["Stuttgart", "Berlin"],
# }
# print(travel_log["France"][1])





#PROGRAM 2 - Nesting Lists inside other Lists
#print out D

Nested_list = ["A", "B", ["C", "D"]]
print(Nested_list[2][1])





#PROGRAM 3 - nested a dictionary in a dictionary:
# print out "Stuttgart" from the following list:
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][2])