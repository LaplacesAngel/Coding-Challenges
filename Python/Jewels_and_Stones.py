# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. 
#Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Example 1:
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

# Example 2:
# Input: jewels = "z", stones = "ZZ"
# Output: 0

# Constraints:
# 1 <= jewels.length, stones.length <= 50
# jewels and stones consist of only English letters.
# All the characters of jewels are unique.

#need to loop through stones and and add 1 to a running total of times a jewel has occured in it
#can make a variable called prev which will return the value of how many times the jewel has been seen previously and add that to the total
#then add 1 to that value

#nested for loop version
def numJewelsInStones(jewels, stones):

    total = 0

    for stone in stones:
        for jewel in jewels:
             if jewel == stone:
                total += 1


    return total


#dictionary version:

def numsInJewelsInStonesDict(jewels, stones):

    counts = {}
    total = 0

    for stone in stones:
        if stone not in counts:
            counts[stone] = 0
        counts[stone] += 1

    for jewel in jewels:
        if jewel in counts:
            total += counts[jewel]
    
    return total

    
print(numsInJewelsInStonesDict('aA', "aAAbbbb"))