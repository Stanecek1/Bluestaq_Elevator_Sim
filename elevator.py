class Elevator:
    def __init__(self):
        self.floors = ['B2', 'B1', 'L', '2', '3', '4', '5', '6']
        self.destinations = []
        self.current_floor = 'L'
        self.shut_down = False
        self.direction = 'Up'

    # function that is used to determine the next stop
    def determine_next_stop(self):
        current_floor_index = self.get_floor_index(self.current_floor)
        next_destination = None
        no_down = False
        no_up = False

        # this is used to check in both directions
        while(no_down is False or no_up is False):
            # find the closest destination above the current floor
            if (self.direction == 'Up'):
                destinations_above_current_floor = []
                # loop through the destinations and determine which, if any are above the current floor
                for i in self.destinations:
                    destination_index = self.get_floor_index(i)
                    if destination_index > current_floor_index:
                        destinations_above_current_floor.append(destination_index)
                #if there are destinations above the current floor determin which one is the closest
                if (len(destinations_above_current_floor) > 0):

                    #if there is only 1 destination above the current floor, that is the next destination
                    if (len(destinations_above_current_floor) == 1):
                        next_destination = destinations_above_current_floor[0]
                    #else loop thourgh each destination to find the closest one
                    else:
                        distance = 999999999
                        for x in destinations_above_current_floor:
                            if (x - current_floor_index < distance):
                                next_destination = x
                                distance = x - current_floor_index
                if( next_destination is not None):
                    return next_destination
                else:
                    # print('no destinations above current floor, switching directions')
                    no_up = True
                    self.direction = 'Down'

            if (self.direction == 'Down'):
                destinations_below_current_floor = []
                for i in self.destinations:
                    destination_index = self.get_floor_index(i)
                    if destination_index < current_floor_index:
                        destinations_below_current_floor.append(destination_index)
                if (len(destinations_below_current_floor) > 0):
                    if (len(destinations_below_current_floor) == 1):
                        next_destination = destinations_below_current_floor[0]
                    else:
                        distance = 999999999
                        for x in destinations_below_current_floor:
                            if (current_floor_index - x < distance):
                                next_destination = x
                                distance = current_floor_index - x
                if (next_destination is not None):
                    return next_destination
                else:
                    # print('no destinations below current floor, switching directions')
                    no_down = True
                    self.direction = 'Up'


    # function that displays the movement of the elevator and sets the new current floor
    def travel_to_floor(self, destination):
        current_floor_index = self.get_floor_index(self.current_floor)
        if (current_floor_index > destination):
            print('going down')
            self.current_floor = self.floors[destination]
            print('welcome to floor: ', self.current_floor)
            self.destinations.remove(self.floors[destination])
        elif(current_floor_index < destination):
            print('going up')
            self.current_floor = self.floors[destination]
            print('welcome to floor: ', self.current_floor)
            self.destinations.remove(self.floors[destination])
        else:
            print('we are already on this floor')
    
    # gets the index of a given floor name
    def get_floor_index(self, floor):
        return (self.floors.index(floor))
    
    # prompts the user to enter an array representing the selected floors to go to
    def input_destinations(self):
        if (len(self.destinations) > 0):
            print("Current Destinations are", self.destinations, ". if you would like to add more please type the floors you wish to stop at with each separated by a comma, else just hit enter")
            print('or type Z to quit shut the elevator down')
        else: 
            print('please type the floors you wish to stop at with each separated by a comma')
            print('or type Z to quit shut the elevator down')

        print("you are currently on floor: ", self.current_floor)
        print("the floor options include: ", self.floors)
        loop = True
        while (loop):
            loop = False
            input1 = input()
            if (input1 == ""):
                loop = False
                break
            result = input1.split(",")
            # for each floor inputed by the user check to see if they are valid floors
            for x in result:
                if x not in self.floors:
                    # if not a valid floor, Z is used to exit the application
                    if (x == 'Z'):
                        print('Shutting Down The Elevator')
                        self.shut_down = True\
                    # else warn the user of the invalid floor inputted
                    else:
                        print (x , ' is not a floor, please try again')
                        loop = True
            # if all the floors are valid
            for x in result:
                # make sure the current floor isnt inputted
                if(x == self.current_floor):
                    print('cannot travel to the floor you are currently on,', x, 'has been removed')
                # add the other floors if not already on the destinations list
                else:
                    if (x not in self.destinations):
                        self.destinations.append(x)


elevator = Elevator()
# main loop used to keep the elevator running unless otherwise prompted
while(not elevator.shut_down):
    elevator.input_destinations()
    if (elevator.shut_down):
        break
    else:
        if (len(elevator.destinations) > 0):
            next_stop = elevator.determine_next_stop()
            if (next_stop is not None):
                elevator.travel_to_floor(next_stop)
            else:
                print('could not determine a next destination')
        else:
            print('No Destinations')




                
        

        

