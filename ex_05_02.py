largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue    
    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num
print("Maximum is", largest)
print("Minimum is", smallest)


nums = []

while True:
    val = input("Enter a number: ")
    if val == "done":
        break
    try:
        nums.append(int(val))
    except:
        print("Invalid input")

print("Maximum is", max(nums))
print("Minimum is", min(nums))