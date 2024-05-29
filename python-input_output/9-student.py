#!/usr/bin/python3
""" This module contain a class called Student """


class Student:

    def __init__(self, first_name, last_name, age):
        """ method that initialize an instance

        Args:
            first_name ([str]): is the first name
            last_name ([str]): is the second name
            age ([str, int]): is the age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ method to retreive dictionary representation"""
        return self.__dict__
