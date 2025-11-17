try:
    title = input("Enter the book title: ")
    if not all(ch.isalpha() or ch.isspace() for ch in title):
        raise ValueError("Invalid title")

    year = input("Enter the publication year: ")
    if not (year.isdigit() and len(year) == 4 and (year.startswith("19") or year.startswith("20"))):
        raise ValueError("Invalid year")

    print("Title:", title)
    print("Year:", year)

except ValueError as e:
    print(e)

finally:
    print("Process completed")
