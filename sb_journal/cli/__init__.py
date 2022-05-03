from .intro import show_intro
from .prompt import show_prompt
from .actions import ACTIONS


def mainloop():
    show_intro()

    action_choices = {
        name[0].lower(): function
        for function, name, _ in ACTIONS
    }

    while True:
        print()

        show_prompt(ACTIONS)

        choice = input("Choice: ")
        choice = choice.strip()

        if not choice:
            continue

        choice = choice[0].lower()
        if choice not in action_choices:
            continue

        action_choices[choice]()
