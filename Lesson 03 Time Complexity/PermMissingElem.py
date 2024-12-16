# English ver.
'''
An array  A  consisting of  N  unique integers is provided. The integers in the array range from  1  to  N + 1 , which means one element is missing.

The task is to find the missing element.

Write a function:
def solution(A):
This function takes an array  A  and returns the value of the missing element.

Example:
Given the array  A :
A[0] = 2
A[1] = 3
A[2] = 1
A[3] = 5
The function should return  4 , as it is the missing element.

Requirements: Write an efficient algorithm based on the following assumptions:
	•	 N  is an integer within the range [0..100,000].
	•	All elements in  A  are distinct.
	•	Every element in  A  is an integer within the range [1..(N + 1)].

'''



# Chinese ver.
'''
一個包含  N  個不同整數的陣列  A  被提供。該陣列中的整數範圍是從  1  到  N + 1 ，這意味著其中有一個數字缺失。

任務是找到這個缺失的數字。

請撰寫一個函數：
def solution(A):
此函數接受一個陣列  A ，並返回缺失數字的值。

範例：
給定陣列  A ：
A[0] = 2
A[1] = 3
A[2] = 1
A[3] = 5
函數應返回  4 ，因為它是缺失的數字。

需求：根據以下假設撰寫一個高效的算法：
	•	 N  是範圍 [0..100,000] 內的整數。
	•	 A  中的所有元素都是不同的。
	•	 A  中的每個元素都是範圍 [1..(N + 1)] 內的整數。
'''



# Japnese ver.
'''
 N  個の異なる整数から成る配列  A  が与えられています。この配列には、整数の範囲が  1  から  N + 1  まで含まれており、その中の1つの要素が欠けています。

この欠けている要素を見つけることが目的です。

次の関数を作成してください：
def solution(A):
この関数は配列  A  を受け取り、欠けている要素の値を返します。

例：
配列  A  が次の場合：
A[0] = 2
A[1] = 3
A[2] = 1
A[3] = 5
関数は  4  を返すべきです。それが欠けている要素だからです。

要件：次の仮定に基づいて効率的なアルゴリズムを作成してください：
	•	 N  は [0..100,000] の範囲内の整数です。
	•	 A  のすべての要素は異なります。
	•	 A  の各要素は [1..(N + 1)] の範囲内の整数です。
'''

def solution(A):
    # Implement your solution here
    '''
    checker:    input range, empty
    '''
    if not A:
        return 1
    N = len(A)
    if N > 100000:
        raise ValueError('input range Error')

    '''
    main process
    '''
    dup_set = set(num for num in A)
    cache_last_num = 0
    for num in dup_set:
        if num - cache_last_num > 1:
            return cache_last_num + 1
        cache_last_num = num
    
    return cache_last_num + 1

# Example test
test_cases = {
    
    (tuple([2, 3, 1, 5])): 4,  # example

    # Correctness tests
    (tuple([])): 1,                           # empty_and_single: empty list
    (tuple([1])): 2,                          # single: missing 2
    (tuple([2])): 1,                          # single: missing 1
    (tuple([1, 3])): 2,                       # double: missing 2
    (tuple([2, 3])): 1,                       # double: missing 1
    (tuple([1, 2])): 3,                       # double: missing 3
    (tuple([3, 4, 1, 5, 6])): 2,              # simple
    (tuple([1, 2, 4, 5, 6])): 3,              # simple
    (tuple([2, 3, 4, 5, 6])): 1,              # missing_first_or_last
    (tuple([1, 2, 3, 4, 5])): 6,              # missing_first_or_last

    # Performance tests
    (tuple(range(1, 10001))): 10001,          # medium1
    (tuple(range(2, 10002))): 1,              # medium2
    (tuple(range(1, 100000))): 100000,        # large_range
    (tuple(range(2, 100001))): 1,             # large1
    (tuple(range(1, 50000)) + tuple(range(50001, 100001))): 50000,  # large2
}

def run_tests():
    print("Running tests...\n")
    passed = 0
    failed = 0

    for input_array, expected_output in test_cases.items():
        try:
            # Convert tuple back to list for testing
            result = solution(list(input_array))
            if result == expected_output:
                print(f"Test Passed: input={len(input_array)}, output={result}")
                passed += 1
            else:
                print(f"Test Failed: input={len(input_array)}, expected={expected_output}, got={result}")
                failed += 1
        except Exception as e:
            print(f"Test Error: input={len(input_array)}, error={str(e)}")
            failed += 1

    print("\nTest Summary:")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")
    print(f"  Total:  {len(test_cases)}")


run_tests()
