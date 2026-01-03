import mysql.connector
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk

# ---------- DATABASE CONNECTION ----------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",   # change this
    database="cafe_attendance"
)
cursor = conn.cursor()

# ---------- FUNCTIONS ----------

def add_employee():
    name = name_var.get()
    pos = pos_var.get()
    shift_start = shift_start_var.get()
    shift_end = shift_end_var.get()
    rate = rate_var.get()
    
    if not name or not rate:
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    cursor.execute("""
        INSERT INTO employee (name, position, shift_start, shift_end, hourly_rate)
        VALUES (%s, %s, %s, %s, %s)
    """, (name, pos, shift_start, shift_end, rate))
    conn.commit()
    messagebox.showinfo("Success", f"Employee {name} added successfully!")
    clear_fields()

def clear_fields():
    name_var.set("")
    pos_var.set("")
    shift_start_var.set("")
    shift_end_var.set("")
    rate_var.set("")

def mark_attendance():
    emp_id = att_emp_id_var.get()
    in_time = in_time_var.get()
    out_time = out_time_var.get()
    fmt = "%H:%M:%S"

    try:
        cursor.execute("SELECT shift_start, shift_end FROM employee WHERE emp_id=%s", (emp_id,))
        result = cursor.fetchone()
        if not result:
            messagebox.showerror("Error", "Invalid Employee ID")
            return

        shift_start, shift_end = result
        in_dt = datetime.strptime(in_time, fmt)
        out_dt = datetime.strptime(out_time, fmt)
        shift_start_dt = datetime.strptime(str(shift_start), fmt)
        total_hours = (out_dt - in_dt).seconds / 3600
        late_minutes = max(0, int((in_dt - shift_start_dt).seconds / 60))

        if total_hours < 3:
            status = "Absent"
        elif late_minutes > 15:
            status = "Late"
        else:
            status = "Present"

        cursor.execute("""
            INSERT INTO attendance (emp_id, date, in_time, out_time, total_hours, late_minutes, status)
            VALUES (%s, CURDATE(), %s, %s, %s, %s, %s)
        """, (emp_id, in_time, out_time, total_hours, late_minutes, status))
        conn.commit()
        messagebox.showinfo("Success", f"Attendance recorded for Employee {emp_id} ({status})")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def calculate_salary():
    emp_id = salary_emp_id_var.get()
    month = month_var.get()

    cursor.execute("""
        SELECT SUM(total_hours), 
               SUM(CASE WHEN status='Late' THEN 1 ELSE 0 END),
               SUM(CASE WHEN status='Absent' THEN 1 ELSE 0 END)
        FROM attendance 
        WHERE emp_id=%s AND MONTHNAME(date)=%s
    """, (emp_id, month))
    total_hours, late_days, absent_days = cursor.fetchone()
    total_hours = total_hours or 0
    late_days = late_days or 0
    absent_days = absent_days or 0

    cursor.execute("SELECT hourly_rate FROM employee WHERE emp_id=%s", (emp_id,))
    rate = cursor.fetchone()[0]

    total_salary = total_hours * rate
    deductions = (late_days * 50) + (absent_days * 300)
    final_salary = total_salary - deductions

    cursor.execute("""
        INSERT INTO salary (emp_id, month, total_hours, total_salary, deductions, final_salary)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (emp_id, month, total_hours, total_salary, deductions, final_salary))
    conn.commit()

    messagebox.showinfo("Salary Calculated",
        f"Total Hours: {total_hours}\nLate: {late_days}\nAbsent: {absent_days}\nFinal Salary: ₹{final_salary:.2f}")

def show_report():
    emp_id = report_emp_id_var.get()
    month = report_month_var.get()

    cursor.execute("""
        SELECT e.name, COUNT(*) AS total_days,
               SUM(CASE WHEN status='Late' THEN 1 ELSE 0 END) AS late_days,
               SUM(CASE WHEN status='Absent' THEN 1 ELSE 0 END) AS absent_days
        FROM attendance a
        JOIN employee e ON a.emp_id=e.emp_id
        WHERE a.emp_id=%s AND MONTHNAME(a.date)=%s
    """, (emp_id, month))
    result = cursor.fetchone()
    if not result:
        messagebox.showinfo("Report", "No attendance data found.")
        return

    name, total, late, absent = result
    cursor.execute("SELECT final_salary FROM salary WHERE emp_id=%s AND month=%s", (emp_id, month))
    salary = cursor.fetchone()
    salary = salary[0] if salary else 0

    report_text.set(
        f"👤 Name: {name}\n"
        f"🗓️ Total Days: {total}\n"
        f"⏰ Late: {late}\n"
        f"❌ Absent: {absent}\n"
        f"💰 Final Salary: ₹{salary:.2f}"
    )

# ---------- GUI DESIGN ----------
root = tk.Tk()
root.title("☕ Café Attendance & Salary System")
root.geometry("750x600")
root.configure(bg="#f2f2f2")

# Tabs
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Add Employee')
tab_control.add(tab2, text='Mark Attendance')
tab_control.add(tab3, text='Calculate Salary')
tab_control.add(tab4, text='Show Report')
tab_control.pack(expand=1, fill="both")

# ---------- TAB 1: ADD EMPLOYEE ----------
name_var = tk.StringVar()
pos_var = tk.StringVar()
shift_start_var = tk.StringVar()
shift_end_var = tk.StringVar()
rate_var = tk.StringVar()

tk.Label(tab1, text="Employee Name").pack()
tk.Entry(tab1, textvariable=name_var).pack()
tk.Label(tab1, text="Position").pack()
tk.Entry(tab1, textvariable=pos_var).pack()
tk.Label(tab1, text="Shift Start (HH:MM:SS)").pack()
tk.Entry(tab1, textvariable=shift_start_var).pack()
tk.Label(tab1, text="Shift End (HH:MM:SS)").pack()
tk.Entry(tab1, textvariable=shift_end_var).pack()
tk.Label(tab1, text="Hourly Rate (₹)").pack()
tk.Entry(tab1, textvariable=rate_var).pack()
tk.Button(tab1, text="Add Employee", command=add_employee, bg="#4CAF50", fg="white").pack(pady=10)

# ---------- TAB 2: MARK ATTENDANCE ----------
att_emp_id_var = tk.StringVar()
in_time_var = tk.StringVar()
out_time_var = tk.StringVar()

tk.Label(tab2, text="Employee ID").pack()
tk.Entry(tab2, textvariable=att_emp_id_var).pack()
tk.Label(tab2, text="In Time (HH:MM:SS)").pack()
tk.Entry(tab2, textvariable=in_time_var).pack()
tk.Label(tab2, text="Out Time (HH:MM:SS)").pack()
tk.Entry(tab2, textvariable=out_time_var).pack()
tk.Button(tab2, text="Mark Attendance", command=mark_attendance, bg="#2196F3", fg="white").pack(pady=10)

# ---------- TAB 3: CALCULATE SALARY ----------
salary_emp_id_var = tk.StringVar()
month_var = tk.StringVar()

tk.Label(tab3, text="Employee ID").pack()
tk.Entry(tab3, textvariable=salary_emp_id_var).pack()
tk.Label(tab3, text="Month Name (e.g., November)").pack()
tk.Entry(tab3, textvariable=month_var).pack()
tk.Button(tab3, text="Calculate Salary", command=calculate_salary, bg="#FF9800", fg="white").pack(pady=10)

# ---------- TAB 4: SHOW REPORT ----------
report_emp_id_var = tk.StringVar()
report_month_var = tk.StringVar()
report_text = tk.StringVar()

tk.Label(tab4, text="Employee ID").pack()
tk.Entry(tab4, textvariable=report_emp_id_var).pack()
tk.Label(tab4, text="Month Name").pack()
tk.Entry(tab4, textvariable=report_month_var).pack()
tk.Button(tab4, text="Show Report", command=show_report, bg="#9C27B0", fg="white").pack(pady=10)
tk.Label(tab4, textvariable=report_text, justify="left", bg="#f2f2f2", font=("Arial", 11)).pack(pady=10)

root.mainloop()
