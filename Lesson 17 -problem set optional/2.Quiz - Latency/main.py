# Write a procedure, speed_fraction, which takes as its inputs the result of
# a traceroute (in ms) and distance (in km) between two points. It should 
# return the speed the data travels as a decimal fraction of the speed of
# light.

speed_of_light = 300000. # km per second
seconds_in_ms = 1000.0

def speed_fraction(traceroute, distance):
    total_time = traceroute/seconds_in_ms
    total_distance = (distance * 2)/total_time
    result = total_distance/speed_of_light
    return result



print speed_fraction(50,5000)
#>>> 0.666666666667

print speed_fraction(50,10000)
#>>> 1.33333333333  # Any thoughts about this answer, or these inputs?
