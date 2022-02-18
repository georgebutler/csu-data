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
            course_weekly = []
            course_locations = []

            for section in course.sections:
                if section.weekdays not in course_weekly:
                    course_weekly.append(section.weekdays)

                if section.facility_id not in course_locations:
                    course_locations.append(section.facility_id)

            print("> " + str(course))
            # print(">> Sections: " + str(len(course.sections)))
            print(">> How Often: " + str(self.year.yearly_offered[course.id]) + "/3 times yearly.")
            print(">> When: " + ", ".join(course_weekly))
            print(">> Where: " + ", ".join(course_locations))
            print("")

class Year:
    def __init__(self, year):
        self.year = year
        self.yearly_offered = {}
        self.semesters = {
            SEASON_FALL: Semester(SEASON_FALL, self),
            SEASON_SPRING: Semester(SEASON_SPRING, self),
            SEASON_SUMMER: Semester(SEASON_SUMMER, self)
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

            if course.id in self.yearly_offered:
                self.yearly_offered[course.id] = self.yearly_offered[course.id] + 1
            else:
                self.yearly_offered[course.id] = 1