#!/bin/bash

# Установка зависимостей
pip install -r requirements.txt

# Запуск тестов
python -m unittest discover tests

# Запуск эмулятора
python emulator.py
