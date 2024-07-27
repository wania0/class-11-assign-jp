"""
Problem 4:
Design a hotel room managment system

Requirement:
1. I should be able to add hotel info i.e name and address
2. I should be able to add new room info i.e name, num_of_beds, fare_per_day
3. I should be able to book a room for a user/person/account for today and future dates (ignore timezone)
4. I should be able to view the few stats i.e total rooms, total room occupied today, total rooms available today
5. I should be able to check if room is available on future date

Design a good model. Its a simple requirment there will no need to use inheritance
"""

# Solution :

class Hotel:
           
    def __init__(self, hotel_name, hotel_address):
        self.hotel_name = hotel_name
        self.hotel_address = hotel_address
        self.rooms = []
        
    def hotel_info(self):
        print("Hotel name is:", self.hotel_name, "Hotel address is:", self.hotel_address)
        
    def add_new_room(self, room_name, num_of_beds, fare_per_day):
        room =  Room(room_name, num_of_beds, fare_per_day)
        self.rooms.append(room)
        print("Room", room_name, "with", num_of_beds, "beds has been successfully added to the hotel.")
     
class Room:
    
    def __init__(self, room_name, num_of_beds, fare_per_day):
        self.room_name = room_name
        self.num_of_beds = num_of_beds
        self.fare_per_day = fare_per_day
        
    
hotel = Hotel("Mount Feast", "11th St, Naran")
hotel.hotel_info()

hotel.add_new_room("Suite", 2, 200)
hotel.add_new_room("Double Deluxe", 2, 150)
hotel.add_new_room("Single", 1, 100)