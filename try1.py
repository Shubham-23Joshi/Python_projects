import pandas as pd
print ('Welcome to DataGenie, your Data Analyst')
print ('''kindly store the data file (excel or csv) in DataGenie folder
and type the file address here''')
cont = False
while cont == False:
    try:
        filename = input()
        pd.readcsv(filename)
        print ('File read successfully')
        cont = True
    except:
        print ('Sorry, file could not be read. Re-type file location correctly.')
        t = False