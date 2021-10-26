# Assessment for Hyperledger Fabric Training Program
## Question 1
- For Question 1a and 1b deployment, run ```python3 Q1.py```
## Question 2
- Question 2a in ```Q2a.py``` provides the class which is inherited by DevAccount in ```Q2b.py``` which a simple demo can be run as follow:-  
- For deployment run ```python3 Q2b.py```
## Question 2c
- Analysis summary:-
- Object-oriented in general allows the data encapsulation amongst inheritance and polymorphism. While other OOP languages like Java have a very explicit ways of implementation e.g special keywords; Python on the other hands have a less explicit way of developing said approach, hence, the inheritance done in this project is meant to allow class Account to be "independent" from direct access. This is in its natural state to protect access to such attributes such as account name, id and balance. The inheritance done on DevAccount allows the user of the class to only call the constuctor and methods in order to made transfer, get and view balance as well as other intentions without having a direct access to parent class. This is done by supplying an "_" underscore which allows the attributes to be used freely from within the class but not from the outside.
- Additionally, the developer in of the view that by instantiating the Account class will allow for future use-cases such as creation of special type of accounts that may require additional attributes.