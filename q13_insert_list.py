""" Question 13: insert_list """
"""
Inputs: two lists, L and K, and index i
Output: K destructively inserted into L at index i
"""
def insert_element(L, i, el):
    if (i >= len(L)): L.append(el)
    else:
        L.append(L[len(L) - 1])
        for index in range(len(L) - 1, i, -1):
            L[index] = L[index-1]
        L[i] = el

def insert_list(L, i, K):
    if i >= len(L):
        L.extend(K)
    else:
        for index in range(len(K)):
            elem = K[index]
            insert_element(L, i+index, elem)

""" Test 13 """
def test_insert_list():
    print("Testing insert_list...", end='')
    L = [1, 5, 6]
    K = [2, 3, 4]
    assert(insert_list(L, 1, K) == None)
    assert(L == [1, 2, 3, 4, 5, 6])
    L1 = [2, 4]
    K1 = [5, 1, 8]
    assert(insert_list(L1, 2, K1) == None)
    assert(L1 == [2, 4, 5, 1, 8])
    print("... done!")

if __name__ == '__main__':
    test_insert_list()