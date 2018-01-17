## Smart City (MASTER Lighting System) Simulation

The best suited category of simulation is the "discrete-event based simulation". 
My goal is to verify that the proposed system can be self sufficient, which is dependant on:

1. the amount of electricity generated and 

2. the storage capacity of the overal battery system (Bikestands and E-Bikes (when inserted))

3. the average use of electricity by the Lighting system and

4. the average use of the E-Bikes. 

All of those variables are dependant on environmental conditions (winter has less sunshine and usually also less Bike users but longer dark hours).

Discrete-event based simulation produces a system which changes its behavior only in response to specific events (e.g. removal or retrun of E-Bike) and typically models changes to a system resulting from a finite number of events distributed over time (e.g. sunshine, darkness). Examples for discrete-event based simulation includes airports, your line at Starbucks, queues, board games. This directly translates into my proposed system, since change in electrical charge/capacity is implemented by inside (Production of solar power, use of Lighting) and outside (renting E-Bikes, no sunshine) events. 


The simulation would (roughly) be conducted like this:
Starting point is a certain amount of electrical charge in the Bikestand and E-Bikes. 
Input will be dependant on the external environment (tbd), like the seasons. 
--> In sunny weather (summer), there will be higher average amount of E-Bike users, therefore potentially lesser power stored at the beginning of the dark hours/Lighting system. The overall production of electricity was high. The use of power during the night was not intense, due to the shorter night span.
--> in winter time, there is possible snow and dark hours, even during day, so there will be lesser solar power produced. On the other hand, the use of E-Bikes will be severly diminished, therefore the stored electricity will potentially be only used to power the Lighting. 

The inputs will be: 

- sunshine leading to production of solar energy, charging the system
- usage of E-Bikes, therefore partly depleting the stored electricity
- usage of Lighting

all will be depending on the season/weather to be simulated

Outputs will be:

- production of energy (enough?, too much?)
- storage capacity (enough for the energy produced?)

The outputs will help determine what system/class needs to be adapted in size (e.g. larger solar panels, more Bikestands) and/or if the proposed MASTER Lighting System can be indeed self sufficient. 

(remove: Define what category  (or combination of categories) of simulation needed to solve this problem.)

(remove: Why did you choose this simulation type?)

(remove: Roughly, how would you conduct the simulation to produce the results from your specification?)

(remove: images say 1000 words for you...)
