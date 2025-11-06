attendance = 
full_days = 0
for count in attendance:
    if count >= 20:
        print("Full")
        full_days += 1
    else:
        print("Not Full")
print(full_days)
print(sum(attendance))