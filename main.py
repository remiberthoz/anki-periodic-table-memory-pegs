#!/usr/bin/env python3

import json
import genanki
import subprocess
import sys
from markdown2 import Markdown

mk = Markdown()

css = None
card_back = None
card1 = None
card2 = None
card3 = None
card4 = None
card5 = None
elements = None
version = subprocess.check_output(["git", "describe", "--tags", "--always", "--dirty"]).decode(sys.stdout.encoding).strip().replace('v', '')

with open('src/templates/stylesheet.css') as CSS, \
    open('src/templates/card_back.html') as CARD_BACK, \
    open('src/templates/card_front.html') as CARD_FRONT, \
    open('src/data.json') as DATA:

        css = CSS.read()
        card_back = CARD_BACK.read()
        card_front = CARD_FRONT.read()
        elements = json.load(DATA)

deck = genanki.Deck(
        deck_id=490209917,
        name='Periodic table memory pegs')

model = genanki.Model(
        model_id=1484938894779,
        name='PeriodicTable-d75c0',
        fields=[
            {'name': 'Picture'},
            {'name': 'Name'},
            {'name': 'Number'},
            {'name': 'Symbol'},
            {'name': 'Memory sentence'},
            {'name': 'SpecialLocation'},
            ],
        sort_field_index=2,
        templates=[
            {'name': 'Card 1', 'qfmt': card_front, 'afmt': card_back},
            {'name': 'Card 2', 'qfmt': card_front, 'afmt': card_back},
            {'name': 'Card 3', 'qfmt': card_front, 'afmt': card_back},
            {'name': 'Card 4', 'qfmt': card_front, 'afmt': card_back},
            {'name': 'Card 5', 'qfmt': card_front, 'afmt': card_back},
        ],
        css=css)

medias = []
for elt in elements:
    number = elt['atomic_number']
    symbol = elt['symbol']
    phrase = elt['phrase']
    name = elt['name']
    media = elt['media']
    guid = elt['guid']
    period = elt['period']
    group = 'Actinoids' if elt['group'] == 'A' else 'Lanthanoids' if  elt['group'] == 'L' else elt['group']

    phrase_html = mk.convert(phrase)

    medias.append('src/{}'.format(media))
    media_src = media.split('/')[-1]
    media_insert = '<IMG SRC="{}">'.format(media_src)  # This line is not as nice as it could, the HTML tag
                                                       # would normally be placed in the HTML template.
                                                       # However Anki or genanki require a complete HTML image
                                                       # tag to *really* associate images with notes.
                                                       # See on GitHub:
                                                       # commit a247eb5
                                                       # and
                                                       # [issue #143](https://github.com/remiberthoz/anki-periodic-table-memory-pegs/issues/143)
                                                       # and
                                                       # [this comment from issue #140](https://github.com/remiberthoz/anki-periodic-table-memory-pegs/pull/140#issuecomment-2913382646).
    note = genanki.Note(
            model=model,
            fields=[media_insert, name, number, symbol, phrase_html, ''],
            tags=[f'period:{period}', f'group:{group}'])
    note.guid = guid

    deck.add_note(note)

package = genanki.Package(deck)
package.media_files = medias
package.write_to_file('packages/periodic-table-memory-pegs_{}.apkg'.format(version))
