# Parking Garage Project

###### List group responsiblities below:
###### Provide name and approxamite line numbers where each person wrote their code



# Responsibilities...        (line numbers)


# Anthony LaTorre:
#    __init__ method            (52-55)
#    payForParking method       (62-68)
#    created class instance     (84)

# Rhianna Dicent:
#    takeTicket method          (57-60)
#    leaveGarage method         (70-80)
#    modified class instance    (84)
#    method/attribute calls     (86,88)




##### Visual of Dictionaries layout ####


# (parking spot occupancy)
# ('True' means spot is occupied, False for otherwise)

    # spot_nums {
    #     0: True,
    #     1: True,
    #     2: False,
    #     3: True,
    #     4: False
    # }


# (see who's paid for parking)
# ('True' means person in that spot number has paid, False for otherwise)

    # currentTicket {
    #     0: True,
    #     1: True,
    #     2: False,
    #     3: True,
    #     4: False,
    # }



class ParkingGarage():
    """Simulate a parking garage."""

    def __init__(self, tickets = 5, parkingSpaces = 5, spot_key = 0):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.spot_nums = {
            0: False,
            1: False,
            2: False,
            3: False,
            4: False,
        }
        self.currentTicket = {}


    def takeTicket(self):
        if self.tickets and self.parkingSpaces:
            print("\nTickets available")
            self.tickets -= 1
            self.parkingSpaces -= 1
        else:
            print("\nSorry, you'll have to come back later when a spot opens " +
                  "up.\n")
            return 1
        print("\nHere is your Ticket...\n")
        for key, value in self.spot_nums.items():
            if value == False:
                print("You are in spot number " + str(key) + ".")
                self.spot_nums[key] = True
                self.currentTicket[key] = False
                print("\nCurrent Occupancy ('True' means spot is taken):")
                print(f"{self.spot_nums}")
                break


    def payForParking(self):
        spot = int(input("\nWhat spot are you in? "))
        while spot > 4:
            print("Sorry, but our parking spaces are numbered 0 - 4.")
            spot = int(input("Please enter a valid spot number. (0, 1, etc.) "))
        print()
        amount = int(input("Parking costs $20, enter amount: "))
        while amount < 20:
            amount = int(input("\nSorry, but the amount is $20. Please enter " +
                               "'20' to continue: "))
        if amount >= 20: 
            print("\nYour ticket has been paid. You have 15 minutes to leave.")
            self.currentTicket[spot] = True


    def leaveGarage(self):
        spot = int(input("\nWhat spot are you in? "))
        while spot > 4:
            print("\nSorry, but our parking spaces are numbered 0 - 4")
            spot = int(input("Please enter a valid spot number (0, 1, etc.): "))
        if self.currentTicket[spot] == True:
            print("\nThank you, have a nice day!")
            self.tickets+=1
            self.parkingSpaces+=1
            self.spot_nums[spot] = False
            del self.currentTicket[spot]
        else:
            print("\nYou need to pay for parking first.")


    def runner(self):
        print("\n--------- Welcome to the Parking Garage Simulator! ---------")
        while True:
            response = input("\n\n\nDo you want to... Take a ticket, Pay for " +
                             "parking, Leave garage or Quit? ").lower()
            
            if response == 'take ticket' or response == 'take a ticket':
                exit = self.takeTicket()
                if exit == 1:
                    break
            elif response == 'pay' or response == 'pay for parking':
                self.payForParking()
            elif response == 'leave' or response == 'leave garage':
                self.leaveGarage()
            elif response == 'quit':
                break
            else:
                print("\nInvalid Response... Please enter 'take ticket', " +
                      "'pay', or 'leave'.")
            
            
        


my_parking_garage = ParkingGarage()


my_parking_garage.runner()
