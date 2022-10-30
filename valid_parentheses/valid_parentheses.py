class ValidParentheses:
    def valid_parenthesis(s):
        mapp = {'(': ')', '[': ']', '{': '}'}
        queue = []
        for paren in s:
            if len(queue) == 0:
                queue.append(paren)
            else:
                last_ele = queue[-1]
                if mapp[last_ele] == paren:
                    queue.pop()
        return not len(queue)
