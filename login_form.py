import tkinter as tk

r = tk.Tk()
r.title('Main Page')

def open_signin():
    signin_window = tk.Toplevel(r)
    signin_window.title("Sign In Page")

    tk.Label(signin_window, text="Welcome to the Sign In Page!").grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(signin_window, text="Enter Your Username:").grid(row=1, column=0, padx=5, pady=5)
    username_entry = tk.Entry(signin_window, width=20)
    username_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(signin_window, text="Enter Your Password:").grid(row=2, column=0, padx=5, pady=5)
    password_entry = tk.Entry(signin_window, width=20, show="*")
    password_entry.grid(row=2, column=1, padx=5, pady=5)

    def signin_success():
        success_window = tk.Toplevel(signin_window)
        success_window.title("Successful Login")
        tk.Label(success_window, text="You have successfully signed in!").pack(padx=20, pady=20)
        tk.Button(success_window, text="Close", command=success_window.destroy).pack(pady=10)

    tk.Button(signin_window, text="Sign In", command=signin_success).grid(row=3, column=0, columnspan=2, pady=10)
    tk.Button(signin_window, text="Close", command=signin_window.destroy).grid(row=4, column=0, columnspan=2, pady=5)

def open_signup():
    signup_window = tk.Toplevel(r)
    signup_window.title("Sign Up Page")

    tk.Label(signup_window, text="Welcome to the Sign Up Page!").grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(signup_window, text="Create Username:").grid(row=1, column=0, padx=5, pady=5)
    username_entry = tk.Entry(signup_window, width=20)
    username_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(signup_window, text="Create Password:").grid(row=2, column=0, padx=5, pady=5)
    password_entry = tk.Entry(signup_window, width=20, show="*")
    password_entry.grid(row=2, column=1, padx=5, pady=5)

    def signup_success():
        success_window = tk.Toplevel(signup_window)
        success_window.title("Successful Registration")
        tk.Label(success_window, text="You have successfully registered!").pack(padx=20, pady=20)
        tk.Button(success_window, text="Close", command=success_window.destroy).pack(pady=10)

    tk.Button(signup_window, text="Sign Up", command=signup_success).grid(row=3, column=0, columnspan=2, pady=10)
    tk.Button(signup_window, text="Close", command=signup_window.destroy).grid(row=4, column=0, columnspan=2, pady=5)


tk.Button(r, text="Sign In", width=15, command=open_signin).grid(row=0, column=0, padx=10, pady=10)
tk.Button(r, text="Sign Up", width=15, command=open_signup).grid(row=0, column=1, padx=10, pady=10)

r.mainloop()
