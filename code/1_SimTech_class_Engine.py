# Usually I would have to import the inherited "parent" data, being the EBike class but it returns a mistake, so I put the # in front of it...
# from EBike import EBike
# and it has to be: class Engine(EBike), but that return a mistake due to unresolved references...

class Engine:
    # This is the engine for the E-Bike
    def __init__(self, DN, SS, MS):
        # Initializes the E-Bike and defines the most significant attributes
        self.Designation = DN
        self.Status = SS
        self.maxSpeed = MS
        Engine.__init__(self, DN, SS, MS)

    def use_power(self, factor):
        Charge = 100
        Charge -= 4 * factor
        return Charge

    def produce_power(self, factor2):
        # There is power generation involved in  manual driving, depending on the conditions, e.g. rolling downhill
        Charge = 50
        Charge += 0.4 * factor2
        return Charge

    def get_status(self):
        # This is the self testing function
        self.Status = True
        return print("all systems GO")
