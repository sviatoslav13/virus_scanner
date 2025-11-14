def load_rules(filepath):
    rules = []
    try:
        with open(filepath, 'r', encoding="utf-8") as file:
            for line in file:
                rule = line.strip()
                if rule:
                    rules.append(rule)
    except FileNotFoundError:
        print("Rules file not found")
    return rules


def scan_file(filepath, rules):
    found = []
    try:
        with open(filepath, 'r', encoding="utf-8", errors="ignore") as file:
            content = file.read()
            for rule in rules:
                if rule in content:
                    found.append(rule)
    except:
        print("Could not read file")
    return found
