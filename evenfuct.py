def sum_even_numbers(numbers):
    even=0
    for num in numbers:
        if num %2==0:
            even+=num
    return even
number1=[1,2,3,4,5,6,7,8,9,10]
sum=sum_even_numbers(number1)
print(sum)