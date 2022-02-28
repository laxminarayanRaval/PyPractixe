import json

user_data = dict()
fname = "studentsData_json.txt"

def readStudentsData():
    global user_data
    fhandle = open(fname)
    user_data = json.load(fhandle)

    print(user_data)


def writeStudentsData():
    readStudentsData()
    while True:
        name = input("Student Name  : ")
        cors = input("Course  Name  : ")
        univ = input("University    : ")
        grad = input("Obtained Grade: ")
        user_data["Student"].append(dict(Name=name, Course=cors, University=univ, Grade=float(grad)))
        # user_data["Student"].append({"Name": name, "Course": cors, "University": univ, "Grade": grad})

        if "y" == input("Do You want to stop (Y/y) : ").lower():
            print(" Bye ".center(30, '-'))
            break

    data_json = json.dumps(user_data, indent=3)
    # print(data_json)

    # fhandle = open(fname, 'w')
    with open(fname, 'w') as fhandle:
        fhandle.write(data_json)
    # fhandle.close()



writeStudentsData()
# readStudentsData()

# print(user_data)
