#!/usr/bin/python3

class example(object):
    var1 = 3
    var2 = "this is a string"
    var3 = []

    def turn_to_list(self):
        pass
    def turn_to_string(self):
        print("can I see var1 {0}".format(var1))

thisisaclass = example()
thisisaclass.turn_to_string()