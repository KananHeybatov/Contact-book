# Contact book

A command-line contact manager that stores names, phone numbers and email addresses and saves them permanently to a JSON file.

## Features

- Add contacts with name, phone number and email address
- View all saved contacts
- Search for contacts by name
- Delete contacts by name
- Saves contacts to a JSON file, so data is never lost
- Handles case-sensitive duplicate names using `.strip().title()`

## How to Run

1. Ensure Python 3 is installed
2. Clone this repository:

```bash
git clone https://github.com/KananHeybatov/Contact-book.git
```

3. Navigate to the directory and run the file:

```bash
python contact_book.py
```

## How Does It Work?

Contacts are stored as a nested dictionary, where each contact name is a key and the value is another dictionary containing the phone number and email address. The programme initially loads existing contacts from a JSON file and automatically saves them after every change.

## What I Learned

- Working with nested dictionaries
- Saving and loading data using JSON
- Using `.strip().title()` to normalise user input
- Searching for and deleting dictionary entries by key
- Handling missing files with `try/except FileNotFoundError`

## Potential Improvements

- Adding a feature to edit existing contacts
- Searching by phone number or email
- Exporting contacts to a CSV file

## Author

Kanan Heybatov — 2026
