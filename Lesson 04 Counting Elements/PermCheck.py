# English ver.
'''
An array A containing N integers is provided, and it is not empty.

A permutation is a sequence that includes every number from 1 to N exactly once.

For instance, the array A:
A[0] = 4
A[1] = 1
A[2] = 3
A[3] = 2
is a valid permutation, The function should return 1.


but the array:
A[0] = 4
A[1] = 1
A[2] = 3
is not a valid permutation because the number 2 is missing.
The function should return 0.

Your task is to determine if the array A is a permutation.

Write a function:

def solution(A):

This function takes the array A and returns 1 if A is a permutation, otherwise it returns 0.

The algorithm must be efficient given the constraints:
	•	N is an integer within [1..100,000].
	•	Each element of A is an integer within [1..1,000,000,000].
'''



# Chinese ver.
'''
一個包含 N 個整數的非空陣列 A 已給定。

排列是指一個包含每個從 1 到 N 的數字，且僅包含一次的序列。

例如，以下陣列 A：
A[0] = 4
A[1] = 1
A[2] = 3
A[3] = 2
是一個有效的排列，該函數應返回 1。

但以下陣列：
A[0] = 4
A[1] = 1
A[2] = 3
不是一個有效的排列，因為數值 2 缺失。
該函數應返回 0。


目標是檢查陣列 A 是否為一個排列。

請撰寫函數：

def solution(A):
該函數給定陣列 A，如果 A 是排列則返回 1，否則返回 0。
需要撰寫一個高效的演算法，滿足以下假設條件：
	•	N 是範圍 [1..100,000] 內的整數；
	•	陣列 A 中的每個元素皆為範圍 [1..1,000,000,000] 內的整數。
'''



# Japnese ver.
'''

N 個の整数を含む非空の配列 A が与えられています。

順列とは、1 から N までの各数字が 1 回だけ含まれる配列のことです。

例えば、次の配列 A:
A[0] = 4
A[1] = 1
A[2] = 3
A[3] = 2
は有効な順列ですが、この関数は 1 を返すべきです。


次の配列:
A[0] = 4
A[1] = 1
A[2] = 3
は 2 が欠けているため、有効な順列ではありません。
この関数は 0 を返すべきです。

目的は、配列 A が順列であるかどうかを確認することです。

次のような関数を作成してください：

def solution(A):

この関数は配列 A を受け取り、A が順列であれば 1 を返し、そうでなければ 0 を返します。
以下の条件を満たす効率的なアルゴリズムを書く必要があります：
	•	N は [1..100,000] の範囲内の整数です。
	•	配列 A の各要素は [1..1,000,000,000] の範囲内の整数です。
'''


def solution(A):
    # Implement your solution here
    '''
    checker:    input range, empty
    '''
    if not A:
        return 0
    N = len(A)

    if N > 100000 or N < 1:
        return 0
    
    if min(A) < 1 or max(A) > N:
        return 0
    
    '''
    main process
    '''
    setA = set(A)
    if len(setA) != N:
        return 0
    
    return 1

test_cases = {
    # Example cases
    (4, 1, 3, 2): 1,  # Valid permutation
    (4, 1, 3): 0,     # Missing 2

    # Edge cases
    (1,): 1,          # Single element (valid)
    (2,): 0,          # Single element (invalid)
    (1, 1): 0,        # Duplicate element

    # Small cases
    (1, 2, 3, 4, 5): 1,  # Valid permutation
    (5, 3, 4, 2, 1): 1,  # Valid permutation
    (5, 3, 4, 2, 2): 0,  # Duplicate element

    # Performance cases
    tuple(range(1, 100001)): 1,               # Large valid permutation
    tuple(range(1, 100000)) + (100001,): 0,  # Missing one element
    (1,) * 100000: 0,                        # All the same value
    tuple(range(1, 50001)) + tuple(range(50001, 100001)): 1,  # Split valid range
    tuple(range(2, 100001)): 0,              # Missing 1

    # Stress cases
    tuple([i for i in range(1, 100001) if i != 99999]): 0,  # Missing one element in middle
    (100000,) + tuple(range(1, 99999)): 0,                 # Invalid order with missing
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
