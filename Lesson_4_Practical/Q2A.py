def result(m1, m2, m3):
    ttl = m1 + m2 + m3
    percent = ttl / 3
    if percent >= 50:
        print("Result: Pass")
    else:
        print("Result: Fail")
    return

p = int(input("Enter your marks in physics: "))
c = int(input("Enter your marks in chemistry: "))
m = int(input("Enter your marks in math: "))
result(p, c, m)
