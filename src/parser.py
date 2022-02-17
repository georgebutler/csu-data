import os, xlrd
from instructor import Instructor
from course import Course
from section import Section

# Constants
CELLKEY_COURSE_ID = 4
CELLKEY_COURSE_CATALOG = 8
CELLKEY_COURSE_DESC = 10
CELLKEY_SECTION_NUMBER = 9
CELLKEY_SECTION_FACILITY = 19
CELLKEY_SECTION_WEEKDAYS = 20
CELLKEY_INSTRUCTOR_LAST = 23
CELLKEY_INSTRUCTOR_FIRST = 24

MONTHKEY_FALL = 7
MONTHKEY_SPRING = 3
MONTHKEY_SUMMER = 5

# Globals
courses = []

workbook = xlrd.open_workbook(os.getcwd() + r"\input\Fall-2018-SFO_CS_AR_CLASS_SCHED_ENR_RCAP_176475251.xlsx")
worksheet = workbook.sheet_by_index(0)

for rx in range(2, worksheet.nrows):
    # print(worksheet.row_values(rx))
    # print("")

    # Extract data from cells
    CELLDATA_Course_ID = worksheet.cell(rx, CELLKEY_COURSE_ID).value
    CELLDATA_Course_CATALOG = worksheet.cell(rx, CELLKEY_COURSE_CATALOG).value
    CELLDATA_Course_DESC = worksheet.cell(rx, CELLKEY_COURSE_DESC).value
    CELLDATA_Section_NUMBER = worksheet.cell(rx, CELLKEY_SECTION_NUMBER).value
    CELLDATA_Section_FACILITY = worksheet.cell(rx, CELLKEY_SECTION_FACILITY).value
    CELLDATA_Section_WEEKDAYS = worksheet.cell(rx, CELLKEY_SECTION_WEEKDAYS).value
    CELLDATA_Instructor_LAST = worksheet.cell(rx, CELLKEY_INSTRUCTOR_LAST).value
    CELLDATA_Instructor_FIRST = worksheet.cell(rx, CELLKEY_INSTRUCTOR_FIRST).value

    course = Course(CELLDATA_Course_ID, CELLDATA_Course_CATALOG, CELLDATA_Course_DESC)
    instructor = Instructor(CELLDATA_Instructor_FIRST, CELLDATA_Instructor_LAST)
    section = Section(course, CELLDATA_Section_NUMBER, instructor, CELLDATA_Section_FACILITY, CELLDATA_Section_WEEKDAYS)

    # section = Section(courseID, catalog)
    # sections.append(section)

    if course in courses:
        existing = courses[courses.index(course)]

        if (section not in existing.sections):
            existing.add_section(section)
    else:
        courses.append(course)

        # Skip this if the section doesn't have an instructor
        if (instructor.name_first and instructor.name_last):
            course.add_section(section)

for course in courses:
    print(str(course))

    course_weekly = []
    course_locations = []

    for section in course.sections:
        if section.weekdays not in course_weekly:
            course_weekly.append(section.weekdays)

        if section.facility_id not in course_locations:
            course_locations.append(section.facility_id)

    print("> Sections: " + str(len(course.sections)))
    print("> When: " + ", ".join(course_weekly))
    print("> Where: " + ", ".join(course_locations))
    print("")

