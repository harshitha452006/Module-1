
""" Question 5: strip """
"""
Input: string s
Output: s with leading and trailing spaces removed
"""
def strip(s):
    if(len(s) == 0): return ""
    # helps to check if entire string is space
    broke = False
    for start in range(len(s)):
        if(s[start] != " "): 
            broke = True
            break
    for end in range(len(s)):
        if(s[len(s)-1-end] != " "):
            broke = True 
            break
    if broke:
        return s[start : len(s)-end]
    return ""

""" Test 5 """
def test_strip():
    print("Testing strip...", end='')
    assert(strip("Hello") == "Hello") 
    assert(strip(" Hello world ") == "Hello world") 
    assert(strip("      apple ") == "apple") 
    assert(strip("    ") == "") 
    print("... done!")

if __name__ == '__main__':
    test_strip()