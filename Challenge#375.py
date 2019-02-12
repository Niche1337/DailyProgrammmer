# [2019-02-11] Challenge #375 [Easy] Print a new number by adding one to each of its digit
# Description
# A number is input in computer then a new no should get printed by adding one to each of its digit. 
# If you encounter a 9, insert a 10 (don't carry over, just shift things around).

# For example, 998 becomes 10109.

# Bonus
# This challenge is trivial to do if you map it to a string to iterate over the input, operate, and then cast it back.
#  Instead, try doing it without casting it as a string at any point, keep it numeric (int, float if you need it) only.

def numberThing(y):
    newNum = []
    for x in y:
        newNum.append(str(int(x) + 1))
    num = "".join(newNum)
    return num
    

if __name__ == "__main__":
    num = (input("Enter a number"))
    print(numberThing(num))
    
    

