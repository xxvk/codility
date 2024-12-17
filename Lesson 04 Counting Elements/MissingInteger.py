# English ver.
'''
Write a function:

def solution(A):

This function takes an array  A  of  N  integers 
and returns the smallest positive integer (greater than 0) that does not appear in  A .

Examples:
	1.	Given  A = [1, 3, 6, 4, 1, 2] , the function should return  5 .
	2.	Given  A = [1, 2, 3] , the function should return  4 .
	3.	Given  A = [-1, -3] , the function should return  1 .

Assumptions:
	•	 N  is an integer within the range [1..100,000].
	•	Each element of array  A  is an integer within the range [-1,000,000..1,000,000].
'''



# Chinese ver.
'''
撰寫一個函數：
def solution(A):
此函數接受一個包含  N  個整數的陣列  A ，並返回陣列中未出現的最小正整數（大於 0）。

範例：
	1.	若  A = [1, 3, 6, 4, 1, 2] ，則函數應返回  5 。
	2.	若  A = [1, 2, 3] ，則函數應返回  4 。
	3.	若  A = [-1, -3] ，則函數應返回  1 。

假設：
	•	 N  是範圍 [1..100,000] 內的整數。
	•	 A  中的每個元素是範圍 [-1,000,000..1,000,000] 內的整數。
'''



# Japnese ver.
'''
次の関数を作成してください：
def solution(A):
この関数は  N  個の整数を含む配列  A  を受け取り、配列に存在しない最小の正の整数（0 より大きい数）を返します。

例：
	1.	 A = [1, 3, 6, 4, 1, 2]  の場合、関数は  5  を返します。
	2.	 A = [1, 2, 3]  の場合、関数は  4  を返します。
	3.	 A = [-1, -3]  の場合、関数は  1  を返します。

前提条件：
	•	 N  は [1..100,000] の範囲内の整数です。
	•	 A  の各要素は [-1,000,000..1,000,000] の範囲内の整数です。
'''

def solution(A):
    # Implement your solution here
    '''
    checker:    input range, empty
    '''
    if not A:
        return 1
    max_count=  100000
    max_num=    1000000
    N = len(A)
    if N > max_count:
        raise ValueError('input range Error')
    setA = set(A)
    # each element of array A is an integer within the range [−1,000,000..1,000,000].
    if min(setA) < -max_num or max(setA) > max_num:
        raise ValueError('input range Error')
    '''
    main process
    '''
    for missing_num in range(1, max_num+2):
        if missing_num not in setA:
            return missing_num
    return 1

test_cases = {
    # Example tests
    (tuple([1, 3, 6, 4, 1, 2])): 5,              # example1
    (tuple([1, 2, 3])): 4,                       # example2
    (tuple([-1, -3])): 1,                        # example3

    # Correctness tests
    (tuple([1])): 2,                             # extreme_single: only one positive element
    (tuple([-1])): 1,                            # extreme_single: one negative element
    (tuple([-100, -50, -1])): 1,                 # negative_only: all negative numbers
    (tuple([2, 3, 4, 5])): 1,                    # simple: no 1 in the array
    (tuple([0, 0, 0])): 1,                       # positive_only: only zeros
    (tuple(list(range(1, 101)) + list(range(102, 201)))): 101,  # positive_only: missing one number

    # Edge cases
    (tuple(list(range(-100000, 0)))): 1,        # all negative values
    (tuple([1] * 100000)): 2,                    # extreme repetition of 1
    (tuple([1000000, 999999, 999998])): 1,       # extreme values with no small positive integers
    (tuple([1, 2, 3, 4, 5, 6, 7, 8, 9, 11])): 10, # missing a middle value
    (tuple([1, -1, 2, -2, 3, -3, 4, -4])): 5,    # mixed positive and negative values

    # Performance tests
    (tuple(list(range(1, 100001)))): 100001,     # large_1: sequential positive integers
    (tuple(list(range(-50000, 50000)))): 50000,  # large_2: large range of negatives and positives
    (tuple([1, 2, 3] * 33333 + [1000000])): 4,   # large_3: repeated sequence with a large value
    (tuple([-1] * 50000 + [1, 2, 3, 4, 5])): 6,  # large_4: many negative numbers with small positives
    (tuple([1000000] * 100000)): 1,              # large_5: all max value
}

def run_tests():
    print("Running tests...\n")
    passed = 0
    failed = 0

    for input_array, expected_output in test_cases.items():
        try:
            result = solution(list(input_array))
            if result == expected_output:
                print(f"Test Passed: input size={len(input_array)}, output={result}")
                passed += 1
            else:
                print(f"Test Failed: input size={len(input_array)}, expected={expected_output}, got={result}")
                failed += 1
        except Exception as e:
            print(f"Test Error: input size={len(input_array)}, error={str(e)}")
            failed += 1

    print("\nTest Summary:")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")
    print(f"  Total:  {len(test_cases)}")


run_tests()
