import sys

def my_round(val):
  if val - int(val) >= 0.5:
    return int(val) + 1
  else:
    return int(val)

n = int(sys.stdin.readline())

if n == 0:
  print(0)
else:
  opinions = []
  for _ in range(n):
    opinions.append(int(sys.stdin.readline()))
  
  opinions.sort()
  
  exclude_num = my_round(n * 0.15)
  
  if exclude_num > 0:
    result_opinions = opinions[exclude_num : -exclude_num]
  else:
    result_opinions = opinions

  if not result_opinions:
      print(0)
  else:
    avg = sum(result_opinions) / len(result_opinions)
    print(my_round(avg))