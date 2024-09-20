'''
४. Dictionary (डिक्सनरी)
Dictionary एक unordered (अक्रमबद्ध), changeable (परिवर्तनीय), र indexed डाटा प्रकार हो 
जसमा key-value जोडीहरू हुन्छन्। डिक्सनरीहरू {} (ब्रेसेस) भित्र लेखिन्छन्, र प्रत्येक आइटमको key र value हुन्छ।

'''

family = {
    "father":"hari",
    "mother":"punti",
    "son":"kale",
    "daughter":"bhulti"
}

print(family)

# डिक्सनरीमा नयाँ आइटम थप्ने
family["Joi"]="punte"
print(family)

# डिक्सनरीबाट आइटम हटाउने
del family["Joi"]
print(family)