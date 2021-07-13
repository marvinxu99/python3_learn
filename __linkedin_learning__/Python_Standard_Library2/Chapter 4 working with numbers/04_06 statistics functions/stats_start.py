# using Python statistics functions
import statistics
import csv
import array


# simple statistics operations
sample_data1 = [1, 3, 5, 7]
sample_data2 = [2, 3, 5, 4, 3, 5, 3, 2, 5, 6, 4, 3]

# TODO: Use the mean function - calculates an average value


# TODO: Use the different median functions


# TODO: The mode function indicates which data item occurs
# most frequently


# Read data from a CSV file and calculate statistics
def readData():
    with open("StockQuotes.csv") as dataFile:
        data = array.array('f', [])

        reader = csv.reader(dataFile)
        curLine = 0
        for row in reader:
            if curLine == 0:
                pass  # this is the headers row
            else:
                # get the closing value from column 4
                item = float(row[4])
                data.append(item)
            curLine += 1

        print(f"Read {curLine+1} rows of data.")
        return data


def calcStats():
    # read the data from the CSV file
    data = readData()

    # TODO: calculate interesting data points
    data_mean = 0
    data_med = 0
    data_std = 0
    data_var = 0

    print("Mean: ", data_mean)
    print("Median: ", data_med)
    print("Standard deviation: ", data_std)
    print("Variance: ", data_var)


# TODO: Calculate stats values from a CSV file of data
# calcStats()
