#!/usr/bin/env python3
import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")
    rocky_mountain = NationalPark("Rocky Mountain")
    visitor1 = Visitor("Stephen")
    visitor2 = Visitor("David")
    trip1 = Trip(visitor1, rocky_mountain, "2/6/24", "2/10/24")
    trip2 = Trip(visitor1, rocky_mountain, "2/6/24", "2/10/24")
    print(rocky_mountain.visitors())    


    ipdb.set_trace()
