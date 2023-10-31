class NationalPark:
    all = []
    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) >= 3 and not hasattr(self, "name"):
            self._name = new_name

    def trips(self):
        return list({trip for trip in Trip.all if trip.national_park is self})
    
    def visitors(self):
        return list({trip.visitor for trip in self.trips()})
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visitors = [trip.visitor for trip in self.trips()]
        return max(set(visitors), key = visitors.count)


class Trip:
    
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, new_start):
        if isinstance(new_start, str) and len(new_start) >= 7:
            self._start_date = new_start

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, new_end):
        if isinstance(new_end, str) and len(new_end) >= 7:
            self._end_date = new_end


    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor

    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park


class Visitor:
    all = []

    def __init__(self, name):
        self.name = name
        Visitor.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_visitor):
        if isinstance(new_visitor, str) and 1 <= len(new_visitor) <= 15:
            self._name = new_visitor

    def trips(self):
        return list({trip for trip in Trip.all if trip.visitor == self})
    
    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})
    
    def total_visits_at_park(self, park):
        if not park.visitors():
            return len(trip for trip in self.trips() if trip.national_park == park)