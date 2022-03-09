import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import random
import csv

#reading the scores data
df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

#calculating mean, standard deviation, median and mode
mean = sum(data) / len(data)
std_deviation = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)

print("Mean is :", mean)
print("Standard deviation is:", std_deviation)
print("Media is:", median)
print("Mode id:", mode)

fig=ff.create_distplot([data],["reading score"],show_hist=False)

standardDev1s, standardDev1e = mean-std_deviation, mean+std_deviation
standardDev2s, standardDev2e = mean-(2*std_deviation), mean+(2*std_deviation)
standardDev3s, standardDev3e = mean-(3*std_deviation), mean+(3*std_deviation)

fig.add_trace(go.Scatter(x = [standardDev1s, standardDev1s], y = [0, 0.17], mode = "lines", name = "STD 1 Start"))
fig.add_trace(go.Scatter(x = [standardDev1e, standardDev1e], y = [0, 0.17], mode = "lines", name = "STD 1 End"))
fig.add_trace(go.Scatter(x = [standardDev2s, standardDev2s], y = [0, 0.17], mode = "lines", name = "STD 2 Start"))
fig.add_trace(go.Scatter(x = [standardDev2e, standardDev2e], y = [0, 0.17], mode = "lines", name = "STD 2 End"))
fig.add_trace(go.Scatter(x = [standardDev3s, standardDev3s], y = [0, 0.17], mode = "lines", name = "STD 3 Start"))
fig.add_trace(go.Scatter(x = [standardDev3e, standardDev3e], y = [0, 0.17], mode = "lines", name = "STD 3 End"))
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))

fig.show()

std1Data = [result for result in data if result > standardDev1s and result < standardDev1e]
std2Data = [result for result in data if result > standardDev2s and result < standardDev2e]
std3Data = [result for result in data if result > standardDev3s and result < standardDev3e]


print("{}% of data lie within 1st standard deviation".format(len(std1Data)*100/len(data)))
print("{}% of data lie within 2nd standard deviation".format(len(std2Data)*100/len(data)))
print("{}% of data lie within 3rd standard deviation".format(len(std3Data)*100/len(data)))
