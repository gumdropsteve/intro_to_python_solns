class ToDoList():
    '''
    Simple class to keep track of a to-do list.
    '''
    def __init__(self):
        '''
        Always initializes empty to-do list. I wish my life was like this...
        '''
        self.todo = []
        self.completed = []

    def __str__(self):
        '''
        Prints to-do list items with numbers next to them. Makes for easier
        referencing when user wants to remove an item.
        '''
        pretty_todo_list = ''
        for i, item in enumerate(self.todo, 1):
            pretty_todo_list += '{}. {} - Priority {}\n'.format(i, item[0], item[1])
        return pretty_todo_list

    def add_item(self, item, priority=2):
        '''
        Input:  Str - to-do item, Int - how much you "have" to do it
        '''
        self.todo.append((item, priority))

    def mark_completed(self, number):
        '''
        Input:  Int - number of item to be removed as referenced by printed
                      version of the to-do list.
        '''
        removed_item = self.todo.pop(number - 1)
        self.completed.append(removed_item)

if __name__ == '__main__':
    tdl = ToDoList()
    tdl.add_item('Do laundry', 1)
    tdl.add_item('Get groceries', 3)
    tdl.add_item('Think about Python')
    print(tdl)
    tdl.mark_completed(2)
    print(tdl.completed)
    print(tdl)
