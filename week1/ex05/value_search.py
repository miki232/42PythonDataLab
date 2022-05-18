from operator import le
import sys

states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}
capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}

if (len(sys.argv) == 2):
	if sys.argv[1] in capital_cities.values() :
		c = [key for key, value in capital_cities.items() if value == sys.argv[1]][0]
		print(c)
		x = [key2 for key2 , value2 in states.items() if value2 == c][0]
		print (x)
	else :
		print("Unknown capital city")
