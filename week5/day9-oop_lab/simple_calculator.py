import math
import operator
from collections import deque, namedtuple

class RPNCalculator():
    '''
    Reverse Polish Notation Calculator
    ----------------------------------
    Uses the deque class to keep track of operations/values to be evaluated
    in a LIFO manner.
    '''
    def __init__(self):
        OperatorPlus = namedtuple('OperatorPlus', ['operator', 'n_args'])
        self._operators = {'+'   :  OperatorPlus(operator.add, 2),
                           '-'   :  OperatorPlus(operator.sub, 2),
                           '*'   :  OperatorPlus(operator.mul, 2),
                           '/'   :  OperatorPlus(operator.truediv, 2),
                           '^'   :  OperatorPlus(operator.pow, 2),
                           '**'  :  OperatorPlus(operator.pow, 2),
                           'sin' :  OperatorPlus(math.sin, 1),
                           'tan' :  OperatorPlus(math.tan, 1),
                           'cos' :  OperatorPlus(math.cos, 1),
                           'sqrt':  OperatorPlus(math.sqrt, 1)}
        self._stack = deque()

    def run(self, operation):
        '''
        Runs computation on operation.

        Parameters
        ----------
        operation: STR - string of operations for evaluation with each element
            seperated by a space

        >>> rpn.run('3 4 + 4 -')
        3.0
        >>> rpn.run('15 7 1 1 + - / 3 * 2 1 1 + + -')
        5.0
        '''
        self._stack = deque()
        for element in operation.split():
            if element.isdigit():
                self._stack.append(float(element))
            elif element in self._operators:
                self._evaluate_stack(self._operators[element])
            else:
                self._print_error(f'Does not recognize \'{element}\'.')
        if len(self._stack) == 1:
            print (self._stack.pop())
        else:
            self._print_error('Imbalanced number of operators and operands.')

    def _evaluate_stack(self, op):
        '''Evaluates stack given a specific OperatorPlus (op).'''
        if len(self._stack) < op.n_args:
            self._print_error('Not enough operands to support operator.')
        args_for_operation = reversed([self._stack.pop() for _ in range(op.n_args)])
        self._stack.append(op.operator(*args_for_operation))

    def _print_error(self, error=''):
        '''Raise standard error message.'''
        raise ValueError(f'You entered invalid operation(s)/values(s). {error}')
