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


def numJewelsInStones(jewels, stones):

    total = 0
    counts = {}

    for stone in stones:

        if stone in jewels:
            prev = counts.get(stone, 0)
            total += prev
            counts[stone] = prev + 1
            print(counts)

    return total

print(numJewelsInStones('aA', "aAAbbbb"))