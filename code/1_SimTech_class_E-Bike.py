class EBike:
    # This is the E-Bike class and will be the 'parent' for Battery, Engine and BikeBody

    def __init__(self, DN, CE, SS, TI):
        # Initializes the E-Bike and defines the most significant attributes
        self.Designation = DN
        self.Charge = CE
        self.Status = SS
        self.time_in_use = TI
        EBike.__init__(self, DN, CE, SS, TI)

    def get_status(self):
        # This is the self testing function
        self.Status = True
        return print("all systems GO")

    def drive_electrical(self, factor):
        Charge = self.Charge
        Charge -= 4 * factor
        return Charge

    def stop(self):
        return ("the Bike has stopped. In this mode of operation, no power is used")

    def drive_pedal(self, factor2):
        # There is even some power generation involved in the manual driving
        Charge = self.Charge
        Charge += 0.4 * factor2
        return Charge

    def get_time_in_use(self):
        # measures time and therefore the spent power
        Time = 15
        Charge = self.Charge
        return print("the bike has been used", Time, "minutes and has", Charge, "charge left")
