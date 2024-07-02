def getRange(data, column): 
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    return (Q3 - Q1), Q1, Q3 