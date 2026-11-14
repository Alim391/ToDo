This is my simple console task manager written in Python.

I made it for myself to practice working with classes and files, and also so I could quickly jot down a to-do list right from the terminal. Tasks are saved directly to a text file, so they won't go anywhere after closing the program.

## Features:

**Adding tasks** — you can throw in tasks in batches, and when finished, simply type `stop` to return to the menu.
**Viewing** — displays all current tasks with proper numbering and capitalized letters.
**Keyword deletion** — you type in a word, and the program automatically finds and clears out the matching line (case-insensitive).
**Foolproofing** — if you type a letter instead of a number in the menu, the program won't crash with an error, it will just ask you to re-enter.

## How to run:

No third-party libraries need to be installed — everything works on pure Python (I ran it on 3.11).

1. Download the code file.
2. Open the terminal in this folder.
3. Run it with the command:

```bash
python main.py

```

*(The `todo.txt` file will be created automatically next to the script when you add your first task).*