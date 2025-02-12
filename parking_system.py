from parking_class import parking
from data_read_write import data_reader
vehicle_type,entry_exit,time_stayed,vehicle_number = data_reader("vehicles.csv")
slots_occupied = 0
car = []
bike =[]
truck = []
parking = parking(slots_occupied,car, bike, truck)
for i in range(0,len(vehicle_type)):
    if entry_exit[i]:
        parking.add_vehicle(vehicle_type[i],vehicle_number[i])
    else:
        parking.exit(vehicle_type[i],vehicle_number[i],time_stayed[i])
    i+=1
    
print("Total cash collected:",parking.cash_collected)
print("Total slots occupied:",parking.slots_occupied)

