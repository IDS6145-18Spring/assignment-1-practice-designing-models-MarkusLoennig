class Lighting:
    # This is the Lighting class and will inherit to "Communication", "Lights" and "Sensors"

    def __init__(self, DN, SS, AL, HT):
        # Initializes the E-Bike and defines the most significant attributes
        self.Designation = DN
        self.Status = SS
        self.Area_ofLight = AL
        self.Height = HT
        Lighting.__init__(self, DN, SS, AL, HT)

    def control_lights(self):
        # This is the function that will use the communication and sensors data and turn on/off the lights
        d = 1+4
        return print("The lights are on")

    def get_status(self):
        # This is the self test function
        self.Status = True
        return print("all systems GO")

