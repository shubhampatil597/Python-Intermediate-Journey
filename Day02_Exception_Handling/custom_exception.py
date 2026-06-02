#Day 2 - Custom Exception Example

class InvalidTimeError(Exception):
pass

try:
current_time = int(input("Enter current time (0-23): "))

if current_time < 0 or current_time > 23:
    raise InvalidTimeError(
        "Time must be between 0 and 23"
    )

print("Valid Time")

except ValueError:
print("Please enter numbers only")

except InvalidTimeError as e:
print("Error:", e)

finally:
print("Validation Completed")