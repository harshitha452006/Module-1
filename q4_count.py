""" Question 4: count """
"""
Inputs: two strings, s and t
Output: number of times t occurs in s
"""
def starts_with(s, t, start):
    return s[start:start+len(t)] == t

def count(s, t):
    if(len(t) == 0): return len(s)+1
    total_count = 0
    i = 0
    while(i<len(s)-len(t)):
        if(starts_with(s,t,i)):
            total_count +=1
            i += len(t)
        else: i += 1
    return total_count

""" Test 4 """
def test_count():
    print("Testing count...", end='')
    assert(count("Hello", "l") == 2)
    assert(count("pineapple", "p") == 3)
    assert(count("farewell everyone", "are") == 1)
    assert(count("", "aa") == 0)
    assert(count("Hello world", " ") == 1)
    print("... done!")

if __name__ == '__main__':
    test_count()