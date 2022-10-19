# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.
salary = float(input("enter your salary $: "))
yos = float(input("enter your year of service in this company : "))
print("bonus for you is $",int(0.1 * salary)  ) if yos > 5 else print("no bonus fro this year")