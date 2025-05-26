from tkinter import *
# allow you to import other python files
import os
main_interface=Tk()
main_interface.geometry("1000x1000")
# label for title
Label(main_interface,text="Student database",fg="red",bg="yellow",font=("Times new roman",30,"bold"),padx=20,pady=20).pack(anchor="n",fill="both")
# button to open student register window
register=Button(main_interface,text="Register New student",font=("Times new roman",18),pady=5,padx=5,command = lambda: os.system('Register_student.py'))
register.pack(pady=30)
# button to open student database  widow
search_student=Button(main_interface, text="Search student detail", font=("Times new roman",18), pady=5, padx=5, command = lambda: os.system(
    'student_database_management.py'))
search_student.pack(pady=20)

main_interface.mainloop()