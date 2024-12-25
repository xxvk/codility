# English ver.
'''
We draw  N  discs on a 2D plane. Each disc is numbered from  0  to  N-1 . An array  A  of  N  non-negative integers represents the radii of the discs. The  J -th disc has its center at (J, 0) and a radius of  A[J] .

Two discs  J  and  K  are said to intersect if  J \neq K  and they have at least one common point, including the boundaries.

For example, for  N = 6  and the array:
A[0] = 1
A[1] = 5
A[2] = 2
A[3] = 1
A[4] = 4
A[5] = 0
There are 11 pairs of intersecting discs:
	•	Discs 1 and 4 intersect with all other discs.
	•	Disc 2 intersects with discs 0 and 3.

Function Description

Write a function:

def solution(A):
The function takes an array  A  that describes  N  discs and returns the number of intersecting pairs. If the number of intersecting pairs exceeds 10,000,000, the function should return  -1 .

Example

For the array:
The function should return  11 , as explained above.

Assumptions
	•	 N  is an integer within the range [0..100,000].
	•	Each element of  A  is an integer within the range [0..2,147,483,647].
'''


# Japnese ver.
'''
平面上に  N  個の円盤を描きます。それぞれの円盤には  0  から  N-1  までの番号が付けられています。配列  A  は  N  個の非負整数で、円盤の半径を表します。円盤  J  の中心は (J, 0) にあり、半径は  A[J]  です。

円盤  J  と  K  が以下の場合に交差すると言います：
	•	 J \neq K 
	•	円盤  J  と  K  が少なくとも 1 点で交差する（境界を含む）。

例えば、 N = 6  で次の配列の場合：
A[0] = 1
A[1] = 5
A[2] = 2
A[3] = 1
A[4] = 4
A[5] = 0
11 組の交差する円盤があります：
	•	円盤 1 と 4 はすべての他の円盤と交差します。
	•	円盤 2 は円盤 0 と 3 と交差します。

関数説明

次の関数を作成してください：

def solution(A):
この関数は  N  個の円盤を記述する配列  A  を受け取り、交差する円盤の組数を返します。交差する組数が 10,000,000 を超える場合は、 -1  を返します。

例

次の配列の場合：
関数は  11  を返します。

前提条件
	•	 N  は [0..100,000] の範囲内の整数。
	•	配列  A  の各要素は [0..2,147,483,647] の範囲内の整数。
'''


# Chinese ver.
'''
在平面上畫出  N  個圓盤，每個圓盤編號從  0  到  N-1 。陣列  A  包含  N  個非負整數，表示圓盤的半徑。第  J  個圓盤的中心位於 (J, 0)，半徑為  A[J] 。

如果兩個圓盤  J  和  K  （ J \neq K ）至少有一個交點（包括邊界），則稱它們相交。

例如，對於  N = 6  和以下陣列：
A[0] = 1
A[1] = 5
A[2] = 2
A[3] = 1
A[4] = 4
A[5] = 0

有 11 對相交的圓盤：
	•	圓盤 1 和 4 與所有其他圓盤相交。
	•	圓盤 2 與圓盤 0 和 3 相交。

函數說明

撰寫函數：
def solution(A):
該函數接受描述  N  個圓盤的陣列  A ，返回相交圓盤的對數。如果相交對數超過 10,000,000，則返回  -1 。

範例

對於陣列：
函數應返回  11 ，如上所述。

假設條件
	•	 N  是範圍 [0..100,000] 內的整數。
	•	陣列  A  中的每個元素是範圍 [0..2,147,483,647] 內的整數。
'''


def if_intersect(rangeA,rangeB):
    return max(rangeA.start, rangeB.start) <= min(rangeA.stop, rangeB.stop)

def solution(A):
    # Implement your solution here
    '''
    checker:    input range, empty
    '''
    if not A:
        return 0
    N = len(A)
    if N > 100000:
        return -1
    if N == 0 or N == 1: return 0
    '''
    main process
    '''
    left = [i - radius for i, radius in enumerate(A)]
    right = [i + radius for i, radius in enumerate(A)]
    
    
    left.sort()
    right.sort()
    
    
    active_discs = 0
    intersections = 0
    max_intersections = 10_000_000
    j = 0 
    
    for i in range(N):
        
        while j < N and left[j] <= right[i]:
            active_discs += 1
            j += 1
        
        
        active_discs -= 1
        intersections += active_discs
        
        if intersections > max_intersections:
            return -1 
    
    return intersections


test_cases = {
    # Example cases
    (1, 5, 2, 1, 4, 0): 11,  # Example with intersections
    (): 0,                    # Empty array
    (10,): 0,                 # Single disc, no intersections

    # Small and edge cases
    (0, 0, 0): 0,             # No intersections
    (1, 1, 1): 3,             # Fully overlapping discs
    (1, 0, 1): 3,             # Some intersections
    (2, 0, 0, 0): 2,          # Only first disc intersects

    # Large cases
    (0,) * 100_000: 0,        # All discs have zero radius
    (1,) * 100_000: 199997,  # All discs intersect
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

# Run tests
run_tests()
