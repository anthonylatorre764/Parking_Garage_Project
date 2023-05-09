# Parking Garage Project

# Your assignment for today is to create a parking garage class to get more familiar with Object Oriented Programming(OOP). This project would usually be a pair programming project. However, for the size our class we will have groups of 3. This means, that one person(The driver) will code the project while the other people(The navigators)will brainstorm and guide to a working solution.
# Each of you should share/switch these roles every 30mins-1hr -- Or you may elect to switch "drivers" after creating specific methods of the class.

# The Initial Driver needs to Make sure to:
# download the files below, create a local folder for the project,  create a github repository, commit the inital files,  share the link

# Both navigators should then:
# fork the code, clone it.

# The current driver MUST share their screen so the navigators can help brainstorm to a working solution.

# When code has been updated, you will need to pull down the changes.

# Here's an article on doing so -- https://stackoverflow.com/questions/3903817/pull-new-updates-from-original-github-repository-into-forked-github-repository

# Your parking gargage class should have the following methods:
# - takeTicket
#    - This should decrease the amount of tickets available by 1
#    - This should decrease the amount of parkingSpaces available by 1
# - payForParking
#    - Display an input that waits for an amount from the user and store it in a variable
#    - If the payment variable is not empty then (meaning the ticket has been paid) ->  display a message to the user that their ticket has been paid and they have 15mins to leave
#    - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
#    - If the ticket has been paid, display a message of "Thank You, have a nice day"
#    - If the ticket has not been paid, display an input prompt for payment
#       - Once paid, display message "Thank you, have a nice day!"
#    - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
#    - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

# note: Use VSCode for this project starting with the following files below. Also, each person in the group should list the portion of the project they were responsible for inside of the python file and inside the README file.

# When the project is completed, commit the final changes, sync all pull requests, and each member should submit their respective GitHub links(though the code in each should be the same)


###### List group responsiblities below:
###### Provide name and approxamite line numbers where each person wrote their code



class ParkingGarage():
    """Simulate a Parking Garage."""


    def __init__(self, tickets = 5, parkingSpaces = 5, currentTicket = { "spot number" : "parking space"}):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    def takeTicket(self):
        self.tickets-=1
        self.parkingSpaces-=1
        self.currentTicket[1]=0
    
    def payForParking(self):
        amount = int(input("Parking amount is $20 enter amount: "))
        while amount <= 20:
            amount = int(input("Sorry, but the amount is $20. Please pay the ticket: "))
        if amount >= 20: 
            print("Your ticket has been paid. You have 15mins to leave.")
            self.currentTicket["Paid"]=True

    def leaveGarage(self):
        if self.currentTicket["Paid"] == True:
            print("Thank you, have a nice day!")
            self.tickets+=1
            self.parkingSpaces+=1
        amount = int(input("Parking amount is $20 enter amount: "))
        while amount <= 20:
            amount = int(input("Sorry, but the amount is $20. Please pay the ticket: ")) 
            if amount >= 20: 
                print("Your ticket has been paid. You have 15mins to leave.")
                self.currentTicket["Paid"]=True



parking_garage = ParkingGarage(tickets=[range(1,51)], parkingSpaces=range(1,51))

parking_garage.takeTicket(50,50)

print(parking_garage.tickets)

                
        

            
