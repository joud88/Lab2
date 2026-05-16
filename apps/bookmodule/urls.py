from django.urls import path
from . import views




urlpatterns = [
    path('', views.index, name="index"),
    path('list_books/', views.list_books, name="list_books"),
    path('<int:bookId>/', views.view_one_book, name="view_one_book"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('html5/links/', views.html5_links, name="html5_links"),
    path('html5/text/formatting/', views.text_formatting, name="text_formatting"),
    path('html5/listing/', views.html5_listing, name="html5_listing"),
    path('html5/tables/', views.html5_tables, name="html5_tables"),
    path('search/', views.search_books, name='search_books'),
    path('simple/query', views.simple_query, name='simple_query'),
    path('complex/query', views.complex_query, name='complex_query'),
    path('lab8/task1', views.lab8_task1, name='lab8_task1'),
    path('lab8/task2', views.lab8_task2, name='lab8_task2'),
    path('lab8/task3', views.lab8_task3, name='lab8_task3'),
    path('lab8/task4', views.lab8_task4, name='lab8_task4'),
    path('lab8/task5', views.lab8_task5, name='lab8_task5'),
    path('lab8/task7', views.lab8_task7, name='lab8_task7'),
    path('lab9/task1', views.lab9_task1, name='lab9_task1'),
    path('lab9/task2', views.lab9_task2, name='lab9_task2'),
    path('lab9/task3', views.lab9_task3, name='lab9_task3'),
    path('lab9/task4', views.lab9_task4, name='lab9_task4'),
    path('lab9/task5', views.lab9_task5, name='lab9_task5'),
    path('lab9/task6', views.lab9_task6, name='lab9_task6'),
    path('lab9_part1/listbooks', views.lab9_part1_listbooks, name='lab9_part1_listbooks'),
    path('lab9_part1/addbook', views.lab9_part1_addbook, name='lab9_part1_addbook'),
    path('lab9_part1/editbook/<int:id>', views.lab9_part1_editbook, name='lab9_part1_editbook'),
    path('lab9_part1/deletebook/<int:id>', views.lab9_part1_deletebook, name='lab9_part1_deletebook'),
    path('lab9_part2/listbooks', views.lab9_part2_listbooks, name='lab9_part2_listbooks'),
    path('lab9_part2/addbook', views.lab9_part2_addbook, name='lab9_part2_addbook'),
    path('lab9_part2/editbook/<int:id>', views.lab9_part2_editbook, name='lab9_part2_editbook'),
    path('lab9_part2/deletebook/<int:id>', views.lab9_part2_deletebook, name='lab9_part2_deletebook'),
     path('addresses/', views.address_list, name='address_list'),
    path('addresses/add/', views.address_add, name='address_add'),
    path('addresses/update/<int:id>/', views.address_update, name='address_update'),
    path('addresses/delete/<int:id>/', views.address_delete, name='address_delete'),

    # Task 1: Student
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_add, name='student_add'),
    path('students/update/<int:id>/', views.student_update, name='student_update'),
    path('students/delete/<int:id>/', views.student_delete, name='student_delete'),

    # Task 2: Address2
    path('addresses2/', views.address2_list, name='address2_list'),
    path('addresses2/add/', views.address2_add, name='address2_add'),
    path('addresses2/update/<int:id>/', views.address2_update, name='address2_update'),
    path('addresses2/delete/<int:id>/', views.address2_delete, name='address2_delete'),

    # Task 2: Student2
    path('students2/', views.student2_list, name='student2_list'),
    path('students2/add/', views.student2_add, name='student2_add'),
    path('students2/update/<int:id>/', views.student2_update, name='student2_update'),
    path('students2/delete/<int:id>/', views.student2_delete, name='student2_delete'),

    # Task 3: Course with image
    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.course_add, name='course_add'),
    path('courses/update/<int:id>/', views.course_update, name='course_update'),
    path('courses/delete/<int:id>/', views.course_delete, name='course_delete'),
    path('users/register/', views.register_user, name='register'),


]