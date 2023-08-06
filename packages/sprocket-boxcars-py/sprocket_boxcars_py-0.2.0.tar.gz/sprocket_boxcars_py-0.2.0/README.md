# Boxcars-py

Python bindings for the [Boxcars](https://github.com/nickbabcock/boxcars) Rocket
League replay parser. This is a fork of [SaltieRL's
package](https://github.com/SaltieRL/boxcars-py) which sadly seems to no longer
be maintained. 

## Installation

Only tested on linux.
You have to compile it yourself if you are using Windows.

```
pip install sprocket-boxcars-py
```

## Usage

```py
from boxcars_py import parse_replay

with open("your_replay.replay", "rb") as f:
  buf = f.read()
  f.close()

replay = parse_replay(buf)
# Use the parsed replay here
```

## Building from source

__Requirements__
  - Rust.
  - `maturin`

```
maturin develop
maturin publish
```
