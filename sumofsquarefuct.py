def three_digits(number):
    three_digits=0
    while number>0:
        digit = number%10
        three_digits+=digit**2
        number//=10
        return three_digits
while True:
    user_input=input("enter 3 digits number:")
    if user_input.isdigit()and len(user_input)==3:
        number=int(user_input)
        break
    
result=three_digits(number)
print(f"output will be:{result}")