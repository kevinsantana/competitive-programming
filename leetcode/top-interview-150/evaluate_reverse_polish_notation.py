"""
https://leetcode.com/problems/evaluate-reverse-polish-notation
"""

from typing import List

import ipdb

# does not work
# keeping track of the tokens while iterating over them is not a good idea
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #ipdb.set_trace()
        operators = {"+", "-", "*", "/"}

        for elem in tokens:
            tmp = []
            pointer = tokens.index(elem)

            if elem in operators:
                op_1 = int(tokens[pointer - 2])
                op_2 = int(tokens[pointer - 1])
                operator = tokens[pointer]
                from_opr_i = tokens[:pointer]
                del tokens[pointer - 2 : pointer + 1]

                if operator == "+":
                    res = op_1 + op_2
                elif operator == "-":
                    res = op_1 - op_2
                elif operator == "*":
                    res = op_1 * op_2
                elif operator == "/":
                    res = op_1 // op_2

                if len(from_opr_i) <= 2:
                    tokens.insert(0, res)
                else:
                    tokens.insert(pointer - 2, res)

                if len(tokens) <= 1:
                    break
                
                tmp = tokens[:]
                tokens.clear()
                tokens.extend(tmp)

        return tokens


if __name__ == "__main__":
    solve = Solution()
    tokens = ["2", "1", "+", "3", "*"]
    print(solve.evalRPN(tokens))
