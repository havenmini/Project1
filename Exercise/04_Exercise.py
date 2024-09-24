'''Number1 = int(input("Enter number 1"))
Number2 = int(input("Enter number 2"))
Number3 = int(input("Enter number 3"))

if Number1>Number2 and Number1>Number3:
    print(f"This is largest number",Number1)
elif Number2>Number1 and Number2>Number3:
    print(f"This is largest number",Number2)
else:
    print(f"this is larges number",Number3)
'''

# प्रयोगकर्ताबाट तीनवटा संख्या लिने
num1 = float(input("पहिलो संख्या प्रविष्ट गर्नुहोस्: "))
num2 = float(input("दोस्रो संख्या प्रविष्ट गर्नुहोस्: "))
num3 = float(input("तेस्रो संख्या प्रविष्ट गर्नुहोस्: "))

# सबैभन्दा ठूलो संख्या पत्ता लगाउने
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print(f"सबैभन्दा ठूलो संख्या {largest} हो।")
