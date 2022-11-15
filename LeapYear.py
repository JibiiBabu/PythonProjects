startYear = int(input("Enter start year: "))
endYear = int(input("Enter end year: "))
while startYear >= endYear:
    print("Check your year input again.")
    start = int(input("Enter start year: "))
    end = int(input("Enter end year: "))

print ("Here is a list of leap years between {0} and {1}:".format(startYear,endYear))

leap_years = []
while startYear <= endYear:
    if startYear % 4 == 0 and startYear % 100 != 0:
        leap_years.append(str(startYear))
    if startYear % 100 == 0 and startYear % 400 == 0:
        leap_years.append(str(startYear))
    startYear += 1

for line in range(0, len(leap_years), 10):
    print ("{0}.".format(", ".join(leap_years[line:line+10])))