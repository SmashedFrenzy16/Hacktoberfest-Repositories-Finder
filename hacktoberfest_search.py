from github import Github

g_cred = Github("<Paste Your Token Here>")

count = int(input("Enter in the number of repositories to display: "))

repo_count = count

icount = 0

for i in g_cred.search_repositories("topic:hacktoberfest"):

    print(f"{icount + 1}. {i}")

    icount += 1

    if icount >= repo_count:

        break
