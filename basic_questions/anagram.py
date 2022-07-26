# verilen 2 kelimenin anagram olup olmadığının kontrolünün yapılması

first_text = "ABC 1BC"
second_text = "BCD ABC"


def solution(firstText, secondText):
    s1 = "".join(text.lower() for text in firstText if text.isalpha())
    s2 = "".join(text.lower() for text in secondText if text.isalpha())
    print(sorted(s1), sorted(s2))
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False


print(solution(first_text, second_text))
