def load_rules(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        rules = [line.strip() for line in f.readlines()]
    return rules

def scan_file(filepath, rules):
    found = []
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    for rule in rules:
        if rule in content:
            found.append(rule)

    return found
