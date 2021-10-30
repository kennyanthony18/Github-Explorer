import requests
import yagmail_outlook


def get_owner_reop(url):
    owner = repo = None
    # your code here

    response_list = url.split('/')
    owner = response_list[3]
    repo = response_list[4]
    return owner, repo


def languages_used(url):
    owner, repo = get_owner_reop(url)
    languages = []

    api_url = f"https://api.github.com/repos/{owner}/{repo}/languages"

    response = requests.get(api_url)

    if response.status_code != 200:
        print("failed to get the languages")
        return

    languages = response.json()
    return list(languages.keys())


def get_repo_stats(url):
    owner, repo = get_owner_reop(url)
    issues_count = 0
    pr_count = 0
    api_url = f"https://api.github.com/repos/{owner}/{repo}"

    open_issues_list = get_open_issues(url)
    issues_count = len(open_issues_list)
    print_issues_list = get_open_pulls(url)
    pr_count = len(print_issues_list)
    s1 = "issues count"
    s2 = "pr count"
    s3 = issues_count
    s4 = pr_count
    s = f'{s1}={s3}\n{s2}={s4}'
    return s


def get_open_issues(url):

    owner, repo = get_owner_reop(url)

    open_issues_list = []

    api_url = f"https://api.github.com/repos/{owner}/{repo}/issues"

    rat = requests.get(api_url)

    response_open_issues_list = rat.json()
    count = 1
    for item in response_open_issues_list:
        if 'pull_request'not in item and 'state' in item or 'number' in item:
            open_issues_list.append(f"{count}: {item['title']}")
            count += 1

    return open_issues_list


def get_open_pulls(url):
    owner, repo = get_owner_reop(url)
    pr_issues_list = []

    api_url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    kat = requests.get(api_url)
    pull_requests_list = kat.json()
    count = 1
    for item in pull_requests_list:
        if 'pull_request' in item and 'state' in item or 'number' in item:
            pr_issues_list.append(f"{count}: {item['title']}")
            count += 1
    return pr_issues_list


def get_projects(url):
    owner, repo = get_owner_reop(url)
    project_list = []

    api_url = f"https://api.github.com/repos/{owner}/{repo}/labels"
    mat = requests.get(api_url)
    projects_lists = mat.json()
    count = 1
    for item in projects_lists:
        project_list.append(f"{count}: {item['name']}")
        count += 1
    return project_list


def save_email(email):
    f = open("emails.txt", 'r').readlines()
    seen = set(f)
    for line in f:
        line_lower = line.lower()
        if line_lower in seen:
            print('save email', email)
            with open('emails.txt', 'a') as f:
                f.write(email + '\n')
        else:
            return f'Email All ready present'


def send_mail(body):
    lines_list = open('emails.txt').readlines()
    for line in lines_list:
        yag = yagmail_outlook.SMTP(user='enter your E-mail ID', password='enter your password')
        yag.send(to=line, subject='test subject', contents=body,
                 attachments=['lang_data.txt', 'repo_data.txt', 'issue_data.txt', 'pr_data.txt'])


if __name__ == 'main':
    send_mail(body="this is a SkillAura internship program")