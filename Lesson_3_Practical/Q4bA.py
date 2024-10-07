subjects = ["English", "Math", "Science", "History"]
i = 0
print(f"{'No':<5}{'Subject'}")
print("------------")
while i < len(subjects):
 print(f"{i+1:<5}{subjects[i]}")
 i += 1