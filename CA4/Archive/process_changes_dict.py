
# open the file - and read all of the lines.
changes_file = 'changes_python.log'
# use strip to strip out spaces and trim the line.

#my_file = open(changes_file, 'r')
#data = my_file.readlines()

data = [line.strip() for line in open(changes_file, 'r')]

# print the number of lines read
print(len(data))

sep = 72*'-'

# create the commit class to hold each of the elements - I am hoping there will be 422
# otherwise I have messed up.


commits = []
current_commit = None
index = 0

author = {}
while True:
    try:
        # parse each of the commits and put them into a list of commits
        current_commit = {}
        details = data[index + 1].split('|')
        current_commit['revision'] = int(details[0].strip().strip('r'))
        current_commit['author'] = details[1].strip()
        current_commit['date'] = details[2].strip()
        current_commit['comment_line_count'] = int(details[3].strip().split(' ')[0])
        current_commit['changes'] = data[index+2:data.index('',index+1)]
        #print(current_commit.changes)
        index = data.index(sep, index + 1)
        current_commit['comment'] = data[index-current_commit['comment_line_count']:index]
        commits.append(current_commit)
    except IndexError:
        break

print(len(commits))

commits.reverse()

print(commits[0])