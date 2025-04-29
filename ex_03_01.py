hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate")
r = float(rate)
if h > 40:
    extra_hours = h - 40
    extra_rate = r * 1.5
    extra_gp = extra_hours * extra_rate
    gp = 40 * r + extra_gp
else:
    gp = h * r  
print(gp)
