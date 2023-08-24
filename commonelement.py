def common_element(list1,list2):
    set1=set(list1)
    set2=set(list2)
    common_element=set1.intersection(set2)
    result_list=list(common_element)
    return result_list
list1=[1,2,3,4]
list2=[2,2,5,6,4]
result=common_element(list1,list2)
print("output will be:",result)