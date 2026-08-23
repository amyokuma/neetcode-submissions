class Solution:
    def isValid(self, s: str) -> bool:
        #initialize stack
        #map (){}[]

        #iterate through s
        #if char is ({[ apppend to stack
        #if last char in stack doesnt match return false
        #pop stack

        #return stack length == 0

        stack = []
        matching = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for char in s:
            if char in "({[":
                stack.append(char)

            else:
                if not stack or stack[-1] != matching[char]:
                    return False

                stack.pop()

        return len(stack) == 0