def search_notes(notes, keyword):
    """Find notes containing a keyword."""
    if keyword is None:
        return []
    return [
        note for note in notes
        if keyword.lower() in note.lower()
    ]


if __name__ == "__main__":
    notes = ["Python Basics", "Git Commands", "Python Functions"]
    print(search_notes(notes, "Python"))
