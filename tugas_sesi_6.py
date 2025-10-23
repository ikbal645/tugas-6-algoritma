def merge_sort(students):
    if len(students) <= 1:
        return students

    mid = len(students) // 2
    left = merge_sort(students[:mid])
    right = merge_sort(students[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][1] < right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Contoh penggunaan
if __name__ == "__main__":
    students = [
        ("Andi", 78),
        ("Budi", 65),
        ("Citra", 85),
        ("Dewi", 72),
        ("Eka", 90)
    ]
    sorted_students = merge_sort(students)
    print("Students sorted by score:")
    for student in sorted_students:
        print(f"{student[0]}: {student[1]}")
