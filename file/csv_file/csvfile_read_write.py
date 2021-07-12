# Reading and writing Comma Separate Values files with Python
import csv


# TODO: list the dialects that are available to use
print(csv.list_dialects())

# TODO: Open a CSV file and read each row of data
def reader_sample():
    with open("StockQuotes.csv") as datafile:
        reader = csv.reader(datafile)
        for row in reader:
            print(row)


# TODO: Use the CSV module Sniffer to see what dialect of CSV this is
def use_sniffer():
    with open("StockQuotes.csv") as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        has_header = csv.Sniffer().has_header(csvfile.read(1024))
        csvfile.seek(0)   
        print("Heads found:", str(has_header))     
        print(dialect.delimiter)
        print(dialect.escapechar)
        print(dialect.quotechar)


# TODO: Write data to a CSV file
def writer_sample():
    with open("sample_data.csv", mode='w') as csvfile:
        csvwriter = csv.writer(csvfile, lineterminator="\n")
        csvwriter.writerow(["Name", "Department", "Locations"])
        csvwriter.writerow(["John Wesley", "Sales", "Vancouver"])
        csvwriter.writerow(["Jane Dae", "Engineering", "NYC"])
        csvwriter.writerow(["Jim Due", "Accounting", "Vancouver"])


# Exercise the samples
# reader_sample()
writer_sample()
use_sniffer()
