import sys
import datetime

def main():
    if len(sys.argv) != 2:
        print("Usage: python version-updater.py <minor|patch>")
        sys.exit(1)
    
    update_type = sys.argv[1]
    
    # Читаем текущую версию
    try:
        with open('version', 'r') as f:
            version = f.read().strip()
    except:
        version = "1.0.0"
    
    # Парсим версию
    parts = version.split('.')
    major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])
    
    # Обновляем версию
    if update_type == 'minor':
        minor += 1
        patch = 0
    elif update_type == 'patch':
        patch += 1
    else:
        print(f"Unknown update type: {update_type}")
        sys.exit(1)
    
    new_version = f"{major}.{minor}.{patch}"
    
    # Записываем новую версию
    with open('version', 'w') as f:
        f.write(new_version)
    
    # Логируем
    with open('version_log', 'a') as f:
        timestamp = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        f.write(f"[{new_version}] < [{version}] [{timestamp}] {update_type} update\n")
    
    print(new_version)

if __name__== "__main__":
    main()