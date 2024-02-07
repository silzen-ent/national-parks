class NationalPark:
    all = [] # D2, S1

    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self) #D2, S2
        
    @property # D2, S3
    def name(self):
        return self._name
    
    @name.setter #D2, S4
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, "name") and len(name) >= 3:
            self._name = name
        else:
            raise Exception("Name must be a string and at least 3 characters long")

    def trips(self): #D7, S1
        return [trip for trip in Trip.all if trip.national_park == self]
    
    
    def visitors(self): #D7, S2
        return list({trip.visitor for trip in self.trips()})
    

    def total_visits(self): #D8, S1 Nat'l Park total_visits()
        return len(self.trips())
    

    def best_visitor(self): #D8, S2 Nat'l Park best_visitor()
        visitors = [trip.visitor for trip in self.trips()]
        return max(visitors, key=visitors.count)

    @classmethod # Bonus 1
    def most_visited(cls):
        return max(cls.all, key=lambda park: park.total_visits())
    

class Trip:

    all = [] # D3, S1
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self) # D3, S2


    @property #D3, S3
    def start_date(self):
        return self._start_date
    @start_date.setter #D3, S4
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            self._start_date = start_date
        else:
            raise Exception("Start date must be greater than 7 characters")


    @property #D3, S5
    def end_date(self):
        return self._end_date
    @end_date.setter #D3, S6
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            self._end_date = end_date
        else: 
            raise Exception("End date must be greater than 7 characters")

    
    @property #D4
    def visitor(self): 
        return self._visitor
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor


    @property #D5, S1
    def national_park(self):
        return self._national_park
    @national_park.setter #D5, S2
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park


class Visitor: 
    all = [] # D1, S1

    def __init__(self, name): # D1, S2
        self.name = name
        Visitor.all.append(self)
        # type(self.all).append(self)

    @property # D1, S3
    def name(self):
        return self._name
    
    @name.setter # D1, S4
    def name(self, name):
        if isinstance(name, str) and 1<= len(name) <= 15:
            self._name = name
        else:
            raise Exception("Name must be between 1 and 15 characters")


    def trips(self): #D6, S1
        return [trip for trip in Trip.all if trip.visitor == self]

    
    def national_parks(self): #D6, S2
        return list({trip.national_park for trip in self.trips()})
    

    def total_visits_at_park(self, park): # D9
        if park.visitors() is None:
            return 0 
        return len([trip for trip in self.trips() if trip.national_park == park])