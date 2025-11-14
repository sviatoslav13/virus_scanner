from scanner import load_rules, scan_file

def main():
    rules_path = 'rules.txt'
    test_file_path = 'test_files/yara_var15.exe'  # твій варіант

    rules = load_rules(rules_path)
    found_rules = scan_file(test_file_path, rules)

    if not found_rules:
        print("File is clean")
    else:
        print(f"File is infected with rules: {', '.join(found_rules)}")

if __name__ == "__main__":
    main()
