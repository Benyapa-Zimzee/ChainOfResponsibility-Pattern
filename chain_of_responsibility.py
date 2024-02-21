import tkinter as tk
from tkinter import messagebox

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("University Support System")

        self.request_label = tk.Label(self, text="Enter your request:")
        self.request_label.pack()

        self.request_entry = tk.Entry(self)
        self.request_entry.pack()

        self.submit_button = tk.Button(self, text="Submit", command=self.handle_request)
        self.submit_button.pack()

    def handle_request(self):
        request = self.request_entry.get()
        support_handler.handle(request)


class SupportHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, request):
        if self.next_handler:
            self.next_handler.handle(request)


class TeacherSupport(SupportHandler):
    def handle(self, request):
        if request == "Teacher":
            messagebox.showinfo("Teacher Support", "The teacher will handle your request.")
        else:
            super().handle(request)


class HeadOfFacultySupport(SupportHandler):
    def handle(self, request):
        if request == "Head":
            messagebox.showinfo("Head of Faculty Support", "The head of faculty will handle your request.")
        else:
            super().handle(request)


class DeanSupport(SupportHandler):
    def handle(self, request):
        if request == "Dean":
            messagebox.showinfo("Dean Support", "The dean will handle your request.")
        else:
            super().handle(request)


class FinanceSupport(SupportHandler):
    def handle(self, request):
        if request == "Finance":
            messagebox.showinfo("Finance Support", "The finance department will handle your request.")
        else:
            super().handle(request)


class HRSupport(SupportHandler):
    def handle(self, request):
        if request == "HR":
            messagebox.showinfo("HR Support", "The HR department will handle your request.")
        else:
            messagebox.showerror("No Support", "Sorry, we don't provide support for this request.")


# Setting up the chain of responsibility
hr_support = HRSupport()
finance_support = FinanceSupport(hr_support)
dean_support = DeanSupport(finance_support)
head_of_faculty_support = HeadOfFacultySupport(dean_support)
teacher_support = TeacherSupport(head_of_faculty_support)
support_handler = teacher_support

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
