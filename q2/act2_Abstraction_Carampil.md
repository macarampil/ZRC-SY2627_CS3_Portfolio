

Activity 2: Follow-Along Challenge

Complete these as you watch! 

    The Blueprint Concept: The narrator says you shouldn't be able to create a generic "Vehicle" object. Why is an Abstract Class called a "blueprint"?
    Your Answer: An Abstract Class is called a blueprint because it serves as a guide for Child Classes. It defines the common attributes and methods that its subclasses should have, without allowing us to create an object directly from it.

    The "Must-Have" Rule: When we use the @abstractmethod decorator, what are we forcing the Child Classes to do?

        [ ] Change their variable names.

        [V] Implement their own version of that specific method.

        [ ] Delete the parent class.

    Safety First: What happens if you try to create an object directly from an Abstract Class? (e.g., my_car = Vehicle())
    Your Answer: Python will raise a TypeError because Abstract Classes cannot be instantiated directly. A Child Class must first implement all the required abstract methods before an object can be created.
