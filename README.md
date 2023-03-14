# **AirBnB Clone Project**
![image](https://user-images.githubusercontent.com/99338832/224989645-2aa6247d-7b73-48bd-b755-2149e45582c1.png)


The goal of the project is to deploy on our server a simple copy of the AirBnB website.

The complete web application will be composed of:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)

- A website (the front-end) that shows the final product to everybody: static and dynamic

- A database or files that store data (data = objects)

- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)


## **Concepts learned**

- Unittests

- Python packages concept page

- Serialization/Deserialization

- *args, **kwargs

- datetime


## **Steps**

Each step will link to a concept:

1. The console
-create your data model
-manage (create, update, destroy, etc) objects via a console / command interpreter
store and persist objects to a file (JSON file)

2. Web static
-learn HTML/CSS
-create the HTML of your application
-create template of each object

3. MySQL storage
-replace the file storage by a Database storage
-map your models to a table in database by using an O.R.M.

4. Web framework - templating
-create your first web server in Python
-make your static HTML file dynamic by using objects stored in a file or database

5. RESTful API
-expose all your objects stored via a JSON web interface
-manipulate your objects via a RESTful API

6. Web dynamic
-learn JQuery
-load objects from the client side by using your own RESTful API



## **AirBnB Project: The Console**

This is a team project to build a clone of AirBnB.

The console is a command interpreter to manage objects abstraction between objects and how they are stored.

The console will:

- create a new object
- retrive an object from a file
- do operations on objects
- destroy an object
- Storage(All the classes are handled by the storage engine in the FileStorage Class.)

The files were interpreted and compiled using Ubuntu 20.04 LTS and the  programming language used was Python 3.8.3. 
The editor used was VIM.


### 1. **Installation**

Clone the repository.
```
$ git clone https://github.com/------/AirBnB_clone.git
```

### 2. **Usage**



|Method|Description| 
|:-------|:-----------|
|create|Creates object of given class|
|show|Prints the string representation of an instance based on the class name and id|
|all|Prints all string representation of all instances based or not on the class name|
|update|Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file|
|destroy|Deletes an instance based on the class name and id (save the change into the JSON file)|
|count|Retrieve the number of instances of a class|
|help|Prints information about specific command|
|quit/ EOF|Exit the program|


####  Application
Start the console in interactive mode:
```
$ ./console.py
(hbnb)
```
Use help to see the available commands:
```
(hbnb) help
```

in Non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```
Quit the console:
```
(hbnb) quit
$
```

### 3. **Tests**
All the tests are defined in the tests folder.

- Documentation

Modules:
```
python3 -c 'print(__import__("my_module").__doc__)'
```
Classes:
```
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
```
Functions (inside and outside a class):
```
python3 -c 'print(__import__("my_module").my_function.__doc__)'
```
and
```
python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
```

#### - Python Unit Tests

unittest module

File extension .py

Files and folders star with test_

Organization:for models/base.py, unit tests in: tests/test_models/test_base.py

Execution command: 

```
python3 -m unittest discover tests
```

or:
```
python3 -m unittest tests/test_models/test_base.py
```

- Run test in interactive mode

```
echo "python3 -m unittest discover tests" | bash
```

- Run test in non-interactive mode

To run the tests in non-interactive mode, and discover all the test, you can use the command:

```
python3 -m unittest discover tests
```
