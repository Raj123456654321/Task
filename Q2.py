# Function to find pair with given difference in the list
# This method handles duplicates in the list
def findPair(list1, k):

    # take an empty set
    s = set()

    # do for each element in the list
    i = 0
    while i < len(list1):

        # to avoid printing duplicates (skip adjacent duplicates)
        while i + 1 < len(list1) and list1[i] == list1[i + 1]:
            i = i + 1

        # check if pair with given difference (list1[i], list1[i] - k) exists
        if list1[i] - k in s:
            
            print(list1[i] - k,(list1[i]))

        # check if pair with given difference (list1[i] + k, list1[i]) exists
        if list1[i] + k in s:
            
            print((list1[i],list1[i] + k ))

        # insert element into the set
        s.add(list1[i])

        i = i + 1


if __name__ == '__main__':

    try: 
        my_list = [] 
      
        while True:
            print("Please Enter one Number at a time to fill the list. press any Alphabet to stop filling the list")
            my_list.append(int(input()))
            #print("press any alphabet to stop filling list")
          
    # if the input is not-integer, just print the list 
    except: 
        print(my_list) 
    
    # number of elements 
    n = int(input("Enter a K difference number : "))
    findPair(my_list, n)
    
