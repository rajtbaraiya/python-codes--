bookings = [
    ('Falcon', 10, 11),
    ('Falcon', 10.5, 12),
    ('Tiger', 10, 11),
    ('Falcon', 14, 15),
    ('Tiger', 11, 12)
]

clashes_found = False

for i in range(len(bookings)):
    for j in range(i + 1, len(bookings)):
        room1, start1, end1 = bookings[i]
        room2, start2, end2 = bookings[j]

        if room1 == room2:
            # Check overlap
            if start1 < end2 and start2 < end1:
                print(f"CLASH in {room1}: ({start1}, {end1}) overlaps ({start2}, {end2})")
                clashes_found = True

if not clashes_found:
    print("Schedule OK")
