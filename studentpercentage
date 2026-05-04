# Lists (arrays)
metric = []
inter = []
test = []
aggregate = []

# 10 students loop
for i in range(10):
    print("Student", i+1)

    m = int(input("Matric %: "))
    i2 = int(input("Inter %: "))
    t = int(input("Test marks: "))

    metric.append(m)
    inter.append(i2)
    test.append(t)

    # Aggregate
    agg = (m*0.3) + (i2*0.3) + (t*0.4)
    aggregate.append(agg)

    print("Aggregate:", agg)

    # Eligibility
    if agg >= 80:
        print("CS (All fields)")
        fields = ["CS", "SE", "AI", "DS", "IT"]

    elif agg >= 70:
        print("SE")
        fields = ["SE", "DS", "IT"]

    elif agg >= 60:
        print("AI")
        fields = ["AI"]

    elif agg >= 50:
        print("DS, IT")
        fields = ["DS", "IT"]

    else:
        print("Not eligible")
        fields = []

    # Choice

        if choice in fields:
            print("Congratulations! Admission in", choice)
        else:
            print("Invalid choice")