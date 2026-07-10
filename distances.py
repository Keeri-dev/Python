# Dictionary 
distances = {
    "Voyager 1": 163,
    "Voyager 1": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}
# Access keys

#def main():
#    for name in distances.keys():
#        print(f"{name} is {distances[name]} AU from Earth")
#
#main()


##Convert from AU to Meters
def main():
  for distance in distances.vaules():
      print(f"{distance} AU is {convert(distance)} m")

def convert(au):
    return au * 149597870700
