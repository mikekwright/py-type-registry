Python Type Registry
=======================================

[![Build Status](https://travis-ci.org/mikekwright/py-type-registry.svg?branch=master)](https://travis-ci.org/mikekwright/py-type-registry) 

The `type-registry` library provides the ability to easily register factory methods (or classes) that can be
used in a configuration file to quickly construct complex objects (or models).  

## Example

Lets demonstrate how to easily use this library.  There are a functions and decorators, but the most important is the `register`
decorator.  By registering a type, we are telling the system that when a configuration section has a special key `__factory__`
to construct that section into an object.  

We start by registering our `PytorchExample` and give it a more usable name of `pytorch-model`.  

```python
import torch.nn as nn

from type_registry import register

@register('pytorch-model', input_size=1024, output_size=8)
def PytorchExample(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
      ...
```

Now that we have the type registered with the system, in the configuration we can supplied the details
around its construction (in this case we are just providing the value of the `hidden_size`)  

```yaml
model:
  __factory__: pytorch-model
  hidden_size: ...
```

### Constructing from config

Once we have our types registered and a config defined, we need to correctly load the configuration so that
it will construct the types.  This is accomplished using the `load_yaml` and `load_yaml_str` functions.  

```python
from type_registery import load_yaml_str

yaml_str = get_config()
result = load_yaml_str(yaml_str)
```

You can also have environment variables (or custom variables) automatically expanded in the same configuration
file.  

```yaml
model:
  __factory__: simple-model
  use_aws: $USE_AWS
```

## Viewing the Registery

To make working with the library a little easier, there is a function that can be called which will print out
the details of the registery (at the time the call takes place).  

```python
from type_registery import print_registry

if __name__ == '__main__':
  print_registery(color=True)
```

Setting the `color` value to True will have the system print out the results using shell coloring (termcolor library).
You can also have the output of the `print_registry` call target a file instead of `stdout`.  

```python
from type_registery import print_registry

if __name__ == '__main__':
  with open('registry.txt', 'w') as f:
    print_registry(file=f)
```
