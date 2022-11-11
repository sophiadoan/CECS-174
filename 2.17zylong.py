import math
C = 299792458   # in meters/second
SECONDS_PER_DAY = 86400  
DISTANCE_TO_PROXIMA_ALPHA = 7.4740 * 10**16   # in meters
DAYS_PER_YEAR = 365

space_ship_velocity = float(input("Enter space ship velocity as a fraction of the speed of light:"))

print("Traveling to Proxima Alpha...")
v = space_ship_velocity * C #converts to meters per second
dilation_factor = math.sqrt(1 - (v ** 2 / C ** 2 ))

earth_time_secs = DISTANCE_TO_PROXIMA_ALPHA / v
ship_time_secs = dilation_factor * earth_time_secs

earth_time_days = earth_time_secs / SECONDS_PER_DAY
earth_time_years = earth_time_days // DAYS_PER_YEAR
earth_leftover_days = earth_time_days % DAYS_PER_YEAR

ship_time_days = ship_time_secs / SECONDS_PER_DAY
ship_time_years = ship_time_days // DAYS_PER_YEAR
ship_leftover_days = ship_time_days % DAYS_PER_YEAR

print(f"An observer on Earth ages {int(earth_time_years)} years, {int(earth_leftover_days)} days during the trip.")
print(f"A passenger on the ship ages {int(ship_time_years)} years, {int(ship_leftover_days)} days during the trip.")
