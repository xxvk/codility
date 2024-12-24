# English ver.
'''
def solution(A):
that takes an array A of size  N , containing integers, and returns the count of unique values in the array.

For example, given the array A with six elements:

A[0] = 2    A[1] = 1    A[2] = 1
A[3] = 2    A[4] = 3    A[5] = 1

The function should return 3, because there are three distinct values in the array: 1, 2, and 3.

Assumptions
	•	 N  is an integer in the range [0..100,000].
	•	Each element of array  A  is an integer in the range [-1,000,000..1,000,000].
'''





# Japnese ver.
'''
def solution(A):
この関数は、サイズ  N  の整数配列 A を受け取り、配列内の異なる値の数を返します。

例えば、次の6つの要素を持つ配列 A が与えられた場合：

A[0] = 2    A[1] = 1    A[2] = 1
A[3] = 2    A[4] = 3    A[5] = 1

関数は 3 を返すべきです。なぜなら、配列内には 1、2、3 という3つの異なる値が含まれているからです。

前提条件
	•	 N  は範囲 [0..100,000] の整数です。
	•	配列  A  の各要素は、範囲 [-1,000,000..1,000,000] の整数です。
'''




# Chinese ver.
'''
def solution(A):
該函數接受一個大小為  N  的整數陣列 A，並返回陣列中不重複值的數量。

例如，給定陣列 A，包含六個元素：

A[0] = 2    A[1] = 1    A[2] = 1
A[3] = 2    A[4] = 3    A[5] = 1

函數應返回 3，因為陣列中有三個不重複的值：1、2 和 3。

假設條件
	•	 N  是範圍 [0..100,000] 內的整數。
	•	陣列  A  中的每個元素是範圍 [-1,000,000..1,000,000] 內的整數。
'''



def solution(A):
    # Implement your solution here
    '''
    checker:    input range, empty
    '''
    if not A: return 0
    N = len(A)
    if N > 100000:
        raise ValueError('input range Error')
    '''
    main process
    '''
    setA = set(A)
    return len(setA)


test_cases = {
    # Example cases
    (2, 1, 1, 2, 3, 1): 3,  # Example test case with positive integers

    # Edge cases
    (): 0,                   # Empty array
    (1,): 1,                 # Single element
    (-1,): 1,                # Single negative element
    (1, 1, 1, 1, 1): 1,      # All elements are the same
    (-1, -2, -3, -4, -5): 5, # All elements are distinct negatives

    # Small and medium-sized cases
    (1, 2, 3, 4, 5): 5,                # All distinct values
    (0, 0, 1, 1, 2, 2, 3, 3): 4,      # Repeated values
    (1000, 2000, 3000, 4000): 4,      # Large distinct values
    tuple(range(100)): 100,           # Sequence from 0 to 99
    tuple([-i for i in range(100)]): 100, # Negative sequence from -1 to -99

    # Performance tests
    tuple(range(100000)): 100000,      # Sequence of 0 to 99,999
    tuple([-i for i in range(100000)]): 100000, # Sequence of -1 to -99,999
    tuple([i % 1000 for i in range(100000)]): 1000, # Repeated pattern
}

def run_tests():
    print("Running tests...\n")
    passed = 0
    failed = 0

    for input_array, expected_output in test_cases.items():
        try:
            result = solution(list(input_array))
            if result == expected_output:
                print(f"Test Passed: input_length={len(input_array)}, output={result}")
                passed += 1
            else:
                print(f"Test Failed: input_length={len(input_array)}, expected={expected_output}, got={result}")
                failed += 1
        except Exception as e:
            print(f"Test Error: input_length={len(input_array)}, error={str(e)}")
            failed += 1

    print("\nTest Summary:")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")
    print(f"  Total:  {len(test_cases)}")

# Run the tests
run_tests()
