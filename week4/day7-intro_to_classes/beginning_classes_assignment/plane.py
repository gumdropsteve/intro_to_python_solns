class Plane(): 
    """This docstring will describe the Plane class. 

    This plane class will hold three attributes that describe where
    it's flying to and from, as well as the distance of that trip. 
    It will have one method, fly, that enacts the flight. 

    Parameters
    ----------
        destination: str
        departure_city: str
        trip_distance: float
    """

    def __init__(self, destination, departure_city, trip_distance): 
        self.destination = destination 
        self.departure_city = departure_city
        self.trip_distance = trip_distance

    def fly(self): 
        """Fly the plane and adjust it's destination and departure_city. 

        We're assuming that this plane only flies one flight path - to 
        and from the destination and departure_city. Therefore, when it
        completes a flight, the departure_city and the destination simply
        switch places, and then it flies back to where it came from. 
        """

        self.departure_city, self.destination = self.destination, self.departure_city
