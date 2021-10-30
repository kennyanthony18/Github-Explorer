import tkinter as tk
import ghex


def enter_email_btn1_click(event):
    if enter_email.get() == 'Email':
        enter_email.config(state=tk.NORMAL)
        enter_email.delete(0, tk.END)
    else:
        enter_email.config(state=tk.NORMAL)


def enter_url_btn1_click(event):
    if url_entry_output.get() == 'Sample URL':
        enter_url.config(state=tk.NORMAL)
        enter_url.delete(0, tk.END)
    else:
        enter_url.config(state=tk.NORMAL)


def enter_email_btn1_unclick(event):
    if enter_email.get() == '':
        enter_email.config(state=tk.NORMAL)
        enter_email.insert(0, 'Email')
        enter_email.config(state=tk.DISABLED)
    elif enter_email.get() == 'Email':
        enter_email.delete(0, tk.END)
        enter_email.config(state=tk.DISABLED)
    else:
        enter_email.config(state=tk.DISABLED)


def enter_url_btn1_unclick(event):
    if enter_url.get() == '':
        enter_url.config(state=tk.NORMAL)
        enter_url.insert(0, 'Sample URL')
        enter_url.config(state=tk.DISABLED)
    elif enter_url.get() == 'Sample URL':
        pass
        enter_url.config(state=tk.DISABLED)
    else:
        enter_url.config(state=tk.DISABLED)


def display_output(output):
    txt_output_area.configure(state='normal')
    txt_output_area.delete('1.0', tk.END)
    txt_output_area.insert(tk.END, output)
    txt_output_area.configure(state='disabled')


def get_languages_used():
    url = enter_url.get()
    if not url.startswith('https://github.com/'):
        display_output("")
        return
    languages_used_list = ghex.languages_used(url)
    languages_used_str = "\n".join(languages_used_list)
    display_output(languages_used_str)
    with open("lang_data.txt", 'w') as f:
        f.write(languages_used_str)


def is_valid_url(url):
    if not url.startswith('https://github.com/'):
        return False
    return True


def get_repo_stats():
    url = enter_url.get()
    if not is_valid_url(url):
        display_output("")
        return
    repo_stats = ghex.get_repo_stats(url)
    display_output(repo_stats)
    with open("repo_data.txt", 'w') as f:
        f.write(repo_stats)


def get_open_issues():
    url = enter_url.get()
    if not url.startswith('https://github.com/'):
        display_output("ERROR: Invalid URL")
        return
    open_issues_list = ghex.get_open_issues(url)
    open_issues_str = '\n'.join(open_issues_list)
    display_output(open_issues_str)
    with open("issue_data.txt", 'w') as f:
        f.write(open_issues_str)


def get_open_pulls():
    url = enter_url.get()
    if not url.startswith('https://github.com/'):
        display_output("ERROR: Invalid URL")
        return
    open_pulls_list = ghex.get_open_pulls(url)
    open_pr_str = '\n'.join(open_pulls_list)
    display_output(open_pr_str)
    with open("pr_data.txt", 'w') as f:
        f.write(open_pr_str)


def get_projects():
    url = enter_url.get()
    if not url.startswith('https://github.com/'):
        display_output("ERROR: Invalid URL")
        return
    open_projects_list = ghex.get_projects(url)
    open_proj_str = '\n'.join(open_projects_list)
    display_output(open_proj_str)


def valid_email(email):
    if email == '' or email == 'Email' or '@' not in email:
        return False
    return True


def send_mail():
    ghex.send_mail(body='this is Skill Aura Internship')


def subscribe_email():
    # Get the email address and store to a file
    emails = enter_email.get()
    print(emails)
    if not valid_email(emails):
        display_output("Invalid Email")
        return

    ghex.save_email(emails)


# Main Window
main_window = tk.Tk()
main_window.title("GIT-HUB Webpage")

# Frame for main Label
from_url = tk.LabelFrame(main_window, bg="blue", fg="white")
from_url.pack()

lbl_title = tk.Label(from_url, text="GitHub Repo Explorer", bg="grey",
                     fg="white", font='Charter 32 ', width=50)
lbl_title.pack(side="top", fill="both", expand="yes")

lbl_url = tk.Label(from_url, text='GitHub Repo URL', bg="black", fg="white", font='Charter 16', width=15)
lbl_url.pack(side=tk.LEFT)

# URL Entry
url_entry_output = tk.StringVar()
enter_url = tk.Entry(from_url, bg="blue", textvariable=url_entry_output, fg="black", font='Charter 14', width=72)
enter_url.insert(0, 'Sample URL')
# ent_ghurl.config(state=tk.DISABLED)
enter_url.bind("<Button-1>", enter_url_btn1_click)
enter_url.bind('<Leave>', enter_url_btn1_unclick)
enter_url.pack(side=tk.LEFT, padx=45, pady=5)

# Frame for buttons
from_buttons = tk.LabelFrame(main_window, bg="grey", padx=15, pady=15)
from_buttons.pack(side=tk.TOP, anchor=tk.W, fill="both", expand="yes")

# Buttons

button_lang_used = tk.Button(from_buttons, text='Languages Used', font='Charter 18', width=15, fg='red', command=get_languages_used)
button_lang_used.grid(row=0, column=0)

button_repo_stats = tk.Button(from_buttons, text='Repo Stats', font='Charter 18', width=15, fg='red', command=get_repo_stats)
button_repo_stats.grid(row=1, column=0)

button_open_issues = tk.Button(
    from_buttons, text='Open Issues', font='Charter 18', width=15, fg='red', command=get_open_issues)
button_open_issues.grid(row=2, column=0)

button_open_prs = tk.Button(from_buttons, text='Open PRs', font='Charter 18', width=15, fg='red', command=get_open_pulls)
button_open_prs.grid(row=3, column=0)

button_projects = tk.Button(
    from_buttons, text='Issue Labels', font='Charter 18', width=15, fg='red', command=get_projects)
button_projects.grid(row=4, column=0)

button_lang_used.bind('<Motion>', lambda _: button_lang_used.config(
    bg='blue', highlightbackground='blue', fg='white'))
button_lang_used.bind('<Leave>', lambda _: button_lang_used.config(
    bg='white', highlightbackground='white', fg='blue'))

button_repo_stats.bind('<Motion>', lambda _: button_repo_stats.config(
    bg='blue', highlightbackground='blue', fg='white'))
button_repo_stats.bind('<Leave>', lambda _: button_repo_stats.config(
    bg='white', highlightbackground='white', fg='blue'))

button_open_issues.bind('<Motion>', lambda _: button_open_issues.config(
    bg='blue', highlightbackground='blue', fg='white'))
button_open_issues.bind('<Leave>', lambda _: button_open_issues.config(
    bg='white', highlightbackground='white', fg='blue'))

button_open_prs.bind('<Motion>', lambda _: button_open_prs.config(
    bg='blue', highlightbackground='blue', fg='white'))
button_open_prs.bind('<Leave>', lambda _: button_open_prs.config(
    bg='white', highlightbackground='white', fg='blue'))

button_projects.bind('<Motion>', lambda _: button_projects.config(
    bg='blue', highlightbackground='blue', fg='white'))
button_projects.bind('<Leave>', lambda _: button_projects.config(
    bg='white', highlightbackground='white', fg='blue'))

# Nested Frame for text area i.e Output Layout

from_output_area = tk.LabelFrame(
    from_buttons, bg="blue", padx=2, pady=2, width=150)
from_output_area.grid(row=0, column=1, rowspan=5, padx=9, pady=9)

# text area i.e Output Layou

txt_output_area = tk.Text(from_output_area, bg='beige')
txt_output_area.pack(side=tk.RIGHT, anchor=tk.E, expand=tk.YES)
txt_output_area.configure(state='disabled')

# Frame for email Entry

frm_subscription = tk.LabelFrame(main_window, bg="black", padx=9, pady=9)
frm_subscription.pack(fill="both", expand="yes")

# Entry for email

enter_email = tk.StringVar()
enter_email = tk.Entry(frm_subscription, bg='blue', textvariable=enter_email, fg="black", font='Charter 14', width=75)
enter_email.insert(0, 'Email')
enter_email.config(state=tk.DISABLED)
enter_email.bind("<Button-1>", enter_email_btn1_click)
enter_email.bind('<Leave>', enter_email_btn1_unclick)
enter_email.pack(side=tk.LEFT, padx=10)

button_subscribe = tk.Button(frm_subscription, text='Subscribe', font='Charter 18', width=12, fg='white', bg='red',command=subscribe_email)
button_subscribe.pack(side=tk.LEFT, padx=15)
button_subscribe.bind('<Motion>', lambda _: button_subscribe.config(bg='blue', highlightbackground='blue', fg='white'))
button_subscribe.bind('<Leave>', lambda _: button_subscribe.config(bg='white', highlightbackground='white', fg='blue'))

# button for send mail
send = tk.Button(frm_subscription, text="send mail", font="times 15", width=16, fg="black", bg="rosy brown",command=send_mail)
send.pack(side=tk.LEFT, padx=15)
send.bind('<Motion>',
          lambda _: send.config(bg='gray', highlightbackground='black', fg='black'))  # while clicking on button
send.bind('<Leave>',
          lambda _: send.config(bg='white', highlightbackground='blue', fg='black'))  # after clicking on button


main_window.mainloop()