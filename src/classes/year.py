from collections import Counter

SEASON_FALL = '7'
SEASON_SPRING = '3'
SEASON_SUMMER = '5'

# https://stackoverflow.com/questions/9890364/combine-two-dictionaries-and-remove-duplicates-in-python
def DictListUpdate(lis1, lis2):
    for aLis1 in lis1:
        if aLis1 not in lis2:
            lis2.append(aLis1)
    return lis2

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
        self.courses = []
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
        if course not in self.courses:
            self.courses.append(course)
        
        if course not in self.semesters[semester_code].courses:
            self.semesters[semester_code].courses.append(course)

            converted_code = ""

            if (semester_code == SEASON_FALL):
                converted_code = "Fall"
            elif (semester_code == SEASON_SPRING):
                converted_code = "Spring"
            elif (semester_code == SEASON_SUMMER):
                converted_code = "Summer"

            if course.id not in self.yearly_offered:
                self.yearly_offered[course.id] = []
            
            self.yearly_offered[course.id].append(converted_code)