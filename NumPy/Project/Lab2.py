import numpy

data = numpy.genfromtxt(
            'DATASet.csv', # FIle Name
            delimiter=",", # Header and Values saperation
            names=True,    # Read the Header as Filed Name
            dtype=None,    # Handle the String types Properly
            encoding=None
        )
#print(data)

print(data.dtype.names)

print(type(data)) #class 'numpy.ndarray'