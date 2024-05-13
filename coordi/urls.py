from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("my_classroom", views.classroom, name="classroom"),
    path("my_library", views.library, name="library"),
    path("my_assignments", views.assignments, name="assignments"),
    path("assignments_custom/<int:id>", views.assignments_custom, name="assignments_custom"),
    path("grades", views.grades, name="grades"),
    path("grade_template/<int:id>", views.grade_template, name="grade_template"),
    path("my_library/two_col_chart", views.two_col_chart , name="two_col_chart"),

    path("assignments_student", views.assignments_student, name="assignments_student"),
    path("submit_student", views.submit_student, name="submit_student"),
    path("grades_student", views.grades_student, name="grades_student"),
    path("profile_student", views.profile_student, name="profile_student"),
    
    path("save_custom_go", views.save_custom_go, name="save_custom_go"),
    path("assign/<int:id>", views.assign, name="assign"),
    path("custom/<int:id>", views.render_custom, name="custom"),
    
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register")
]