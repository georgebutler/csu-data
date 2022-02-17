import os, xlrd
from instructor import Instructor
from course import Course
from section import Section
from year import Year

# Constants
CELLKEY_COURSE_TERM = 0
CELLKEY_COURSE_ID = 4
CELLKEY_COURSE_CATALOG = 8
CELLKEY_COURSE_DESC = 10
CELLKEY_SECTION_NUMBER = 9
CELLKEY_SECTION_FACILITY = 19
CELLKEY_SECTION_WEEKDAYS = 20
CELLKEY_INSTRUCTOR_LAST = 23
CELLKEY_INSTRUCTOR_FIRST = 24

# Globals
for filename in os.listdir(os.getcwd() + ".\input"):
    workbook = xlrd.open_workbook(os.path.join(".\input", filename))
    worksheet = workbook.sheet_by_index(0)

    # Extract year from cell
    CELLDATA_YearSeason = worksheet.cell(2, CELLKEY_COURSE_TERM).value

    year = Year(CELLDATA_YearSeason[0] + "0" + CELLDATA_YearSeason[1:3])
    semester = CELLDATA_YearSeason[3]
    courses = []
    print("- " + str(year))
    print("")

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
        print("-- " + str(course))
        year.add_course(course, semester)

        course_weekly = []
        course_locations = []

        for section in course.sections:
            if section.weekdays not in course_weekly:
                course_weekly.append(section.weekdays)

            if section.facility_id not in course_locations:
                course_locations.append(section.facility_id)

        print("--- Sections: " + str(len(course.sections)))
        print("--- When: " + ", ".join(course_weekly))
        print("--- Where: " + ", ".join(course_locations))
        print("")

