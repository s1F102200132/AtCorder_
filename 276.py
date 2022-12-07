def main():
  s = input()
  n = len(s)
  for i in range(n, 0, -1):
    if s[i - 1] == 'a':
      print(i)
      return
  print(-1)
main()