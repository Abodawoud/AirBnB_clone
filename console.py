#!/usr/bin/python3
"""cmd module to make command interpreter"""


import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models import storage


class HBNBCommand(cmd.Cmd):
    """class commands"""

    prompt = "(hbnb) "
    list_of_classes = ["BaseModel", "User",
                       "City", "State", "Amenity", "Review", "Place"]

    def do_EOF(self, line):
        """EOF command to exit the program"""

        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""

        return True

    def emptyline(self):
        """emptyline command to execute anything"""

        pass

    def do_create(self, line):
        """Creates a new instance"""

        if line:
            if line not in HBNBCommand.list_of_classes:
                print("** class doesn't exist **")
            else:
                instance = eval(f"{line}()")
                instance.save()
                print(instance.id)
        else:
            print("** class name missing **")

    def do_show(self, line):
        """Prints the string representation of \
            an instance based on the class name and id"""

        if line:
            list_line = line.split(" ")
            if list_line[0] not in HBNBCommand.list_of_classes:
                print("** class doesn't exist **")
            elif len(list_line) == 1:
                print("** instance id missing **")
            elif list_line[1]:
                dic = storage.all()
                flag = 0
                for key, value in dic.items():
                    if f"{list_line[0]}.{list_line[1]}" == key:
                        print(value)
                        flag = 1
                        break
                if flag == 0:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""

        if line:
            list_line = line.split(" ")
            if list_line[0] not in HBNBCommand.list_of_classes:
                print("** class doesn't exist **")
            elif len(list_line) == 1:
                print("** instance id missing **")
            elif list_line[1]:
                dic = storage.all()
                flag = 0
                for key, value in dic.items():
                    if f"{list_line[0]}.{list_line[1]}" == key:
                        del dic[key]
                        storage.save()
                        flag = 1
                        break
                if flag == 0:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """Prints all string representation of all\
            instances based or not on the class name"""

        new_list = []
        dic = storage.all()
        for value in dic.values():
            new_list.append(str(value))
        if line:
            if line not in HBNBCommand.list_of_classes:
                print("** class doesn't exist **")
            else:
                print(new_list)
        else:
            print(new_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""

        list_line = line.split(" ")
        if line:
            list_line = line.split(" ")
            if list_line[0] not in HBNBCommand.list_of_classes:
                print("** class doesn't exist **")
            elif len(list_line) == 1:
                print("** instance id missing **")
            elif list_line[1]:
                dic = storage.all()
                flag = 0
                for key, value in dic.items():
                    if f"{list_line[0]}.{list_line[1]}" == key:
                        if len(list_line) == 2:
                            print("** attribute name missing **")
                            flag = 1
                        elif len(list_line) == 3:
                            print("** value missing **")
                            flag = 1
                        else:
                            if list_line[3][0] == '"':
                                atr_value = list_line[3][1:-1]
                            else:
                                if list_line[3].isdigit():
                                    atr_value = int(list_line[3])
                                else:
                                    atr_value = list_line[3]
                            setattr(value, list_line[2], atr_value)
                            storage.save()
                            flag = 1
                            break
                if flag == 0:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def default(self, line):
        """specfic commands"""

        if '.' in line:
            dic = storage.all()
            cls, method = line.split(".")
            if method == 'all()':
                list_of_cls = []
                for key, value in dic.items():
                    cls_name = str(key).split(".")
                    if cls == cls_name[0]:
                        list_of_cls.append(str(value))
                print(f"[{list_of_cls}]")

            elif method == "count()":
                cnt = 0
                for key, value in dic.items():
                    cls_name = str(key).split(".")
                    if cls == cls_name[0]:
                        cnt += 1
                print(cnt)

            elif method[:6] == "show(\"" and method[-2:] == "\")":
                line = f"{cls} {method[6:-2]}"
                self.do_show(line)

            elif method[:9] == "destroy(\"" and method[-2:] == "\")":
                line = f"{cls} {method[9:-2]}"
                self.do_destroy(line)

            elif method[:8] == "update(\"" and method[-1] == ")":
                args = method[7:-1].split(", ", 1)
                if args[1][0] == "{":
                    dictionary = eval(args[1])
                    for key, value in dictionary.items():
                        if type(value) is int:
                            line = f"{cls} {args[0][1:-1]} {key} {value}"
                        else:
                            line = f"{cls} {args[0][1:-1]} {key} \"{value}\""
                        self.do_update(line)
                else:
                    list_method = method.split(", ")
                    line = f"{cls} {list_method[0][8:-1]} \
{list_method[1][1:-1]} {list_method[2][:-1]}"
                    self.do_update(line)
            else:
                return cmd.Cmd.default(self, line)
        else:
            return cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
