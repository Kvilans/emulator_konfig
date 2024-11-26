import os
import zipfile
import yaml
from datetime import datetime

class Emulator:
    def __init__(self, config):
        # Загрузка конфигурационного файла
        with open(config, 'r') as file:
            config_data = yaml.safe_load(file)
        self.hostname = config_data['hostname']
        self.filesystem_path = config_data['filesystem_path']
        self.startup_script = config_data['startup_script']
        
        # Инициализация переменных
        self.history = []
        self.current_directory = "/"
        self.virtual_filesystem = {}

        # Загрузка виртуальной файловой системы
        self.load_filesystem()

        # Выполнение стартового скрипта
        self.execute_startup_script()

    def load_filesystem(self):
        with zipfile.ZipFile(self.filesystem_path, 'r') as zip_ref:
            zip_ref.extractall("/tmp/virtual_fs")
        print("Файловая система загружена")

    def execute_startup_script(self):
        with open(self.startup_script, 'r') as script:
            for command in script:
                self.execute_command(command.strip())

    def execute_command(self, command):
        self.history.append(command)
        parts = command.split()

        if not parts:
            return
        
        cmd = parts[0]
        args = parts[1:] if len(parts) > 1 else []

        if cmd == "ls":
            self.ls()
        elif cmd == "cd":
            self.cd(args)
        elif cmd == "mkdir":
            self.mkdir(args)
        elif cmd == "date":
            self.show_date()
        elif cmd == "history":
            self.show_history()
        elif cmd == "exit":
            self.exit_shell()
        else:
            print(f"Команда '{cmd}' не найдена.")

    def ls(self):
        try:
            files = os.listdir(f"/tmp/virtual_fs{self.current_directory}")
            for f in files:
                print(f)
        except FileNotFoundError:
            print(f"Директория '{self.current_directory}' не существует.")

    def cd(self, args):
        if len(args) != 1:
            print("Неверное количество аргументов для команды 'cd'.")
            return
        new_dir = args[0]
        potential_path = os.path.join(self.current_directory, new_dir)
        if os.path.isdir(f"/tmp/virtual_fs{potential_path}"):
            self.current_directory = os.path.normpath(potential_path)
        else:
            print(f"Директория '{new_dir}' не найдена.")

    def mkdir(self, args):
        if len(args) != 1:
            print("Неверное количество аргументов для команды 'mkdir'.")
            return
        new_dir = args[0]
        path_to_create = os.path.join(f"/tmp/virtual_fs{self.current_directory}", new_dir)
        if not os.path.exists(path_to_create):
            os.makedirs(path_to_create)
            print(f"Директория '{new_dir}' создана.")
        else:
            print(f"Директория '{new_dir}' уже существует.")

    def show_date(self):
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def show_history(self):
        for i, cmd in enumerate(self.history, 1):
            print(f"{i} {cmd}")

    def exit_shell(self):
        print("Завершение работы эмулятора.")
        exit(0)


if __name__ == "__main__":
    config_path = "config.yaml"
    emulator = Emulator(config=config_path)
    
    while True:
        command = input(f"{emulator.hostname}:{emulator.current_directory}$ ")
        emulator.execute_command(command)

def execute_startup_script(self):
    if not self.startup_script:
        return
    try:
        with open(self.startup_script, 'r', encoding='utf-8') as script:
            for line in script:
                line = line.strip()
                if line.startswith("#"):  # Пропуск комментариев
                    continue
                self.process_command(line)  # Передача строки как команды
    except FileNotFoundError:
        print(f"Файл стартового скрипта {self.startup_script} не найден.")
    except Exception as e:
        print(f"Ошибка выполнения стартового скрипта: {e}")

