#!/usr/bin/python3
""" Unittest for base.py """
import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ class for test base """

    def testid(self):
        """testing id """
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base(48)
        b3 = Base()
        b4 = Base()
        b5 = Base(-1)
        b6 = Base(None)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 48)
        self.assertEqual(b3.id, 2)
        self.assertEqual(b4.id, 3)
        self.assertEqual(b5.id, -1)
        self.assertEqual(b6.id, 4)

        self.assertEqual(str(type(Base)), "<class 'type'>")
        self.assertEqual(str(type(Rectangle)), "<class 'type'>")
        self.assertEqual(str(type(Square)), "<class 'type'>")

        r1 = Rectangle(2, 4)
        self.assertEqual(isinstance(r1, Rectangle), True)

        sq1 = Square(4)
        self.assertEqual(isinstance(sq1, Square), True)

        self.assertEqual(str(type(r1)), "<class 'models.rectangle.Rectangle'>")
        self.assertEqual(str(type(sq1)), "<class 'models.square.Square'>")
        self.assertEqual(issubclass(Square, Rectangle), True)
        self.assertEqual(issubclass(Square, Base), True)
        self.assertEqual(issubclass(Rectangle, Base), True)

        self.assertEqual(issubclass(Base, Rectangle), False)
        self.assertEqual(issubclass(Base, Square), False)

        r2 = Rectangle(4, 5)
        r3 = Rectangle(4, 5)
        self.assertEqual(r2 is r3, False)

        sq2 = Square(4)
        sq3 = Square(4)
        self.assertEqual(sq2 is sq3, False)

    def test_json_dict_to_str_0(self):
        """test json, convert dict to str"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(dictionary, {'width': 10, 'height': 7, 'x': 2,
                                      'id': 1, 'y': 8})
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(json_dictionary), str)

    def test_json_dict_to_str_0(self):
        """test json, convert dict to str"""
        Base._Base__nb_objects = 0
        dictionary = None
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, '[null]')

    def test3_to_json_string(self):
        """funct to pass to JSON string"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            Base.to_json_string()

        Base._Base__nb_objects = 0
        jstrg = Base.to_json_string([])
        self.assertEqual(jstrg, '[]')

        Base._Base__nb_objects = 0
        MyList = [1, 2, 3]
        jstrg = Base.to_json_string([MyList])
        self.assertEqual(jstrg, "[[1, 2, 3]]")

        Base._Base__nb_objects = 0
        with self.assertRaises(NameError):
            MyString = "Hello"
            jstrg = Base.to_json_string(MyString)
            self.assertEqual(jstrg, Hello)

        Base._Base__nb_objects = 0
        i = (1, "foo", "bar")
        jsdict = Base.to_json_string(i)
        self.assertEqual(jsdict, '[1, "foo", "bar"]')

        Base._Base__nb_objects = 0
        Rect2 = Rectangle(5, 4)
        new_dict2 = Rect2.to_dictionary()
        jstrg = Base.to_json_string([new_dict2])
        self.assertEqual(new_dict2, {'y': 0, 'height': 4,
                                     'width': 5, 'x': 0, 'id': 1})

        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            Rect3 = Rectangle(1)
            new_dict3 = Rect3.to_dictionary()
            jstrg2 = Base.to_json_string([new_dict3])
            Base.to_json_string(jstrg2)

    def test1_jsonstr_to_dic(self):
        """ test json to dict """
        list_input1 = [
            {'id': 97, 'width': 5, 'height': 4},
            {'id': 79, 'width': 4, 'height': 5}
        ]
        json_list_input1 = Rectangle.to_json_string(list_input1)
        list_output1 = Rectangle.from_json_string(json_list_input1)
        self.assertEqual(list_output1, [{'height': 4, 'width': 5,
                                        'id': 97}, {'height': 5, 'width': 4,
                                                    'id': 79}])

        json_list_input2 = "[]"
        list_output2 = Rectangle.from_json_string(json_list_input2)
        self.assertEqual(list_output2, [])

        json_list_input3 = None
        list_output3 = Rectangle.from_json_string(json_list_input3)
        self.assertEqual(list_output3, [])

        with self.assertRaises(ValueError):
            json_list_input4 = "Hello Python"
            list_output4 = Rectangle.from_json_string(json_list_input4)
            self.assertEqual(list_output4, "")

        list_input5 = [
            {'id': 97, 'width': 5}
        ]
        json_list_input5 = Rectangle.to_json_string(list_input5)
        list_output5 = Rectangle.from_json_string(json_list_input5)
        self.assertEqual(list_output5, [{'id': 97, 'width': 5}])

    def test3_json_to_file1(self):
        """ test json string into file"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(2, 4)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        lista = [{"id": 1, "width": 2, "y": 0, "x": 0, "height": 4},
                 {"id": 2, "width": 2, "y": 0, "x": 0, "height": 4}]
        with open("Rectangle.json", "r") as file:
            file1 = file.read()
            list_output = Rectangle.from_json_string(file1)
            self.assertEqual(list_output, lista)

    def test4_json_to_file2(self):
        """ test json string into file"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(2, 4)
        Rectangle.save_to_file([r1])
        lista = [{"id": 1, "x": 0, "width": 2, "y": 0, "height": 4}]
        with open("Rectangle.json", "r") as file:
            file1 = file.read()
            list_output = Rectangle.from_json_string(file1)
            self.assertEqual(list_output, lista)

    def test5_json_to_file3(self):
        """ test json string into file"""
        Base._Base__nb_objects = 0
        s1 = Rectangle(4, 5)
        s2 = Rectangle(6, 7)
        s3 = Rectangle(8, 9)
        Rectangle.save_to_file([s1, s2, s3])
        with open("Rectangle.json", "r") as file:
            file1 = file.read()
            list_output = Rectangle.from_json_string(file1)
            lista = [{'x': 0, 'width': 4, 'id': 1, 'height': 5, 'y': 0},
                     {'x': 0, 'width': 6, 'id': 2, 'height': 7, 'y': 0},
                     {'x': 0, 'width': 8, 'id': 3, 'height': 9, 'y': 0}]
            self.assertEqual(list_output, lista)

    def test3_json_to_file(self):
            """ test json string into file"""
            Base._Base__nb_objects = 0
            r1 = Rectangle(2, 4)
            r2 = Rectangle(2, 4)
            Rectangle.save_to_file([r1, r2])
            with open("Rectangle.json", "r") as file:
                file1 = file.read()
                self.assertEqual(sorted(file1), sorted('[{"id": 1, ' +
                                                       '"width": 2, ' +
                                                       '"y": 0, ' +
                                                       '"x": 0, ' +
                                                       '"height": 4}, ' +
                                                       '{"id": 2, ' +
                                                       '"width": 2, ' +
                                                       '"y": 0, ' +
                                                       '"x": 0, ' +
                                                       '"height": 4}]'))

    def test_csv_1(self):
        """test csv1"""
        Base._Base__nb_objects = 0
        r2 = Rectangle(10, 7, 2, 8)
        r3 = Rectangle(2, 4)
        list_rectangles_input = [r2, r3]
        list_rectangles_input = [r2, r3]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        for rect in list_rectangles_output:
            self.assertEquals(rect.__str__(), '[Rectangle] ({}) {}/{} - {}/{}'
                              .format(rect.id, rect.x, rect.y, rect.width,
                                      rect.height))

    def test_csv_2(self):
        """test csv2"""
        Base._Base__nb_objects = 0
        self.s1 = Square(5)
        self.s2 = Square(7, 9, 1)
        list_squares_input = [self.s1, self.s2]
        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()
        for rect in list_squares_output:
            self.assertEquals(rect.__str__(), '[Square] ({}) {}/{} - {}'
                              .format(rect.id, rect.x, rect.y, rect.size))

if __name__ == "__main__":
    unittest.main()