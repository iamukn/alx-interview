def minOperations(n):
  """
  Calculates the fewest number of operations needed to result in exactly n H characters in the file.

  Args:
    n: The number of H characters to be achieved.

  Returns:
    The fewest number of operations needed.
  """

  if n <= 1:
    return 0

  operations = 0
  current = 1
  while current < n:
    if current * 2 <= n:
      current *= 2
      operations += 1
    else:
      current += 1
      operations += 1

  return operations


if __name__ == "__main__":
  print(minOperations(9))

