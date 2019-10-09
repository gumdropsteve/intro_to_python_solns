class Television():

    def __init__(self, brand, on_status=False,
            current_channel=0, life_perc=100.0):
        self.brand = brand
        self.on_status = on_status
        self.current_channel = current_channel
        self.life_perc = life_perc

    def hit_power(self):
        """Switches the television either on or off. """

        # This simply switches the self.on_status to the
        # opposite of what it currently is (True to False, and
        # vice versa).
        self.on_status = not self.on_status

        if not self.on_status:
            self.current_channel = 0
            self.life_perc -= 0.01

    def change_channel(self, channel_num):
        """Change the channel of the television to the inputted channel.

        Args:
            channel_num: int
        """

        if self.on_status:
            self.current_channel = channel_num
        else:
            print('Television is not on!')
