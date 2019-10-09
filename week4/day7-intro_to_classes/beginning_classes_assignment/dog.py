class Dog(): 
    """This docstring will discuss how to interact with our Dog class. 

    Our Dog class will have two attributes - a name and happiness_level. 
    It's one method, wag_tail, will simulate the dog wagging it's tail 
    some number of times, and increasing it's happiness level. 

    Parameters: 
    -----------
        name: str
        happiness_level: int
    """

    def __init__(self, name, happiness_level=5): 
        self.name = name
        self.happiness_level = happiness_level

    def wag_tail(self, n): 
        """Wags the dogs tail n times, each time increase happiness level by 5. 

        Args: 
            n: int
        """

        for _ in range(n): 
            self.happiness_level += 5
