chappie
=======

A minimal Finite State Machine library.

Ported from [soveran/micromachine](https://github.com/soveran/micromachine).

Installation
------------

```
$ pip install chappie
```

Usage
-----

```python
from chappie import Machine

# Setting an initial state
machine = Machine.new("new")

# Define the possible transitions
machine.when("confirm", {"new": "confirmed"})
machine.when("ignore", {"new": "ignored"})
machine.when("reset", {"confirmed": "new", "ignored": "new"})

# Trigger events
machine.trigger("confirm") # => True
machine.state              # => "confirmed"

machine.trigger("ignore")  # => False
machine.state              # => "confirmed"

machine.trigger("reset")   # => True
machine.state              # => "new"

# Includes support for callbacks
def on_ignore
  print("Don't laugh, I'm being cool")

def on_any
  print("I'm consciousness. I'm alive. I'm Chappie")

machine.on("ignored", on_ignore)
machine.on("any", on_any)

machine.trigger("ignore")
# => "Don't laugh, I'm being cool"
# => "I'm consciousness. I'm alive. I'm Chappie"

machine.state
# => "ignored"
```

License
-------

Released under the [MIT License](http://www.opensource.org/licenses/MIT).
