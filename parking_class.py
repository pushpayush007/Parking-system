import numpy as np
class parking:
    def __init__(self, slots_occupied,car_list, bike_list,truck_list,cash_collected = 0, car_price = 20, bike_price =10, truck_price=50, max_slots =10):
        self.max_slots = max_slots
        self.car_price_hr = car_price
        self.bike_price_hr = bike_price
        self.truck_price_hr = truck_price
        self.slots_occupied = slots_occupied
        self.bike_list = bike_list
        self.car_list = car_list
        self.truck_list = truck_list
        self.cash_collected = cash_collected

    def check_availability(self):
        if self.slots_occupied<self.max_slots:
             return 1
        else:
             return 0
    def price_vehicle_type(self , vehicle_type):
        if vehicle_type == "car" or vehicle_type== "Car":
            return self.car_price_hr,self.car_list
        if vehicle_type == "Bike" or vehicle_type== "bike":
            return self.bike_price_hr,self.bike_list
        if vehicle_type == "Truck" or vehicle_type== "truck":
            return self.truck_price_hr,self.truck_list
    def add_vehicle(self, vehicle_type, vehicle_number):
        _ ,vehicle_list = self.price_vehicle_type(vehicle_type)
        
        if self.check_availability():
            if vehicle_number in vehicle_list:
                print("Invalid number (duplicate)")
                return 
            else:
                self.slots_occupied+=1
                vehicle_list.append(vehicle_number)
                return 
        else:
            print("Slot not available")
            return 

    def exit(self,vehicle_type, vehicle_number ,time_stayed):
        price ,vehicle_list= self.price_vehicle_type(vehicle_type)
        if vehicle_number not in vehicle_list:
            print("Vehicle not in entered list of vehicles")
            return
        price = np.ceil(time_stayed)*price
        self.cash_collected+=price
        print(f"Vehicle Type: {vehicle_type} -> Vehicle number: {vehicle_number} -> time stayed: {time_stayed} ->> Price: {price}")
        vehicle_list.remove(vehicle_number)
        self.slots_occupied-=1
        return price

            



