class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        for i in s:
            if i in ['(', '{', '[']:
                lst.append(i)
            else:
                if len(lst) == 0:
                    return False
                top = lst.pop()
                if i ==')' and top != "(":
                    return False
                if i=='}' and top != '{':
                    return False
                if i==']' and top != '[':
                    return False
        if len(lst) == 0:
            return True
        else:
            return False