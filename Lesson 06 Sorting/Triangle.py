# English ver.
'''

def solution(A):
This function, given an array  A  of size  N , returns 1 if a triangular triplet exists and 0 otherwise.

Example

Given:
An array A containing  N  integers is provided. A triplet (P, Q, R) is considered triangular if:
	•	 0 \leq P < Q < R < N 
	•	 A[P] + A[Q] > A[R] 
	•	 A[Q] + A[R] > A[P] 
	•	 A[R] + A[P] > A[Q] 

For example, consider the array:
A[0] = 10    A[1] = 2    A[2] = 5
A[3] = 1     A[4] = 8    A[5] = 20
The function should return 1, as triplet (0, 2, 4) is triangular.

Given:

A[0] = 10    A[1] = 50    A[2] = 5
A[3] = 1

The function should return 0, as no triangular triplet exists.

Assumptions
	•	 N  is an integer within the range [0..100,000].
	•	Each element of array  A  is an integer in the range [-2,147,483,648..2,147,483,647].
'''


# Japnese ver.
'''

def solution(A):
この関数は、サイズ  N  の配列 A を受け取り、三角形の三つ組が存在する場合は 1 を、存在しない場合は 0 を返します。

例

次の配列：
配列 A に  N  個の整数が含まれています。三つ組 (P, Q, R) が三角形になる条件は以下のとおりです：
	•	 0 \leq P < Q < R < N 
	•	 A[P] + A[Q] > A[R] 
	•	 A[Q] + A[R] > A[P] 
	•	 A[R] + A[P] > A[Q] 

例えば、次の配列を考えます：
A[0] = 10    A[1] = 2    A[2] = 5
A[3] = 1     A[4] = 8    A[5] = 20

関数は 1 を返します。三つ組 (0, 2, 4) は三角形です。

次の配列：

A[0] = 10    A[1] = 50    A[2] = 5
A[3] = 1

関数は 0 を返します。三角形の三つ組は存在しません。

前提条件
	•	 N  は範囲 [0..100,000] の整数。
	•	配列  A  の各要素は範囲 [-2,147,483,648..2,147,483,647] の整数。

'''





# Chinese ver.
'''

def solution(A):
該函數接受大小為  N  的陣列 A，如果存在三角形三元組，返回 1；否則返回 0。

範例

給定：
給定一個包含  N  個整數的陣列 A。三元組 (P, Q, R) 是三角形的條件如下：
	•	 0 \leq P < Q < R < N 
	•	 A[P] + A[Q] > A[R] 
	•	 A[Q] + A[R] > A[P] 
	•	 A[R] + A[P] > A[Q] 

例如，考慮以下陣列：
A[0] = 10    A[1] = 2    A[2] = 5
A[3] = 1     A[4] = 8    A[5] = 20

函數應返回 1，因為 (0, 2, 4) 是三角形。

給定：
A[0] = 10    A[1] = 50    A[2] = 5
A[3] = 1

函數應返回 0，因為不存在三角形三元組。

假設條件
	•	 N  是範圍 [0..100,000] 內的整數。
	•	陣列  A  的每個元素是範圍 [-2,147,483,648..2,147,483,647] 的整數。
'''

def solution(A):
    # Implement your solution here
    '''
    checker:    input range, empty
    '''
    # If the array has fewer than 3 elements, no triangular triplet can exist
    if len(A) < 3:
        return 0

    '''
    main process
    '''
    # Sort the array
    A.sort()

    # Check for a triangular triplet
    for i in range(len(A) - 2):
        # A[i] + A[i+1] > A[i+2] is enough due to sorted order
        if A[i] + A[i+1] > A[i+2]:
            return 1

    return 0


test_cases = {
    # Example cases
    (10, 2, 5, 1, 8, 20): 1,  # Triangular triplet exists
    (10, 50, 5, 1): 0,        # No triangular triplet

    # Edge cases
    (): 0,                     # Empty array
    (1,): 0,                   # Single element
    (1, 2): 0,                 # Two elements
    (-3, -3, -3): 0,           # All negatives, valid triplet
    (-10, -1, 0, 1): 0,        # Mix of negatives and small positives

    # Small and large tests
    (1, 2, 3, 4, 5): 1,        # Increasing sequence
    (-10, -10, 1, 2, 3): 0,    # Negative and positive values
    tuple(range(1, 100000)): 1, # Large increasing sequence
    tuple([-i for i in range(1, 100000)]): 0, # Large decreasing negatives
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
