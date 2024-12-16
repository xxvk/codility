# English ver.
'''
A frog wants to cross a river. The frog starts on one side of the river 
(position 0) and needs to reach the opposite side (position  X+1 ). 
Leaves fall from a tree onto the river.

You are given an array  A , which consists of  N  integers representing the positions where leaves fall.  A[K]  indicates the position where a leaf falls at second  K .

The goal is to find the earliest time the frog can jump to the other side. 
The frog can cross only when all positions from  1  to  X  are covered by leaves. 
Once a leaf falls, it stays at its position.

Example:
If  X = 5  and  A  is given as:
  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
  At second  6 , all positions from  1  to  5  are covered. 
  Therefore, the frog can cross the river at this time.

Write a function:
def solution(X, A):

This function takes an integer  X  and an array  A , 
and returns the earliest time when the frog can cross the river. 
If the frog is never able to cross, return -1.

Example:
For  X = 5  and  A  as:
The function should return  6 .

Constraints:
	•	 N  and  X  are integers within the range [1..100,000].
	•	Each element of  A  is an integer within the range [1..X].
'''



# Chinese ver.
'''
一隻青蛙想要過河。青蛙從河的一側（位置 0）開始，需要到達對岸（位置  X+1 ）。
樹葉從樹上掉落到河面上。

給定一個由  N  個整數組成的陣列  A ，代表樹葉掉落的位置。 
A[K]  表示在第  K  秒時，樹葉掉落到位置  A[K] 。

目標是找到青蛙能跳過河的最早時間。
青蛙只有在從位置  1  到位置  X  的所有位置都被樹葉覆蓋時才能過河。
一旦樹葉掉落到河中，它的位置不會改變。

範例：
如果  X = 5  且  A  為：
  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
在第 6 秒時，所有從位置  1  到  5  的位置都被樹葉覆蓋。因此，青蛙可以在此時過河。

請撰寫一個函數：
  def solution(X, A):
  
此函數接收整數  X  和陣列  A ，返回青蛙能過河的最早時間。如果青蛙無法過河，返回 -1。

範例：
對於  X = 5  和  A ：
函數應返回  6 。

約束：
	•	 N  和  X  是範圍 [1..100,000] 內的整數。
	•	 A  的每個元素是範圍 [1..X] 內的整數。
'''



# Japnese ver.
'''
カエルが川を渡ろうとしています。カエルは川の片側（位置 0）からスタートし、
反対側（位置  X+1 ）に到達する必要があります。
葉が木から川の表面に落ちます。

整数  N  個で構成される配列  A  が与えられます。
この配列は落ち葉の位置を表します。 A[K]  は、 K  秒目に葉が落ちた位置を示します。

カエルが川を渡れる最も早い時間を見つけることが目標です。
カエルは、位置  1  から  X  までのすべての位置に葉が落ちているときにのみ川を渡ることができます。
葉は一度落ちると位置を変えません。

例：
 X = 5  とし、配列  A  が次のように与えられる場合：
  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4

  6 秒目にすべての位置（1 から 5）が葉で覆われます。
  このため、カエルは6秒目に川を渡ることができます。

次の関数を作成してください：

    def solution(X, A):
    
この関数は、整数  X  と配列  A  を受け取り、カエルが川を渡れる最も早い時間を返します。
カエルが川を渡れない場合は、-1 を返してください。

例：
 X = 5  、配列  A  が次のように与えられる場合：
この場合、関数は  6  を返すべきです。

制約：
	•	 N  および  X  は範囲 [1..100,000] の整数です。
	•	配列  A  の各要素は範囲 [1..X] の整数です。
'''

def solution(X, A):
    # Implement your solution here
    '''
    checker:    input range, empty
    '''
    if not A or not X:
        raise ValueError('input range Error')
    N = len(A)
    max = 100000
    if N > max or N < 1:
        raise ValueError('input range Error')
    if X > max or X < 1:
        raise ValueError('input range Error')
    for num in A:
        if num > X or num < 1:
             raise ValueError('input range Error')
    '''
    checker:    can not cross the river
    '''
    reduce_set_As = set(numA for numA in A)
    cache_set_Xs = set(numX for numX in range(1,X+1))
    difference_set = cache_set_Xs.difference(reduce_set_As)
    if len(difference_set) > 0:
        return -1
    
    '''
    main process
    '''
    # print(cache_set_Xs)
    # print(A)
    index = 0
    for num in A:
        cache_set_Xs.discard(num)
        if len(cache_set_Xs) == 0:
            return index
        index += 1
    
    return -1

# Example test
test_cases = {
    # Example test
    ((5, (1, 3, 1, 4, 2, 3, 5, 4))): 6,  # example test

    # Correctness tests
    ((1, (1,))): 0,                              # single: single element
    ((5, (1, 2, 3, 4, 5))): 4,                  # simple: sequential leaves
    ((3, (3, 3, 3))): -1,                       # extreme_frog: all leaves in same place
    ((2, (2, 2, 2, 2, 2))): -1,                 # extreme_frog: frog cannot cross
    ((3, (1, 3, 2))): 2,                        # simple test: unordered but complete
    ((4, (4, 1, 3, 2))): 3,                     # simple test: out of order leaves
    ((5, (1, 1, 1, 1, 1))): -1,                 # extreme_frog: only one repeated value

    # Edge cases
    ((1000, tuple(range(1, 1001)))): 999,        # large range, sequential
    ((10, (10, 9, 8, 7, 6, 5, 4, 3, 2, 1))): 9, # reversed order
    ((50, (1,) * 50)): -1,                       # all same number

    # Performance tests
    ((10000, tuple(range(1, 10001)))): 9999,     # large_permutation: sequential large range
    ((30000, tuple(range(1, 30001)))): 29999,    # large_range: arithmetic sequence
    ((10000, tuple(i % 50 + 1 for i in range(10000)))): -1, # repeated small range
    ((5000, (5000, 1, 3, 2, 4))): -1,            # medium_random: unordered with duplicates
    ((1000, tuple(range(1, 1001)) + (500,) * 100)): 999, # redundant leaves
}

def run_tests():
    print("Running tests...\n")
    passed = 0
    failed = 0

    for (X, A), expected_output in test_cases.items():
        try:
            result = solution(X, list(A))
            if result == expected_output:
                print(f"Test Passed: input=(X={X}, len(A)={len(A)}), output={result}")
                passed += 1
            else:
                print(f"Test Failed: input=(X={X}, len(A)={len(A)}), expected={expected_output}, got={result}")
                failed += 1
        except Exception as e:
            print(f"Test Error: input=(X={X}, len(A)={len(A)}), error={str(e)}")
            failed += 1

    print("\nTest Summary:")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")
    print(f"  Total:  {len(test_cases)}")


run_tests()
