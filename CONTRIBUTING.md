# Contributing

### Release process

1. Checkout the `master` branch.
1. Merge new features from `develop`.

    **[Build]**
1. Bump the version number in `version.txt`.
1. Commit, and create a tag named as the version number prefixed with `v` (for *version*).
1. Run the `main.py` python script to create the new `.apkg` package file.

    **[Release to AnkiWeb]**
1. Create a fresh Anki user on your local install.
1. Login into Anki with the project's owner credentials.
1. Import the `.apkg` created before.
1. Synchronise Anki with AnkiWeb.
1. Go to [AnkiWeb](https://ankiweb.net/decks/) (login if required).
1. Find the *Periodic table memory pegs* deck and select *Actions > Share*.
1. Optionally edit the *Description* with the content from `src/desc.html`.
1. Click *Share*.

    **[Release to GitHub]**
1. Push the `master` branch and the new tag.
1. Go to the [Releases](https://github.com/remiberthoz/anki-periodic-table-memory-pegs/releases) page.
1. Edit the release title and note.

    **[Terminate release]**
1. Merge `master` into `develop` (no fast-forward).
