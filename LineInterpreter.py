# LineInterpreter.py
# Written Ian Rankin - April 2021
#
# This is an abstract class to manage to localize the location of the line.


class LineInterpreter():
    def __init__(self):
        pass

    # This function should return the estimated location of the line.
    #
    # @return - location of line to the left or right [-1,0,1] or None if the
    # the line is not detected.
    def get(self):
        raise NotImplementedError('LineInterpreter should be an abstract class')
