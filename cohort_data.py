def unique_houses(filename):
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called "houses" that holds those names.

        ex. houses = set([ "Hufflepuff",
                    "Slytherin",
                    "Ravenclaw",
                    "Gryffindor",
                    "Dumbledore's Army"
            ])

    """

    houses = set()

    data_file = open(filename)
    for file in data_file:
        line = file.split("|")
        house = line[2]
        if house != "":
            houses.add(house)

    data_file.close()


    return houses


def sort_by_cohort(filename):
    """TODO: Sort students by cohort, skipping instructors.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name. Puts ghosts into a separate list entitled "ghosts".
    Returns a list of these lists.

        ex. fall_15 = ["Colin Creevey", "Dennis Creevey", "Seamus Finnigan", ""Hermione Granger", ... ]
        ex. all_students = [["Colin Creevey", "Dennis Creevey", "Seamus Finnigan", ...],
        ["Lee Jordan", "Andrew Kirke", "Neville Longbottom", ...],
        ["Cormac McLaggen", "Parvati Patil", "Jimmy Peakes", ...], 
        ["Euan Abercrombie", "Katie Bell", "Lavender Brown", ...]]

    """

    all_students = []
    winter_16 = []
    spring_16 = []
    summer_16 = []
    fall_15 = []
    ghosts = []

    data_file = open(filename)
    for file in data_file:
        line = file.rstrip()
        data = line.split("|")
        cohort = data[4]

        name = "{}, {}".format(data[0], data[1])        

        if cohort == "G":
            ghosts.append(name)

        elif cohort == "Winter 2016":
            winter_16.append(name)

        elif cohort == "Spring 2016":
            spring_16.append(name)

        elif cohort == "Summer 2016":
            summer_16.append(name)

        elif cohort == "Fall 2015":
            fall_15.append(name)

    fall_15 = sorted(fall_15)
    winter_16 =  sorted(winter_16)
    spring_16 =  sorted(spring_16)
    summer_16 =  sorted(summer_16)


        
    all_students.append(fall_15)
    all_students.append(winter_16)
    all_students.append(spring_16)
    all_students.append(summer_16)

    data_file.close()


    return all_students


def students_by_house(filename):
    """TODO: Sort students by house.


    Iterates over the data to create a list for each house, and sorts students
    into their appropriate houses by last name. Sorts ghosts into a list called "ghosts"
    and instructors into a list called "instructors".
    Returns all lists in one list of lists.

        ex. gryffindor = ["Abercrombie", "Bell", "..." ]
        ex. ghosts = ["Baron", "Friar", "..."]
        ex. all_students = [ hufflepuff,
                    gryffindor,
                    ravenclaw,
                    slytherin,
                    dumbledores_army,
                    ghosts,
                    instructors
        ]

    """

    all_students = []
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    ravenclaw = []
    ghosts = []
    instructors = []

    data_file = open(filename)
    for file in data_file:
        line = file.rstrip()
        data = line.split("|")
        house = data[2]
        cohort = data[4]
        name = "{}, {}".format(data[1], data[0])        

        if cohort == "G":
            ghosts.append(name)

        elif cohort == "I":
            instructors.append(name)

        else:
            if house == "Gryffindor":
                gryffindor.append(name)
            elif house == "Hufflepuff":
                hufflepuff.append(name)
            elif house == "Slytherin":
                slytherin.append(name)
            elif house == "Ravenclaw":
                ravenclaw.append(name)
            elif house == "Dumbledore's Army":
                dumbledores_army.append(name)

    gryffindor = sorted(gryffindor)
    hufflepuff = sorted(hufflepuff)
    slytherin = sorted(slytherin)
    ravenclaw = sorted(ravenclaw)
    ghosts = sorted(ghosts)
    instructors = sorted(instructors)

    all_students.append(ghosts)
    all_students.append(instructors)
    all_students.append(gryffindor)
    all_students.append(hufflepuff)
    all_students.append(slytherin)
    all_students.append(ravenclaw)
    all_students.append(dumbledores_army)


    data_file.close()


    return all_students


def all_students_tuple_list(filename):
    """TODO: Create a list of tuples of student data.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. student_list = [
                ("Euan Abercrombie", "Gryffindor", "McGonagall", "Summer 2016"),
                ("Katie Bell", "Gryffindor", "McGonagall", "Summer 2016"),
                # ...
            ]
    """

    student_list = []

    data_file = open(filename)
    for file in data_file:
        line = file.rstrip()
        data = line.split("|")
        house = (data[2],)
        cohort = (data[4],)
        name = ("{}, {}".format(data[0], data[1]),)
        instructor = (data[3],)
        student_tuple = name + house + instructor + cohort

        student_list.append(student_tuple)

        # data_file.close()

    return student_list


def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Uses the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name from the command line, returns that
    student's cohort, or returns "Student not found." when appropriate. """

    ask_student = raw_input("What student are you looking: (name) ")
    full_name = ask_student.split()
    name = full_name[0].lower()
    for student_tuple in student_list:
        info_student = student_tuple
        name_info = info_student[0]
        name_student = name_info.lower().split(",")
        first_name = name_student[0]

        if first_name == name:
            print "The student {}, in the house: {}, is in the cohort {}".format(info_student[0], info_student[1], student_tuple[3])
        
        
    return "Student not found."


##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Using set operations, make a set of student last names that have duplicates.

    Iterates over the data to find any last names that exist across all cohorts.
    Uses set operations (set math) to create a set of these names.
    NOTE: Do not include staff -- or do, if you want a greater challenge.

       ex. duplicate_names = set(["Weasley"])

    """

    duplicate_names = set()
    last_name_set = set()
    
    data_file = open(filename)
    for file in data_file:
        line = file.rstrip()
        data = line.split("|")
        last_name = data[1]
        if not last_name in last_name_set:
            last_name_set.add(last_name)
        else:
            duplicate_names.add(last_name)

    return duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Create a function that prompts the user for a name via the command line
    and when given a name, print a statement of everyone in their house in their cohort.

    Uses the list of tuples generated by all_students_tuple_list to make a small function
    that, when given a student's first and last name, print students that are in both
    that student's cohort and that student"s house.

    ex: Choose a student: Hermione Granger
        Hermione Granger was in house Gryffindor in the Fall 2015
        cohort.
        The following students are also in their house:
        Seamus Finnigan
        Angelina Johnson
        Harry Potter
        Ron Weasley
        Oliver Wood


    """

    ask_student = raw_input("What student are you looking: (name) ")
    full_name = ask_student.split()
    name = full_name[0].lower()
    
    students_in_house = set()

    for student_tuple in student_list:
        name_info = student_tuple[0]
        name_student = name_info.lower().split(",")[0]

        if name_student == name:
            student_house = student_tuple[1]
            cohort_student = student_tuple[3]
            break
    
    for student_tuple in student_list:
        if student_tuple[1] == student_house and student_tuple[3] == cohort_student and student_tuple[0] != name_info:
            students_in_house.add(student_tuple[0])
                
    print """The student {}, in the house: {}, is in the cohort {}
        The following students are also in their house {}""".format(name_info, student_house, cohort_student, ". ".join(students_in_house))



#########################################################################################

# Here is some useful code to run these functions!

# print "This are the Houses of Howgarts"

# print unique_houses("cohort_data.txt")

# print "This are the Students of Howgarts"

# print sort_by_cohort("cohort_data.txt")

# print "We, the people of Hogwarts"

# print students_by_house("cohort_data.txt")

# print 

all_students_data = all_students_tuple_list("cohort_data.txt")

# #print all_students_data

# find_cohort_by_student_name(all_students_data)

#print find_name_duplicates("cohort_data.txt")

find_house_members_by_student_name(all_students_data)
