hrs  = input("Enter Hours:")
hrs = float(hrs)
r = input("Enter Rate:")
r = float(r)
def computepay(hrs, r):
    if hrs <= 40:
        p = hrs * r
    else:
        extra_hours = hrs - 40
        extra_rate = r * 1.5
        extra_gp = extra_hours * extra_rate
        p = 40 * r + extra_gp
    return(p)
p = computepay(hrs, r)
print("Pay", p)

def computepay(hrs, r):
    if hrs <= 40:
        return hrs * r
    else:
        return (40 * r) + ((hrs - 40) * r * 1.5)
hrs = float(input("Enter Hours: "))
r = float(input("Enter Rate: "))
p = computepay(hrs, r)
print("Pay", p)