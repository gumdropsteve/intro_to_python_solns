from collections import deque

class RPNCalculator():
    '''A reversed polish notation calculator'''
    def __init__(self):                             # Note: NEVER pass a mutable object as default
        self.equation = []                          # value; i.e. `def my_funct(param1, param2=[]):`
        self._stack = deque()                       # For more, read http://docs.python-guide.org/en/latest/writing/gotchas/
        self._valid_operators = {'+', '-', '/', '*', '^', '**'}

    def add(self):                                  # Note: this is not a magic method b/c a
        operand2 = self._stack.pop()                # magic method is not needed. __add__() tells
        operand1 = self._stack.pop()                # the python interpreter how to add (using '+')
        self._stack.append(operand1 + operand2)     # an object of this class (i.e., a calculator
                                                    # object) to other objects. However, here in
    def subtract(self):                             # this function, we want add together two ints
        operand2 = self._stack.pop()
        operand1 = self._stack.pop()
        self._stack.append(operand1 - operand2)

    def multiply(self):
        operand2 = self._stack.pop()
        operand1 = self._stack.pop()
        self._stack.append(operand1 * operand2)

    def divide(self):
        operand2 = self._stack.pop()
        operand1 = self._stack.pop()
        self._stack.append(operand1 / operand2)

    def power(self):
        operand2 = self._stack.pop()
        operand1 = self._stack.pop()
        self._stack.append(operand1 ** operand2)

    def perform_operation(self, operator):
        if operator == '+':
            self.add()
        elif operator == '-':
            self.subtract()
        elif operator == '*':
            self.multiply()
        elif operator == '/':
            self.divide()
        elif operator == '^' or operator == '**':
            self.power()

    def _check_valid_operator(self, operator):      # Note: leading underscore hides method,
        if operator in self._valid_operators:       # or attribute, from user after object
            return True                             # instantiation.
        else:                                       # In python, the underscore has many
            return False                            # special uses.
                                                    # For more, read https://hackernoon.com/understanding-the-underscore-of-python-309d1a029edc
    def _check_stack_length(self):
        if len(self._stack) < 2:
            return False
        else:
            return True

    def _print_error(self, error=''):
        '''Raise standard error message.'''
        raise ValueError(f'Invalid input(s). {error}')

    def calc_stack(self):
        self._stack = deque()
        for element in self.equation:
            if element.isdigit():
                self._stack.append(float(element))
            elif self._check_valid_operator(element):
                if self._check_stack_length():
                    self.perform_operation(element)
                else:
                    self._print_error('Imbalanced number of operators/operands.')
            else:
                error = f"'{element}' is not recognized"
                self._print_error(error=error)
        if len(self._stack) > 1:
            self._print_error('Imbalanced number of operators/operands.')
        elif len(self._stack) == 1:
            return round(self._stack.pop(), 2)

    def __call__(self, equation):  # the __call__() magic method makes an object of this class callable
        '''
        Run reverse polish notation calculator.

        Inputs:
            equation: STR - equation for computation where each operator
                      and operand are seperated by a single space

        Example:
        >>> stack = '2 3 +'
        >>> calc = RPNCalculator()
        >>> calc(stack)
        5.0

        Example:
        >>> calc = RPNCalculator()
        >>> calc('1 2 -')
        -1.0
        '''
        self.equation = equation.strip().split()
        return self.calc_stack()


if __name__ == '__main__':
    calc = RPNCalculator()

    print("calc('2 3 +') = 5.0")
    print(calc('2 3 +'))

    print("\ncalc('15 7 1 1 + − / 3 * 2 1 1 + + −') = 5.0")
    print(calc('15 7 1 1 + - / 3 * 2 1 1 + + -'))
