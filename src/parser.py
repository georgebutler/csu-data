import os, xlrd

# Instructor
class Instructor:
    def __init__(self, name_first, name_last):
        self.name_first = name_first
        self.name_last = name_last

# Course
class Course:
    def __init__(self, id, catalog):
        self.id = id
        self.catalog = catalog
        self.desc = ""
        self.sections = []
    
    def __str__(self):
        return '[Course] ID: {self.id}'.format(self=self)

# Section
class Section:
    def __init__(self, course: Course, number, instructor: Instructor):
        self.course = course
        self.instructor = instructor
        self.number = -1
        self.enroll_cap = -1
        self.enroll_total = -1
        self.waitlist_cap = -1
        self.waitlist_total = -1
        self.facility_id = ""
        self.weekdays = []

    def __str__(self):
        return '[Section] Course: {self.course}'.format(self=self)
    
    def addWeekday(self, weekday):
        self.dates.append(weekday)

# Constants
CELLKEY_Course_ID = 4
CELLKEY_Course_CATALOG = 8

# Globals
courses = []

workbook = xlrd.open_workbook(os.getcwd() + r"\input\Fall-2018-SFO_CS_AR_CLASS_SCHED_ENR_RCAP_176475251.xlsx")
worksheet = workbook.sheet_by_index(0)

for rx in range(2, worksheet.nrows):
    # print(worksheet.row_values(rx))
    # print("")

    courseID = worksheet.cell(rx, CELLKEY_Course_ID).value
    catalog = worksheet.cell(rx, CELLKEY_Course_CATALOG).value

    # section = Section(courseID, catalog)
    # sections.append(section)

    for course in courses:
        print(str(course))
