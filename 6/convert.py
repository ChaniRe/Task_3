def dd_to_dms(dd_coords):
    results = []
    for i, val in enumerate(dd_coords): # Loop through each value in the input list
        # if the index is 2 or more, it is altitude
        if i > 1:
            results.append(val)
            continue
        # determine the direction    
        if i == 0:
            direction = "W" if val < 0 else "E"
        else:
            direction = "N" if val > 0 else "S"
            
        abs_val = abs(val)
        degrees = int(abs_val) # 1. Degrees: The whole number part
       
        minutes_float = (abs_val - degrees) * 60 # 2. Minutes: Multiply the decimal remainder by 60
        minutes = int(minutes_float)
        
        seconds = round((minutes_float - minutes) * 60, 2) # 3. Seconds: Multiply the remaining decimal by 60 and round to 2 digits
        results.append([degrees, minutes, seconds, direction])
    return results

#checking the code
anchorage_input = [-149.9002, 61.2181, 22]
print("Anchorage:", dd_to_dms(anchorage_input))

la_input = [-118.2437, 34.0522]
print("Los Angeles:", dd_to_dms(la_input))