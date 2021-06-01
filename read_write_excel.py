import pandas as pd

def readExcel(loc):
    # file =('path_of_excel_file')
    newData = pd.read_excel(loc)
    a = newData['Unnamed: 3']
    queryString = a.loc[3:]
    return list(queryString)

def writeExcel(dataToAddInExcel):       
    df = pd.DataFrame(dataToAddInExcel)
    df.to_excel('./scrapped_lists.xlsx')

