import unittest
from credentials import Info

class TestInfo(unittest.TestCase):
    def setUp(self):
        self.new_info =Info("mwangi.maggie","mwangi.maggie")
    def test_init(self):
        self.assertEqual(self.new_info.face_bookp,"mwangi.maggie")
        self.assertEqual(self.new_info.email_p,"mwangi.maggie")
    def test_save_info(self):
        '''
        to test if user info is saved
        '''
        self.new_info.save_info()
        self.assertEqual(len(Info.info_list),1)
    def tearDown(self):
        Info.info_list = []
    def test_delete_info(self):
        self.new_info.save_info()
        test_info = Info("kyle.89","kyle.89")
        test_info.save_info()
        test_info.delete_info()
        self.assertEqual(len(Info.info_list),1)
    def test_display_creds(self):
        self.assertEqual(Info.display_info(),Info.info)

if __name__ == '__main__':
    unittest.main()