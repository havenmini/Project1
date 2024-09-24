# प्रयोगकर्ताबाट वर्ष लिने
year = int(input("Type any Year: "))

# लिप वर्ष जाँच गर्ने
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} This is Leap year")
else:
    print(f"{year} This is not leap year")
