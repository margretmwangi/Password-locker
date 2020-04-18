import unittest # Importing the unittest module
from user import Users

class TestUsers(unittest.TestCase):
    
    '''
    Test class that defines test cases for the user class behaviours.
    
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = Users("MaggieNymoh", "telegram") # create new user
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name,"MaggieNymoh")
        self.assertEqual(self.new_user.password,"telegram")
        
            
        
class TestCredentials(unittest.TestCase):
    
    '''
    Test class that defines test cases for the credential behaviours.
    
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''
    
    def setUp(self):
        '''
        set up method to run before each test cases.
        '''

        
   
if __name__== '__main__':
    unittest.main()        
        
    