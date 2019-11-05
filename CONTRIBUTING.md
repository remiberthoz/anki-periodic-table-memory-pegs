# Contributing

### Release process

1. **[Build process]** Checkout the `master` branch.
2. Merge new features from `develop`.
3. Bump the version number in `version.txt`.
4. Commit, and create a tag named as the version number prefixed with `v`.
5. Run the `main.py` python script to create the new `.apkg`.
6. **[AnkiWeb release]** Create a fresh Anki user on your local install.
7. Login into Anki with the project's owner credentials.
8. Import the `.apkg` created in step 4.
9. Synchronise Anki with AnkiWeb.
10. Go to [AnkiWeb](https://ankiweb.net/decks/) (login if required).
11. Find the *Periodic table memory pegs* deck and select *Actions > Share*.
12. Click *Share*.
13. **[GitHub release]** Push the `master` branch and the new tag.
14. Go to the [Releases](https://github.com/remiberthoz/anki-periodic-table-memory-pegs/releases) page.
15. Edit the release title and note.
16. **[Post release]** Merge `master` into `develop` (no fast-forward).
