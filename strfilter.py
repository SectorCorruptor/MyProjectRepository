# This module originates from scratch.mit.edu user rizwan4j
# 141 lined program.
# Email: mohammed.r210@outlook.com
# textfilter.py v2.0
# 
# UPDATES:
#
# V2: self.findclosest() is now self.findclosest(place)
#

"""
This modules filters words from a list based on an input.

In the code, what you see are 2 classes, 2 internal
functions, and 3 variables. There are only 2 things to do:

1. Defining. The argument "this" is the list Python will check for
   whether the input suits it. "recinput" is the "base" we're checking
   "this" on, and lastly, "casesenstive". Not stored in the object, only
   there since Python supports case-sensitivity, and if not wanted, it should
   be False, else True.
2. Find closest. Returns a list, with all the possibilities found by
   findclosest()
"""

from sys import version as _vers

__all__ = ["TextFilter", "findclosest", "NotCaseSensitiveError"]

def obtaintill(string, char):
    """
    Internal function.
    """
    i = 0
    j = ""
    while not i == len(string):
        if not string[i] == char:
            j = j + string[i]
            i = i + 1
        else:
            break
    return j

class NotCaseSensitiveError(Exception):
    """
    Raised when the current version of Python is not case-sensitive.
    """
    pass

class TextFilter:
    """
    A TextFilter instance. It can filter words
    from a list based on an input.
    """
    def __init__(self, this, recinput, casesensitive):
        """
        Initialise a TextFilter instance.

        Arguments --
        this - list to filter from  --> list
        recinput - base to filter on  --> str
        casesensitive - whether casesensitivity should affect the results --> bool
        """
        # test for case-sensitivity, if ever since Python Version 3.10.0 it has been case-insensitive
        if 'LoRem Ipsum' != 'Lorem Ipsum': # only difference is that 'r' is lowercase
            if casesensitive:  # meaning 'LoRem IPsuM' is not the same as 'Lorem Ipsum'
                self.this = this
                self.recinput = recinput
            else:  # by default, Python is case-sensitive
                l = 0
                self.this = []
                while not l == len(this):
                    self.this.append(this[l].lower()) # an easy convention is to lowercase all the letters
                    l = l + 1
                self.recinput = recinput.lower() # and of the recinput, so case-sentivity won't affect the results here
            self.inclist = []
        else: # textfilter won't work properly when Python is case-insensitive
            raise NotCaseSensitiveError("current version of Python is not case-sensitive: Python Version " + obtaintill(_vers, " "))
    def findclosest(self, place="first"):
        """
        Return a list of filtered words from self.this based on self.recinput.
        """
        if not str(type(self.recinput)) == "<class 'str'>": # Python 3.10 returns this now
            raise TypeError("type of recinput needs to be str, not " + str(type(self.recinput))[8:-2])
        aimidx = 0 # list item base, every check on aimidx item, if not resembling recinput, change recinput by 1
        aimletidx = 0 # text base, if aimletidx letter of self.recinput is also aimletidx letter of aimidxth item of self.this, continue
        inclist = [] # filtered list
        # bit confusing to understand,
        # so comments in the while loop
        if place == "first": # if ["chant"] == self.this and "ant" == self.recinput: [] == self.findclosest()
            while not aimidx == len(self.this): # do this till all items are checked
                while not aimletidx == len(self.recinput): # do this until all letters are checked, or if loop was broken using break
                    if (self.this[aimidx])[aimletidx] == self.recinput[aimletidx]:
                        # if letter aimletidx of item aimidx in self.this matches letter
                        # aimletidx of self.recinput
                        aimletidx = aimletidx + 1 # continue
                    else: # this is where the break happens
                        aimletidx = "Failure" # needed to inform TextFilter object that matching has failed
                        break # get out of loop
                if aimletidx == "Failure": # loop failed, try next item of self.this
                    aimidx = aimidx + 1
                else:
                    inclist.append(self.this[aimidx]) # results matched, add them to the returned list
                    aimidx = aimidx + 1 # and continue
                aimletidx = 0 # restart letter checking
        elif place == "any": # if ["chant"] == self.this and "ant" == self.recinput: ["chant"] == self.findclosest()
            del aimletidx # not needed here
            while not aimidx == len(self.this): # check each item, but don't go beyond len(self.this)
                if self.recinput in self.this[aimidx]: # if it contains self.recinput, add it
                    inclist.append(self.this[aimidx])
                aimidx = aimidx + 1 # I don't trust aimidx =+ 1
        else: # invalid search type
            if str(type(place)) != "<class 'str'>": # to raise ValueError, type should be correct but not value
                # aggh, type(object) = "<class 'object'> gives one a headache now
                raise TypeError("self.findclosest() argument 1 'place' should be of type str, not " + type(place)[8:-2]) 
            else:
                raise ValueError("self.findclosest() argument 1 'place' should be of values 'first' or 'any', not " + place)
        return inclist # the list of possibilities

def rundemo():
    print("Running textfilter.py test with demo as TextFilter() without case-sensitivity:\n")
    demo = TextFilter(["cherry", "chalk", "bells", "carts"], "ch", False)
    print("demo: TextFilter()")
    print("demo.this: " + str(demo.this) + ", demo.recinput: " + str(demo.recinput))
    print("demo.findclosest(): " + str(demo.findclosest()))
    demo.recinput = "cha"
    print("demo.this: " + str(demo.this) + ", demo.recinput: " + str(demo.recinput))
    print("demo.findclosest(): " + str(demo.findclosest()))
    print("\nRunning textfilter.py test with demo as TextFilter() with case-sensitivity:\n")
    demo = TextFilter(["cherry", "chalk", "bells", "Chants"], "Ch", True)
    print("demo: TextFilter()")
    print("demo.this: " + str(demo.this) + ", demo.recinput: " + str(demo.recinput))
    print("demo.findclosest(): " + str(demo.findclosest()))

run = __name__ == "__main__"
    
if run: # won't run until actually executed
    rundemo()

del _vers, run, obtaintill, rundemo
