import math

# function works with list input
def convertOffsetToJulian(offsetDateList, year): # convert offset date to julian
    julianDateList = []
    for count, offsetDate in enumerate(offsetDateList):
        if year % 4 == 0:
            daysInYear = 366
            offsetStartDate = 274
        else:
            daysInYear = 365
            offsetStartDate = 273

        intOffsetDate = int(offsetDate)

        if intOffsetDate <=  offsetStartDate:
            julian_nonoffset_date = intOffsetDate + (daysInYear - offsetStartDate)
            julianDateList.append(julian_nonoffset_date)
        else:
            julian_nonoffset_date = intOffsetDate - offsetStartDate
            julianDateList.append(julian_nonoffset_date)

    return julianDateList

# function works with single values
def convertJulianToOffset(julianDate, year, dry=False):
    if year % 4 == 0:
        daysInYear = 366
        offsetStartDate = 274
    else:
        daysInYear = 365
        offsetStartDate = 273
    if math.isnan(julianDate) == False: 
        intJulianDate = int(julianDate)
        if dry == True:
            if julianDate > 274 and julianDate < 300:
                offsetDate = 365 + (julianDate-daysInYear)
                return offsetDate
            elif intJulianDate >= offsetStartDate:
                offsetDate = intJulianDate - offsetStartDate
            else:
                offsetDate = intJulianDate + (daysInYear - offsetStartDate)
        else: 
            if intJulianDate >= offsetStartDate:
                offsetDate = intJulianDate - offsetStartDate
            else:
                offsetDate = intJulianDate + (daysInYear - offsetStartDate)
    else: offsetDate = julianDate

    return offsetDate
