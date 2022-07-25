# Palindrom, tersten okunuşu da aynı olan cümle, sözcük ve sayılara denilmektedir.


def is_palindrome(str):
    return str == s[::-1]


s = "98778855231222213255887789"
# s = "nebedenimazaminedeben"
print("Yes" if is_palindrome(s) else "No")
