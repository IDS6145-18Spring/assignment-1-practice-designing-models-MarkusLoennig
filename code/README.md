## Smart City MASTER City Lighting Model

Each file is a class which is defining the attributes/variables and the functions. In this case, the functions are basically empty.

[Code for class E-Bike](1_SimTech_class_E-Bike.py)   --- This defines the E-Bike in broad terms with the most mportant attributes (electrical charge) and the respective functions.


[Code for class Lighting](1_SimTech_class_Lighting.py)   --- This defines the Lighting as the parent system, it still has 3 classes which inherite attributes from Lighting. Its a very basic class since the main effort to simulate later is within the Solar/E-Bike connection.  


[Code for class Engine](1_SimTech_class_Engine.py)   --- It is the electricity user/potential generator part from the E-Bike.


[Code for class Solar Panal](1_SimTech_class_Solar_Panel.py)   --- This will be of of the classes which after the simulation might need adaptation in size/generatig power. It is the first step in the system.
