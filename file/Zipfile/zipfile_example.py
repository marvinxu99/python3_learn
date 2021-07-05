import zipfile


with zipfile.ZipFile('myarchive.zip', 'r') as myzip:
    print(myzip.namelist())

    for meta in myzip.infolist():
        print(meta, end='\n')

    info = myzip.getinfo('purchases.txt')
    print(info)

    # Access to file in the zip folder
    print(myzip.read('purchases.txt').decode('utf-8'))
    with myzip.open('purchases.txt') as myfile:
        print(myfile.read().decode('utf-8'))

    # EXtract files
    myzip.extract('purchases.txt')
    # myzip.extractall()