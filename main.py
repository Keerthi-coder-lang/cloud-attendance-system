import requests
import datetime

FIREBASE_URL = "https://cloud-based-attendance-s-dac6a-default-rtdb.firebaseio.com/"

def register_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")

    data = {"name": name}

    response = requests.put(
        FIREBASE_URL + f"students/{roll}.json",
        json=data
    )

    print("Student Registered Successfully!\n")

def mark_attendance():
    roll = input("Enter Roll Number: ")

    attendance_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = {
        "roll": roll,
        "time": attendance_time
    }

    response = requests.post(
        FIREBASE_URL + "attendance.json",
        json=data
    )

    print("Attendance Marked Successfully!\n")

def view_attendance():
    response = requests.get(FIREBASE_URL + "attendance.json")

    if response.json() is None:
        print("No attendance records found.\n")
        return

    print("\n----- Attendance Records -----")
    for key, value in response.json().items():
        print(f"Roll No: {value['roll']} | Time: {value['time']}")
    print("-------------------------------\n")

while True:
    print("===== CLOUD ATTENDANCE SYSTEM =====")
    print("1. Register Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_student()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        view_attendance()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice!\n")
