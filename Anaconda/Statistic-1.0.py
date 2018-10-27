import math

data1 = [0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25, 4.73]
data2 = [0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25,  100]
# tinh trung binh cong
def mean(data):
    return sum(data)/len(data)
# tinh gia tri o giua
def median(data):
    data = sorted(data)
    n = len(data)
    if n % 2 == 1:
        return data[n // 2]
    else:
        i = n // 2
        return (data[i-1] + data[i])/2
# tinh do lech trung binh so voi mean
def mydev1 (data):
    mu = mean(data)
    return sum([point-mu for point in data])/len(data)
def mydev2 (data):
    mu = mean(data)
    return sum([abs(point-mu) for point in data])/len(data)
# tinh phuong sai Variance
def variance(data):
    mu = mean(data)
    return sum([(point-mu)**2  for point in data])/len(data)
# Tinh do lech tieu chuan Standard deviation
def stddev(data):
    return math.sqrt(variance(data))

mu1 = mean(data1)
mu2 = mean(data2)
me1 = median(data1)
me2 = median(data2)
de11 = mydev1(data1)
de12 = mydev1(data2)
de21 = mydev2(data1)
de22 = mydev2(data2)
var1 = variance(data1)
var2 = variance(data2)
sdev1 = stddev(data1)
sdev2 = stddev(data2)

print("Lenght of data1: ",len(data1))
print("Length of data2: ",len(data2))
print ("Mean(agv) of data1: ", mu1)
print("Mean(agv) of data1: ", mu2)
print ("Median of data1: ", me1)
print("Median of data2: ", me2)
print ("Method 1 - Deviation of data1: ", de11)
print("Method 1 - Deviationof data2: ", de12)
print ("Method 2 - Deviation of data1: ", de21)
print("Method 2 - Deviation of data2: ", de22)
print ("Variance of data1: ", var1)
print("Variance of data2: ", var2)
print ("Standard deviation of data1: ", sdev1)
print("Standard deviation of data2: ", sdev2)