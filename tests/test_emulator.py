import unittest
import subprocess

class TestEmulator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Этот метод выполняется один раз перед всеми тестами
        print("Начало тестирования эмулятора...")

    @classmethod
    def tearDownClass(cls):
        # Этот метод выполняется один раз после всех тестов
        print("Завершение тестирования эмулятора.")

    def test_ls(self):
        # Проверка команды 'ls', чтобы убедиться, что она работает и выводит правильные каталоги
        result = subprocess.run(['python', 'emulator.py', 'ls'], capture_output=True, text=True)
        self.assertIn('home', result.stdout)  # Проверяем, что в выводе есть 'home'

    def test_cd(self):
        # Проверка команды 'cd', чтобы убедиться, что она изменяет директорию
        result = subprocess.run(['python', 'emulator.py', 'cd', 'home'], capture_output=True, text=True)
        self.assertIn('my-emulator:/home', result.stdout)  # Проверяем, что мы перешли в /home

    def test_history(self):
        # Проверка команды 'history', чтобы убедиться, что она возвращает историю команд
        result = subprocess.run(['python', 'emulator.py', 'history'], capture_output=True, text=True)
        self.assertIn('history', result.stdout)  # Проверяем, что история команд доступна

    def test_mkdir(self):
        # Проверка команды 'mkdir', чтобы создать каталог и проверить его наличие
        subprocess.run(['python', 'emulator.py', 'mkdir', 'test_dir'])
        result = subprocess.run(['python', 'emulator.py', 'ls'], capture_output=True, text=True)
        self.assertIn('test_dir', result.stdout)  # Проверяем, что директория test_dir появилась

    def test_date(self):
        # Проверка команды 'date', чтобы убедиться, что она выводит текущую дату
        result = subprocess.run(['python', 'emulator.py', 'date'], capture_output=True, text=True)
        self.assertTrue(result.stdout.strip())  # Проверяем, что вывод не пустой

if __name__ == '__main__':
    unittest.main()
