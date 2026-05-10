s1 = float(input("Score 1: "))
s2 = float(input("Score 2: "))
s3 = float(input("Score 3: "))

avg = (s1 + s2 + s3) / 3

if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Average: {avg:.1f}, Grade: {grade}")
