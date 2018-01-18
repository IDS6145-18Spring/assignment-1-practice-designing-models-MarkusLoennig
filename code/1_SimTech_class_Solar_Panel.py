

class SolarPanel:
    # This is the power generating element

    def __init__(self, SA, DN, PC, SS, AH):
        self.SurfaceArea = SA
        self.Designation = DN
        self.PowerCapacity = PC
        self.Status = SS
        self.AngleHorizontal = AH
        SolarPanel.__init__(self, SA, DN, PC, SS, AH)

    def produce_power(self, PC):
        # The function produces the electrical power
        environmental_factor = 0.8
        power = PC * environmental_factor
        return power

    def get_best_angle(self):
        # The function raises the solar panels to get better sun-reception
        best_angle = 15
        self.AngleHorizontal = 12
        if self.AngleHorizontal < best_angle:
            print("The angle towards the sun is too low.")
        elif self.AngleHorizontal > best_angle:
            print("the angle is too high")
        else:
            print("The angle is optimal")

    def get_status(self):
        # This is the self testing function
        self.Status = True
        return print("all systems GO")

    def get_warm(self):
        # This will engage to melt snow
        SurfaceArea_temperature = 0
        SurfaceArea_temperature += 5
        return 5
