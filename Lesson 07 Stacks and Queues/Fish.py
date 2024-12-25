# English ver.
'''
You are given two arrays, A and B, which represent fish in a river. Each fish has a size and a direction:
	•	A[P] is the size of fish P.
	•	B[P] is the direction of fish P:
	•	0 means the fish swims upstream.
	•	1 means the fish swims downstream.

If a downstream fish (direction 1) meets an upstream fish (direction 0), they fight:
	•	The bigger fish survives, and the smaller fish is eaten.

Fish moving in the same direction never meet. The goal is to find how many fish will survive.

Example

Given:
A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]
	•	Fish 1 (size=3, direction=1) moves downstream.
	•	Fish 2 (size=2, direction=0) moves upstream.

Fish 1 and Fish 2 meet:
	•	Fish 1 eats Fish 2 because it is bigger.
	•	Then, Fish 1 meets Fish 3 (size=1) and eats it too.
	•	Finally, Fish 1 meets Fish 4 (size=5) and is eaten.

The remaining survivors are Fish 0 and Fish 4. So, the result is 2.
'''



# Japnese ver.
'''
2つの配列 A と B が与えられます。それぞれの魚にはサイズと移動方向があります：
	•	A[P] は魚 P のサイズ。
	•	B[P] は魚 P の移動方向：
	•	0 は魚が上流に泳ぐことを意味します。
	•	1 は魚が下流に泳ぐことを意味します。

下流に泳ぐ魚（1）が上流に泳ぐ魚（0）に出会うと、戦いが発生します：
	•	大きい魚が生き残り、小さい魚は食べられます。

同じ方向に泳ぐ魚は決して出会いません。最終的に生き残る魚の数を求めます。

例

次のような入力が与えられたとします：
A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]
	•	魚1（サイズ=3、方向=1）は下流に泳ぎます。
	•	魚2（サイズ=2、方向=0）は上流に泳ぎます。

魚1と魚2が出会います：
	•	魚1の方が大きいため、魚2を食べます。
	•	次に、魚1は魚3（サイズ=1）に出会い、これも食べます。
	•	最後に、魚1は魚4（サイズ=5）に出会い、魚4に食べられます。

生き残った魚は魚0と魚4です。したがって、結果は 2 です。
'''



# Chinese ver.
'''
給你兩個陣列 A 和 B，表示河流中的魚。每條魚都有大小和方向：
	•	A[P] 是第 P 條魚的大小。
	•	B[P] 是第 P 條魚的方向：
	•	0 表示魚往上游游。
	•	1 表示魚往下游游。

當一條下游的魚（方向為 1）遇到一條上游的魚（方向為 0）時，牠們會打架：
	•	體型較大的魚會活下來，而體型較小的魚會被吃掉。

朝相同方向游的魚永遠不會相遇。目標是計算最後有多少魚存活。

範例

給定：
A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]
	•	魚1（大小=3，方向=1）往下游游。
	•	魚2（大小=2，方向=0）往上游游。

魚1和魚2相遇：
	•	因為魚1更大，所以牠吃掉了魚2。
	•	接著，魚1遇到魚3（大小=1），也吃掉了牠。
	•	最後，魚1遇到魚4（大小=5），被魚4吃掉。

存活下來的魚是魚0和魚4。因此，結果是 2。
'''



def solution(A, B):
    # Implement your solution here
    '''
    checker:    input range, empty
    '''
    if not A or not B:
        return 0
    N = len(A)
    '''
    main process
    '''
    attackers = []
    remainers = []
    directions = { 0: 'up', 1:'down'}
    for index in range(0, N):
        fish = A[index]
        direction = B[index]
        if direction == 1:
            attackers.append(fish)
        if direction == 0:
            while len(attackers) > 0:
                if attackers[-1] > fish: break
                if attackers[-1] < fish: attackers.pop(-1)
            if len(attackers) == 0:
                remainers.append(fish)
    total = len(attackers) + len(remainers)
    return total

def run_tests():
    print("Running tests...\n")
    test_cases = {
        # Example tests
        ((4, 3, 2, 1, 5), (0, 1, 0, 0, 0)): 2,  # Example case

        # Edge cases
        ((1,), (0,)): 1,  # Single fish moving upstream
        ((1,), (1,)): 1,  # Single fish moving downstream
        ((2, 6), (1, 0)): 1,  # Two fish meet, one survives

        # Additional cases
        ((5, 3, 4, 2, 1), (1, 1, 0, 0, 0)): 1,  # Mixed directions
        ((1, 2, 3, 4, 5), (0, 0, 0, 0, 0)): 5,  # All moving upstream
        ((1, 2, 3, 4, 5), (1, 1, 1, 1, 1)): 5,  # All moving downstream

        # Performance cases
        (tuple(range(100000, 0, -1)), (1,) * 99999 + (0,)): 99999,  # All fish downstream except last
        (tuple(range(1, 100001)), (0,) * 100000): 100000,  # All fish upstream
    }

    passed = 0
    failed = 0

    for (A, B), expected_output in test_cases.items():
        try:
            result = solution(list(A), list(B))
            if result == expected_output:
                print(f"Test Passed: input=({A[:5]}..., {B[:5]}...), output={result}")
                passed += 1
            else:
                print(f"Test Failed: input=({A[:5]}..., {B[:5]}...), expected={expected_output}, got={result}")
                failed += 1
        except Exception as e:
            print(f"Test Error: input=({A[:5]}..., {B[:5]}...), error={str(e)}")
            failed += 1

    print("\nTest Summary:")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")
    print(f"  Total:  {len(test_cases)}")


run_tests()
