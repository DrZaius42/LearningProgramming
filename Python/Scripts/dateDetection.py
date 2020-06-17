#dateDetections.py - Detects and checks for valid dates in fromat DD/MM/YYYY
import re
dateRegex = re.compile(r'''(\d{1,2})  #day
                           (-|/|.)    #separator
                           (\d{1,2})  #month
                           (-|/|.)    #separator
                           (\d{4})''' #year
                           , re.VERBOSE)
while True:
    print('Enter a date to test: ')
    text = input()
    mo = dateRegex.findall(text)
    dayStr, monthStr, yearStr = mo[0][0], mo[0][2], mo[0][4] 
    day = int(dayStr)
    month = int(monthStr)
    year = int(yearStr)
    if ((year % 4 != 0) and (year % 100 != 0)) and month == 2 and day > 28:
        print('Invalid date')
        continue
    if (month not in range(1,8,2) or month not in range(8,13,2)) and day > 30 :
        print('Invalid date')
        continue
    break
print(dayStr+'/'+monthStr+'/'+yearStr)#this output the same format that the
#input entered, doesn't add zeros nor makes everything dd/mm/yyyy
#i got lazy