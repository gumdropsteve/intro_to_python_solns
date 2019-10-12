class TipOutTracker():
    '''
    Class to keep track of bills and their corresponding tips.
    Designed to make tipping out at the end of a night easier.
    '''

    def __init__(self, tip_rate=0.18, bills_n_tips=None):
        '''
        Input:  Float - default tip rate for restaurant
                List - Existing bills and tips, optional
        '''
        self.bills_n_tips = bills_n_tips if bills_n_tips else []
        self.tip_rate = tip_rate

    def __len__(self):
        '''
        Returns total number of bills served, known to TipOutTracker.
        '''
        return len(self.bills_n_tips)

    def __add__(self, other):
        '''
        Adds two TipOutTrackers together. Returns a new TipOutTracker
        instance with bills_n_tips from the other two.
        '''
        combined_bills_n_tips = self.bills_n_tips + other.bills_n_tips
        larger_tip_rate = max(self.tip_rate, other.tip_rate)
        return TipOutTracker(larger_tip_rate, combined_bills_n_tips)

    def add_bill(self, bill_total, tip_rate=None):
        '''
        Input:  Float, Float

        If no tip rate is given, the default tip rate is assumed.
        '''
        bill_tip_rate = tip_rate if tip_rate else self.tip_rate
        self.bills_n_tips.append((bill_total, bill_tip_rate))

    def total_tip_out(self):
        '''
        Returns total amount of tips from all bills served.
        '''
        return sum(bill * tip for bill, tip in self.bills_n_tips)


if __name__ == '__main__':
    tot = TipOutTracker(0.18)
    tot.add_bill(58.90, 0.15)
    tot.add_bill(31.58)
    print(tot.total_tip_out())
    tot.add_bill(81.44, 0.20)
    print(len(tot))

    tot2 = TipOutTracker(0.2)
    tot2.add_bill(106.34)

    tot3 = tot + tot2
    print(tot3.total_tip_out())
