#!/usr/bin/python3
class MyInt(int):
    """
    this a class to change operations
    """
    def __eq__(self, other):
        """
        inverts the behaviour of  ==
        """
        return super().__ne__(other)
    def __ne__(self, other):
        """
        inverts the behavior of !=
        """
        return super().__eq__(other)
