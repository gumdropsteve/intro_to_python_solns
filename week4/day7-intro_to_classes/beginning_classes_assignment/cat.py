class Cat():
    """This docstring will discuss how to interact with our Cat class.

    Our Cat class will have three attributes - a name, laziness level,
    and a location. It's one method, sense_earthquake, will change
    the cats location based on whether or not there is an earthquake.

    Parameters
    ----------
        name: str
        laziness_level: int
            This holds how lazy the cat is on a scale of 1 to 10.
        location: str
            This holds where the cat is currently located at.
    """

    def __init__(self, name, laziness_level, location):
        self.name = name
        self.laziness_level = laziness_level
        self.location = location

    def sense_earthquake(self, earthquake):
        """Checks if the cat senses and earthquake, and if so changes the cat's
        location to 'gone dark'.

        Args:
            earthquake: boolean
                Holds a True or False as to whether there was an earthquake.
        """

        if earthquake:
            self.location = "Gone dark"
            print("{} has gone dark!".format(self.name))
        else:
            print("{} is at {}".format(self.name, self.location))
