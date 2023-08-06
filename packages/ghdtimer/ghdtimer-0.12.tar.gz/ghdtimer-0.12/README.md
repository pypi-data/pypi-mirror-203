# GHD Timer

A Simple tick-tock based timer.

## Install
```bash
pip install ghdtimer
```

## Usage

```python
from ghdtimer import Timer

# prints the time taken to execute
# do_something()in ms with 3 decimals
timer = Timer(mode="ms", decimals=3)
timer.tick()
do_something()
timer.tock()
```
