"""
CTEC 121
<your name>
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main():
    # section 1
    # define a string
    myStr = "Hello World"

    print()
    '''
    print(myStr)
    print(myStr[6])
    print(myStr[len(myStr)-1])
    print(myStr[10])
    #print(myStr[11])
    print(myStr[0])
    print(myStr[-1])
    print(myStr[-5])
    print(myStr[-len(myStr)])
    
    word1 = "Hello"
    word2 = "World"
    myStr2 = word1 + " " + word2
    print(myStr2)
    myStr3 = word1 + word2
    print(myStr3)

    print(myStr2[6:len(myStr2)])
    '''

    # section 2
    '''
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    n = int(input("Enter a month number (1 - 12): "))
    pos = (n-1) * 3
    print(pos)
    # slice to get abbreviation
    monthAbr = months[pos:pos+3]
    print(monthAbr)

    print(months[(n-1)*3:(n-1)*3+3])
    '''

    # lists
    '''
    # create an empty list
    myList1 = []
    print("myList1:", myList1)

    myList2 = [1, 2, 3, 4]
    print("myList2:", myList2)

    myList3 = [42, "forty-two", 3.14]
    print("myList3: ", myList3)

    print("third element of myList2:", myList2[2])

    # initialization example
    for i in range(1,6):
        myList1.append(i)
    print("myList1:", myList1)

    # illustrate insert()
    myList1.insert(2, 3.14)
    print("myList1:", myList1)

    # illustrate sort()
    myList1.sort()
    print("myList1:", myList1)
    '''
    '''
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    n = int( input("Enter a month number (1-12): ") )
    print(months[n-1])
    
    print("A:", ord('A'))
    print("97:", chr(97))
    '''

    myStr = "text   \n"
    print("*", myStr, "*", sep="")
    print()
    myStr = myStr.rstrip()
    print("*", myStr, "*", sep="")

    myStr = "CamelCase"
    print(myStr)
    s1 = myStr.upper()
    print(s1)
    s2 = myStr.lower()
    print(s2)

    myStr = "Mary had a little lamb"
    myList = myStr.split()
    print(myList)
    
    print()

main()    
