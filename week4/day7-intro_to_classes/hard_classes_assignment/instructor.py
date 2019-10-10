class Instructor(): 
    """This docstring will discuss how to work with the instructor class. 

    This class will try to mimic an Instructor of a class, and will be 
    built to theoretically interact with the OurClass class that has been 
    created in the our_class.py file in this directory. 

    Parameters
    ----------
    name: str
        Holds the name of the Instructor. 
    questions_answered: list
        Holds a list of strings for all of the questions answers that the 
        Instructor has given. 
    """

    def __init__(self, name): 
        self.name = name
        self.questions_answered=[]

    def add_question_answered(self, question): 
        """Add a question answered to the questions_answered attribute."""
        self.questions_answered.append(question)
    
