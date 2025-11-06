web_dev = ["John", "Priya", "Sam"]
data_science = ["Asha", "Vikram", "Sara"]
ui_ux = ["Mike", "Lina", "Arjun"]
all_participants = [web_dev, data_science, ui_ux]
web_dev.append("Rina")
data_science.insert(1, "Tina")
ui_ux.pop()
copied_data_science = data_science.copy()
data_science.clear()
print(web_dev[:2])
name_lengths = [len(name) for name in copied_data_science]
print(name_lengths)
found_asha = "Asha" in web_dev or "Asha" in copied_data_science or "Asha" in ui_ux
print(found_asha)
first_names = (web_dev, copied_data_science, ui_ux)
print(first_names)