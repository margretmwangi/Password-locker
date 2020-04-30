import unittest
from user import User


class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviors.

    Args:
        unittest.TestCases: TestCase class that helps in creatng test cases

    '''

    def setUp(self):
        '''
        Set up method to run before each test case.
        '''
        self.new_user = User('Instagram', 'Kyle', 'Mwangi','kylemort','123456')



    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.platform,"Instagram")
        self.assertEqual(self.new_user.first_name,"Kyle")
        self.assertEqual(self.new_user.last_name,"Mwangi")
        self.assertEqual(self.new_user.username,"kylemort")
        self.assertEqual(self.new_user.password,"123456")


    def test_save_user(self):
        '''
        test_save_user to test if the user object is saved into the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)


    def test_save_multiple_users(self):
        '''
        test_save_multiple_users to check if we can save multiple users/ accounts
        '''
        self.new_user.save_user()
        test_user = User('Instagram','Steve','Ndegwa','stevendegwa','8767')
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    


    

if __name__ == '__main__':
    unittest.main(verbosity=2)