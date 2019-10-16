import math
import operator
from collections import deque, namedtuple

class RPNCalculator():
    '''
    Reverse Polish Notation Calculator
    ----------------------------------
    Uses the deque class to keep track of operations/values
    to be evaluated in a LIFO manner.
    '''
    def __init__(self):
        OperatorPlus = namedtuple('OperatorPlus', ['operator', 'n_args'])
        self._operators = {'+'   :  OperatorPlus(operator.add, 2),
                           '-'   :  OperatorPlus(operator.sub, 2),
                           '*'   :  OperatorPlus(operator.mul, 2),
                           '/'   :  OperatorPlus(operator.truediv, 2),
                           '^'   :  OperatorPlus(operator.pow, 2),
                           'sin' :  OperatorPlus(math.sin, 1),
                           'tan' :  OperatorPlus(math.tan, 1),
                           'cos' :  OperatorPlus(math.cos, 1),
                           'sqrt':  OperatorPlus(math.sqrt, 1)}
        self._stack = deque()

    @property
    def stack_to_evaluate(self):
        return self.stack_length > 1

    @property
    def stack_length(self):
        return len(self._stack)

    def run(self):
        '''
        Starts running the calculator. Accepts operation, or list separated
        by spaces with <CR> until asked to execute the operations on the stack
        by entering nothing.

        Will evaluate until no operations are left on the stack and display
        the current state of the stack.

        Enter q to quit
        Enter c to clear stack
        Enter s to display stack
        '''
        while True:
            elements = input('Operation(s)/Value(s): ').split()
            if not elements:
                self._evaluate_stack()
                if not self.stack_to_evaluate:
                    self._print_stack()
            elif elements[0] == 'q':
                break
            elif elements[0] == 's':
                self._print_stack()
            elif elements[0] == 'c':
                self._stack.clear()
            elif self.elements_known(elements):
                self._approve_push_elements(elements)
            else:
                self._print_error()

    def _evaluate_stack(self):
        '''
        Method that steps through the current stack and
        transforms it into the simplest form it can.
        '''
        def evaluate_operation(op):
            '''
            Input:  OperatorPlus
            Helper function with logic to correctly evaluate next operation.
            '''
            ordered_args_for_op = reversed([new_stack.pop() for _ in range(op.n_args)])
            new_stack.append(op.operator(*ordered_args_for_op))

        new_stack = deque()
        for element in self._stack:
            if isinstance(element, float):
                new_stack.append(element)
            else:
                evaluate_operation(self._operators[element])
        self._stack = new_stack

    def elements_known(self, elements):
        '''
        Helper function to test if all elements entered by user are valid.
        '''
        for element in elements:
            if not (element.isdigit() or (element in self._operators)):
                return False
        return True

    def _approve_push_elements(self, elements):
        '''
        Input:  List
        Output: None

        Checks elements one at a time to make sure that if they were added to the
        stack, operations could be performed legally.
        '''
        approved_elements = []
        for i, element in enumerate(elements):
            if not element.isdigit():
                temp_op = self._operators[element]
                if temp_op.n_args > i + self.stack_length:
                    self._print_error()
                    return
                temp_element = element
            else:
                temp_element = float(element)
            approved_elements.append(temp_element)

        self._stack.extend(approved_elements)

    def _print_stack(self):
        '''
        Prints the state of the stack in a kinda pretty way...
        '''
        stack_state = ', '.join(str(elem) for elem in self._stack) if self._stack else 'empty'
        print('Stack: {}'.format(stack_state))

    def _print_error(self):
        '''
        Prints standard error message.
        '''
        print('You entered invalid operation(s)/value(s).')

if __name__ == '__main__':
    rpn = RPNCalculator().run()
