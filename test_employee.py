import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Tuan', 'Nguyen', 50000)
        self.emp_2 = Employee('Mike', 'Baker', 60000)

    def tearDown(self):
        print('tearDown\n')
        pass

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Tuan.Nguyen@email.com')
        self.assertEqual(self.emp_2.email, 'Mike.Baker@email.com')

        self.emp_1.first = 'Mike'
        self.emp_2.first = 'Tuan'

        self.assertEqual(self.emp_1.email, 'Mike.Nguyen@email.com')
        self.assertEqual(self.emp_2.email, 'Tuan.Baker@email.com')

    def test_fullname(self):
        print('test_full_name')
        self.assertEqual(self.emp_1.full_name, 'Tuan Nguyen')
        self.assertEqual(self.emp_2.full_name, 'Mike Baker')

        self.emp_1.first = 'Mike'
        self.emp_2.first = 'Tuan'

        self.assertEqual(self.emp_1.full_name, 'Mike Nguyen')
        self.assertEqual(self.emp_2.full_name, 'Tuan Baker')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 50000 * 1.05)
        self.assertEqual(self.emp_2.pay, 60000 * 1.05)

    def test_mothly_schedule(self):
        print('test_monthly_schedule')
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Nguyen/May')
            self.assertEqual(schedule, 'Success')

            # For bad response
            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Baker/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
