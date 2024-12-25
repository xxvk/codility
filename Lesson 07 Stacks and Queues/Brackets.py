# English ver.
'''
A string S made up of N characters is considered properly nested if one of these conditions is met:
	1.	S is empty.
	2.	S has the form “(U)”, “[U]”, or “{U}”, where U is also a properly nested string.
	3.	S has the form “VW”, where both V and W are properly nested strings.

For example, the string “{[()()]}” is properly nested, but “([)()]” is not.

Write a function:
def solution(S):

The function should return 1 if the input string S is properly nested and 0 otherwise.

Examples:
	•	If S = "{[()()]}", the function returns 1.
	•	If S = "([)()]", the function returns 0.

Assumptions:
	•	N is an integer within the range [0..200,000].
	•	The string S contains only these characters: '(', '{', '[', ']', '}', ')'.

'''


# Japnese ver.
'''
文字列 S が N 個の文字で構成され、次のいずれかの条件を満たす場合、適切にネストされているとみなされます：
	1.	S は空の文字列です。
	2.	S の形式が “(U)”、”[U]”、または “{U}” であり、U も適切にネストされた文字列です。
	3.	S の形式が “VW” であり、V と W の両方が適切にネストされた文字列です。

例えば、文字列 “{[()()]}” は適切にネストされていますが、”([)()]” は適切ではありません。

以下の関数を作成してください：
def solution(S):

この関数は、入力文字列 S が適切にネストされている場合は 1 を返し、それ以外の場合は 0 を返します。

例：
	•	S = "{[()()]}" の場合、関数は 1 を返します。
	•	S = "([)()]" の場合、関数は 0 を返します。

前提条件：
	•	N は [0..200,000] の範囲の整数です。
	•	文字列 S は次の文字のみを含みます： '(', '{', '[', ']', '}', ')'。

'''



# Chinese ver.
'''
一個由 N 個字符組成的字串 S，在以下任一條件成立時，會被視為正確嵌套：
	1.	S 是空字串。
	2.	S 的形式為 “(U)”、”[U]” 或 “{U}”，其中 U 也是正確嵌套的字串。
	3.	S 的形式為 “VW”，其中 V 和 W 均為正確嵌套的字串。

例如，字串 “{[()()]}” 是正確嵌套的，而 “([)()]” 則不是。

請撰寫一個函式：
def solution(S):


該函式在字串 S 是正確嵌套時返回 1，否則返回 0。

範例：
	•	若 S = "{[()()]}"，函式應返回 1。
	•	若 S = "([)()]"，函式應返回 0。

假設：
	•	N 是 [0..200,000] 範圍內的整數。
	•	字串 S 僅包含以下字符： '(', '{', '[', ']', '}', ')'。
'''



def solution(S):
    # Implement your solution here
    '''
    checker:    input range, empty
    '''
    if not S:
        return 1
    N = len(S)
    if N > 200_000:
        return 0
    '''
    main process
    '''
    dic = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    setK = set(dic.keys())
    setV = set(dic.values())
    stack = []

    for char in S:
        if char in setK:
            # Push opening bracket onto the stack
            stack.append(char)
        elif char in setV:
            # Check if stack is empty or top of stack doesn't match
            if not stack or dic[stack.pop()] != char:
                return 0

    # If stack is empty, all brackets were matched
    return 1 if not stack else 0


test_cases = {
    "{[()()]}": 1,  # Properly nested
    "([)()]": 0,    # Not nested
    "": 1,          # Empty string is nested
    "()[]{}": 1,    # Nested, no nesting inside
    "(((((())))))": 1,  # Deeply nested
    "{[([({[()]})])]}": 1,  # Complex nesting
    "([)]": 0,       # Misplaced brackets
    "{{{{": 0,       # Too many opening brackets
    "}}}}": 0        # Too many closing brackets
}

test_cases.update({
    "()" * 100000: 1,  # Long alternating brackets
    "(" * 100000 + ")" * 100000: 1,  # Perfectly nested but sequential
    "(" * 100000: 0,  # All opening brackets
    ")" * 100000: 0   # All closing brackets
})

def run_tests():
    print("Running tests...\n")
    passed = 0
    failed = 0

    for input_string, expected_output in test_cases.items():
        try:
            result = solution(input_string)
            if result == expected_output:
                print(f"Test Passed: input length={len(input_string)}, output={result}")
                passed += 1
            else:
                print(f"Test Failed: input length={len(input_string)}, expected={expected_output}, got={result}")
                failed += 1
        except Exception as e:
            print(f"Test Error: input length={len(input_string)}, error={str(e)}")
            failed += 1

    print("\nTest Summary:")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")
    print(f"  Total:  {len(test_cases)}")

run_tests()

