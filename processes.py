def unit_system():
  unit_base = 0
  metrics = ["mm","dm","cm","m","km"]
  imperials = ["in","ft","yd","mi"]
  units = input("Our systems use the metric system.\nWhat units do you prefer?\n'Metric' or 'Imperial': ")
  units = units.lower()
  if units == "metric":
    unit_base = metrics
  elif units == "imperial":
    unit_base = imperials
  return unit_base

def unit_pick(unit_base):
  print("Your measurements:")
  for i in unit_base:
    print(i, end = ' ')
  print("\n")
  used = int(input("Use the list and the numbers (1,2,3 etc) to pick your units: "))
  units = unit_base[used-1]
  print("\n")
  return units

def one_dimension():
  number_array = []
  print("X")
  while True:
    try:
      num = float(input("Value (type any letter to break): "))
      number_array.append(num)
    except ValueError:
      break
  return number_array


def two_dimensions():
  number_array = []
  number_array2 = []
  n = 0
  print("X")
  while True:
    try:
      num = float(input("Value (type any letter to break): "))
      number_array.append(num)
    except ValueError:
      break
  print("Y")
  while n != len(number_array):
    try:
      num = float(input("Value: "))
      number_array2.append(num)
      n = n + 1
    except ValueError:
      print("A number error occured.")
  return number_array, number_array2


def three_dimensions():
  y = input("Error, 3D not supported yet!")
  if y == "3d":
    number_array = []
    number_array2 = []
    number_array3 = []
    n = 0
    print("X")
    while True:
      try:
        num = float(input("Value (type any letter to break): "))
        number_array.append(num)
      except ValueError:
        break
    print("Y")
    while n != len(number_array):
      try:
        num = float(input("Value: "))
        number_array2.append(num)
        n = n + 1
      except ValueError:
        print("A number error occured.")
    print("Z")
    n = 0
    while n != len(number_array):
      try:
        num = float(input("Value: "))
        number_array3.append(num)
        n = n + 1
      except ValueError:
        print("A number error occured.")
    return number_array, number_array2, number_array3
