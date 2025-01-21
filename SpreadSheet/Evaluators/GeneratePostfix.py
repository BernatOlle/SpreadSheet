
class GeneratePostfix:
    def __init__(self):
        self.precedence = {'+': 2, '-': 2, '*': 3, '/': 3, "PROMEDIO":10, "SUMA":10, "MAX":10, "MIN":10, ":":10, ";":1}
        
    def generatePostfix(self, tokens):
        stack = []
        postfix = []
        i = 0
        for i in range(len(tokens)):
            if self.precedence.get(tokens[i], False):
                if len(stack) == 0:
                    stack.append(tokens[i])
                    
                elif self.precedence.get(stack[len(stack)-1], False) < self.precedence.get(tokens[i], False):
                    stack.append(tokens[i])
                
                else:
                    while len(stack) > 0 and self.precedence.get(stack[len(stack)-1], False) >= self.precedence.get(tokens[i], False):
                        last = stack[len(stack)-1]
                        postfix.append(last)
                        stack.pop()
        
                    stack.append(tokens[i])
            
                
         
            elif tokens[i] == "(":
                stack.append(tokens[i])
                
            
            elif tokens[i] == ")":
                while len(stack) > 0 and self.precedence.get(stack[len(stack)-1], False) >= self.precedence.get(tokens[i], False):
                    last = stack[len(stack)-1]
                    if last != "(":
                        postfix.append(last)
                        stack.pop()
                    else:   
                        stack.pop()
                        break
            
            else:
                postfix.append(tokens[i])
        
        if len(stack)!=0:
            sorted_stack = sorted(stack, key=lambda x: self.precedence[x], reverse=True)

        postfix = postfix + sorted_stack
          
                
                        
                        
        return postfix
        
 