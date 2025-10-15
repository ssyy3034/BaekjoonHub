n = int(input())
month = 7+(n-1)*7
year = month//12+2024
month = month%12+1
print(year,month)
