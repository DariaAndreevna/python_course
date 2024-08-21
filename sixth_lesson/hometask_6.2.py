number = int(input("Please enter integer number from 0 to 8640000:"))

days, days_rem = divmod(number, 86400)
days = str(days)
hours, hours_rem = divmod(days_rem, 3600)
hours = str(hours)
seconds, milliseconds = divmod(hours_rem, 60)
seconds = str(seconds)
milliseconds = str(milliseconds)

if days[-1] in ["2", "3", "4"] and days not in ["12", "13", "14"]:
    numerator = "дні"
elif days.endswith("1") and days != "11":
    numerator = "день"
else:
    numerator = "днів"

result_string = f"{days} {numerator}, {(hours.zfill(2))}:{seconds.zfill(2)}:{milliseconds.zfill(2)}"
print(result_string)