import glob
from calculations.sortGages import sortGages
from calculations.wetInitCount import wetInitCount
from calculations.wetCount import wetCount
from calculations.springBflLag import springBflLag
from calculations.snowEarly import snowEarly
from calculations.snowSpringBfl import snowSpringBfl
from calculations.LSRspringBfl import LSRspringBfl
from calculations.rainWetSpring import rainWetSpring
from calculations.rainZeroFlow import rainZeroFlow

files = glob.glob("All-Results/*_annual_result_matrix.csv")

classes = sortGages(files)

allResults = classes['class1'] + classes['class2'] + classes['class3'] +classes['class4'] + classes['class5']+ classes['class6']+ classes['class7']+ classes['class8']+ classes['class9']
snowResults = classes['class1'] + classes['class2']+ classes['class9']
LSRresults = classes['class3']
rainResults = classes['class4'] + classes['class6']+ classes['class7']+ classes['class8']
    

wetInitCount = wetInitCount(allResults)
wetCount = wetCount(allResults)
springBflLag = springBflLag(allResults)
snowEarlySpring, snowEarlyWet = snowEarly(snowResults) 
snowSpringBfl, snowSpringBflRate = snowSpringBfl(snowResults) 
LSRspringBfl, LSRspringBflRate = LSRspringBfl(LSRresults) 
rainWetSpring = rainWetSpring(LSRresults, rainResults)
rainZeroFlow = rainZeroFlow(classes)
    