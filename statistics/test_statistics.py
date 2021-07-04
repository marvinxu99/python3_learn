import statistics

ageData = [10, 12, 13, 11, 14, 10, 12, 14, 15, 11, 11]

print(statistics.mean(ageData))
print(statistics.mode(ageData))
print(statistics.median(ageData))
print(sorted(ageData))

# Variance - the average of the squared differences from the mean.
# Standard deviation - the square root of the variance
print(statistics.variance(ageData))
print(statistics.stdev(ageData))
