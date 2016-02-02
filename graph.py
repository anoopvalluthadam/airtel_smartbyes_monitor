from matplotlib import pyplot as pl
from dateutil import parser
import calendar
import numpy as np
import csv

'''
The 'fname' sent to this module should be the name of a file which
has comma separated values in the format: MM-DD-YYYY, value
E.g:

12-10-2014, 5
12-11-2014, 11
12-12-2014, 14
12-13-2014, 19
12-14-2014, 23

The 'value' is nothing but the GiB used until that date.

Access this module as given below:

plotgraph(<filename>)

'''


def getdata(fname):
    '''
    This function accepts file name and return two vectors
    containing date and value separately.
    '''
    with open(fname) as f:
        x = []
        y = []
        try:
            reader = csv.reader(f)
            for row in reader:
                x.append(row[:1])
                y.append(row[1:])
        except Exception as error:
            print str(error)
    return x, y


def get_my(date):
    '''
    To strip day from date. Used for plotting the X-axis
    '''
    date_object = parser.parse(date)
    return date_object.month, date_object.year


def getdateonly(dates):
    '''
    To strip month and year. Used for giving title to the graph
    '''
    date_stripped = []
    for date in dates:
        date_object = parser.parse(date[0])
        date_stripped.append(str(date_object.day))
    return date_stripped


def plotgraph(fname):
    '''
    Core method of this module. Accepts the file name
    of a csv as input and draws graph.
    '''
    x_ticks, y = getdata(fname)
    x_ticks = getdateonly(x_ticks)
    l = len(x_ticks)
    x = np.array(range(1, l+1))
    pl.xticks(x, x_ticks)
    y_temp = y
    pl.plot(x, y, color='green', marker='o', linestyle='solid')
    m, y = get_my(x_ticks[0][0])
    month = calendar.month_name[int(m)]
    title = 'Airtel Internet: Usage Statistics for '+month+' '+str(y)
    pl.title(title)
    pl.ylabel("GiB Used So Far This Month")
    pl.xlabel("Date")
    pl.show()


if __name__ == '__main__':
    plotgraph('samplefile.csv')
