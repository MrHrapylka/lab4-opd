import unittest  # Импортируем модуль unittest
from flask import Flask  # Импортируем класс Flask из модуля flask
from flask_testing import TestCase  # Импортируем класс TestCase из модуля flask_testing
from app import app  # Импортируем модуль app из пакета app


class FlaskAppTests(TestCase):  # Определяем класс тестов FlaskAppTests, который наследуется от TestCase

    def create_app(self):  # Определяем метод create_app
        app.config['TESTING'] = True  # Устанавливаем конфигурацию TESTING для приложения Flask в значение True
        return app  # Возвращаем объект приложения Flask

    def test_index_page(self):  # Определяем метод test_index_page
        response = self.client.get('/')  # Отправляем GET-запрос на корневой URL
        self.assert200(response)  # Проверяем, что код состояния ответа равен 200
        self.assert_template_used('index.html')  # Проверяем, что используется шаблон 'index.html'

    def test_calculate_cube_volume(self):  # Определяем метод test_calculate_cube_volume
        data = {  # Создаем словарь data
            'shape': 'cube',
            'precision': '0',
            'side': '5'
        }
        response = self.client.post('/calculate', data=data, follow_redirects=True)  # Отправляем POST-запрос на '/calculate' с данными
        self.assert200(response)  # Проверяем, что код состояния ответа равен 200
        self.assert_template_used('index.html')  # Проверяем, что используется шаблон 'index.html'
        self.assert_context('volume', 125)  # Проверяем, что переменная контекста 'volume' равна 125

    def test_calculate_sphere_volume(self):  # Определяем метод test_calculate_sphere_volume
        data = {  # Создаем словарь data
            'shape': 'sphere',
            'precision': '1',
            'radius': '3'
        }
        response = self.client.post('/calculate', data=data, follow_redirects=True)  # Отправляем POST-запрос на '/calculate' с данными
        self.assert200(response)  # Проверяем, что код состояния ответа равен 200
        self.assert_template_used('index.html')  # Проверяем, что используется шаблон 'index.html'
        self.assert_context('volume', 113.1)  # Проверяем, что переменная контекста 'volume' равна 113.1

    def test_calculate_cylinder_volume(self):  # Определяем метод test_calculate_cylinder_volume
        data = {  # Создаем словарь data
            'shape': 'cylinder',
            'precision': '2',
            'radius': '2',
            'height': '5'
        }
        response = self.client.post('/calculate', data=data, follow_redirects=True)  # Отправляем POST-запрос на '/calculate' с данными
        self.assert200(response)  # Проверяем, что код состояния ответа равен 200
        self.assert_template_used('index.html')  # Проверяем, что используется шаблон 'index.html'
        self.assert_context('volume', 62.83)  # Проверяем, что переменная контекста 'volume' равна 62.83

    def test_calculate_cone_volume(self):  # Определяем метод test_calculate_cone_volume
        data = {  # Создаем словарь data
            'shape': 'cone',
            'precision': '1',
            'radius': '3',
            'height': '4'
        }
        response = self.client.post('/calculate', data=data, follow_redirects=True)  # Отправляем POST-запрос на '/calculate' с данными
        self.assert200(response)  # Проверяем, что код состояния ответа равен 200
        self.assert_template_used('index.html')  # Проверяем, что используется шаблон 'index.html'
        self.assert_context('volume', 37.7)  # Проверяем, что переменная контекста 'volume' равна 37.7

    def test_calculate_pyramid_volume(self):  # Определяем метод test_calculate_pyramid_volume
        data = {  # Создаем словарь data
            'shape': 'pyramid',
            'precision': '0',
            'base_length': '4',
            'base_width': '6',
            'height': '8'
        }
        response = self.client.post('/calculate', data=data, follow_redirects=True)  # Отправляем POST-запрос на '/calculate' с данными
        self.assert200(response)  # Проверяем, что код состояния ответа равен 200
        self.assert_template_used('index.html')  # Проверяем, что используется шаблон 'index.html'
        self.assert_context('volume', 64)  # Проверяем, что переменная контекста 'volume' равна 64

    def test_invalid_shape(self):  # Определяем метод test_invalid_shape
        data = {  # Создаем словарь data
            'shape': 'invalid_shape',
            'precision': '2',
            'side': '5'
        }
        response = self.client.post('/calculate', data=data, follow_redirects=True)  # Отправляем POST-запрос на '/calculate' с данными
        self.assert200(response)  # Проверяем, что код состояния ответа равен 200
        self.assert_template_used('index.html')  # Проверяем, что используется шаблон 'index.html'
        self.assert_context('volume', None)  # Проверяем, что переменная контекста 'volume' равна None


if __name__ == '__main__':  # Проверяем, запускается ли скрипт непосредственно
    unittest.main()  # Запускаем модуль unittest
