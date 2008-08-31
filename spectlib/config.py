# -*- coding: UTF8 -*-

# Specto , Unobtrusive event notifier
#
#       config.py
#
# Copyright (c) 2005-2007, Jean-François Fortin Tam

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.


class Integer() :
    """
    A config node containing a integer value.

    Supports restricting the valid values to a range.
    """

    def __init__(self, mandatory, low=None, high=None) :
        self.mandatory = mandatory
        self.low = low
        self.high = high

    def checkRestrictions(self, value):
        try :
            val = int(value)
        except ValueError :
            #self.logError('Malformed value: cannot parse "%s" as an integer' % (value, ))
            return False, -1
        return True, val
    
    def getStandardValue(self):
        return -1
        
class String() :
    """
    A config node containing a string value.
    """

    def __init__(self, mandatory) :
        self.mandatory = mandatory

    def checkRestrictions(self, value):
        try :
            val = str(value)
        except ValueError :
            #self.logError('Malformed value: cannot parse "%s" as a string' % (value, ))
            return False
        return True, val
    
    def getStandardValue(self):
        return ""
        
class Dec() :
    """
    A config node containing a decimal value.
    """

    def __init__(self, mandatory) :
        self.mandatory = mandatory

    def checkRestrictions(self, value):
        try :
            val = float(value)
        except ValueError :
            #self.logError('Malformed value: cannot parse "%s" as a decimal' % (value, ))
            return False
        return True, val
    
    def getStandardValue(self):
        return -1    
        
class Boolean() :
    """
    A config node containing a boolean value.
    """

    def __init__(self, mandatory) :
        self.mandatory = mandatory

    def checkRestrictions(self, value):
        valid = False
        if value == "True" or value == 1 or value == True:
          val = True
          valid = True
        if value == "False" or value == 0 or value == False:
          val = False
          valid = True
          
        if valid == False:
          return False, ""
        else:
          return True, val
    
    def getStandardValue(self):
        return False 