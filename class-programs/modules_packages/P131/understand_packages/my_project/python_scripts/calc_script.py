import sys

print(sys.path)
sys.path.append(r'D:\Python\calc')
print(sys.path)
import calculator

print(calculator.add(2, 3))
