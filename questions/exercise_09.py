resting_heart_rate = int(input("Enter your resting heart rate (BPM): "))

heart_health = ""

if resting_heart_rate >= 78 and resting_heart_rate <= 82:
    heart_health = "Below Average"
elif resting_heart_rate >= 73 and resting_heart_rate <= 77:
    heart_health = "Average"
elif resting_heart_rate >= 69 and resting_heart_rate <= 72:
    heart_health = "Good"
elif resting_heart_rate >= 62 and resting_heart_rate <= 68:
    heart_health = "Great"
elif resting_heart_rate >= 56 and resting_heart_rate <= 61:
    heart_health = "Excellent"
elif resting_heart_rate >= 50 and resting_heart_rate <= 55:
    heart_health = "Athlete"
else:
    heart_health = "Poor"

print(f"Your heart health is {heart_health}.")
