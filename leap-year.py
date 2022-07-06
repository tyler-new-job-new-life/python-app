
# Default function to implement conditions to check leap year  
def CheckLeap(year) :  
  # Checking if the given year is leap year  
  if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)) :   
    print(f"{year} is a leap Year.")  

  # Else it is not a leap year  
  else :  
    print (f"{year} is not a leap Year")  
# Taking an input year from user  
year = int(input("Enter a year : "))  

# Printing result  

#Eklendi
CheckLeap(Year) 


# Celsius u Fahrenat'e çevirme.

a = int(input('celcius değer girin :'))  # Celsius u Fahrenat'e çevirme.
b = a*9/5+32
print(b)
print("Hello Cohort-12")
print("merhaba bu ilk forkum ve pushum")


