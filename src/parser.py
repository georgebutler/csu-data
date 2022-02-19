import os
import xlrd
from classes.instructor import Instructor
from classes.course import Course
from classes.section import Section
from classes.year import Year

# Constants
SEASON_FALL = '7'
SEASON_SPRING = '3'
SEASON_SUMMER = '5'

CELLKEY_COURSE_TERM = 0
CELLKEY_COURSE_ID = 4
CELLKEY_COURSE_CATALOG = 8
CELLKEY_COURSE_DESC = 10
CELLKEY_SECTION_NUMBER = 9
CELLKEY_SECTION_FACILITY = 19
CELLKEY_SECTION_WEEKDAYS = 20
CELLKEY_SECTION_ENROLLED_CAP = 14
CELLKEY_SECTION_ENROLLED_TOTAL = 15
CELLKEY_SECTION_WAITLIST_CAP = 16
CELLKEY_SECTION_WAITLIST_TOTAL = 17
CELLKEY_INSTRUCTOR_LAST = 23
CELLKEY_INSTRUCTOR_FIRST = 24

# Globals
years = []

# File Extraction
for filename in os.listdir(os.getcwd() + ".\input"):
    workbook = xlrd.open_workbook(os.path.join(".\input", filename))
    worksheet = workbook.sheet_by_index(0)

    # Extract year from cell
    CELLDATA_YearSeason = worksheet.cell(2, CELLKEY_COURSE_TERM).value
    STRING_Year = CELLDATA_YearSeason[0] + "0" + CELLDATA_YearSeason[1:3]
    year = Year(STRING_Year)

    if (year in years):
        year = years[years.index(year)]
    else:
        years.append(year)

    semester = CELLDATA_YearSeason[3]
    courses = []

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
        CELLDATA_Section_WAITLIST_CAP = worksheet.cell(rx, CELLKEY_SECTION_WAITLIST_CAP).value
        CELLDATA_Section_WAITLIST_TOTAL = worksheet.cell(rx, CELLKEY_SECTION_WAITLIST_TOTAL).value
        CELLDATA_Section_ENROLLED_CAP = worksheet.cell(rx, CELLKEY_SECTION_ENROLLED_CAP).value
        CELLDATA_Section_ENROLLED_TOTAL = worksheet.cell(rx, CELLKEY_SECTION_ENROLLED_TOTAL).value
        CELLDATA_Instructor_LAST = worksheet.cell(rx, CELLKEY_INSTRUCTOR_LAST).value
        CELLDATA_Instructor_FIRST = worksheet.cell(rx, CELLKEY_INSTRUCTOR_FIRST).value

        course = Course(CELLDATA_Course_ID, CELLDATA_Course_CATALOG, CELLDATA_Course_DESC)
        instructor = Instructor(CELLDATA_Instructor_FIRST, CELLDATA_Instructor_LAST)
        section = Section(course, CELLDATA_Section_NUMBER, instructor, CELLDATA_Section_FACILITY, CELLDATA_Section_WEEKDAYS)
        section.waitlist_cap = CELLDATA_Section_WAITLIST_CAP
        section.waitlist_total = CELLDATA_Section_WAITLIST_TOTAL
        section.enroll_cap = CELLDATA_Section_ENROLLED_CAP
        section.enroll_total = CELLDATA_Section_ENROLLED_TOTAL

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
        year.add_course(course, semester)

for year in years:
    output = open(os.getcwd() + ".\output\%s.txt" % year.year, "w")

    output.write(str(year) + "\n")
    output.write("\n")

    print(str(year))
    print("")

    for _, semester in year.semesters.items():
        if (semester.season == SEASON_FALL):
            output.write("Fall\n")
            print("Fall")
        elif (semester.season == SEASON_SPRING):
            output.write("Spring\n")
            print("Spring")
        elif (semester.season == SEASON_SUMMER):
            output.write("Summer\n")
            print("Summer")

        output.write("\n")
        print("----")

        for course in semester.courses:
            course_weekly = []
            course_locations = []

            for section in course.sections:
                if section.weekdays not in course_weekly:
                    course_weekly.append(section.weekdays)

                if section.facility_id not in course_locations:
                    course_locations.append(section.facility_id)

            output.write(str(course) + "\n")
            output.write("> How Often: " + str(semester.year.yearly_offered[course.id]) + "/3 (FALL, SPRING, SUMMER). \n")
            output.write("> When: " + ", ".join(course_weekly) + "\n")
            output.write("> Where: " + ", ".join(course_locations) + "\n")
            output.write("\n")

            print("> " + str(course))
            # print(">> Sections: " + str(len(course.sections)))
            print(">> How Often: " + str(semester.year.yearly_offered[course.id]) + "/3 (FALL, SPRING, SUMMER).")
            print(">> When: " + ", ".join(course_weekly))
            print(">> Where: " + ", ".join(course_locations))
            # print(">> Total Enrollment: " + str(section.enroll_total) + " / " + str(section.enroll_cap))
            print("")

output.close()