import json
import os

TASKS_FILE = 'tasks.json'


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f)
    try:
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            tasks = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        tasks = []
    return tasks


def save_tasks(tasks):
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def add_task(description):
    tasks = load_tasks()
    tasks.append({'description': description, 'completed': False})
    save_tasks(tasks)
    print('وظیفه اضافه شد.')


def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print('هیچ وظیفه‌ای وجود ندارد.')
        return
    for i, task in enumerate(tasks, 1):
        status = '✓' if task.get('completed') else '✗'
        print(f'{i}. [{status}] {task.get("description", "")}')


def complete_task(number):
    tasks = load_tasks()
    if 1 <= number <= len(tasks):
        tasks[number - 1]['completed'] = True
        save_tasks(tasks)
        print('وظیفه انجام شد.')
    else:
        print('شماره وظیفه نامعتبر است.')


def main():
    while True:
        command = input('> ').strip()
        if command == 'exit':
            print('خروج...')
            break
        elif command.startswith('add '):
            desc = command[4:].strip()
            if desc:
                add_task(desc)
            else:
                print('توضیح وظیفه را وارد کنید.')
        elif command == 'view':
            view_tasks()
        elif command.startswith('complete '):
            num = command[9:].strip()
            if num.isdigit():
                complete_task(int(num))
            else:
                print('شماره وظیفه نامعتبر است.')
        else:
            print('دستور نامعتبر است.')


if __name__ == '__main__':
    main()
