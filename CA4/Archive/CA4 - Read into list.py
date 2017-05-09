# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 18:36:33 2017

@author: macan
"""

class Commit:
    'class for commits'
   
    def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None):
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment

    def get_commit_comment(self):
        return 'svn merge -r' + str(self.revision-1) + ':' + str(self.revision) + ' by ' \
                + self.author + ' with the comment ' + ','.join(self.comment) \
                + ' and the changes ' + ','.join(self.changes)




# enable so that this is only called when the script run from the command line
if __name__ == '__main__':
    fname = 'changes_python.log'
    commits_values = []
    count_sections = 0    
    sep_term = 72*"-"
    
    
    
    try:
        data = [line.strip() for line in open(fname, 'r')]
        print len(data)
    except:
        print "File name as typed cannot be opened or does not exist:", fname
        exit()
    
    for line in data:
        #line = line.split()
        if line == sep_term:
            user_commit = line
            count_sections += 1
            if commits_values == []:
                commits_values = [user_commit]
            else:
                commits_values.append(user_commit)
    print(commits_values)
    #i = 0
    #while i < len(commits_values):
    #    print commits_values[i]
    #    i += 1
    print "There were {0} sections in the file.".format(count_sections)