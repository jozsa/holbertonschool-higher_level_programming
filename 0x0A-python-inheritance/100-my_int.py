#!/usr/bin/python3
class MyInt(int):
    """
    class MyInt inherited from int
    """
    def __ne__(self, other):
        """Redefines != to mean =="""
        return MyInt == MyInt

    def __eq__(self, other):
        """Redefines == to mean !="""
        return MyInt != MyInt
