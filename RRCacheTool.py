import os
import sys
import platform

version = 0.1


def is_ascii(s):
    return all(ord(c) < 128 for c in s)


def parse_library(library):
    # Categorize links
    category = {
        "png": [],
        "jpg": [],
        "room": [],
        "htr": [],
        "meta": [],
        "other": [],
        "not image": []
    }

    # Parse
    for word in library.split("\\"):
        if is_ascii(word) and len(word) > 10:  # If it's ascii and not just random characters
            if "https://" in word:  # if it's a link
                purified = "https://" + word.replace("\\", "").replace("|", "").split("https://")[1]  # purify link
                # remove possible params
                if "?" in purified:
                    purified = purified.split("?")[0]

                # remove possible garbage after file extensions
                for extension in [".htr", ".meta", ".room"]:
                    if extension in purified:
                        purified = purified.split(extension)[0] + extension

                # categorize
                link_dict = {"link": purified, "hex": None, "date": None, "category": None}

                if any(ext in purified for ext in category):  # if extension has a category
                    extension = purified.split(".")[-1]
                    link_dict = {"link": purified, "hex": None, "date": None, "category": extension}
                else:  # it's uncategorized
                    if "img.rec.net" in purified:  # Check if it's an image
                        link_dict = {"link": purified, "hex": None, "date": None, "category": "other"}
                    else:  # URL isn't an image
                        link_dict = {"link": purified, "hex": None, "date": None, "category": "not image"}

            else:
                if not link_dict:
                    continue

                # Purify link
                purified = word.replace("\\", "")[3:]

                # Insert correct data
                if "GMT" in purified:
                    link_dict['date'] = purified
                else:
                    link_dict['hex'] = purified

                # Append to category
                if link_dict['hex'] and link_dict['date']:
                    category[link_dict['category']].append(link_dict)

    # Category == Parsed
    return category


def option_menu(location_info=""):
    print(f"Rec Room Cache Library Tool v{version} by @Jegarde")
    print("Dir:", location_info)
    print("1. Parse and Export")
    print("2. Delete Library")
    print("3. Exit")

    while True:
        option = input("Option > ")

        try:
            option = int(option)
        except ValueError:
            option = ""
            continue

        if option in (1, 2, 3):
            break

    return option


def find_library():
    if os.path.isfile("./Library"):
        location = "./Library"
    elif "userprofile" in os.environ:
        location = os.environ["userprofile"] + "\AppData\LocalLow\Against Gravity\Rec Room\Library"
        if not os.path.isfile(location):
            return ""
    else:
        return ""

    return location


def main():
    # Clear
    pf = platform.system()
    if pf == "Windows":
        os.system("cls")
    else:
        os.system("clear")

    # Load library file
    location = find_library()

    max_attempts = 3
    attempts = 0
    while not location:
        attempts += 1
        input(
            f"Couldn't find 'Library' file. Please try duplicating it in this script's directory and press enter. "
            f"Attempts: {attempts}/{max_attempts}")

        location = find_library()

        if location:
            break

        if attempts >= max_attempts:
            sys.exit("Try again when the library file is available!")

    if location == "./Library":
        location_info = sys.path[0] + "\\Library"
    else:
        location_info = location

    # Get option
    option = option_menu(location_info)

    if option == 1:  # Parse and export library
        # Load library
        with open(location, "rb") as lib:
            library = str(lib.read())

        parsed = parse_library(library)

        # Export it
        export = "Parsed Rec Room Cache Library\nhttps://github.com/Jegarde/RecRoom-Cache-Library-Tool\n[URL / Cache Date]\n"
        for key in parsed:
            export += f"\nEXTENSION - {key} (Amount: {len(parsed[key])})\n\n"
            for item in parsed[key]:
                export += f"{item['link']} ({item['date']})\n"

        file_name = "Output.txt"
        with open(file_name, "w") as output:
            output.write(export)

        # Open export
        os.startfile(file_name)

        main()
    elif option == 2:
        if os.path.exists(location):
            os.remove(location)
        else:
            print("The library does not exist!")

        main()
    else:
        sys.exit("Exiting!")


if __name__ == "__main__":
    main()
