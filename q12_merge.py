
""" Question 12: merge """
"""
Inputs: two sorted lists, A and B
Output: a sorted list combining the elements in A and B
"""
def merge(A, B):
    length = len(A) + len(B)
    M = []
    index_A = index_B = 0
    for i in range(length):
        if(index_A == len(A)):
            M.append(B[index_B])
            index_B += 1
        elif(index_B == len(B)):
            M.append(A[index_A])
            index_A += 1
        elif(A[index_A] < B[index_B]):
            M.append(A[index_A])
            index_A += 1
        else:
            M.append(B[index_B])
            index_B += 1
    return M

""" Test 12 """
def test_merge():
    print("Testing merge...", end='')
    L1 = [1, 3, 5]
    L2 = [2, 4, 6]
    assert(merge(L1, L2) == [1, 2, 3, 4, 5, 6])
    assert(L1 == [1, 3, 5])
    assert(L2 == [2, 4, 6])
    assert(merge([1, 2, 5], [4, 6, 7]) == [1, 2, 4, 5, 6, 7])
    print("... done!")

if __name__ == '__main__':
    test_merge()