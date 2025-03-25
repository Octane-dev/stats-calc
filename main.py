# vars
number_array = []
number_array2 = []
number_array3 = []
number_arrays = 0
n = 0

# defining math modules
import statisticsmaths as sm
import processes as pr

#inputs
print("""Statistics Calculator

Input the amount of dimensions then the axes.
""")

# unit_base = pr.unit_system()
try:
  d = int(input("How many dimensions: "))
  print(d)
except:
  d = 1
  print("Defaulting to 1 dimension.")
while d < 1 or d > 3:
  print(d)
  print("Not a valid dimension")
  try:
    d = int(input("How many dimensions: "))
  except:
    d = 1
    print("Defaulting to 1 dimension.")
if d == 1:
  number_array = pr.one_dimension()
if d == 2:
  number_array, number_array2 = pr.two_dimensions()
if d == 3:
  number_array, number_array2, number_array3 = pr.three_dimensions()


if d > 0 and d < 4:
  rounding = int(input("Decimal places to round to: "))

median_array_1 = number_array
median_array_2 = number_array2
median_array_3 = number_array3

test = sm.mean(number_array,rounding)
if test == 'NAN':
  print("Error! Can't use no values.")
else:

  print()
  print()
  if d == 1:
    print(f"""Mean: {sm.mean(number_array,rounding)}
Median: {sm.median(median_array_1)}
Mode: {sm.mode(number_array)}
Standard Deviation: {sm.standard_deviation(number_array,rounding)}""")

  elif d == 2:
    r_sqrd, dummy, dummy = sm.r_sqr(number_array, number_array2)
    print(f"""R^2: {r_sqrd}
    
X:
Mean: {sm.mean(number_array,rounding)}
Median: {sm.median(median_array_1)}
Mode: {sm.mode(number_array)}
Standard Deviation: {sm.standard_deviation(number_array,rounding)}
  
Y:
Mean: {sm.mean(number_array2,rounding)}
Median: {sm.median(median_array_2)}
Mode: {sm.mode(number_array2)}
Standard Deviation: {sm.standard_deviation(number_array2,rounding)}""")
    linear_interpolation_y = input(
      "Would you like to interpolate a value on the x-axis? (y/n): ")
    if linear_interpolation_y == "y":
      linear_interpolation = float(input("Number: "))
      print(
        f"{sm.linear_interpolation(number_array,number_array2,linear_interpolation)}=m*{linear_interpolation}+c"
      )
  
  elif d == 3:
    print(f"""X:
Mean: {sm.mean(number_array,rounding)}
Median: {sm.median(median_array_1)}
Mode: {sm.mode(number_array)}
Standard Deviation: {sm.standard_deviation(number_array,rounding)}
  
Y:
Mean: {sm.mean(number_array2,rounding)}
Median: {sm.median(median_array_2)}
Mode: {sm.mode(number_array2)}
Standard Deviation: {sm.standard_deviation(number_array2,rounding)}

Z:
Mean: {sm.mean(number_array3,rounding)}
Median: {sm.median(median_array_3)}
Mode: {sm.mode(number_array3)}
Standard Deviation: {sm.standard_deviation(number_array3,rounding)}
""")

    # pr.unit_pick(unit_base)
    # units = pr.unit_pick(unit_base)
    units = "cm"
    
    print("XY:")
    r_sqrdxy, dummy, dummy = sm.r_sqr(number_array, number_array2)
    print(f"R^2: {r_sqrdxy}\n\nXZ:")
    r_sqrdxz, dummy, dummy = sm.r_sqr(number_array, number_array2)
    print(f"R^2: {r_sqrdxz}\n\nYZ:")
    r_sqrdyz, dummy, dummy = sm.r_sqr(number_array, number_array2)
    print(f"R^2: {r_sqrdyz}\n\n3D Space Line: {sm.space_diagonal(number_array,number_array2,number_array3,rounding)}{units}")
