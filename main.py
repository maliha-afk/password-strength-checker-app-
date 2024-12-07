import tkinter as tk


root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("600x400")
root.config(bg="green")


wel=tk.Label(root,text="Welcome To Password strength Checker App",font=("Arial",15,"bold"),fg="black",bg="green")
wel.grid(row=1,column=1)

wel2=tk.Label(root,text="----------------------------------------------------------------",font=("Arial",15,"bold"),fg="black",bg="green")
wel2.grid(row=2,column=1)
 



def check_password():
    password = password_entry.get()
    strength = get_password_strength(password)
    result_label.config(text=f"Password Strength: {strength}")


def get_password_strength(password):
    score = 0
    length = len(password)
    if length >= 8:
        score += 1
    
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_symbol = False
    
    for char in password:
        if char.islower():
            has_lowercase = True
        
        elif char.isupper():
            has_uppercase = True
        
        elif char.isdigit():
            has_digit = True
        
        elif not char.isalnum():  
            has_symbol = True
    
    
    if has_lowercase:
        score += 1
    
    if has_uppercase:
        score += 1
    
    if has_digit:
        score += 1
    
    if has_symbol:
        score += 1
    
    if score == 5:
        return "Very Strong"
    
    elif score == 4:
        return "Strong"
    
    elif score == 3:
        return "Medium"
    
    elif score == 2:
        return "Weak"
    
    else:
        return "Very Weak"
    



password_label = tk.Label(root, text="Enter Password:",font=("Arial",15,"bold"),fg="black",bg="green")
password_label.grid(row=4,column=1)

password_entry = tk.Entry(root,  width=30)
password_entry.grid(row=6,column=1)

check_button = tk.Button(root, text="Check Strength",font=("Arial",10,"bold"),fg="black",bg="white",relief="raised", command=check_password)
check_button.grid(row=7,column=1)

result_label = tk.Label(root, text="",font=("Arial",15,"bold"),fg="black",bg="green")
result_label.grid(row=9,column=1)


def refresh():
    result_label.config(text="")

reset_button=tk.Button(root, text="reset",font=("Arial",10,"bold"),fg="black",bg="white",relief="raised", command=refresh)
reset_button.grid(row=8,column=0)


def hide():
   password_entry.config(show="*")

hide_button=tk.Button(root, text="hide",font=("Arial",10,"bold"),fg="black",bg="white",relief="raised", command=hide)
hide_button.grid(row=8,column=1)


def show():
   password_entry.config(show="")

show_button=tk.Button(root, text="show",font=("Arial",10,"bold"),fg="black",bg="white",relief="raised", command=show)
show_button.grid(row=8,column=2)








root.mainloop()