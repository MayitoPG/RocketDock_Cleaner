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
    listing = []
    new_lines = []
    sec_list = []
    un_sectioned = []
    for line in lines:
        listing.append(line)
    command_key = None
    for line in listing:
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
            if n_command_path.exists():
                new_lines.append(line)
            else:
                sec_list.append(command_key.split("-")[0])
                new_lines.append(line)
        else:
            new_lines.append(line)
    for item in new_lines:
        number = item.split("-")[0]
        if item.startswith(number) and number not in sec_list:
            un_sectioned.append(item)
    line_number = 0
    count = 0
    enumerated_lines = []
    for line in un_sectioned:
        if line.split("-")[0].strip().isdigit():
            rest_of_line = line.split("-", maxsplit=1)[1]
            mod_line = f"{line_number}-{rest_of_line}"
            if line.split("=")[0].strip().endswith("DockletFile"):
                line_number += 1
            enumerated_lines.append(mod_line)
        elif line.startswith("count") and count == 0:
            mod_line = f"count = {line_number}\n"
            count += 1
            enumerated_lines.append(mod_line)
        else:
            enumerated_lines.append(line)
    return enumerated_lines


def update_rocket_dock_config(config_path):
    lines_to_keep = parse_rocket_dock_config(config_path)
    print(lines_to_keep)
    updated_lines = check_and_remove_nonexistent_icons(lines_to_keep)
    print(updated_lines)
    mod_settings = Path() / "mod_Settings.ini"
    with open(mod_settings, "w") as file:
        file.writelines(updated_lines)


update_rocket_dock_config(settings)
