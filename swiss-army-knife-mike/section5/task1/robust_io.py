CONFIG_PATH = "config.txt"

def main():
    try:
        with open(CONFIG_PATH, "r") as f:
            lines = f.readlines()

        print("Current contents:")
        print("".join(lines))

        updated_lines = []
        for line in lines:
            if line.strip().startswith("debug_mode="):
                updated_lines.append("debug_mode=True\n")
            else:
                updated_lines.append(line)

        with open(CONFIG_PATH, "w") as f:
            f.writelines(updated_lines)

        print("Updated debug_mode to True and saved.")

    except FileNotFoundError:
        print(f"[ERROR] Configuration file '{CONFIG_PATH}' was not found.")

    except PermissionError:
        print(f"[ERROR] Permission denied when accessing '{CONFIG_PATH}'.")

    except Exception as e:
        print(f"[ERROR] Unexpected error: {type(e).__name__}: {e}")

    finally:
        print("Operation Attempted.")

if __name__ == "__main__":
    main()
