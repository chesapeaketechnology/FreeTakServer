#######################################################
# 
# link.py
# Python implementation of the Class link
# Generated by Enterprise Architect
# Created on:      11-Feb-2020 11:08:08 AM
# Original author: Corvo
# 
#######################################################


class link:
    def __init__(self, linkType=None, linkuid = None, linkproduction_time=None, linkrelation=None, linktype=None, linkparent_callsign=None):

        argumentsRecieved = locals()

        args = self.createArguments(argumentsRecieved)

        case = {
            
            'timeout':self.timeoutFunc
            
            }
        print(args)
        case[linkType](args)


    def createArguments(self, argumentsRecieved):
        argumentsToBePassed = {}
        for x, y in argumentsRecieved.items():
            if x != 'self' and x != 'argumentsRecieved' and y != None:
                argumentsToBePassed[x] = y
            else:
                pass
        return argumentsToBePassed
    def timeoutFunc(self, args):

        self.setuid(args['linkuid'])

        self.settype(args['linktype'])

        self.setrelation(args['linkrelation'])

    # uid getter 
    def getuid(self): 
        return self.uid 

    # uid setter 
    def setuid(self, uid=0):  
        self.uid=uid 

    # production_time getter 
    def getproduction_time(self): 
        return self.production_time 

    # production_time setter 
    def setproduction_time(self, production_time=0):  
        self.production_time=production_time 

    # relation getter 
    def getrelation(self): 
        return self.relation 

    # relation setter 
    def setrelation(self, relation=0):  
        self.relation=relation 

    # type getter 
    def gettype(self): 
        return self.type 

    # type setter 
    def settype(self, type=0):  
        self.type=type 

    # parent_callsign getter 
    def getparent_callsign(self): 
        return self.parent_callsign 

    # parent_callsign setter 
    def setparent_callsign(self, parent_callsign=0):  
        self.parent_callsign=parent_callsign 
