def median(list_to_median):
  list_to_median = sorted(list_to_median)
  length = len(list_to_median)
  if length % 2 == 0:
    a1 = int(length/2)
    a2 = int(length/2 - 1)
    median = (list_to_median[a1] + list_to_median[a2])/2
  else:
    a = int(length/2)
    median = list_to_median[a]
  return median

print(median([4, 5, 5, 4]))