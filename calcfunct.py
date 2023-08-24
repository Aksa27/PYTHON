def main():
    dic={'tshirt':350,'shirt':450,'jeans':400,'pants':150}
    selected_items={}
    total_price=0
    
    while True:
        print("\navailable item")
        for item,price in dic.items():
            print(f"{item}:{price}")   
            
        num_items=int(input("enter the number of items you want to select(0 to stop):"))
        if num_items==0:
            break
        if num_items>len(dic):
            print("error:you can select more items than available.")
            continue
        sorted_items=sorted(dic.items())
        for item,price in sorted_items[:num_items]:
            selected_items[item]=price
            total_price += price
    print("\n selected items:")
    for item,price in selected_items.items():
        print(f"{item}:{price}") 
    print("total price:",total_price)
    
main()
    