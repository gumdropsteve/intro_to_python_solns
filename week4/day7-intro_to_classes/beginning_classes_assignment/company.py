class Company(): 
    """This docstring will describe how to interact with the Company class. 

    The company class will have attributes that are standard to a company, 
    and methods that interact with a couple of those attributes. 

    Parameters
    ----------
        name: str
            Holds the company name. 
        industry_type: str
            Holds what industry the company belongs to. 
        num_employees: int
        total_revenue - float
    """

    def __init__(self, name, industry_type, num_employees, total_revenue): 
        self.name = name
        self.industry_type = industry_type
        self.num_employees = num_employees
        self.total_revenue = total_revenue

    def serve_customer(self, cost): 
        """Adjusts the company's total_revenue by the cost required 
        to serve a customer. 

        Args: 
            cost: float
        """

        self.total_revenue += cost 

    def gain_employees(self, new_employee_lst): 
        """Adjusts the company's num_employees to account for new employees. 

        Args: 
            new_employee_lst: list 
        """

        self.num_employees += len(new_employee_lst)
