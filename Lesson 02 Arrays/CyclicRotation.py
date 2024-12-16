# English ver.
'''
Problem Description

An array  A  of  N  integers is given. 
Rotating the array means shifting each element one position to the right, 
with the last element moving to the front. 
For example, rotating  A = [3, 8, 9, 7, 6]  once gives  [6, 3, 8, 9, 7] .

The task is to rotate  A  exactly  K  times. Each element of  A  will shift  K  positions to the right.
Write a function:

def solution(A, K):

This function takes an array  A  of  N  integers and an integer  K , and returns the array after  K  rotations.

Examples:
	1.	Given:
 A = [3, 8, 9, 7, 6] ,  K = 3 
The function should return  [9, 7, 6, 3, 8] .
Three rotations were performed as follows:

[3, 8, 9, 7, 6] \to [6, 3, 8, 9, 7] \to [7, 6, 3, 8, 9] \to [9, 7, 6, 3, 8]

	2.	Given:
 A = [0, 0, 0] ,  K = 1 
The function should return  [0, 0, 0] .
	3.	Given:
 A = [1, 2, 3, 4] ,  K = 4 
The function should return  [1, 2, 3, 4] .
Since  K = 4  (equal to the length of the array), the array remains unchanged.

Assumptions:
	•	 N  and  K  are integers within the range [0..100].
	•	Each element in array  A  is an integer within the range [-1,000..1,000].

In your solution, prioritize correctness. 
Performance is not a primary concern for this task.
'''



# Chinese ver.
'''
一個包含  N  個整數的陣列  A  被提供。旋轉 陣列的意思是將每個元素向右移動一個位置，並將最後一個元素移到最前面。例如，當  A = [3, 8, 9, 7, 6]  時，旋轉一次的結果是  [6, 3, 8, 9, 7] ，所有元素向右移動，而  6  移到了最前面。

任務是將陣列  A  旋轉  K  次，也就是說，每個元素向右移動  K  個位置。

請撰寫一個函數：

def solution(A, K):

此函數接受一個包含  N  個整數的陣列  A  和一個整數  K ，並返回旋轉  K  次後的陣列。

範例：
	1.	給定：
 A = [3, 8, 9, 7, 6] ,  K = 3 
函數應回傳  [9, 7, 6, 3, 8] 。
三次旋轉的過程如下：

[3, 8, 9, 7, 6] \to [6, 3, 8, 9, 7] \to [7, 6, 3, 8, 9] \to [9, 7, 6, 3, 8]

	2.	給定：
 A = [0, 0, 0] ,  K = 1 
函數應回傳  [0, 0, 0] 。
	3.	給定：
 A = [1, 2, 3, 4] ,  K = 4 
函數應回傳  [1, 2, 3, 4] 。
因為  K = 4 （等於陣列的長度），陣列保持不變。

假設：
	•	 N  和  K  是 [0..100] 範圍內的整數。
	•	陣列  A  中的每個元素是 [-1,000..1,000] 範圍內的整數。

在你的解法中，請著重於正確性。本題的評估不關注效能。
'''



# Japnese ver.
'''
 N  個の整数から成る配列  A  が与えられています。回転 とは、配列内の各要素を右に1つ移動し、
 最後の要素を先頭に移すことを意味します。
 例えば、 A = [3, 8, 9, 7, 6]  の場合、1回回転させると  [6, 3, 8, 9, 7]  になり、
 全ての要素が右に移動し、 6  が最初に移動します。

このタスクでは、配列  A  を  K  回回転させます。つまり、全ての要素を右に  K  回移動させます。

次の関数を作成してください：

def solution(A, K):

この関数は、 N  個の整数から成る配列  A  と整数  K  を受け取り、 
K  回回転させた後の配列を返します。

例：
	1.	入力：
 A = [3, 8, 9, 7, 6] ,  K = 3 
出力： [9, 7, 6, 3, 8] 
3回回転した結果：

[3, 8, 9, 7, 6] \to [6, 3, 8, 9, 7] \to [7, 6, 3, 8, 9] \to [9, 7, 6, 3, 8]

	2.	入力：
 A = [0, 0, 0] ,  K = 1 
出力： [0, 0, 0] 
	3.	入力：
 A = [1, 2, 3, 4] ,  K = 4 
出力： [1, 2, 3, 4] 
 K = 4 （配列の長さと同じ）の場合、配列は変わりません。

前提：
	•	 N  と  K  は [0..100] の範囲内の整数です。
	•	配列  A  の各要素は [-1,000..1,000] の範囲内の整数です。

実装では、正確さに重点を置いてください。このタスクでは、パフォーマンスは重要ではありません。
'''


def solution(A, K):
    # Implement your solution here
    '''
    checker:    input range
    '''
    N =  len(A)
    if N > 1000:
        raise ValueError('input range Error')
    if K < 0 or K > 1000:
        raise ValueError('input range Error')
    '''
    checker:    empty
    '''
    if not A:
        return A
    if K == 0:
        return A
    '''
    checker:    same elements array
    '''
    one_ele_set = set(x for x in A)
    one_ele_set_length = len(one_ele_set) 
    if one_ele_set_length == 1 or one_ele_set_length == 0:
        return A

    '''
    main process
    '''
    modK = K % N

    result_arr = A[-modK:] + A[:-modK]
    return result_arr

# Example tests
test_cases = {
    (tuple([]), 3): [],                              # Empty array
    (tuple([3, 8, 9, 7, 6]), 3): [9, 7, 6, 3, 8],    # Example test
    (tuple([0, 0, 0]), 1): [0, 0, 0],                # Example test
    (tuple([1, 2, 3, 4]), 4): [1, 2, 3, 4],          # Example test

    # Correctness tests
    (tuple([]), 0): [],                              # extreme_empty
    (tuple([1]), 0): [1],                            # single, K=0
    (tuple([1]), 3): [1],                            # single, K>1
    (tuple([1, 2]), 1): [2, 1],                      # double, K <= N
    (tuple([1, 2]), 2): [1, 2],                      # double, K == N
    (tuple([1, 2, 3, 4]), 2): [3, 4, 1, 2],          # small1, K < N
    (tuple([1, 2, 3, 4]), 6): [3, 4, 1, 2],          # small2, K >= N
    (tuple([5, 6, 7, 8, 9]), 15): [5, 6, 7, 8, 9],   # small_random_all_rotations
    (tuple(range(1, 101)), 50): list(range(51, 101)) + list(range(1, 51)), # medium_random
    (tuple(range(1, 1001)), 1000): list(range(1, 1001))                    # maximal
}

def run_tests():
    print("Running tests...\n")
    passed = 0
    failed = 0

    for (input_array, K), expected_output in test_cases.items():
        try:
            result = solution(list(input_array), K)
            if result == expected_output:
                print(f"Test Passed: input=({input_array}, {K}), output={result}")
                passed += 1
            else:
                print(f"Test Failed: input=({input_array}, {K}), expected={expected_output}, got={result}")
                failed += 1
        except Exception as e:
            print(f"Test Error: input=({input_array}, {K}), error={str(e)}")
            failed += 1

    print("\nTest Summary:")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")
    print(f"  Total:  {len(test_cases)}")

run_tests()