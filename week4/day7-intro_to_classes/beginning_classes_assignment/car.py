class Car(): 
    """This docstring will describe how to interact with the Car class. 

    This Car class will have a couple of different attributes - model, 
    color, tank_size, and gallons_of_gas. It will have one method, drive, 
    that simply adjusts the gallons_of_gas based off an inputted number
    of miles driven. 

    Parameters
    ----------
        model: str
            Holds the model of the car (Toyota, Honda, etc.). 
        color: str
        tank_size: float
    """

    def __init__(self, model, color, tank_size): 
        self.model = model 
        self.color = color
        self.tank_size = tank_size
        self.gallons_of_gas = self.tank_size # We're assuming its tank is full. 

    def drive(self, miles_driven): 
        """This will drive the car some number of miles, and adjust the 
        gallons_of_gas in the tank. 

        Args: 
            miles_driven: float 
        """

        self.gallons_of_gas -= miles_driven / 10. 
