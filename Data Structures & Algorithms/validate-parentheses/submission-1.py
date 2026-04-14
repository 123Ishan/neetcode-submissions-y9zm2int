class Solution:
    def isValid(self, s: str) -> bool:
        dic = []
        for i in s:
            if i in ['(', '{', '[']:
                dic.append(i)
            else:
                if len(dic) == 0:
                    return False
                top_Stack = dic.pop()
                if i ==')' and top_Stack!= "(":
                    return False
                if i=='}' and top_Stack != '{':
                    return False
                if i==']' and top_Stack != '[':
                    return False
        if len(dic) == 0:
            return True
        else:
            return False