import pprint
stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuffs = {'first': 123, 'second': 456, 'third': {1:1, 2:2}}

tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead',('parrot', ('fresh fruit',))))))))
stuffer = ['a' * 10, tup, ['a' * 30, 'b' * 30], ['c' * 20, 'd' * 20]]
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stuff)

pprint.pprint(stuffer)
pp.pprint(stuffs)
