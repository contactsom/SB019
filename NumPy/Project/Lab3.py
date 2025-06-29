import numpy

data = numpy.genfromtxt('DATASet.csv',delimiter=",",skip_header=1)

ages=data[:,1]

# Max Age
max_age=numpy.nanmax(ages)
print("MAX AGE : ",max_age)

# MIN Age
min_age=numpy.nanmin(ages)
print("MIN AGE : ",min_age)

# MEAN Age
min_age=numpy.nanmean(ages)
print("Mean AGE : ",min_age)

# Standerd Division
std_age=numpy.nanstd(ages)
print("Standerd AGE : ",std_age)

# Create a Subset os senoior Citizen age >60 Years

seniar_citizen=data[data[:,0]>60]
len_seniar_citizen=len(seniar_citizen)
print("Total Number of seniar citizen",len_seniar_citizen) # 62

# Um of seniar_citizen  working hours
sum_Of_working_Hours=numpy.sum(seniar_citizen[:,6])
print(" avg_working_Hours",sum_Of_working_Hours) #

avg_working_hour_seniar_citizen=sum_Of_working_Hours/len_seniar_citizen
print(" avg_working_hour_seniar_citizen",avg_working_hour_seniar_citizen) # 31.725806451612904

if(avg_working_hour_seniar_citizen>20):
    print("seniar_citizen is working more than 20 hours")
else:
    print("seniar_citizen is NOT working more than 20 hours")

