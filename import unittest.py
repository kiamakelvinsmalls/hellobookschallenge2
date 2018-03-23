# class of unittests
import unittest
from app import app
class HelloBook(unittest.TestCase):
    def setUp(self):
    # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True
    def tearDown(self):
        pass
    #test for index page
    def test_urlindex(self):
    # creates a test client
        result = self.app.get('/index')
        # repond with code 200 if page found
        self.assertEqual(result.status_code, 200)
    #test for admindashboard
    def test_urladmindashboard(self):
        result = self.app.get('/admindashboard')
        # repond with code 200 if page found
        self.assertEqual(result.status_code, 200)
    #test for add page
    def test_urladd(self):
        result = self.app.get('/add')
        # repond with code 200 if page found
        self.assertEqual(result.status_code, 200)
    #test for update page
    def test_urlupdate(self):
        result = self.app.get('/update')
    	# repond with code 200 if page found
        self.assertEqual(result.status_code, 200)
    #test for delete page
    def test_urldelete(self):
        result = self.app.get('/delete')
        # repond with code 200 if page found
        self.assertEqual(result.status_code, 200)
    # test for view page
    def test_urlview(self):
        result = self.app.get('/view')
        # repond with code 200 if page found
        self.assertEqual(result.status_code, 200)
    #test for dashboard
    def test_urldashboard(self):
        result = self.app.get('/dashboard')
        # repond with code 200 if page found
        self.assertEqual(result.status_code, 200)
    #test for borrow page
    def test_urlborrow(self):
        result = self.app.get('/borrow')
        # repond with code 200 if page found
        self.assertEqual(result.status_code, 200)
    def test_urlreturned(self):
        result = self.app.get('/returned')
        # repond with code 200 if page found
        self.assertEqual(result.status_code, 200)
    def test_urlduereturn(self):
        result = self.app.get('/dueReturn')
        # repond with code 200 if page found
        self.assertEqual(result.status_code, 200)
    def test_urlprofile(self):
        #test for profile paGE
        result = self.app.get('/profile')
        # repond with code 200 if page found
        self.assertEqual(result.status_code, 200)
if __name__ == "__main__":
    unittest.main()
