from taiga import TaigaAPI
import os
import sys

api = TaigaAPI(
    host=os.environ["HOST"]
)

api.auth(
    username=os.environ["USERNAME"],
    password=os.environ["PASSWD_TAIGA"]
)

projects = api.projects.list()
asan_bridge = projects[0]
operations = projects[1]

print("Current Projects: ",projects[0],'(1)','and', projects[1],'(2)')
print("Choose one.")
project_name = projects[int(input())-1]
print(project_name)

presentation = ""

stories = project_name.list_user_stories()

milestones = project_name.list_milestones()
currentMilestoneId = len(milestones)

presentation += "Project name is: " + str(project_name) + '\n' + '\n'

for story in project_name.list_user_stories():

    if story.milestone != currentMilestoneId:
        continue
    if story.to_dict()['status'] == 19:
        presentation += "[" + str(story) + "]" + ' ' + '[status=New]' + '\n'
    if story.to_dict()['status'] == 20:
        presentation += "[" + str(story) + "]" + ' ' + '[status=Ready]' + '\n'
    if story.to_dict()['status'] == 21:
        presentation += "[" + str(story) + "]" + ' ' + '[status=In Progress]' + '\n'
    if story.to_dict()['status'] == 22:
        presentation += "[" + str(story) + "]" + ' ' + '[status=Ready for Test]' + '\n'
    if story.to_dict()['status'] == 23:
        presentation += "[" + str(story) + "]" + ' ' + '[status=Done]' + '\n'
    if story.to_dict()['status'] == 24:
        presentation += "[" + str(story) + "]" + ' ' + '[status=Archived]' + '\n'
    presentation += '\n'

    for task in story.list_tasks():
        if task.to_dict()['status'] == 16:
            presentation += "\t" + str(task) + ' ' + '[status=New]' + "\n"
        if task.to_dict()['status'] == 17:
            presentation += "\t" + str(task) + ' ' + '[status=In Progress]' + "\n"
        if task.to_dict()['status'] == 18:
            presentation += "\t" + str(task) + ' ' + '[status=Ready For test]' + "\n"
        if task.to_dict()['status'] == 19:
            presentation += "\t" + str(task) + ' ' + '[status=Closed]' + "\n"
        if task.to_dict()['status'] == 20:
            presentation += "\t" + str(task) + ' ' + '[status=Need Info]' + "\n"
    presentation += '\n'


issues = project_name.list_issues()
for issue in issues:
    if issue.to_dict()['status'] == 22:
        presentation += 'Issue:' + ' ' + str(issue) + ' ' + '[status=New]' + '\n'
    if issue.to_dict()['status'] == 23:
        presentation += 'Issue:' + ' ' + str(issue) + ' ' + '[status=In Progress]' + '\n'
    if issue.to_dict()['status'] == 24:
        presentation += 'Issue:' + ' ' + str(issue) + ' ' + '[status=Ready For Test]' + '\n'
    if issue.to_dict()['status'] == 25:
        presentation += 'Issue:' + ' ' + str(issue) + ' ' + '[status=Closed]' + '\n'
    if issue.to_dict()['status'] == 26:
        presentation += 'Issue:' + ' ' + str(issue) + ' ' + '[status=Need Info]' + '\n'
    if issue.to_dict()['status'] == 27:
        presentation += 'Issue:' + ' ' + str(issue) + ' ' + '[status=Rejected]' + '\n'
    if issue.to_dict()['status'] == 28:
        presentation += 'Issue:' + ' ' + str(issue) + ' ' + '[status=Postponed]' + '\n'

f = open(str(project_name)+'.txt', 'w')
print(presentation)
f.write(presentation)