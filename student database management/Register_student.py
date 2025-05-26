from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
from datetime import datetime
from tkinter import messagebox


interface = Tk()
interface.geometry("1000x1000")
# List to store all user entered details
global Student_details
Student_details=[]


# function to set-up first tab for personal details
def Personal():
    # function to enable next next tab
    def next_page():
        # activate next tab
        tabs.tab(1, state=NORMAL)
        # move to next tab
        tabs.select(tab2)

    # function to reset or save user entered/selected values
    def database(values):
        # temporary list to store user entered/selected values
        new_list = []
        # getting entry box variables from the list
        for send_list in Personal_details_list:
            # store all entry box variables into temporary list
            new_list.append(send_list)
        new_list.append(placeholder)
        new_list.append(filename)
        i = 0
        # check whether 'reset' button got clicked
        if values == "reset":
            # getting variables from temporary list
            for data in new_list:
                # 'i' act as an index number that start from 1
                i += 1
                # 14 th index,holds student image address
                if i == 14:
                    # resetting selected image  by destroy its label,edit button
                    stdplace.place_forget()
                    change.place_forget()
                    # function to create upload image button
                    Gallery()
                # 13 th index ,holds selected dropdown option
                elif i == 13:
                    # reset the dropdown option to default
                    onclicked.set("Select a Government Proof")
                    # reset the label to default
                    GovernId.config(text="Government Id")
                # 5 th index hold textbox value
                elif i == 5:
                    # delete(empty) text box values
                    data.delete(1.0, END)
                # other index holds entry box values
                else:
                    # delete values in entry box
                    data.delete(0, END)
        # check whether save button is clicked
        if values == "save":
            # enable Next button
            Next.config(state=NORMAL)
            for data in new_list:
                # 'i' act as an index number that start from 1
                i += 1
                # 5th index holds textbox values
                if i == 5:
                    # getting entry box value
                    holding = data.get(1.0,END)
                    # replace '\n' to '-' from textbox value
                    holding = holding.replace('\n','-')
                    # append the textbox values
                    Student_details.append(str(holding))
                    # disable the entry box after save button is clicked
                    data.config(state=DISABLED)
                # getting image address and dropdown option
                elif i == 13 or i == 14:
                    Student_details.append(data)
                    # disable the entry boxes
                    Government.config(state=DISABLED)
                    change.config(state=DISABLED)
                # append entry box values into list and disabling them
                else:
                    Student_details.append(data.get())
                    data.config(state=DISABLED)
            # disable reset button and save button
            reset.config(state=DISABLED)
            save.config(state=DISABLED)

    # function to select student image
    def stdimage():
        # globally declaring images and variable to be used in different functions
        global stdPhoto,change,filename,stdplace
        # open and store the selected image storage path
        filename = filedialog.askopenfilename(initialdir="/vishnupython/", title="select",
                                                  filetypes=(("txt", "*png"), ("allfile", "*.*")))
        # destroy button for image upload
        StudentLab.place_forget()
        # destroy previous image if edit button is clicked
        try:
            stdplace.place_forget()
        except:
            pass
        # resize selected image
        stdPhoto0 = Image.open(filename)
        resize=stdPhoto0.resize((100, 100))
        stdPhoto=ImageTk.PhotoImage(resize)
        # labeling resized selected image
        stdplace = Label(tab1, image=stdPhoto, width=100, height=100)
        stdplace.place(x=560, y=360)
        # button to (edit) replace current image
        change = Button(tab1, text="Edit", command=stdimage)
        change.place(x=700, y=400)

    # function to create button that allow user to select student image
    def Gallery():
        global StudentLab
        # button to call stdimage function to select image
        StudentLab = Button(tab1, text="Upload Image", font=("Times new roman", 12), width=10, height=6, bg='white',
                            bd=0, command=stdimage)
        StudentLab.place(x=560, y=360)

    # function to select government proof
    def selector(clicked, GovernId):
        global placeholder
        # check whether first option is selected
        if clicked == Ids[0]:
            # change text in below label
            GovernId.config(text="Aadhar card:")
            # variable to store user choice
            placeholder="Aadhar card"
        # repeat above process for all options available
        if clicked == Ids[1]:
            GovernId.config(text="Ration card:")
            placeholder = "Ration card"
        if clicked == Ids[2]:
            GovernId.config(text="Driving Licence")
            placeholder = "Driving Licence"
        if clicked == Ids[3]:
            GovernId.config(text="Voter Id")
            placeholder="Voter Id"
        # allow user to enter id proof in textbox
        GovernmentId.config(state=NORMAL,bg="white")
    # label for first name
    FN=Label(tab1,text="First Name: ", font=("Times new roman", 12))
    FN.grid(row=0,column=0,pady=15,padx=25)
    # entry box for first name
    FirstName=Entry(tab1,font=("Times new roman", 12), width=30)
    FirstName.grid(row=0,column=1)
    # repeating above code for other entry box and labels with different texts and variables
    # last name
    LN = Label(tab1 ,text="Last Name: ", font=("Times new roman", 12))
    LN.grid(row=1, column=0, pady=10)
    LastName = Entry(tab1, font=("Times new roman", 12), width=30)
    LastName.grid(row=1, column=1)
    # date of birth
    Birth = Label(tab1,text="D.O.B",font=("Times new roman", 12))
    Birth.grid(row=2,column=0,pady=10)
    DOB = Entry(tab1, font=("Times new roman", 12), width=30)
    DOB.grid(row=2, column=1)
    # blood group
    BG=Label(tab1,text="Blood Group: ",font=("Times new roman", 12))
    BG.grid(row=3,column=0,pady=10)
    BloodGroup= Entry(tab1, font=("Times new roman", 12), width=30)
    BloodGroup.grid(row=3,column=1)
    # address
    Ad = Label(tab1, text="Address: ", font=("Times new roman", 12))
    Ad.grid(row=4, column=0, pady=15)
    Address = Text(tab1, font=("Times new roman", 12), width=30,height=10,bd=3)
    Address.grid(row=4, column=1,pady=15)
    # mobile number
    MN= Label(tab1, text="Mobile Number : ", font=("Times new roman", 12))
    MN.grid(row=5 ,column=0, pady=10)
    Mobile = Entry(tab1, font=("Times new roman", 12), width=30)
    Mobile.grid(row=5, column=1)
    # email address
    EM = Label(tab1, text="Email ID: ", font=("Times new roman", 12))
    EM.grid(row=6, column=0, pady=10)
    EmailId = Entry(tab1, font=("Times new roman", 12), width=30)
    EmailId.grid(row=6, column=1)
    # father name
    Father = Label(tab1, text="Father Name: ", font=("Times new roman", 12))
    Father.grid(row=0, column=2,padx=40)
    FatherName = Entry(tab1, font=("Times new roman", 12), width=30)
    FatherName.grid(row=0, column=3)
    # mother name
    Mother = Label(tab1, text="Mother Name: ", font=("Times new roman", 12))
    Mother.grid(row=1, column=2 )
    MotherName = Entry(tab1, font=("Times new roman", 12), width=30)
    MotherName.grid(row=1, column=3)
    # father occupation
    FatherOcc=Label(tab1, text="Father's Occupation: ", font=("Times new roman", 12))
    FatherOcc.grid(row=2, column=2 )
    FatherOccupation = Entry(tab1, font=("Times new roman", 12), width=30)
    FatherOccupation.grid(row=2, column=3)
    # mother occupation
    MotherOcc=Label(tab1, text="Mother's Occupation: ", font=("Times new roman", 12))
    MotherOcc.grid(row=3, column=2 )
    MotherOccupation = Entry(tab1, font=("Times new roman", 12), width=30)
    MotherOccupation.grid(row=3, column=3)
    # string variable to store selected dropdown option
    global onclicked
    onclicked=StringVar()
    # list of govt. Proof
    Ids =["Aadhar card","Ration card","Driving Licence","Votar ID"]

    onclicked.set("Select a Government Proof")
    # government proof
    Govern=Label(tab1,text="Government Proof:", font=("Times new roman", 12))
    Govern.place(x=400,y=200)
    global GovernId
    GovernId = Label(tab1, text="Government Id:", padx=20, pady=5, font=("Times new roman", 12))
    GovernId.place(x=404, y=300)
    # drop down menu for selecting any one government proof
    Government=OptionMenu(tab1,onclicked,*Ids,command=lambda click=onclicked:selector(click,GovernId))
    Government.place(x=560,y=200)
    # government id
    GovernmentId = Entry(tab1, font=("Times new roman", 12),width=29,bg="grey",state=DISABLED)
    GovernmentId.place(x=560, y=300)
    # student Image
    studentImage=Label(tab1,text="Student Image:",font=("Times new roman", 12))
    studentImage.grid(row=5,column=2)
    # function to select student image
    Gallery()
    # List of all variables  that store all entry box values available in this tab
    global Personal_details_list
    Personal_details_list=[FirstName,LastName,DOB,BloodGroup,Address,Mobile,EmailId,FatherName,MotherName,FatherOccupation,MotherOccupation,GovernmentId]
    # button to reset (empty) all entry box using database function
    reset=Button(tab1,text="reset", font=("Times new roman", 12),command=lambda do="reset":database(do),padx=15,pady=2)
    reset.grid(row=1,column=4,padx=70)
    # button to store all user entered/selected using database function
    save = Button(tab1, text="save", font=("Times new roman", 12), command=lambda do="save": database(do), padx=15, pady=2)
    save.grid(row=3, column=4, padx=70)
    # button for moving to next tab
    Next = Button(tab1,text="Next",state=DISABLED,font=("Times new roman", 12), command=next_page)
    Next.grid(row=4,column=4,padx=70)

# function to setup tab2 for academics details
def Academic():
    # function enable next tab
    def next_page2():
        tabs.tab(2, state="disabled")
        tabs.select(tab3)

    # function to reset and save entry box values
    def database2(values2):
        new_list=[]
        for send_list in Academic_list:
            new_list.append(send_list)
        # check whether reset button is clicked
        if values2 == "reset":
            # reset (delete) all entry box values
            for data in new_list:
                data.delete(0, END)
        # check whether save button is clicked
        if values2 == "save":
            # enables next button
            Next.config(state=NORMAL)
            # append all entry box values into list and disable them
            for data in new_list:
                Student_details.append(data.get())
                data.config(state=DISABLED)
        # disable reset and save buttons
        reset.config(state=DISABLED)
        save.config(state=DISABLED)

    # function to calculate percentage for 10th
    def calculate10(event):
        percentage=(int(tenth_mark.get())/500)*100
        tenth_percentage.delete(0,END)
        # insert calculated values into entry box
        tenth_percentage.insert(0, str(percentage)+'%')

    # function to calculate percentage for 11th
    def calculate11(event):

        percentage = (int(eleven_mark.get()) / 500) * 100
        eleven_percentage.delete(0,END)
        # insert calculated values into entry box
        eleven_percentage.insert(0, str(percentage) + '%')

    # function to calculate percentage for 12th
    def calculate12(event):
        percentage = (int(twelve_mark.get()) / 500) * 100
        twelve_percentage.delete(0,END)
        # insert calculated values into entry box
        twelve_percentage.insert(0, str(percentage) + '%')
    # creating labels and entry box
    # tenth mark and percentage
    tenth=Label(tab2,text="10th mark:",font=("Times new roman", 12))
    tenth.grid(row=0,column=0,pady=15,padx=25)
    tenth_mark=Entry(tab2,font=("Times new roman", 12),width=30)
    tenth_mark.grid(row=0,column=1)
    tenth_percent=Label(tab2,text="10th percentage:",font=("Times new roman", 12))
    tenth_percent.grid(row=1,column=0,pady=15,padx=25)
    tenth_percentage = Entry(tab2, font=("Times new roman", 12), width=30)
    tenth_percentage.grid(row=1, column=1)
    # bind "Focus In" to automatically calculate percentage using calculate10 function
    tenth_percentage.bind("<FocusIn>",calculate10)
    # 11 th mark and percentage
    eleven = Label(tab2, text="11th mark:", font=("Times new roman", 12))
    eleven.grid(row=2, column=0, pady=15, padx=25)
    eleven_mark = Entry(tab2, font=("Times new roman", 12), width=30)
    eleven_mark.grid(row=2, column=1)
    eleven_percent = Label(tab2, text="11th percentage:", font=("Times new roman", 12))
    eleven_percent.grid(row=3, column=0, pady=15, padx=25)
    eleven_percentage = Entry(tab2, font=("Times new roman", 12), width=30)
    eleven_percentage.grid(row=3, column=1)
    # bind "Focus In" to automatically calculate percentage using calculate11 function
    eleven_percentage.bind("<FocusIn>", calculate11)
    # 12 th mark and percentage
    twelve = Label(tab2, text="12th mark:", font=("Times new roman", 12))
    twelve.grid(row=4, column=0, pady=15, padx=25)
    twelve_mark = Entry(tab2, font=("Times new roman", 12), width=30)
    twelve_mark.grid(row=4, column=1)
    twelve_percent = Label(tab2, text="12th percentage:", font=("Times new roman", 12))
    twelve_percent.grid(row=5, column=0, pady=15, padx=25)
    twelve_percentage = Entry(tab2, font=("Times new roman", 12), width=30)
    twelve_percentage.grid(row=5, column=1)
    # bind "Focus In" to automatically calculate percentage using calculate12 function
    twelve_percentage.bind("<FocusIn>", calculate12)
    # 10th roll number
    tenth_rollno = Label(tab2, text="10th Roll_No:", font=("Times new roman", 12))
    tenth_rollno.grid(row=0, column=2, pady=15, padx=25)
    tenth_rollnum= Entry(tab2, font=("Times new roman", 12), width=30)
    tenth_rollnum.grid(row=0, column=3)
    # 11 th roll number
    eleven_rollno = Label(tab2, text="11th Roll_No:", font=("Times new roman", 12))
    eleven_rollno.grid(row=2, column=2, pady=15, padx=25)
    eleven_rollnum = Entry(tab2, font=("Times new roman", 12), width=30)
    eleven_rollnum.grid(row=2, column=3)
    # 12 th roll number
    twelve_rollno = Label(tab2, text="12th Roll_No:", font=("Times new roman", 12))
    twelve_rollno.grid(row=4, column=2, pady=15, padx=25)
    twelve_rollnum = Entry(tab2, font=("Times new roman", 12), width=30)
    twelve_rollnum.grid(row=4, column=3)
    # Transfer certificate
    TC_No =Label(tab2, text="Transfer certificate:", font=("Times new roman", 12))
    TC_No.grid(row=6, column=2, pady=15, padx=25)
    TC_number = Entry(tab2, font=("Times new roman", 12), width=30)
    TC_number.grid(row=6, column=3)
    # List of all variables  that stores all entry box values available in this tab
    global Academic_list
    Academic_list=[tenth_mark,tenth_percentage,tenth_rollnum,eleven_mark,eleven_percentage,eleven_rollnum,twelve_mark,twelve_percentage,twelve_rollnum,TC_number]
    # button to reset all entry box
    reset = Button(tab2, text="reset", font=("Times new roman", 12), command=lambda do2="reset": database2(do2), padx=15,
                   pady=2)
    reset.grid(row=1, column=4, padx=70)
    # button to store all entry box values in a List
    save = Button(tab2, text="save", font=("Times new roman", 12), command=lambda do2="save": database2(do2), padx=15,
                  pady=2)
    save.grid(row=3, column=4, padx=70)
    # button for moving into next tab(disabled until save button got clicked)
    Next = Button(tab2, text="Next",state=DISABLED, font=("Times new roman", 12), command=next_page2)
    Next.grid(row=5, column=4, padx=70)


# function to setup tab3 for admission details
def Admission():
    # function to store all user entered values into a file
    def Complete():
        with open("Student Management.txt", 'a') as files:
            # write datas from Student_details list to a text file
            for storage in Student_details:
                files.write(f"{storage},")
            files.write(f"\n")
        # close the application window
        interface.quit()

    # function to save(store) and reset entry box
    def database3(values3):
        new_list = []
        for send_list in Admission_list:
            # append entry variable into new list
            new_list.append(send_list)
        # reset all entry box
        if values3 == "reset":
            for data in new_list:
                # delete(empty) all entry box
                data.delete(0, END)
        # check whether save button is clicked
        if values3 == "save":
            # enable complete button
            Completed.config(state=NORMAL)
            for data in new_list:
                # append all entry box values into List and disabling them
                Student_details.append(data.get())
                data.config(state=DISABLED)
        # disable reset and save button
        reset.config(state=DISABLED)
        save.config(state=DISABLED)

    # function to calculate balance due amount
    def due(event):
        due=int(Total_fees.get())-int(Paid.get())
        Balance.delete(0,END)
        # insert the result into the balance entry box
        Balance.insert(0,str(due))
    # creating labels and its entry box
    # register Number
    register_no = Label(tab3, text="Register Number: ", font=("Times new roman", 12))
    register_no.grid(row=0, column=0,pady=15, padx=25)
    register_number = Entry(tab3, font=("Times new roman", 12), width=30)
    register_number.grid(row=0, column=1,pady=15, padx=25)
    # department
    DepartmentL=Label(tab3, text="Department: ", font=("Times new roman", 12))
    DepartmentL.grid(row=1, column=0,pady=15, padx=25)
    Department = Entry(tab3, font=("Times new roman", 12), width=30)
    Department.grid(row=1, column=1,pady=15, padx=25)
    # total fees
    Total_feesL=Label(tab3, text="Total Fees : ", font=("Times new roman", 12))
    Total_feesL.grid(row=2, column=0,pady=15, padx=25)
    Total_fees = Entry(tab3, font=("Times new roman", 12), width=30)
    Total_fees.grid(row=2, column=1,pady=15, padx=25)
    # fees paid
    PaidL=Label(tab3, text="Amount Paid ", font=("Times new roman", 12))
    PaidL.grid(row=3, column=0,pady=15, padx=25)
    Paid = Entry(tab3, font=("Times new roman", 12), width=30)
    Paid.grid(row=3, column=1,pady=15, padx=25)
    # balance due
    BalanceL = Label(tab3, text="Balance due ", font=("Times new roman", 12))
    BalanceL.grid(row=4, column=0, pady=15, padx=25)
    Balance = Entry(tab3, font=("Times new roman", 12), width=30)
    Balance.grid(row=4, column=1, pady=15, padx=25)
    # use bind "FocusIn" to automatically calculating due amount
    Balance.bind("<FocusIn>",due)
    # admission date(current date)
    AdmissionDateL=Label(tab3, text="Admission Date", font=("Times new roman", 12))
    AdmissionDateL.grid(row=5, column=0, pady=15, padx=25)
    AdmissionDate = Entry(tab3, font=("Times new roman", 12), width=30)
    AdmissionDate.grid(row=5, column=1, pady=15, padx=25)
    AdmissionDate.insert(0,datetime.today().strftime('%Y-%m-%d'))
    # Year of passing
    PassingL = Label(tab3, text="Year of Passing", font=("Times new roman", 12))
    PassingL.grid(row=6, column=0, pady=15, padx=25)
    Passing = Entry(tab3, font=("Times new roman", 12), width=30)
    Passing.grid(row=6, column=1, pady=15, padx=25)
    # course duration
    courseL = Label(tab3, text="Course Duration", font=("Times new roman", 12))
    courseL.grid(row=7, column=0, pady=15, padx=25)
    Course = Entry(tab3, font=("Times new roman", 12), width=30)
    Course.grid(row=7, column=1, pady=15, padx=25)
    # List of all variables  that store all entry box values available in this tab
    Admission_list=[register_number,Department,Total_fees,Paid,Balance,AdmissionDate,Passing,Course]
    # button to reset all entry box
    reset = Button(tab3, text="reset", font=("Times new roman", 12), command=lambda do="reset": database3(do), padx=15,
                   pady=2)
    reset.grid(row=1, column=2, padx=70)
    # button to store all entry box values into list
    save = Button(tab3, text="save", font=("Times new roman", 12), command=lambda do="save": database3(do), padx=15,
                  pady=2)
    save.grid(row=2, column=2, padx=70)
    # button to store all entered values into a file (inactive until save button is clicked)
    Completed = Button(tab3, state=DISABLED,text="Complete Registration", font=("Times new roman", 12), command=Complete)
    Completed.grid(row=3, column=2, padx=70)


# creating title label for the page
Label(interface,text="Student data Registration",fg="red",bg="yellow",font=("Times new roman",30,"bold"),padx=20,pady=20).pack(anchor="n",fill="both")
# creation tabs
tabs=ttk.Notebook(interface)
tab1=Frame(tabs)
tab2=Frame(tabs)
tab3=Frame(tabs)
# naming and adding tabs in current page(frame)
tabs.add(tab1,text="Personal details")
tabs.add(tab2,text="Academic details")
tabs.add(tab3,text="Admission details")
tabs.pack(expand=True,fill="both")

# function to setup tab1
Personal()
tabs.tab(1,state="disabled")
# function to setup tab2( disable until tab1 is completed)
Academic()
tabs.tab(2,state="disabled")
# function to setup tab3 (disable until tab2 is completed)
Admission()

# run the Application code
interface.mainloop()