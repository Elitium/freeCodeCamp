def add_time(start, duration, day=""):
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday","sunday"]

    item = start.split()
    startHours = int(item[0].split(":")[0])
    startMin = int(item[0].split(":")[1])
    addHours = int(duration.split(":")[0])
    addMin = int(duration.split(":")[1])
    addDays = 0

    new_time = ""

    if addHours >= 24:
        addDays += (addHours // 24)
        addHours = (addHours % 24)
    
    if startHours + addHours > 12 and ((addHours) // 12) % 2 == 1  or (startHours + addHours == 11 and startMin + addMin > 60):
        if item[1] == "PM":
            item[1] = "AM"
        else: 
            item[1] == "PM"
        new_time = str(((startHours + addHours)%12 + (startMin + addMin)//60)) + ":" + str((startMin + addMin)%60) + " " + item[1]
    else:
        print(addHours)
        new_time = str(((startHours + addHours) + (startMin + addMin)//60)) + ":" + str((startMin + addMin)%60) + " " + item[1]
    
    if day:
        new_time += f", {days[(days.index(day.lower()) + addDays) % 7][0].upper() + days[(days.index(day.lower()) + addDays) % 7][1:]}"

    if addDays == 1:
        new_time += " (next day)"
    elif addDays > 1:
        new_time += f" ({addDays} days later)" 


    print(new_time)
    return new_time

add_time('10:10 PM', '1241:30', "tuesday")
