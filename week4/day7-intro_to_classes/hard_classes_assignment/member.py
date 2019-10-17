class Member(): 
    """This docstring will discuss how to interact with the Member class.

    This Member class will be used to model a member/student of a classroom. 
    As such, it will have attributes that a person typically has, and methods
    that relate to actions of a member/student of a classroom. 

    Parameters
    ----------
    name: str
        Holds the name of the Member.
    hair_color: str
        Holds the hair color of the Member.
    birthdate: str
        Holds the birthdate of the Member. 
    questions_asked: list
        Holds any questions asked by that Member during the class.
    lines_of_code: list
        Holds a list of the lines of code written by that Member. 
    num_lines_coded: int
        Holds the number of lines of code written by the Member. 
    coding_level: str
        Holds the coding level of the Member, based on how many total lines
        of code that they have written.
    """

    def __init__(self, name, hair_color, birthdate): 
        self.name = name
        self.hair_color = hair_color 
        self.birthdate = birthdate
        self.questions_asked = []
        self.lines_of_code = []
        self.num_lines_coded = 0
        self.coding_level = 'beginner'
    
    def get_coding_level(self): 
        """Checks the Members num_lines_coded to get their coding level."""
        if self.num_lines_coded <= 100: 
            self.coding_level = 'beginner'
        elif self.num_lines_coded <= 1000: 
            self.coding_level = 'novice'
        elif self.num_lines_coded <= 10000: 
            self.coding_level = 'intermediate'
        else: 
            self.coding_level = 'master'

        return self.coding_level

    def add_question_asked(self, question): 
        """Adds an asked question to the questions_asked attribute."""
        self.questions_asked.append(question)

    def add_coded_line(self, line_of_code): 
        """Adds a coded line to the lines_of_code attribute. 

        This will first add a coded line to the lines_of_code attribute, 
        and then increment the num_lines_coded attribute. Finally, it 
        will check the total num_lines_coded to see if the Members coding
        level needs to be updated/changed. 
        """
        self.lines_of_code.append(line_of_code)
        self.num_lines_coded += 1
        self.get_coding_level()
