
# Operator Overloading

Python has a long list of special **double-underscore methods** ("dunder methods").
They all have in common that they should never be called directly. 
Practically, every Python operator can be overloaded by a method.

## Common use cases

* making objects printable with `__repr__()`  and `__str__()`
* checking equality with `__eq__()`
* making objects sortable with `__lt__()` (less than) or `__gt__()`

You find an application example in [sortable_objects.py](sortable_objects.py)

I would advise using operator overloading sparingly. Most of the time, a regular method is easier to read.

## Dynamic Attributes

The special methods `__getattr__` and `__setattr__` allow you to intercept the process of attribute access. They work like a more generic **property**. You can use them to retrieve attributes from elsewhere or to generate them on-the-fly. However, since methods use the same mechanism you will always want to call the inherited method.

Execute the example in [getattr_setattr.py](getattr_setattr.py)

## Slots

The `__slots__` attribute is a mechanism to define the available attributes more strictly.
This mechanism is used by **dataclasses** and **pydantic** with a more comfortable interface.

Run the example in [slots.py](slots.py). Remove the comment and run the code again.
