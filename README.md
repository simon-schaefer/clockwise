# clockwise 🕰️
Simple but expressive timing package in Python

## Installation
```
pip install clockwise
```

## Minimal Example
```
import clockwise

@clockwise.timing("foo")
def foo(a: int): 
   return a + 4

def main():
    for i in range(10):
        foo(i)
    clockwise.print_timings() 

if __name__ == '__main__':
    main()
```

