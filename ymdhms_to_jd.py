# ymdhms_to_jd.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second
# Converts year, month, day, hour, minute, second to fractional Julian date.
#
# Parameters:
# year XXXX
# month XX
# day XX
# hour XX
# minute XX
# second XX.XX
# Output:
# Prints the fractional Julian date.

# Written By: Samuel Jacobson

import sys

# Parse script arguments
if len(sys.argv) == 7:
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    day = int(sys.argv[3])
    hour = int(sys.argv[4])
    minute = int(sys.argv[5])
    second = float(sys.argv[6])
else:
    print('Usage: python3 ymdhms_to_jd.py year month day hour minute second')
    exit()

# Julian Date calculation
def ymdhms_to_jd(year, month, day, hour, minute, second):
    # Convert time to fractional day
    day_fraction = (hour + minute / 60 + second / 3600) / 24.0

    # Adjust year and month for the algorithm
    if month <= 2:
        year -= 1
        month += 12

    # Integer division
    A = year // 100
    B = 2 - A + (A // 4)

    # Julian Date
    jd = int(365.25 * (year + 4716)) \
         + int(30.6001 * (month + 1)) \
         + day + day_fraction + B - 1524.5

    return jd

# Compute the fractional Julian date
jd_frac = ymdhms_to_jd(year, month, day, hour, minute, second)

# Print the result
print(jd_frac)