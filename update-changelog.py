import sys
import datetime

def update_changelog(version, branch_name):
    changelog_file = 'changelog.md'
    
    # Определяем тип изменения
    if branch_name.startswith('feature/'):
        change_type = 'Feature'
    elif branch_name.startswith('hotfix/'):
        change_type = 'Hotfix'
    else:
        change_type = 'Change'
    
    # Создаем запись
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
    entry = f"## {version} - {timestamp}\n"
    entry += f"- {change_type}: Changes from {branch_name}\n"
    entry += f"- Author: GitHub Actions\n\n"
    
    # Читаем существующий контент
    try:
        with open(changelog_file, 'r') as f:
            existing_content = f.read()
    except FileNotFoundError:
        existing_content = "# Changelog\n\n"
    
    # Добавляем новую запись в начало
    new_content = "# Changelog\n\n" + entry
    
    # Если есть старый контент, добавляем его после новой записи
    if existing_content.startswith("# Changelog\n\n"):
        old_entries = existing_content.replace("# Changelog\n\n", "", 1)
        new_content += old_entries
    else:
        new_content += existing_content
    
    # Записываем обратно
    with open(changelog_file, 'w') as f:
        f.write(new_content)
    
    print(f"Changelog updated for version {version}")

if name == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python update_changelog.py <version> <branch_name>")
        sys.exit(1)
    
    version = sys.argv[1]
    branch_name = sys.argv[2]
    update_changelog(version, branch_name)