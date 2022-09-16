# C++-like output in Python

> **Disclaimer:** This project does not have any value. It's nothing but a funny thing designed to make it possible to use C++ output operators `<<` in Python.

Consider the following ways to print something (a string or a number) to console output:

1. **Python** is pretty simple and straightforward:

```python
print("Hello", "world")
```

2. **C++** supports both similar `printf()` function and `<<` operator:

```cpp
#include <iostream>
using namespace std;

int main() {
    printf("Hello");
    cout << " " << "world" << endl;
    return 0;
}
```

3. **This project** implements standard output in Python with left shift operator `<<`. The class below [defines](main.py) its corresponidng magic method:

```python
class COut:

    def __lshift__(self, other) -> 'COut':
        print(other, end='')
        return self
        
    def __repr__(self) -> str:
        return ''
```

Its use is similar to C++:

```python
cout = COut()
# prints 'Hello world'
cout << 'Hello' << ' ' << 'world'
```
