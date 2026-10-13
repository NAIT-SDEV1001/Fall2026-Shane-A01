print("Hotel Guest Counter")
floors = int(input("Number of floors: "))
rooms_per_floor = int(input("Rooms per floor: "))
hotel_total = 0
floor = 1

while floor <= floors:
    room = 1  # Restart room numbering for each floor.
    floor_total = 0  # Challenge: track the current floor separately.

    while room <= rooms_per_floor:
        guests = int(input(f"Floor {floor}, Room {room} - number of guests: "))
        floor_total += guests
        hotel_total += guests
        room += 1

    print(f"Floor {floor} guests: {floor_total}")
    floor += 1

print(f"Total guests: {hotel_total}")
