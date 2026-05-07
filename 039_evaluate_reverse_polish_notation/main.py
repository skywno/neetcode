from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['*', '+', '-', '/']

        def op(prior, latter, operator):
            if operator == '+':
                return int(prior) + int(latter)
            if operator == '-':
                return int(prior) - int(latter)
            if operator == '*':
                return int(prior) * int(latter)
            if operator == "/":
                return int(prior) / int(latter)

        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                operator = token
                latter, prior = stack.pop(), stack.pop()
                result = op(prior, latter, operator)
                stack.append(result) 
        res = stack.pop()      
        return int(res)s