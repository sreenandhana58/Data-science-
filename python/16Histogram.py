
from matplotlib import pyplot
from numpy import array
marks=[22,87,5,43,56,73,55,54,11,20,51,5,79,31,27]
bins=[0,10,20,30,40,50,60,70,80,90,100]
pyplot.hist(marks,bins=bins)
pyplot.xlabel("Marks Range")
pyplot.ylabel("Number of student")
pyplot.title("Histogram of student mark")

pyplot.show()
