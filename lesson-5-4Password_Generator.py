# Password Generator - Practical Functions Exercise

## Problem
You need to create a secure password generator for a company's IT department. 
Different departments have different password requirements, and the tool needs to be flexible and reusable.

## Requirements
Create a password generator that can:

1. **Generate different types of passwords:**
   - Simple (letters only)
   - Standard (letters + numbers)
   - Strong (letters + numbers + symbols)
   - Ultra-secure (all characters with specific requirements)

2. **Validate password strength:**
   - Check length requirements
   - Verify character type requirements
   - Calculate strength score

3. **Batch generation:**
   - Generate multiple passwords at once
   - Allow customization of requirements

## Expected Behavior
```
Password Generator
=================

1. Generate Single Password
2. Generate Multiple Passwords
3. Check Password Strength
4. Exit

Choose an option: 1

Password Types:
1. Simple (letters only)
2. Standard (letters + numbers)  
3. Strong (letters + numbers + symbols)
4. Ultra-secure (all types + requirements)

Choose password type: 3
Enter password length (8-50): 12

Generated Password: Kp9$mN2@vX8!
Password Strength: Strong (Score: 85/100)

Would you like another password? (y/n): n
```

## Real-World Value
This exercise demonstrates functions in a practical context where:
- Code reusability is essential (different password types)
- Validation logic is complex but reusable
- The main program logic stays clean and focused
- Functions make testing and maintenance easier

## Hints
Consider functions for:
- Generating different character sets
- Creating passwords with specific rules
- Validating password requirements
- Calculating strength scores
- Formatting output
- Menu handling