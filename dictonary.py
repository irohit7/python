#mydic = {"first":"one","Two":"second","three":"Third",
       #  "four":"forth","Five":"Fifth"}
#print(mydic["first"])
#print(mydic["Two"])

my = {"vin":"dominic","corner":"paul","robert":"Iron man","jonny":"jack","paresh":"Babu bhaiya"}
my["rajnikant"] = "thala"
my["paneer"] = "65"
del my["paneer"]
#my1 = my.copy()
#print(my1)
#my.update({"akshay":"kumar"})
print(my)
#print(my.keys())
#print(my.items())
my.popitem()
print(my)
my["ranjikant"] = "thala"
print(my)
