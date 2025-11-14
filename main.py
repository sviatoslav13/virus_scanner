from scanner import load_rules, scan_file

file_to_scan = "test_files/15.txt"   # твій файл варіанту 15
rules = load_rules("rules.txt")
results = scan_file(file_to_scan, rules)

if not results:
    print(f"Файл {file_to_scan} чистий.")
else:
    print(f"УВАГА! У файлі {file_to_scan} знайдено загрози: {results}")
