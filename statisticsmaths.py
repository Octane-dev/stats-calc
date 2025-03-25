def mean(numbers: list, decimal: int) -> float:
  try:
    return round(sum(numbers) / len(numbers), decimal)
  except:
    return 'NAN'


def r_sqr(X: list, Y: list) -> float:
  mean_x = sum(X) / len(X)
  mean_y = sum(Y) / len(Y)
  n = len(X)
  numer = 0
  denom = 0
  ss_xy_pt1 = 0
  ss_xx_pt1 = 0
  for i in range(n):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x)**2

    ss_xy_pt1 += X[i] * Y[i]
    ss_xx_pt1 += X[i] * X[i]

  ss_xy = ss_xy_pt1 - n * mean_x * mean_y
  ss_xx = ss_xx_pt1 - n * mean_x**2
  try:
    m = ss_xy / ss_xx
  except ZeroDivisionError:
    return 1.0
  c = mean_y - m * mean_x

  covariance = numer / (n - 1)
  std_dev_x = standard_deviation(X, 10)
  std_dev_y = standard_deviation(Y, 10)
  correl_coeff = covariance / (std_dev_x * std_dev_y)
  ss_t = 0
  ss_r = 0
  for i in range(int(n)):
    y_pred = c + m * X[i]
    ss_t += (Y[i] - mean_y)**2
    ss_r += (Y[i] - y_pred)**2
  r2 = 1 - (ss_r / ss_t)
  print(f"Best Fit Line: y = {round(m,3)}x + {round(c,3)}")
  print(f"Correlation Coefficient: {round(correl_coeff,5)}")
  return round(r2, 5), m, c


def square_root(num: "int or str") -> float:
  root = num**0.5
  return root


def standard_deviation(numbers: list, decimal: int) -> float:
  mean = sum(numbers) / len(numbers)
  sum_all = [(x - mean)**2 for x in numbers]
  total = round(square_root((sum(sum_all)) / (len(numbers) - 1)), decimal)
  return total


def median(temp1: list) -> float:
  length = len(temp1)
  temp1.sort()
  if length % 2 == 0:
    median1 = temp1[length // 2]
    median2 = temp1[length // 2 - 1]
    median = (median1 + median2) / 2
  else:
    median = temp1[length // 2]
  return median


def mode(numbers: list) -> list:
  freq = {}
  for number in numbers:
    freq.setdefault(number, 0)
    freq[number] += 1
  highFreq = max(freq.values())
  highFreqList = []
  for number, freq1 in freq.items():
    if freq1 == highFreq:
      highFreqList.append(number)
  if len(highFreqList) > 1:
    return 'No Mode'
  else:
    return highFreqList


def linear_interpolation(X: list, Y: list, value: float) -> float:
  dummy, m, c = r_sqr(X, Y)
  y = m * value + c
  return y

def pythagoras(x:float, y:float) -> float:
  xS = x**2
  yS = y**2
  cS = xS + yS
  c = square_root(cS)
  return c


def space_diagonal(X: list, Y: list, Z: list, rounding: int) -> float:
  #repeated use pythag
  # a + b = c
  x1 = X[0]
  x2 = X[-1]
  y1 = Y[0]
  y2 = Y[-1]
  z1 = Z[0]
  z2 = Z[-1]
  x_d = x2 - x1
  y_d = y2 - y1
  z_d = z2 - z1
  #xy pythag
  pythag_xy = pythagoras(x_d,y_d)
  pythag_z = pythagoras(pythag_xy,z_d)
  return round(pythag_z,rounding)
