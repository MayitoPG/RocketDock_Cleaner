from pathlib import Path

settings = Path() / "Settings.ini"
result = Path() / "result.ini"


def check_and_remove_nonexistent_icons(setting):
    # lists I need
    listing = []
    new_lines = []
    sec_list = []
    un_sectioned = []

    # read file
    with open(setting, "r") as file:
        for line in file:
            listing.append(line)

    # check keys and values
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

    # remove useless sections
    for item in new_lines:
        number = item.split("-")[0]
        if item.startswith(number) and number not in sec_list:
            un_sectioned.append(item)
    return un_sectioned


def enumerator(new_lines):
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
    final_list = check_and_remove_nonexistent_icons(config_path)
    setting_updated = enumerator(final_list)
    with open(result, "w") as file:
        file.writelines(setting_updated)


update_rocket_dock_config(settings)
