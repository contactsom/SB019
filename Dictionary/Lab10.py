employeeNameID={
    1:"Deepak Raj",
    2:"Raj",
    3:"Florance",
    4:"Sripriya"
}

print(employeeNameID[1]) # Deepak Raj
print(employeeNameID[2]) # Raj
print(employeeNameID[3]) # Florance
print(employeeNameID[4]) # Sripriya


if 5 in employeeNameID:
    print(employeeNameID[5])
else:
    print("KEY Not Exist")


if 4 in employeeNameID:
    print(employeeNameID[4])
else:
    print("KEY Not Exist")