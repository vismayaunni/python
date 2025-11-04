header = "\n\tBOOKSTORE RECEIPT\n====================\n"
book1_title = "Python Basics"
book1_price = 450
book2_title = "Data Science Intro"
book2_price = 600
book1_line = "Book: {}\tPrice: ₹{}\n".format(book1_title, book1_price)
book2_line = "Book: {}\tPrice: ₹{}\n".format(book2_title, book2_price)
total_price = book1_price + book2_price
total_line = "TOTAL\t\t₹{}\n".format(total_price)
thank_you = "\n\tTHANK YOU FOR YOUR PURCHASE!"
receipt = header + book1_line + book2_line + total_line + thank_you
print(receipt.upper())