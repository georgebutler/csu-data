SEASON_FALL = '7'
SEASON_SPRING = '3'
SEASON_SUMMER = '5'

class Semester:
    def __init__(self, season, year):
        self.season = season
        self.year = year
        self.courses = []

    def __eq__(self, other):
        return self.season == other.season

    def __repr__(self):
        return (f'{self.__class__.__name__}('f'{self.season!r})')

class Year:
    def __init__(self, year):
        self.year = year
        self.yearly_offered = {}
        self.enrolled_average = {}
        self.semesters = {
            SEASON_FALL: Semester(SEASON_FALL, self),
            SEASON_SPRING: Semester(SEASON_SPRING, self),
            SEASON_SUMMER: Semester(SEASON_SUMMER, self)
        }

    def __eq__(self, other):
        return self.year == other.year

    def __repr__(self):
        return (f'{self.__class__.__name__}('f'{self.year!r})')

    def add_course(self, course, semester_code):
        if course not in self.semesters[semester_code].courses:
            self.semesters[semester_code].courses.append(course)

            if course.id in self.yearly_offered:
                self.yearly_offered[course.id] = self.yearly_offered[course.id] + 1
            else:
                self.yearly_offered[course.id] = 1