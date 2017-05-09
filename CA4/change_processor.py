import csv
sep = 72*'-'

# the class to process changes
class ChangeProcessor(object):
    def __init__(self, file_name):
        self.read_file(file_name)

    # open the file - and read all of the lines.
    # use strip to strip out spaces and trim the line.
    def read_file(self, file_name):
        self.data = [line.strip() for line in open(file_name, 'r')]
        self.process_commits()
        return len(self.data)

    def process_commits(self):
        self.commits = []
        self.authors = {}
        current_commit = None
        index = 0

        while True:
            try:
                # parse each of the commits and put them into a list of commits
                details = self.data[index + 1].split('|')
                details = [column.strip() for column in details]

                # the file changes with spaces at end removed.
                details.append(self.data[index+2:self.data.index('',index+1)])

                # add details to the list of commits.
                self.commits.append(details)
                index = self.data.index(sep, index + 1)
                if details[1] not in self.authors: #if author in authors
                    self.authors[details[1]] = 1
                else:
                    self.authors[details[1]] = self.authors[details[1]] + 1

                comment_line_count = int(details[3].strip().split(' ')[0])
                # add the comments to the details.
                details.append(self.data[index-comment_line_count:index])

            except IndexError:
                break
        # return the order of the file to the same sequence it was created
        self.commits.reverse()
        # create a writable file to output our container to
        ofile = open('ttest.csv', "wb")
        writer = csv.writer(ofile, delimiter=',')
        # write to the file and use ',' as a delimitor - csv
        for index in self.commits:
            writer.writerow(index)
        # close the opened file so it can be accessed
        ofile.close()


    def get_author(self, index):
        return self.commits[index][1]

    def get_date(self, index):
        return self.commits[index][2]

    def get_number_of_comment_lines(self, index):
        return self.commits[index][3]

    def get_revision(self, index):
        return self.commits[index][0]

    def get_file_changes(self, index):
        return self.commits[index][4]

    def get_comment(self, index):
        return self.commits[index][5]

    def get_number_of_commits(self):
        return len(self.commits)

    def get_number_of_authors(self):
        return len(self.authors)

    def get_number_of_commit_by_author(self, author):
        return self.authors[author]


# enable so that this is only called when the script run from the command line
if __name__ == '__main__':
    fname = 'changes_python.log'
    changes = ChangeProcessor(fname)

    #print(changes.commits)
    #print(changes.authors)
    #print(changes.get_author(5))
    #print(changes.get_comment(102))