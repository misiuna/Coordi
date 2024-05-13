from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

import json

from .models import *

# INDEX VIEW
@login_required
def index(request):
    user = request.user #logined in user
    now = datetime.now()
    time = now.time().hour
    if user.user_type == "student":
        return render(request, 'coordi/studentDashboard.html', {
            "user" : user,
            "now" : time,
            "newGrades" : Assignments.objects.filter(student_id = user.id, graded__isnull=False).count(),
            "newAssignments" : Assignments.objects.filter(student_id = user.id, assigned__isnull=False, completed__isnull=True).count(),
        })
    if user.user_type == "teacher":
        assignments = Assignments.objects.all()
        toGrade = []
        for assignment in assignments:
            if assignment.completed != None and assignment.graded == None:
                toGrade.append(assignment)
        return render(request, "coordi/teacherDashboard.html", {
            "user" : user,
            "now" : time,
            "toGradeCount" : len(toGrade)
        })

# CLASSROOM VIEW TEACHER
@login_required
def classroom(request):
    students = User.objects.filter(user_type = "student")

    for student in students:
        # count of all students assignments
        count = student.assignments_set.all().count()
        # count of all assignments per student
        student.count = count
        ready = 0
        graded = 0
        for assignment in student.assignments_set.all():
            if assignment.completed:
                ready = ready + 1
            if assignment.graded:
                graded = graded + 1
        # count of all assignments submitted per student
        student.ready = ready
        # count of all assignments graded per student
        student.graded = graded
        print(student)
        print("PRINTING Assignments ready to grade")
        print(student.ready)
        print("PRINTING ALREADY GRADED assignments")
        print(student.graded)
        student.toGrade = ready - graded
        if count == 0 or graded == 0:
            student.progress = 0
        else:
            student.progress = ( graded/count ) * 100
        print("PRINTING graded/count")
        print(graded/count)
        print("END LOOP")

    return render(request, "coordi/classroom.html", {
        "students" : students,
        "count" : count
    })

# LIBRARY VIEW TEACHER
@login_required
def library(request):
    customLibrary = CustomGO.objects.all()
    return render(request, "coordi/goLibrary.html", {
        "customLibrary" : customLibrary,
    })

# SAVE_CUSTOM VIEW TEACHER
@login_required
def save_custom_go(request):
    if request.method == "POST":
        custom = json.loads(request.body)
        type = custom.get("type")
        namesave = custom.get("nameSave")
        instruction = custom.get("instruction")
        numRows = custom.get("numRows")
        col1Title = custom.get("col1Title")
        col2Title = custom.get("col2Title")

        newCustom = CustomGO.objects.create(
            type = type,
            name = namesave,
            instruction = instruction,
            numRows = numRows,
            col1Title = col1Title,
            col2Title = col2Title
        )
        newCustom.save()
        return HttpResponseRedirect(reverse(index))

#RENDER CUSTOM VIEW TEACHER
def render_custom(request, id):
    user = request.user
    students = User.objects.filter(user_type = "student")
    template = CustomGO.objects.get(id=id)
    load = template.type
    numRows = template.numRows
    isTeacher = False
    if user.user_type == "teacher":
        isTeacher = True    
    
    if load == "twoCol":
        return render(request, "coordi/twoCol.html", {
            "template" : template,
            "load" : load,
            "range" : range(numRows),
            "students" : students,
            "isTeacher" : isTeacher,
        })
    
#RENDER CUSTOM VIEW STUDENT -- DONT THINK IM USING IT
def render_assignments(request, id):
    user = request.user
    students = User.objects.filter(user_type = "student")
    template = CustomGO.objects.get(id=id)
    load = template.type
    numRows = template.numRows
    isTeacher = False
    if user.user_type == "teacher":
        isTeacher = True

    if load == "twoCol":
        return render(request, "coordi/twoCol.html", {
            "template" : template,
            "load" : load,
            "range" : range(numRows),
            "students" : students,
            "isTeacher" : isTeacher,
        })

# TWO_COL_CHART VIEW Empty template TEACHER SIDE
def two_col_chart(request):
    return render(request, "coordi/two_col_chart.html")

# ASSIGN VIEW TEACHER
@login_required
def assign(request, id):
    now = datetime.now()
    allStudents = User.objects.filter(user_type = "student")
    if request.method == "POST":
        go_id = CustomGO.objects.get(pk=id)
        # if all students selected, select all students
        # make an array of students
        students = request.POST.getlist('student', '')
        if "allStudents" in students:            
            for student in allStudents:
                student_id = User.objects.get(username = student)
                # assign to all students
                # if assignment already assigned to a student ERROR
                if Assignments.objects.filter(student_id = student_id, go_id = go_id):
                    return HttpResponse(f"{go_id.name} was already assigned to {student}")
                newAssignment = Assignments.objects.create(
                    student_id = User.objects.get(username = student),
                    go_id = CustomGO.objects.get(pk=id),
                    assigned = now
                )
                newAssignment.save()
            return HttpResponseRedirect(reverse(assignments))
        else:
            for student in students:
                student = User.objects.get(first_name=student)
                print(Assignments.objects.filter(student_id = student.id, go_id = go_id))
                if Assignments.objects.filter(student_id = student.id, go_id = go_id):
                    return HttpResponse(f"{go_id.name} was already assigned to {student}")
                #assign to only selected
                newAssignment = Assignments.objects.create(
                    student_id = User.objects.get(username = student),
                    go_id = CustomGO.objects.get(pk=id),
                    assigned = now
                )
                newAssignment.save()
            return HttpResponseRedirect(reverse(assignments))
    return render(request, "coordi/assignments.html")

# MY ASSIGNMENTS TEACHER VIEW  
@login_required
def assignments(request):
    assignments = Assignments.objects.all().order_by('-assigned')
    return render(request, "coordi/assignments.html", {
        "assignments" : assignments
    })

# CUSTOM ASSIGNMENTS TEACHER VIEW  
@login_required
def assignments_custom(request, id):
    student = User.objects.get(pk = id)
    assignments = Assignments.objects.filter(student_id = student).order_by('-assigned')
    return render(request, "coordi/assignmentsCustom.html", {
        "assignments" : assignments,
        "student" : student
    })

# ASSIGNMENTS STUDENT VIEW  
@login_required
def assignments_student(request):
    user = request.user.id
    studentAssignments = Assignments.objects.filter(student_id = user)
    current = Assignments.objects.filter(student_id = user, assigned__isnull=False, graded__isnull=True)
    past = Assignments.objects.filter(student_id = user, graded__isnull=False)
    print(studentAssignments)
    for assignment in studentAssignments:
        assignment.goid = assignment.go_id.id
        assignment.name = CustomGO.objects.get(id = assignment.go_id.id)
        
    return render(request, "coordi/assignmentsStudents.html", {
        "assignments" : studentAssignments,
        "current" : current,
        "currentCount" : current.count(),
        "past" : past,
        "pastCount" : past.count(),
    })

# SUBMIT STUDENT 
@login_required
def submit_student(request):
    student_id = request.user.id
    
    now = datetime.now()

    if request.method == "POST":
        submit = json.loads(request.body)
        go_id = submit.get("go_id")
        answer1 = submit.get("answer1")
        answer2 = submit.get("answer2")
        answer3 = submit.get("answer3")
        answer4 = submit.get("answer4")
        answer5 = submit.get("answer5")
        answer6 = submit.get("answer6")
        answer7 = submit.get("answer7")
        answer8 = submit.get("answer8")

        assignment = Assignments.objects.get(student_id = student_id, go_id = CustomGO.objects.get(pk=go_id))
        print("PRINTING")
        print(assignment)
        print(assignment.id)
        newSubmit = Data.objects.create(
            student_id = User.objects.get(pk=student_id), 
            assignment_id = Assignments.objects.get(student_id = student_id, go_id = CustomGO.objects.get(pk=go_id)),
            go_id = CustomGO.objects.get(pk=go_id), 
            answer1 = answer1, 
            answer2 = answer2, 
            answer3 = answer3, 
            answer4 = answer4, 
            answer5 = answer5, 
            answer6 = answer6, 
            answer7 = answer7, 
            answer8 = answer8
        )
        newSubmit.save()
        
        submitCompleted = now
        assignment.completed = submitCompleted
        assignment.save()
        return HttpResponseRedirect(reverse(index))

# GRADES TEACHER
@login_required
def grades(request):
    assignments = Assignments.objects.all()
    toGrade = []
    for assignment in assignments:
        if assignment.completed != None and assignment.graded == None:
            toGrade.append(assignment)
        student = User.objects.get(pk = assignment.student_id.id)
        assignment.student_first = student.first_name
        assignment.student_last = student.last_name
        go = CustomGO.objects.get(pk = assignment.go_id.id)
        assignment.title = go.name
    return render(request, "coordi/grades.html", {
        "toGrade" : toGrade,
        "toGradeCount" : len(toGrade),
        })   

# TEMPLATE FOR GRADING TEACHER
@login_required
def grade_template(request, id):
    now = datetime.now()
    assignment = Assignments.objects.get(pk=id)
    data = Data.objects.get(assignment_id = assignment.id)
    template = data.go_id
    numRows = template.numRows
    answers = [data.answer1, data.answer2]
    answers1 = [data.answer3, data.answer4]
    answers2 = [data.answer5, data.answer6] 
    answers3 = [data.answer7, data.answer8]

    if request.method == "POST":
        grade = request.POST["grade"]
        if grade == "Choose the grade":
            return render(request, "coordi/grade_template.html", {
            "student" : User.objects.get(pk = assignment.student_id.id),
            "assignment" : assignment,
            "data" : data,
            "template" : template,
            "range" : range(numRows),
            "range2" : range(2),
            "answers" : answers,
            "answers1" : answers1,
            "answers2" : answers2,
            "answers3" : answers3,
            "message" : "Did you forget to choose the grade?"
        }) 
        assignment.graded = now
        assignment.grade = grade
        assignment.save()
        return HttpResponseRedirect(reverse(index))

    return render(request, "coordi/grade_template.html", {
        "student" : User.objects.get(pk = assignment.student_id.id),
        "assignment" : assignment,
        "data" : data,
        "template" : template,
        "range" : range(numRows),
        "range2" : range(2),
        "answers" : answers,
        "answers1" : answers1,
        "answers2" : answers2,
        "answers3" : answers3
    })

# GRADES STUDENT VIEW  
@login_required
def grades_student(request):
    user = request.user.id
    assignments = Assignments.objects.filter(student_id = user, graded__isnull=False).order_by('-assigned')
    return render(request, "coordi/gradesStudents.html", {
        "assignments" : assignments
    })

# PROFILE STUDENT VIEW  
@login_required
def profile_student(request):
    user = request.user
    assignments = Assignments.objects.filter(student_id = user.id).order_by('-assigned')
    submissions = assignments.filter(completed__isnull=False)
    grades = assignments.filter(completed__isnull=False, graded__isnull=False)
    gradeTotal = 0
    gradeCount = 0

    for assignment in assignments:
        grade = assignment.grade
        percent = gradeToPercentage(grade)
        if percent != None:
            gradeTotal = gradeTotal +  percent
            gradeCount = gradeCount + 1

    avgGrade = gradeTotal / gradeCount
    print("PRINTING")
    print(avgGrade)

    return render(request, "coordi/profileStudent.html", {
        "assignments" : assignments,
        "user" : user,
        "submissions" : submissions,
        "avgGrade" : int(avgGrade),
        "grades" : grades,
    })

def gradeToPercentage(grade):
    if grade == "A":
        return 100
    elif grade == "B":
        return 79
    elif grade == "C":
        return 64
    elif grade == "D":
        return 54
    elif grade == "E":
        return 49

#to avoid errors do not call login view just "login". Can not have a function def login and a library import with the same name.
def login_view(request):
    #signing in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        #authenticating the user 
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse(index))  
        else:
            return render(request, "coordi/login.html", {
                "message" : 'Invalid username and/or password.'
            })   
    return render(request, "coordi/login.html")

def logout_view(request):
    logout(request)
    return render(request, "coordi/login.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        print("PRINTING")
        print(request.POST)
        firstName = request.POST["firstName"]
        last = request.POST["lastName"]
        print(last)
        password = request.POST["password"]
        confirm = request.POST["confirm"]
        userType = request.POST["settings"]

        #password confirmation
        if password != confirm:
            return render(request, "coordi/register.html", {
                "message" : "Password does not match confirmation password"
            })
        
        #create new user
        try:
            user = User.objects.create_user(username = username, email = email, first_name = firstName, last_name = last, password = password)
            user.user_type = userType
            user.save()
        except IntegrityError:
            return render(request, "coordi/register", {
                "message" : "Unable to add user to database"
            })
        login(request, user)
        return HttpResponseRedirect(reverse(index))
    else:
        return render(request, "coordi/register.html")
