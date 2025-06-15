employeeNameID={
    1:"Deepak Raj",
    2:"Raj",
    3:"Florance",
    4:"Sripriya",
    500:"PANKAJ KUMAR"
}

employeeNameID.setdefault(500,"Default Value-ABC")
# If Key 500 does not exist then take the Default Value Else take the Value for the Dictionary for the respective KEY
print(employeeNameID[500]) # 

