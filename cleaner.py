from pathlib import Path

settings = Path() / "Settings.ini"

print(settings)


def parse_rocket_dock_config(config_path):
    lines_to_keep = []

    with open(config_path, "r") as file:
        for line in file:
            lines_to_keep.append(line)
    return lines_to_keep


def check_and_remove_nonexistent_icons(lines):
    new_lines = []
    command_key = None
    for line in lines:
        key_value = line.split("=", 1)
        if len(key_value) == 2:
            key, value = map(str.strip, key_value)
        else:
            key = key_value[0].strip()
            value = ''
        if key.lower().endswith("command"):
            command_key = key
            n_command_line = value.split("?")[0].strip()
            n_command_path = Path(n_command_line)
            if n_command_path.exists():
                new_lines.append(line)

        else:
            new_lines.append(line)


    updated_lines = []
    last_memory = 0
    for line in new_lines:
        if not line.split('-')[0].isdigit():
            updated_lines.append(line)
        elif line.split('-')[0].isdigit():
            line_number = int(line.split('-')[0])
            last_memory = line_number
            if line_number == last_memory:
                updated_lines.append(line)
            elif line_number > last_memory + 1:
                updated_lines[-1] = f'{last_memory + 1}-{line.split("-", 1)[1]}'
                last_memory = line_number

    return updated_lines


def update_rocket_dock_config(config_path):
    lines_to_keep = parse_rocket_dock_config(config_path)
    print(lines_to_keep)
    updated_lines = check_and_remove_nonexistent_icons(lines_to_keep)
    print(updated_lines)
    # with open(config_path, "w") as file:
    #     file.writelines(updated_lines)

update_rocket_dock_config(settings)
