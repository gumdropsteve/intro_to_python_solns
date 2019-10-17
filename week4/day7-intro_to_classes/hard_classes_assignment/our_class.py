from collections import Counter 

class OurClass(): 
    """This docstring describes how to interact with OurClass

    This is a class designed to mimic a classroom. Along those lines, 
    it will have attributes that many classrooms have, along with methods
    that will mimic the actions/events that occur in many classrooms.

    Parameters: 
    -----------
    name: str 
        Holds the name of the class. 
    location:  str
        Holds the location of the class. 
    size - int 
        Holds the size of the class. Defaults to 0
    members - list
        Holds the members in the class. Defaults to empty, and otherwise
        should hold Member objects. 
    at_capacity - bool
        Keeps track of whether or not the class is at capacity. 
    """

    def __init__(self, name, location, size=0, members=None, instructors=None): 
        self.name = name
        self.location = location
        self.members = [] if not members else members 
        self.size = len(members)
        self.at_capacity = self.check_if_at_capacity()
        self.instructors = [] if not instructors else instructors

    def check_if_at_capacity(self): 
        """Check if the class size is greater than 30. 

        Return a true if the class size is greater than 30, 
        and a false otherwise. 
        """

        return True if self.size >= 31 else False

    def add_class_members(self, member): 
        """Try to add member to class. If class is at capacity, alert user and do nothing.

        Args: 
            member: Member object
        """
        if self.at_capacity:
            print('The class is full.')
        else:
            self.members.append(member)

    def get_num_questions_asked(self): 
        """Calculate the total number of questions asked across all members.""" 
        
        num_questions_asked = 0
        for member in self.members: 
            num_questions_asked += len(member.questions_asked)

        return num_questions_asked

        '''This would work the same way, just written in one line: 

        return sum(len(member.questions_asked) for member in self.members)

        '''

    def get_num_questions_answered(self): 
        """Calculate the total number of questions asked across all instructors."""

        num_questions_answered = 0
        for instructor in self.instructors: 
            num_questions_answered += len(instructor.questions_answered)
        
        return num_questions_answered

        '''This would work the same way, just written in one line: 

        return sum(len(instructor.questions_answered) for instructor in 
            self.instructors)

        '''

    def get_num_lines_code(self): 
        """Calculate the total number of coded lines across all members."""

        coded_lines = 0
        for member in self.members: 
            coded_lines += member.num_lines_coded

        return coded_lines

        '''This would work the same way, just written in one line: 

        return sum(member.num_lines_coded for member in self.members)

        '''
    
    def check_outstanding_questions(self): 
        """See if there are any outstanding questions not answered"""

        return True if self.get_num_questions_answered() == \
                self.get_num_questions_asked() else False

if __name__ == '__main__':
    oc = OurClass('thing', 'stuff')
    print('full', oc.at_capacity)
