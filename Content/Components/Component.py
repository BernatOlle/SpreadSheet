##POSTFIXEVALUATOR
from Content.Components.Operand.Cell_Range import Cell_Range
from .Operator import Operator
from Content.Components.Operand.Number import Number
from Content.Components.Operand.Function.SUM_Function import SUM_Function
from Content.Components.Operand.Function.Min_Function import MinOperand
from Content.Components.Operand.Function.Max_Function import MaxOperand
from Content.Components.Operand.Function.Promedio_Function import PromedioOperand

class Component():
    
    def __init__(self, operations, formulaComputing, spreadsheet) -> None:
        self.operators = ["+","-","*","/"]
        self.functions = ["MAX", "MIN", "SUMA", "PROMEDIO"]
        self.postfix = formulaComputing.computeFormula(operations)
        self.spreadsheet = spreadsheet
        self.iDependOn = []
    def calculateFormulaValue(self):
        stack = []
        args = []
        
        i = 0
        for token in self.postfix:

            if token in self.operators:
                operand = [stack[len(stack)-2], stack[len(stack)-1]]
                res = self.calculate(operand, token)
                stack.pop()
                stack.pop()
                stack.append(res)
            else:
                if token == ":":
                    
                    rangecells = Cell_Range(self.postfix[i-2], self.postfix[i-1], self.spreadsheet)
                    stack.pop()
                    stack.pop()
                    stack.append(rangecells)
                    if len(args) == 0:
                        args.append(rangecells)
                    
                    self.iDependOn.extend(rangecells.getCells())
                
                
                elif token == ";":
                    if len(args) == 0:
                        
                        args.append(stack[len(stack)-1])
                        args.append(stack[len(stack)-2])
                        stack.pop()
                        stack.pop()
                    else:
                        args.append(stack[len(stack)-1])
                        stack.pop()


                elif token in self.functions:
                    new_args = []
                    supply = []
                    if self.postfix[i-1] == ":":
                        new_args = stack.pop()
                        supply = args
                        args = []
                        args.append(new_args)
              
              
                    if token == "MIN":
                        min = MinOperand(args)
                        stack.append(Number(min.getValue()))

                    elif token == "MAX":
                        max = MaxOperand(args)
                        stack.append(Number(max.getValue()))

                    elif token == "PROMEDIO":
                        promedio = PromedioOperand(args)
                        stack.append(Number(promedio.getValue()))

                    elif token == "SUMA":
                        suma = SUM_Function(args)
                        stack.append(Number(suma.getValue()))
                                                
                    args = supply
                elif token.isdigit():
                    num = Number(token)
                    stack.append(num)
                    
                else:
                    
                    #CAS ESPECIAL CELLREFERENCE
                    
                        
                        
                    cell_value = Cell_Range(token, token, self.spreadsheet)
                    self.iDependOn.extend(cell_value.getCells())
                    stack.append(cell_value)
                
                        
       
            i+=1
        
        return stack[0].getValue()         
                    
    def calculate(self, operands, operator):
            first_value = operands[0].getValue()
            second_value = operands[1].getValue()
            
            if(operands[0].isType() == "Cell_Range"):
                first_value = operands[0].getValue()[0]
            if(operands[1].isType() == "Cell_Range"):
                second_value = operands[1].getValue()[0]
                
            return Number(Operator(operator).execute(first_value, second_value))


    def dependingCells(self):
        return self.iDependOn