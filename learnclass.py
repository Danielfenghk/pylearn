class RevealAccess(object):
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """
<<<<<<< HEAD

<<<<<<< HEAD
=======
>>>>>>> add second line
<<<<<<< HEAD
>>>>>>> no message
=======
=======
#this is a comment
#add sencond line
#dev4 add
>>>>>>> add by dev4
>>>>>>> add by dev4
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Retrieving', self.name)
        return self.val

    def __set__(self, obj, val):
        print('Updating', self.name)
        self.val = val

