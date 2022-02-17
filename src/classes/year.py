SEASON_FALL = '7'
SEASON_SPRING = '3'
SEASON_SUMMER = '5'

class Semester:
    def __init__(self, season):
        self.season = season
        self.courses = []

    def __eq__(self, other):
        return self.season == other.season

    def __repr__(self):
        return (f'{self.__class__.__name__}('f'{self.season!r})')

    def display(self):
        print("----")

        if (self.season == SEASON_FALL):
            print("Fall")
        elif (self.season == SEASON_SPRING):
            print("Spring")
        elif (self.season == SEASON_SUMMER):
            print("Summer")
        else:
            print("Unknown Season")

        print("----")
        for course in self.courses:
            print(str(course))

class Year:
    def __init__(self, year):
        self.year = year
        self.semesters = {
            SEASON_FALL: Semester(SEASON_FALL),
            SEASON_SPRING: Semester(SEASON_SPRING),
            SEASON_SUMMER: Semester(SEASON_SUMMER)
        }

    def __eq__(self, other):
        return self.year == other.year

    def __repr__(self):
        return (f'{self.__class__.__name__}('f'{self.year!r})')

    def display(self):
        print("============")
        print(str(self))
        print("============")

        for _, semester in self.semesters.items():
            semester.display()

    def add_course(self, course, semester_code):
        if course not in self.semesters[semester_code].courses:
            self.semesters[semester_code].courses.append(course)