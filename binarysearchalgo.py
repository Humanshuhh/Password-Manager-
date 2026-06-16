def binary_search(list,element):
    midd = 0;
    st = 0;
    end = len(list)
    steps = 0

    while(st <= end ):


      
       midd = st + (end - st)// 2   # here due to pyhton language we use doible slash  to convert it to int

    if(element == midd):
            print("Element found at index",midd)
            return
    elif(element < list[midd]):
            end = midd-1

    else:
            st = midd + 1 


    return -1;



my_list = [1,2,3,4,5,6,7,8]

target = 5

binary_search(my_list,target)