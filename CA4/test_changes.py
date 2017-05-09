import unittest
from change_processor import ChangeProcessor

# test the changes functionality
class TestChanges(unittest.TestCase):

    def setUp(self):
        self.change_processor = ChangeProcessor('test_changes_1.txt')
        self.change_processor2 = ChangeProcessor('test_changes_2.txt')
        self.change_processor3 = ChangeProcessor('changes_python.log')

    # this tests the length of data file is read correctly.
    def test_changes_length_of_data(self):
        result = len(self.change_processor.data)
        self.assertEqual(10, result)
        result = len(self.change_processor2.data)
        self.assertEqual(99, result)
        result = len(self.change_processor3.data)
        self.assertEqual(5255, result)

    # this tests the number of commits by author 
    def test_changes_get_number_of_commit_by_author(self):
        result = self.change_processor3.get_number_of_commit_by_author('Thomas')
        self.assertEqual(191, result)

	# this tests the number of authors
    def test_changes_number_of_authors(self):
        result = self.change_processor.get_number_of_authors()
        self.assertEqual(1, result)
        result = self.change_processor2.get_number_of_authors()
        self.assertEqual(3, result)
        result = self.change_processor3.get_number_of_authors()
        self.assertEqual(10, result)

    # this tests the number of commits
    def test_changes_number_of_commits(self):
        result = self.change_processor.get_number_of_commits()
        self.assertEqual(1, result)
        result = self.change_processor2.get_number_of_commits()
        self.assertEqual(9, result)
        result = self.change_processor3.get_number_of_commits()
        self.assertEqual(422, result)

    # this tests the author
    def test_changes_get_author(self):
        result = self.change_processor.get_author(0)
        self.assertEqual('viacheslav.vdovenko', result)
        result = self.change_processor2.get_author(6)
        self.assertEqual('vnai0001', result)
        result = self.change_processor3.get_author(420)
        self.assertEqual('Thomas', result)

    # this tests the first revision
    def test_changes_get_revision(self):
        result = self.change_processor3.get_revision(0)
        self.assertEqual('r1491146', result)

    # this tests the date
    def test_changes_get_date(self):
        result = self.change_processor3.get_date(0)
        self.assertEqual('2015-07-13 09:21:48 +0100 (Mon, 13 Jul 2015)', result)

    # this tests the comment
    def test_changes_get_comment(self):
        result = self.change_processor.get_comment(0)
        self.assertEqual(['Renamed folder to the correct name'], result)
        result = self.change_processor2.get_comment(5)
        self.assertEqual(['Chnaged jira url to htps'], result)
        result = self.change_processor3.get_comment(420)
        self.assertEqual(['Removed unused webview.plan.management and webview_plan_management properties'], result)
        result = self.change_processor3.get_comment(421)
        self.assertEqual(['Renamed folder to the correct name'], result)

    # this tests the number of comment lines
    def test_changes_get_number_of_comment_lines(self):
        result = self.change_processor3.get_number_of_comment_lines(0)
        self.assertEqual('1 line', result)

    # this tests the file changes of first revision
    def test_changes_get_file_changes(self):
        result = self.change_processor3.get_file_changes(0)
        self.assertEqual(['Changed paths:',\
        'D /cloud/personal/client-international/android/branches/15-2-solutions',\
        'A /cloud/personal/client-international/android/branches/android-15.2-solutions (from /cloud/personal/client-international/android/branches/15-2-solutions:1491145)'], result)

if __name__ == '__main__':
    unittest.main()
