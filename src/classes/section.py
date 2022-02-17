class Section:
    def __init__(self, course, number, instructor, facility, weekdays):
        self.course = course
        self.instructor = instructor
        self.number = number.strip()
        self.enroll_cap = -1
        self.enroll_total = -1
        self.waitlist_cap = -1
        self.waitlist_total = -1
        self.facility_id = facility.strip()
        self.weekdays = weekdays.strip()

    def __eq__(self, other):
        return self.number == other.number

    def __repr__(self):
        return (f'{self.__class__.__name__}('f'{self.course!r}, {self.number!r}, {self.weekdays!r}, {self.instructor!r})')