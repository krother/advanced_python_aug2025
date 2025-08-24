
# Abstract Base Classes

The **abc** module allows to declare abstract classes and methods. 
You find an example in [descriptors.py](descriptors.py).
Create both valid and invalid instances of the defined class.

The example uses the **descriptor protocol**, a mechanism to control the getting and setting of attributes using object composition. 

## Exercise

Create a superclass `GameObject` for the player and ghost classes in the Pac game. Use the following example code:


    from abc import ABC, abstractmethod

    class Command(ABC):
    
        def __init__(self, name):
            self.name = name

        @abstractmethod
        def executed(self):
            pass



## Multiple Inheritance

Python allows multiple inheritance, often found under the term **mixins**.
It is tricky, because the namespaces potentially collide.
I advise to avoid multiple inheritance whenever possible.

A lifesaver is checking the **method resolution order**, see [multiple_inheritance.py](multiple_inheritance.py)

## Metaclasses

**Metaclasses** control how Python creates objects. This helps to understand the language better.
There are not too many reasons to use metaclasses in a project.

Execute the example in [metaclasses.py](metaclasses.py) and see what it does.
