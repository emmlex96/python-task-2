passed, failed = 0, 0
for student in range(1, 16):
    score = int(input(f"Enter score for student {student}: "))
    if score >= 45:
        passed += 1
    else:
        failed += 1
print(f"Passed: {passed}, Failed: {failed}")
