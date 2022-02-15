import os, xlrd

# Instructor
class Instructor:
    def __init__(self, name_first, name_last):
        self.name_first = name_first.strip()
        self.name_last = name_last.strip()

    def __repr__(self):
        return (f'{self.__class__.__name__}('f'{self.name_first!r} {self.name_last!r})')

# Course
class Course:
    def __init__(self, id, catalog):
        self.id = id.strip()
        self.catalog = catalog.strip()
        self.desc = ""
        self.sections = []

    def __eq__(self, other):
        return self.id == other.id
    
    def __repr__(self):
        return (f'{self.__class__.__name__}('f'{self.id!r}, {self.catalog!r})')

    def add_section(self, section):
        if section not in self.sections:
            self.sections.append(section)

# Section
class Section:
    def __init__(self, course: Course, number, instructor: Instructor):
        self.course = course
        self.instructor = instructor
        self.number = number
        self.enroll_cap = -1
        self.enroll_total = -1
        self.waitlist_cap = -1
        self.waitlist_total = -1
        self.facility_id = ""
        self.weekdays = []

    def __eq__(self, other):
        return self.number == other.number

    def __repr__(self):
        return (f'{self.__class__.__name__}('f'{self.course!r}, {self.number!r}, {self.instructor!r})')
    
    def add_weekday(self, weekday):
        if weekday not in self.weekdays:
            self.weekdays.append(weekday)

# Constants
CELLKEY_Course_ID = 4
CELLKEY_Course_CATALOG = 8
CELLKEY_Section_NUMBER = 9
CELLKEY_Course_DESC = 10
CELLKEY_Instructor_LAST = 23
CELLKEY_Instructor_FIRST = 24

# Globals
courses = []

workbook = xlrd.open_workbook(os.getcwd() + r"\input\Fall-2018-SFO_CS_AR_CLASS_SCHED_ENR_RCAP_176475251.xlsx")
worksheet = workbook.sheet_by_index(0)

for rx in range(2, worksheet.nrows):
    # print(worksheet.row_values(rx))
    # print("")

    # Extract data from cells
    CELLDATA_Course_ID = worksheet.cell(rx, CELLKEY_Course_ID).value
    CELLDATA_Course_CATALOG = worksheet.cell(rx, CELLKEY_Course_CATALOG).value
    CELLDATA_Section_NUMBER = worksheet.cell(rx, CELLKEY_Section_NUMBER).value
    CELLDATA_Instructor_LAST = worksheet.cell(rx, CELLKEY_Instructor_LAST).value
    CELLDATA_Instructor_FIRST = worksheet.cell(rx, CELLKEY_Instructor_FIRST).value

    course = Course(CELLDATA_Course_ID, CELLDATA_Course_CATALOG)
    instructor = Instructor(CELLDATA_Instructor_FIRST, CELLDATA_Instructor_LAST)
    section = Section(course, CELLDATA_Section_NUMBER, instructor)

    # section = Section(courseID, catalog)
    # sections.append(section)

    if course in courses:
        existing = courses[courses.index(course)]

        if (section not in existing.sections):
            existing.add_section(section)
    else:
        course.add_section(section)
        courses.append(course)

for course in courses:
    print(str(course))

    for section in course.sections:
        print("> " + str(section))

    print("")

