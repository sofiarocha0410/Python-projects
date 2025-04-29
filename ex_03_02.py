score = input("Enter Score: ")
try:
    score = float(score)
except:
    print("Error, pelase enter a numeric input between 0.0 and 1.0")
    quit()
#próximo bloco não era necessário neste ex,mas melhora o programa
if score < 0.0 or score > 1.0: 
    print("Error, score out of range")
    quit()
if score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
else:
    print("F")
