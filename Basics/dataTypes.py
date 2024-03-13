id = 1
firstName = "Mahesh"
lastName = "    Babu"
ssn = "999-45-6789"
hasInsurance = True
billingAmount = "100102"
print(type(billingAmount))
billingAmount = float(billingAmount)
print(type(billingAmount))
print(id, firstName, lastName.lstrip(), ssn, hasInsurance, billingAmount, ssn[7:len(ssn)])

