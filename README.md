# clockwise 🕰️
Simple but expressive timing package in Python

## Installation
```
pip install clockwise
```

## Minimal Example
```
import clockwise

@clockwise.timing("time-as-decorator")
def foo(a: int): 
   return a + 4

def main():
    for i in range(10):
        foo(i)

    with clockwise.timing_context("time-as-context"):
        foo(1)

    clockwise.print_timings() 

if __name__ == '__main__':
    main()
```

## Debug Mode
The profiling is skipped when running in optimized mode using the `-O` or `-OO` tags. 
