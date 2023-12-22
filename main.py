from pathlib import Path

settings = Path() / "Settings.ini"
result = Path() / "result.ini"


def parse_rocket_dock_config(config_path):
    lines_to_keep = []
    with open(config_path, "r") as file:
        for line in file:
            lines_to_keep.append(line)
    print(lines_to_keep)
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
            value = ""

        if key.lower().endswith("command"):
            command_key = key
            n_command_line = value.split("=")[0].strip()
            n_command_path = Path(n_command_line)
            print(n_command_path)
            if n_command_path.exists():
                new_lines.append(line)
            else:
                new_lines = [
                    index
                    for index in new_lines
                    if not index.startswith(command_key.split("-")[0] + "-")
                ]
        else:
            new_lines.append(line)
    return new_lines



def renumerator(new_lines):
    reminder = 0
    final_lines = []
    for line in new_lines:
        if not line.split("-")[0].isdigit():
            final_lines.append(line)
        elif line.split("-")[0].isdigit():
            line_number = int(line.split("-")[0])
            reminder = line_number
            if line_number > reminder + 1:
                mod_line = f"{reminder + 1}-{line.split('-', 1)[1]}"
                final_lines.append(mod_line)
            else:
                final_lines.append(line)
    return final_lines


def update_rocket_dock_config(config_path):
    list_of_lines = parse_rocket_dock_config(config_path)
    final_list = renumerator(list_of_lines)
    left_lines = check_and_remove_nonexistent_icons(final_list)

    with open(result, "w") as file:
        file.writelines(left_lines)


update_rocket_dock_config(settings)
