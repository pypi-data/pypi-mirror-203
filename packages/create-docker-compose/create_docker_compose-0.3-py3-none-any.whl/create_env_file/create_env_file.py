import os
import json

def main():
    create_env_file()

def create_env_file():
    consolidated_vars = {}
    update_consolidated_vars(consolidated_vars)
    write_consolidated_vars(consolidated_vars)

def update_consolidated_vars(consolidated_vars):
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in filenames:
            if filename == "env_config.json":
                with open(os.path.join(dirpath, filename), "r") as f:
                    config = json.load(f)
                    for key, value in config.items():
                        if isinstance(value, list):
                            value = " ".join(value)
                        update_consolidated_var(consolidated_vars, key, value)

def update_consolidated_var(consolidated_vars, key, value):
    if key in consolidated_vars:
        existing_values = set(consolidated_vars[key].split())
        new_values = set(value.split())
        merged_values = existing_values | new_values
        consolidated_vars[key] = " ".join(merged_values)
    else:
        consolidated_vars[key] = value

def write_consolidated_vars(consolidated_vars):
    with open(os.path.join(".", ".env"), "w") as f:
        for key, value in consolidated_vars.items():
            f.write(f"{key}={value}\n")

if __name__ == '__main__':
    main()