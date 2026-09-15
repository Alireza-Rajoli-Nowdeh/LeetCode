# in this code we learn how to use .pop()/ .append()/ stack only ever holds numbers. / Using int() to convert a string to a number & converting float to integer

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        for i in range(len(tokens)):
            if tokens[i] in ['+', '-','*','/']:
                first = stack.pop()
                second = stack.pop()
                if tokens[i] == "+":
                    Final = second + first
                if tokens[i] == "-":
                    Final = second - first
                if tokens[i] == "*":
                    Final = second * first
                if tokens[i] == "/":
                    Final = int(second / first)
                stack.append(Final)
            else:
                stack.append(int(tokens[i]))
        return stack[0]
