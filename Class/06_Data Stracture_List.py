'''
१. List (सूची)
List एक अर्डर गरिएको, परिवर्तनशील (mutable) डाटा प्रकार हो जसमा 
विभिन्न प्रकारका डाटा समावेश गर्न सकिन्छ। Lists [] (ब्राकेट) भित्र लेखिन्छन्।
'''
name= ["ram","shyam", "hari","kale"]
print(name)

# List मा आइटम थप्ने (Add)
name.append("vogate")
print(name)

# List मा आइटम परिवर्तन गर्ने (Modify)
name[0]="gore"
print(name)

# दोस्रो स्थानमा थप्‍न परेमा
name.insert(2,"gopal")
print(name)

# List बाट आइटम हटाउने (Remove)
name.remove("gore")

print(name)