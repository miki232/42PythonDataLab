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
	if sys.argv[1] in states:
		x = states[sys.argv[1]]
		y = capital_cities[x]
		print(y)
	else :
		print("Unknown state")
