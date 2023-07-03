
# 1.4.1
x = "X "
for i in range(1, 5+1, 1):
  print(i*x)
for i in range(4, 1-1, -1):
  print(i*x)

#1.4.2
input_str = "n45as29@#8ss6"
x = list(input_str)
#x = input_str.split('',4)
y = [0]
for i in range(0, len(x),1):
  try:
    y.append(int(x[i]))
  except:
    pass
y.pop(0)
print(sum(y))

#1.4.3
number = 10
b = [0]
while number >= 1:
  number = number // 2
  b.append(str(number % 2))
b.pop(0)
print("".join(b)) 

#1.5.1
def fibonaci(upper_threshold: int) -> list:
  z = 0
  x = 0
  y = 1
  e = [0,1]
  while z < upper_threshold:
    i = 2
    z = x + y
    if z < upper_threshold:
      e.append(z)
    i += 1
    x = y
    y = z
  return e
print(fibonaci(10))

#1.5.2 Basic
def digi0(row):
    global rowline
    if row == 0:
        rowline = "xxx"
    if row == 1:
        rowline = "x x"
    if row == 2:
        rowline = "x x"
    if row == 3:
        rowline = "x x"
    if row == 4:
        rowline = "xxx"
    return rowline

def digi1(row):
    global rowline
    if row == 0:
        rowline = "  x"
    if row == 1:
        rowline = "  x"
    if row == 2:
        rowline = "  x"
    if row == 3:
        rowline = "  x"
    if row == 4:
        rowline = "  x"
    return rowline

def digi2(row):
    global rowline
    if row == 0:
        rowline = "xxx"
    if row == 1:
        rowline = "  x"
    if row == 2:
        rowline = "xxx"
    if row == 3:
        rowline = "x  "
    if row == 4:
        rowline = "xxx"
    return rowline

def digi3(row):
    global rowline
    if row == 0:
        rowline = "xxx"
    if row == 1:
        rowline = "  x"
    if row == 2:
        rowline = "xxx"
    if row == 3:
        rowline = "  x"
    if row == 4:
        rowline = "xxx"
    return rowline

def digi4(row):
    global rowline
    if row == 0:
        rowline = "x x"
    if row == 1:
        rowline = "x x"
    if row == 2:
        rowline = "xxx"
    if row == 3:
        rowline = "  x"
    if row == 4:
        rowline = "  x"
    return rowline

def digi5(row):
    global rowline
    if row == 0:
        rowline = "xxx"
    if row == 1:
        rowline = "x  "
    if row == 2:
        rowline = "xxx"
    if row == 3:
        rowline = "  x"
    if row == 4:
        rowline = "xxx"
    return rowline

def digi6(row):
    global rowline
    if row == 0:
        rowline = "xxx"
    if row == 1:
        rowline = "x  "
    if row == 2:
        rowline = "xxx"
    if row == 3:
        rowline = "x x"
    if row == 4:
        rowline = "xxx"
    return rowline

def digi7(row):
    global rowline
    if row == 0:
        rowline = "xxx"
    if row == 1:
        rowline = "  x"
    if row == 2:
        rowline = "  x"
    if row == 3:
        rowline = "  x"
    if row == 4:
        rowline = "  x"
    return rowline

def digi8(row):
    global rowline
    if row == 0:
        rowline = "xxx"
    if row == 1:
        rowline = "x x"
    if row == 2:
        rowline = "xxx"
    if row == 3:
        rowline = "x x"
    if row == 4:
        rowline = "xxx"
    return rowline

def digi9(row):
    global rowline
    if row == 0:
        rowline = "xxx"
    if row == 1:
        rowline = "x x"
    if row == 2:
        rowline = "xxx"
    if row == 3:
        rowline = "  x"
    if row == 4:
        rowline = "  x"
    return rowline

drow = ["","","","",""]
def display_as_digi(number: int) -> None:
    x = list(str(number))
    for num in range(len(x)):
        for row in range(0,5,1):
            if x[num] == "0":
                drow[row] = drow[row] + digi0(row)
            elif x[num] == "1":
                drow[row] = drow[row] + digi1(row)
            elif x[num] == "2":
                drow[row] = drow[row] + digi2(row)
            elif x[num] == "3":
                drow[row] = drow[row] + digi3(row)
            elif x[num] == "4":
                drow[row] = drow[row] + digi4(row)
            elif x[num] == "5":
                drow[row] = drow[row] + digi5(row)
            elif x[num] == "6":
                drow[row] = drow[row] + digi6(row)
            elif x[num] == "7":
                drow[row] = drow[row] + digi7(row)
            elif x[num] == "8":
                drow[row] = drow[row] + digi8(row)
            elif x[num] == "9":
                drow[row] = drow[row] + digi9(row)
            else:
                pass
            drow[row] = drow[row]+" "
    for i in range(0,5,1):
        print(drow[i])

display_as_digi(1234567890)

#1.5.2 Extension
def digi0(row):
    global rowline
    if row == 0:
        rowline = "xxx"
    if row == 1:
        rowline = "x x"
    if row == 2:
        rowline = "x x"
    if row == 3:
        rowline = "x x"
    if row == 4:
        rowline = "xxx"
    return rowline

def digi1(row):
    global rowline
    if row == 0:
        rowline = "  x"
    if row == 1:
        rowline = "  x"
    if row == 2:
        rowline = "  x"
    if row == 3:
        rowline = "  x"
    if row == 4:
        rowline = "  x"
    return rowline

def digi2(row):
    global rowline
    if row == 0:
        rowline = "xxx"
    if row == 1:
        rowline = "  x"
    if row == 2:
        rowline = "xxx"
    if row == 3:
        rowline = "x  "
    if row == 4:
        rowline = "xxx"
    return rowline

def digi3(row):
    global rowline
    if row == 0:
        rowline = "xxx"
    if row == 1:
        rowline = "  x"
    if row == 2:
        rowline = "xxx"
    if row == 3:
        rowline = "  x"
    if row == 4:
        rowline = "xxx"
    return rowline

def digi4(row):
    global rowline
    if row == 0:
        rowline = "x x"
    if row == 1:
        rowline = "x x"
    if row == 2:
        rowline = "xxx"
    if row == 3:
        rowline = "  x"
    if row == 4:
        rowline = "  x"
    return rowline

def digi5(row):
    global rowline
    if row == 0:
        rowline = "xxx"
    if row == 1:
        rowline = "x  "
    if row == 2:
        rowline = "xxx"
    if row == 3:
        rowline = "  x"
    if row == 4:
        rowline = "xxx"
    return rowline

def digi6(row):
    global rowline
    if row == 0:
        rowline = "xxx"
    if row == 1:
        rowline = "x  "
    if row == 2:
        rowline = "xxx"
    if row == 3:
        rowline = "x x"
    if row == 4:
        rowline = "xxx"
    return rowline

def digi7(row):
    global rowline
    if row == 0:
        rowline = "xxx"
    if row == 1:
        rowline = "  x"
    if row == 2:
        rowline = "  x"
    if row == 3:
        rowline = "  x"
    if row == 4:
        rowline = "  x"
    return rowline

def digi8(row):
    global rowline
    if row == 0:
        rowline = "xxx"
    if row == 1:
        rowline = "x x"
    if row == 2:
        rowline = "xxx"
    if row == 3:
        rowline = "x x"
    if row == 4:
        rowline = "xxx"
    return rowline

def digi9(row):
    global rowline
    if row == 0:
        rowline = "xxx"
    if row == 1:
        rowline = "x x"
    if row == 2:
        rowline = "xxx"
    if row == 3:
        rowline = "  x"
    if row == 4:
        rowline = "  x"
    return rowline

def digidec(row):    
    global rowline 
    if row == 0:   
        rowline = "   "
    if row == 1:   
        rowline = "   "
    if row == 2:   
        rowline = "   "
    if row == 3:   
        rowline = "   "
    if row == 4:   
        rowline = "  x"
    return rowline

drow = ["","","","",""]
def display_as_digi(number: int) -> None:
    x = list(str(number))
    for num in range(len(x)):
        for row in range(0,5,1):
            if x[num] == "0":
                drow[row] = drow[row] + digi0(row)
            elif x[num] == "1":
                drow[row] = drow[row] + digi1(row)
            elif x[num] == "2":
                drow[row] = drow[row] + digi2(row)
            elif x[num] == "3":
                drow[row] = drow[row] + digi3(row)
            elif x[num] == "4":
                drow[row] = drow[row] + digi4(row)
            elif x[num] == "5":
                drow[row] = drow[row] + digi5(row)
            elif x[num] == "6":
                drow[row] = drow[row] + digi6(row)
            elif x[num] == "7":
                drow[row] = drow[row] + digi7(row)
            elif x[num] == "8":
                drow[row] = drow[row] + digi8(row)
            elif x[num] == "9":
                drow[row] = drow[row] + digi9(row)
            elif x[num] == ".":
                drow[row] = drow[row] + digidec(row)
            else:
                pass
            drow[row] = drow[row]+" "
    for i in range(0,5,1):
        print(drow[i])

display_as_digi(0.123456789)

#2.1
import numpy as np
import time

matrix = np.arange(25, 0, -1).reshape((5,5))

def thresholder(threshold):
    start = time.time()
    np.where(matrix < threshold, 0, matrix)
    end = time.time()
    thresholder_time = end - start
    print(thresholder_time)

def thresholderloop(threshold):
    start = time.time()
    for i in range(0,5,1):
        for j in range(0,5,1):
            if matrix[i][j] < threshold:
                matrix[i][j] = 0
    end = time.time()
    thresholderloop_time = end - start
    print(thresholderloop_time)

threshold = 12
matrix = np.arange(25, 0, -1).reshape((5,5))
thresholder(threshold)
matrix = np.arange(25, 0, -1).reshape((5,5))
thresholderloop(threshold)

#2.2
import numpy as np
import matplotlib.pyplot as plt

def digi0(row):
    global rowline
    if row == 0:
        rowline = "000"
    if row == 1:   
        rowline = "010"
    if row == 2:   
        rowline = "010"
    if row == 3:   
        rowline = "010"
    if row == 4:   
        rowline = "000"
    return rowline 
                   
def digi1(row):    
    global rowline 
    if row == 0:   
        rowline = "110"
    if row == 1:   
        rowline = "110"
    if row == 2:   
        rowline = "110"
    if row == 3:   
        rowline = "110"
    if row == 4:   
        rowline = "110"
    return rowline 
                   
def digi2(row):    
    global rowline 
    if row == 0:   
        rowline = "000"
    if row == 1:   
        rowline = "110"
    if row == 2:   
        rowline = "000"
    if row == 3:   
        rowline = "011"
    if row == 4:   
        rowline = "000"
    return rowline 
                   
def digi3(row):    
    global rowline 
    if row == 0:   
        rowline = "000"
    if row == 1:   
        rowline = "110"
    if row == 2:   
        rowline = "000"
    if row == 3:   
        rowline = "110"
    if row == 4:   
        rowline = "000"
    return rowline 
                   
def digi4(row):    
    global rowline 
    if row == 0:   
        rowline = "010"
    if row == 1:   
        rowline = "010"
    if row == 2:   
        rowline = "000"
    if row == 3:   
        rowline = "110"
    if row == 4:   
        rowline = "110"
    return rowline 
                   
def digi5(row):    
    global rowline 
    if row == 0:   
        rowline = "000"
    if row == 1:   
        rowline = "011"
    if row == 2:   
        rowline = "000"
    if row == 3:   
        rowline = "110"
    if row == 4:   
        rowline = "000"
    return rowline 
                   
def digi6(row):    
    global rowline 
    if row == 0:   
        rowline = "000"
    if row == 1:   
        rowline = "011"
    if row == 2:   
        rowline = "000"
    if row == 3:   
        rowline = "010"
    if row == 4:   
        rowline = "000"
    return rowline 
                   
def digi7(row):    
    global rowline 
    if row == 0:   
        rowline = "000"
    if row == 1:   
        rowline = "110"
    if row == 2:   
        rowline = "110"
    if row == 3:   
        rowline = "110"
    if row == 4:   
        rowline = "110"
    return rowline 
                   
def digi8(row):    
    global rowline 
    if row == 0:   
        rowline = "000"
    if row == 1:   
        rowline = "010"
    if row == 2:   
        rowline = "000"
    if row == 3:   
        rowline = "010"
    if row == 4:   
        rowline = "000"
    return rowline 
                   
def digi9(row):    
    global rowline 
    if row == 0:   
        rowline = "000"
    if row == 1:   
        rowline = "010"
    if row == 2:   
        rowline = "000"
    if row == 3:   
        rowline = "110"
    if row == 4:   
        rowline = "110"
    return rowline

drow = ["","","","",""]
b = []
def show_in_digi(input_integer: int) -> None:

    global c
    x = list(str(input_integer))
    for num in range(len(x)):
        for row in range(0,5,1):
            drow[row] = drow[row]+"1"
            if x[num] == "0":
                drow[row] = drow[row] + digi0(row)
            elif x[num] == "1":
                drow[row] = drow[row] + digi1(row)
            elif x[num] == "2":
                drow[row] = drow[row] + digi2(row)
            elif x[num] == "3":
                drow[row] = drow[row] + digi3(row)
            elif x[num] == "4":
                drow[row] = drow[row] + digi4(row)
            elif x[num] == "5":
                drow[row] = drow[row] + digi5(row)
            elif x[num] == "6":
                drow[row] = drow[row] + digi6(row)
            elif x[num] == "7":
                drow[row] = drow[row] + digi7(row)
            elif x[num] == "8":
                drow[row] = drow[row] + digi8(row)
            elif x[num] == "9":
                drow[row] = drow[row] + digi9(row)
            else:
                pass
    for i in range(0,5,1):
#        print(list(drow[i])+list("1"))
        b.append(list(drow[i])+list("1"))
    c = np.array(b).reshape((5,17))
    c = c.astype(int)
    plt.figure(1)
    plt.imshow(c, cmap='Greys')

show_in_digi(5289)

#3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('sample_data/california_housing_test.csv')

describe = dataset.describe()

print(dataset[dataset['total_bedrooms'] > 310])

dataset = dataset.drop(dataset.head(1).index)
dataset = dataset.drop(dataset.tail(1).index)

mean = dataset['households'].mean()
print(mean)

plt.figure(2)
plt.plot(dataset['households'],':')
plt.axhline(y=mean, color='red')

if dataset.isnull().values.any():
    print ("True")
    dataset.replace(to_replace = pd.NA, value = dataset.mean(), inplace=True)
else:
    print ("False")

x = dataset['latitude']
y = dataset['longitude']
plt.figure(3)
plt.scatter(x, y)

normalize=(dataset['total_bedrooms']-dataset['total_bedrooms'].min())/(dataset['total_bedrooms'].max()-dataset['total_bedrooms'].min())
print(normalize)

CorrelationMatrix = dataset.corr()
print(CorrelationMatrix)



