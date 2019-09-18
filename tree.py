Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> n = int(input("Enter size of tree:"))
for x in range(n):
  for y in range(n-x):
    print(' ', end='')
  print('\b', end='')
  for z in range(x+n-y):
    print('#', end='') 
  print('')
print('#');
