data1 = [0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25, 4.73, 5.67]
data2 = [0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25, 4.73, 100]
def mean(data):
    return sum(data)/len(data)
def median(data):
    data = sorted(data)
    n = len(data)
    if n % 2 == 1:
        return data[n // 2]
    else:
        i = n // 2
        return (data[i-1] + data[i])/2


mu1 = mean(data1)
mu2 = mean(data2)
me1 = median(data1)
me2=median(data2)

print("Lenght of data1: ",len(data1))
print("Length of data2: ",len(data2))
print ("Mean(agv) of data1: ", mu1)
print("Mean(agv) of data1: ", mu2)
print ("Median of data1: ", me1)
print("Median of data2: ", me2)

