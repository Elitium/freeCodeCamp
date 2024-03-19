def add_time(start, duration, day=""):
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday","sunday"]

    item = start.split()
    startHours = int(item[0].split(":")[0])
    startMin = int(item[0].split(":")[1])
    addHours = int(duration.split(":")[0])
    addMin = int(duration.split(":")[1])
    addDays = 0

    new_time = ""

    def getZero(total):
        if total < 10: #fills in 0 in time if only units
            return "0"
        else:
            return ""
        
    if addHours >= 24:
        addDays += (addHours // 24)
        addHours = (addHours % 24)
    
    if startHours + addHours > 12 or (startHours + addHours == 11 and startMin + addMin >= 60):
        if startHours + addHours > 24: #if start hours and hours to add sum to greater than 24 hrs, increment day by 1 and keep AM/PM the same or minutes cause it to be larger
            addDays += 1 
        else:
            if item[1] == "PM": #if day change
                item[1] = "AM"
                addDays += 1
            else: 
                item[1] = "PM"

        new_time = str(((startHours + addHours)%12 + (startMin + addMin)//60)) + ":" + getZero((startMin + addMin)%60) + str((startMin + addMin)%60) + " " + item[1]
    else:
        new_time = str(((startHours + addHours) + (startMin + addMin)//60)) + ":" + getZero((startMin + addMin)%60) + str((startMin + addMin)%60) + " " + item[1]
    
    if day:
        new_time += f", {days[(days.index(day.lower()) + addDays) % 7][0].upper() + days[(days.index(day.lower()) + addDays) % 7][1:]}"

    if addDays == 1:
        new_time += " (next day)"
    elif addDays > 1:
        new_time += f" ({addDays} days later)" 

    return new_time

