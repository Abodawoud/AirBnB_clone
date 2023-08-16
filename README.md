# Clone AirBnB_Website

![Alt text](image.png)

## Description
Welcome to our "AirBnB Clone - The Console" Project! This project aims to replicate the core functionality of the popular accommodation booking platform, AirBnB. Our console is designed to seamlessly handle project's objects. Whether creating new Users or Places, retrieving data from various sources, performing operations like counting or computing statistics, updating object attributes, or even gracefully destroying objects. ***Our console project aims to  manage data efficiently.***

## Description of our command interpreter

### How to start it

1. Clone the project to your local machine "https://github.com/Abodawoud/AirBnB_clone.git"

2. Execute the `console.py` file and enjoy


### Execution

####  `In interactive mode`

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

#### `In non-interactive mode`
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### How to use it

After Execution `console.py` file, you are ready to manage your project's objects by writing commands in this way
`(hbnb) <command> [agruments]`

| Commands | Description | Arguments |
| --- | ----------- | ------- |
| `help` | provide description about all commands |  command |
| `create` | create new class | class name |
| `destroy` | Deletes an instance based on the class name and id | `<class name> <obj id>` |
| `update` | Updates an instance based on the class name and id by adding or updating attribute | `<class name> <id> <attribute name> <attribute value>` |
| `all` | Prints all string representation of all instances based or not on the class name | `<class name>` or not |
| `show` | Prints the string representation of an instance based on the class name and id | `<class name> <obj id>` |
| `EOF` | exit the program | -- |
| `quit` | exit the program | -- |
---

### 📌 Simple Note :
---
provided classes are `{Basemodel, User, State, City, Amenity, Place, Review}`.

## Examples

``` Shell
~/alx/AirBnB_clone# ./console.py 
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) create User
abca4e8c-d797-44d1-a53f-e3158fef0bc9
(hbnb) create Place
b51ed93d-b8bc-4f54-ac12-8f5fa4b3f51a
(hbnb) update User abca4e8c-d797-44d1-a53f-e3158fef0bc9 age "12"
(hbnb) all
["[User] (abca4e8c-d797-44d1-a53f-e3158fef0bc9) {'id': 'abca4e8c-d797-44d1-a53f-e3158fef0bc9', 'created_at': datetime.datetime(2023, 8, 12, 10, 9, 12, 886105), 'updated_at': datetime.datetime(2023, 8, 12, 10, 9, 12, 886150), 'age': '12'}", "[Place] (b51ed93d-b8bc-4f54-ac12-8f5fa4b3f51a) {'id': 'b51ed93d-b8bc-4f54-ac12-8f5fa4b3f51a', 'created_at': datetime.datetime(2023, 8, 12, 10, 9, 22, 643120), 'updated_at': datetime.datetime(2023, 8, 12, 10, 9, 22, 643151)}"]
(hbnb) show Place b51ed93d-b8bc-4f54-ac12-8f5fa4b3f51a
[Place] (b51ed93d-b8bc-4f54-ac12-8f5fa4b3f51a) {'id': 'b51ed93d-b8bc-4f54-ac12-8f5fa4b3f51a', 'created_at': datetime.datetime(2023, 8, 12, 10, 9, 22, 643120), 'updated_at': datetime.datetime(2023, 8, 12, 10, 9, 22, 643151)}
(hbnb) destroy Place
** instance id missing **
(hbnb) destroy Place b51ed93d-b8bc-4f54-ac12-8f5fa4b3f51a
(hbnb) quit
~/alx/AirBnB_clone#
```










