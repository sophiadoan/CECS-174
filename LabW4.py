# inputs age (years), weight (pounds), heart rate (beats per minute), and time (minutes)
age_years = int(input("What is your age? "))
weight_pounds = int(input("What is your weight (pounds)? "))
heartrate_bpm = int(input("What is your heart rate (BPM)? "))
time_minutes = int(input("For how long were you exercising (minutes)? "))

# Output the average calories burned for a person.
# Calories = ( (Age x 0.2757) + (Weight x 0.03295) + (Heart Rate x 1.0781) — 75.4991 ) x Time / 8.368

calories = ((age_years * 0.2757) + (weight_pounds * 0.03295) + (heartrate_bpm * 1.0781) - 75.4991)  * time_minutes / 8.368

print(f'Calories: {calories:.2f} calories')
