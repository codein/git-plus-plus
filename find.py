# import cmd

# class HelloWorld(cmd.Cmd):
#     """Simple command processor example."""

#     def do_greet(self, person):
#         if person:
#             print "hi,", person
#         else:
#             print 'hi'

#     def help_greet(self):
#         print '\n'.join([ 'greet [person]',
#                            'Greet the named person',
#                            ])

#     def do_EOF(self, line):
#         print

# if __name__ == '__main__':
#     HelloWorld().cmdloop()

# import readline

# addrs = ['angela@domain.com', 'michael@domain.com', 'david@test.com']

# def completer(text, state):
#     options = [x for x in addrs if x.startswith(text)]
#     try:
#         return options[state]
#     except IndexError:
#         return None

# readline.set_completer(completer)
# readline.parse_and_bind("tab: complete")

# while 1:
#     a = raw_input("> ")
#     print "You entered", a

