ACTIONS = (
    (lambda: print("import"), "import", "import teams from JSON"),
    (lambda: print("view"), "view", "view teams"),
    (lambda: print("add"), "add", "add new team"),
    (lambda: print("edit"), "edit", "edit a team"),
    (lambda: print("delete"), "delete", "delete a team"),
    (lambda: print("quit"), "quit", "quit this app")
)


def show_intro():
    print("Welcome to the Super Bowl Catalog!")
    print()

    print(
        "This command-line application provides information"
        " about Super Bowl teams and seasons when they played."
        "\n"
        "You can import/view/add/edit/delete data "
        "from the DB collection."
    )
    print()


def show_prompt():
    print(f"There are {None} teams in the DB.")
    print()

    print("Actions:")
    for _, name, description in ACTIONS:
        print(f"\t({name[0]}){name[1:]} \u2014 {description}")


def mainloop():
    show_intro()

    action_choices = {
        name[0].lower(): function
        for function, name, _ in ACTIONS
    }

    while True:
        print()

        show_prompt()

        choice = input("Choice: ")
        choice = choice.strip()

        if not choice:
            continue

        choice = choice[0].lower()
        if choice not in action_choices:
            continue

        action_choices[choice]()
