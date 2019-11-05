# Contributing

Thanks for taking the time to contribute!

Whether you want to correct a spelling mistake, update a picture, rephrase a
sentence or create a memory peg for a new element, you are on the right page!
Below you will find guidelines to help you go through the process.

If you have an idea but do not feel like implementing it youself, you can
[open a new issue](https://github.com/remiberthoz/anki-periodic-table-memory-pegs/issues).

## Contributor's guide

- If you are new to git or GitHub, you can read
[this guide](https://opensource.guide/how-to-contribute/).
- If you want to edit or add data concerning an element,
you can jump to the **Data contributions** section below.
- If you want to redesign the deck (nightmode, text position on cards, etc.)
you can jump to the **Other contributions** section below.

### Data contributions

Data concerning the elements are stored in two files:

- Textual data is stored in `src/data.json` this includes atomic number, name,
memory sentence, and symbol.

    If you want to modify textual data about one of the elements (or add some),
    you can edit the `src/data.json` file with any text editor.
    You need to keep or reproduce the structure of the file.
    You will notice that each element has its own `guid`: the value it contains
    is important to Anki and you cannot modify it.
    If you are creating a new element, you need to choose a random guid
    value: it has to be 10 characters long.

- Each elements has its picture stored in `src/media/` as a `.gif` file.

    If you want to modify or create a new picture
    then the file you produce has to be a `.gif` of size 32x32 pixels,
    preferably with a transparent background.

When you are done, you can jump to the **Build and import** section below
to learn how to test your work.

### Other contributions

This git repository is structured as follow:
- `version.txt` holds the version number of the last release,
- `main.py` is a python script that creates the `.apkg` Anki deck,
- `packages/` contains the legacy deck,
and the package produced by the python script,
- `preview/` contains images used in the repository description on GitHub and
AnkiWeb,
- `src/media/` contains the element's pictures,
- `src/data.json` contains the element's textual data,
- `src/templates/` contains the HTML code
for the cards style and the CSS stylesheet,
- `src/desc.html` contains the HTML code for
the AnkiWeb description of the deck.

You are free to change anything,
when you are done, you can jump to the **Build and import** section below
to learn how to test your work.

### Build and import guide

Executing the `main.py` python script will create a file named with a variant
of `periodic-table-memory-pegs_****.apkg` in the directory named `packages/`.
This file is compatible with Anki, and you want to import it from here.
**Be carefull**, if you did something wrong you may break your Anki review
history. I would suggest that you create a new Anki user for testing purposes!

The python script relies on the following python modules:
`json`, 
`markdown2`,
`genanki` (the latter is found locally in the `genanki` directory) that you
can download with the git command: `git submodule init`.

The script was developped using python version 3.

If everything is in order, you can commit to the `develop` branch and push
your changes to your fork, then submit a pull request (see the
[GitHub guide](https://opensource.guide/how-to-contribute/) again).

## Maintainer's guide

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
