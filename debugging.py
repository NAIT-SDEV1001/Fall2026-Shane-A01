#Use breakpoint() to use the Python debugger
#l - list surrounding lines
#n - next line
#c - go to next breakpoint (continue)

number_of_floors = int(input("Number of floors: "))
rooms_per_floor = int(input("Rooms per floor: "))
#breakpoint()
total_guests = 0
room_records = []

for floor in range(1,number_of_floors + 1):    
    for room in range(1, rooms_per_floor + 1):         
        guests = int(input(f"Floor {floor}, Room {room} - enter number of guests: "))
        print(f"Floor {floor}, room {room} — number of guests: {guests}")
        total_guests -=  guests
        room_records.append((floor,room,guests))

print(room_records)        
#breakpoint()
print("\nHOTEL ROOM SUMMARY\n")
for floor,room,guest in room_records:#unpacking in a for loop
    print(f"Floor {floor} | Room {room} | Guests: {guest}")

print(f"\nTotal number of guests: {total_guests}")

print("\nHOTEL ROOM SUMMARY\n")
print(f"{'Floor':<8}{'Room':<8}{'Guests':<8}")
print("-" * 24)
for floor,room,guest in room_records:#unpacking in a for loop
    print(f"{floor:<8}{room:<8}{guest:<8}")