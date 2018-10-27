data1 = [0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25, 4.73]
data2 = [0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25, 100]
def mean(data):
    return sum(data)/len(data)
mu1 = mean(data1)
mu2 = mean(data2)
print (mu1)
print(mu2)