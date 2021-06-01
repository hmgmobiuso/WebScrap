import read_write_excel
from googlesearch import search

def fetctURLsFromGoogle(queryArray):
    tempLinks = []
    dataToAddInExcel = {}
    for query in queryArray:  
        for j in search(query, tld="co.in", num=10, stop=10, pause=2):
            tempLinks.append(j)
        dataToAddInExcel[query] = tempLinks
        tempLinks = []
    return dataToAddInExcel

path_to_excel = './test open 7 google search tabs.xlsm'
queryArray = read_write_excel.readExcel(path_to_excel)
read_write_excel.writeExcel(fetctURLsFromGoogle(queryArray))