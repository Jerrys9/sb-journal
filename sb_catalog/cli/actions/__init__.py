from .parse import parse
from .view import view
from .add import add
from .edit import edit
from .delete import delete

ACTIONS = (
    (parse, "parse", "import teams from JSON to the DB"),
    (view, "view", "view teams"),
    (add, "add", "add new team"),
    (edit, "edit", "edit a team"),
    (delete, "delete", "delete a team"),
    (lambda: print("quit"), "quit", "quit this app")
)
