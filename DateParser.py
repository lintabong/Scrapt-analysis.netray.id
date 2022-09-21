from datetime import datetime


# sample input ='September 19, 2022'
def date_parser(_date):
    months = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']

    split_date = _date.split(' ')

    for i in range(len(split_date)):
        split_date[i] = split_date[i].replace(',','')
    
    for i in range(len(months)):
        if split_date[0] == months[i]:
            split_date[0] = i + 1

    datetimeStr = str(split_date[0]) + '/' + str(split_date[1]) + '/' + str(split_date[2])[2:]
    result = datetime.strptime(datetimeStr, '%m/%d/%y')

    return result