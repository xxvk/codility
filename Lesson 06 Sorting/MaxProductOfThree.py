# English ver.
'''
A non-empty array A containing  N  integers is provided. The product of a triplet (P, Q, R) is defined as:


\text{Product} = A[P] \cdot A[Q] \cdot A[R] \quad \text{where} \quad 0 \leq P < Q < R < N


For example, given the array A:

A[0] = -3
A[1] = 1
A[2] = 2
A[3] = -2
A[4] = 5
A[5] = 6

Some example triplets are:
	•	Triplet (0, 1, 2): -3 \cdot 1 \cdot 2 = -6
	•	Triplet (1, 2, 4): 1 \cdot 2 \cdot 5 = 10
	•	Triplet (2, 4, 5): 2 \cdot 5 \cdot 6 = 60

Your goal is to find the maximum product of any triplet.

Function Description

Write a function:
def solution(A):
that takes a non-empty array A and returns the maximal product of any triplet.

Example

Given the array:
The function should return 60, which is the product of the triplet (2, 4, 5).
Assumptions
	•	 N  is an integer within the range [3..100,000].
	•	Each element of array  A  is an integer within the range [-1,000..1,000].
'''



# Japnese ver.
'''
非空の配列 A が  N  個の整数を含んでいます。三つ組 (P, Q, R) の積は次のように定義されます：


\text{積} = A[P] \cdot A[Q] \cdot A[R] \quad \text{ただし} \quad 0 \leq P < Q < R < N


例えば、配列 A：

A[0] = -3
A[1] = 1
A[2] = 2
A[3] = -2
A[4] = 5
A[5] = 6

いくつかの三つ組の例：
	•	三つ組 (0, 1, 2)：-3 \cdot 1 \cdot 2 = -6
	•	三つ組 (1, 2, 4)：1 \cdot 2 \cdot 5 = 10
	•	三つ組 (2, 4, 5)：2 \cdot 5 \cdot 6 = 60

目的は、最大の積 を持つ三つ組を見つけることです。

関数説明

次の関数を作成してください：
def solution(A):
この関数は非空の配列 A を受け取り、三つ組の最大積を返します。

例

配列：
関数は 60 を返すべきです。これは三つ組 (2, 4, 5) の積です。
前提条件
	•	 N  は範囲 [3..100,000] 内の整数。
	•	配列  A  の各要素は範囲 [-1,000..1,000] 内の整数。
'''


# Chinese ver.

'''

一個包含  N  個整數的非空陣列 A 被提供。三元組 (P, Q, R) 的乘積定義為：


\text{乘積} = A[P] \cdot A[Q] \cdot A[R] \quad \text{其中} \quad 0 \leq P < Q < R < N


例如，給定陣列 A：
A[0] = -3
A[1] = 1
A[2] = 2
A[3] = -2
A[4] = 5
A[5] = 6

一些三元組的例子是：
	•	三元組 (0, 1, 2)：-3 \cdot 1 \cdot 2 = -6
	•	三元組 (1, 2, 4)：1 \cdot 2 \cdot 5 = 10
	•	三元組 (2, 4, 5)：2 \cdot 5 \cdot 6 = 60

目標是找到 最大乘積 的三元組。

函數說明

撰寫函數：
def solution(A):
該函數接收一個非空陣列 A，並返回任何三元組的最大乘積。

範例

給定陣列：
函數應返回 60，這是三元組 (2, 4, 5) 的乘積。
假設條件
	•	 N  是範圍 [3..100,000] 內的整數。
	•	陣列  A  中的每個元素是範圍 [-1,000..1,000] 內的整數。
'''




def solution(A):
    # Implement your solution here
    '''
    checker:    input range, empty
    '''
    if not A:
        return 0
    N = len(A)
    if N < 3 or N > 100000:
        return 0
    '''
    main process
    '''
    A.sort()
    max_product_1 = A[-1] * A[-2] * A[-3]
    max_product_2 = A[0] * A[1] * A[-1]

    return max(max_product_1, max_product_2)

test_cases = {
    # Example case
    (-3, 1, 2, -2, 5, 6): 60,  # Example from the question

    # Edge cases
    (1, 2, 3): 6,                     # Exactly three elements
    (-1, -2, -3): -6,                 # Only negatives
    (-1, -2, -3, 1): 6,               # Mix of negatives and positive
    (-1000, -1000, -1000): -1000000000, # All elements are the same, negative

    # Small and medium cases
    (1, 1, 1, 1): 1,                  # All elements are the same, positive
    (-1, -1, -1, -1): -1,             # All elements are the same, negative
    (1, 2, 3, 4): 24,                 # All positive increasing
    (-10, -10, 1, 2, 3): 300,         # Two large negatives
    tuple(range(-100, 101)): 990000,  # Sequence from -100 to 100

    # Performance cases
    tuple([-1, 1] * 50000): 1,        # Alternating sequence
    tuple([i for i in range(1000)]): 994010994, # Increasing sequence
    tuple([-i for i in range(1000)]): 0, # Decreasing sequence
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
