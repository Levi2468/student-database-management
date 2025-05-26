from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox

interface2 = Tk()
interface2.geometry("1000x1000")


# function to fetch student details using roll number
def finding():
    global main_frame
    # incase if a student detail is already got searched
    try:
        # destroy main_frame that contains previous student details
        main_frame.pack_forget()
    except:
        pass
    # get the entered value from the entry box
    key=Roll_no.get()
    # creating a frame with scroll bar to show student details
    main_frame=Frame(interface2)
    main_frame.pack(fill="both",expand=1)
    # creating a canvas that scroll along with the scroll bar
    background = Canvas(main_frame)
    background.pack(side=LEFT, fill=BOTH, expand=1)
    # creating a scroll bar
    scroll_bar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=background.yview)
    scroll_bar.pack(side=RIGHT, fill=Y)
    # bind scroll bar with canvas
    background.configure(yscrollcommand=scroll_bar.set)
    background.bind('<Configure>', lambda e: background.configure(scrollregion=background.bbox("all")))
    # creating a frame 1 on the canvas in left side
    page = Frame(background, width=100)
    background.create_window((0, 0), window=page, anchor="ne")
    # creating a frame 2 on the canvas in right side
    page2 = Frame(background, width=100)
    background.create_window((0, 0), window=page2, anchor="nw")
    # creating a list of labels
    Label_List = ["First Name: ", "Last Name: ", "D.O.B:", "BloodGroup:", "Address:", "Mobile:", "Email Id:",
                  "Father Name:", "Mother Name:", "Father Occupation:", "Mother Occupation:", "Government Id:",
                  "Government Proof:", "Photo", "Tenth mark:", "Tenth percentage:", "Tenth Roll number:",
                  "Eleventh mark:", "Eleventh percentage:", "Eleventh Roll number:", "Twelfth mark:",
                  "Twelfth percentage:", "Twelfth roll number:", "Transfer certificate: ", "ID", "Department:",
                  "Total fees:", "Amount Paid:", "Balance:", "Admission Date:", "Year of Passing:", "Course duration:"]
    i = 0
    # variable with boolean value to know the searched value is valid or not
    way=False
    # open file that contain student details
    with open("Student Management.txt", 'r') as file:
        # store each line one by one as list
        for line in file:
            details = line.strip().split(',')
            # check whether the searched value(roll no) is present in the list
            if key in details:
                # if the list has the searched roll no, store the list
                get_Student_details=details
                way=True
    # if way = True ,the search roll number is valid (present in the database)
    if way is True:
        get_Student_details.pop()
        # displaying the labels and its values(student details)
        for Placing in Label_List:
            # placing photo on the  left side
            if Placing == "Photo":
                global stdPhoto
                stdPhoto0 = Image.open(get_Student_details[i])
                resize = stdPhoto0.resize((200, 200))
                stdPhoto = ImageTk.PhotoImage(resize)
                Label(page2, image=stdPhoto, width=200, height=200).grid(row=0, column=1, rowspan=5, padx=100)
            # skip print ID(roll number)
            elif Placing == "ID":
                pass
            # convert address into proper format
            elif Placing == "Address:":
                new_address=get_Student_details[i].replace('-',',').strip(',')
                Label(page, text=Placing, font=("Times new roman", 12, "bold")).pack(anchor="e", padx=10, pady=10)
                Label(page2, text=new_address, font=("Times new roman", 12, "bold")).grid(row=i, column=0,padx=10, pady=10)
            else:
                Label(page, text=Placing, font=("Times new roman", 12, "bold")).pack(anchor="e", padx=10, pady=10)
                Label(page2, text=get_Student_details[i], font=("Times new roman", 12, "bold")).grid(row=i, column=0,
                                                                                                     padx=10, pady=10)
            # dynamic variable act as an index for get_Student_details list
            i += 1
    # if way= false,the searched value is invalid or not found
    else:
        messagebox.showerror("Not Found","No data found for the Entered Rollnumber")


# label for page header
Label(interface2,text="Student database",fg="red",bg="yellow",font=("Times new roman",30,"bold"),padx=20,pady=20).pack(anchor="n",fill="both")
Label(interface2,bg="Lightgreen",pady=10).pack(fill="both")
Label(interface2,text="Student Roll number:",font=("Times new roman",12,"bold"),bg="Lightgreen").place(x=80,y=97)
global Roll_no
# entry box to enter roll number
Roll_no=Entry(interface2,font=("Times new roman",12,"bold"),width=25)
Roll_no.place(x=250,y=97)
# button to get details using entered roll number
Search=Button(interface2,text="search",bd=2,command=finding)
Search.place(x=475,y=97)

interface2.mainloop()