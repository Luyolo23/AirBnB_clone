#!/usr/bin/python3

"""Unittest for console
"""

import sys
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage


class TestConsole(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.console_instance = HBNBCommand()

    def setUp(self):
        self.console_instance.preloop()

    def tearDown(self):
        self.console_instance.postloop()

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expected_output, mock_stdout, command):
        self.console_instance.onecmd(command)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_create_show_destroy_all_update_commands(self):
        storage.reset()

        # Create
        expected_output = "f1r57-1n574nc3\n"
        self.assert_stdout(expected_output, "create BaseModel")
        obj_instance = storage.all()['BaseModel.f1r57-1n574nc3']

        # Show
        expected_output = str(obj_instance) + '\n'
        self.assert_stdout(expected_output, "show BaseModel {}".format(obj_instance.id))

        # Destroy
        self.assert_stdout("", "destroy BaseModel {}".format(obj_instance.id))
        self.assertNotIn(obj_instance, storage.all().values())

        # All
        obj1_instance = BaseModel()
        obj2_instance = BaseModel()
        expected_output = "[{}, {}]\n".format(str(obj1_instance), str(obj2_instance))
        self.assert_stdout(expected_output, "all BaseModel")

        # Update
        self.assert_stdout(
            "",
            'update BaseModel {} name "New Name"'.format(obj1_instance.id)
        )
        updated_obj_instance = storage.all()['BaseModel.' + obj1_instance.id]
        self.assertEqual(updated_obj_instance.name, "New Name")

    def test_invalid_commands(self):
        storage.reset()

        # Invalid create command
        expected_output = "** class doesn't exist **\n"
        self.assert_stdout(expected_output, "create InvalidClass")

        # Invalid show command
        expected_output = "** class doesn't exist **\n"
        self.assert_stdout(expected_output, "show InvalidClass")

        # Invalid destroy command
        expected_output = "** class doesn't exist **\n"
        self.assert_stdout(expected_output, "destroy InvalidClass")

        # Invalid all command
        expected_output = "** class doesn't exist **\n"
        self.assert_stdout(expected_output, "all InvalidClass")

        # Invalid update command
        expected_output = "** class doesn't exist **\n"
        self.assert_stdout(expected_output, "update InvalidClass")

    def test_empty_line_quit_commands(self):
        # Empty line
        expected_output = ""
        self.assert_stdout(expected_output, "")

        # Quit command
        self.assertTrue(self.console_instance.onecmd("quit"))

    def test_help_commands(self):
        expected_output = "Quit command to exit the program\n"
        self.assert_stdout(expected_output, "help quit")


if __name__ == '__main__':
    unittest.main()

