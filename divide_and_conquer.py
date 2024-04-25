def min_max_dc(A, i, j):
  if i == j:
    # Elemen tunggal
    return A[i], A[i]
  elif j - i == 1:
    # Dua Elemen
    return min(A[i], A[j]), max(A[i], A[j])
  else:
    # Divide
    mid = (i + j) // 2
    left_min, left_max = min_max_dc(A, i, mid)
    right_min, right_max = min_max_dc(A, mid + 1, j)
    # Conquer (combine)
    return min(left_min, right_min), max(left_max, right_max)


A = [3, 7, 9, 11, 15]
min_value, max_value = min_max_dc(A, 0, len(A) - 1)
print("Minimal:", min_value)
print("Maksimal:", max_value)
