#!/usr/bin/env python3

import json
import genanki
from markdown2 import Markdown

mk = Markdown()

css = None
card_back = None
card1 = None
card2 = None
card3 = None
card4 = None
elements = None

with open('src/templates/stylesheet.css') as CSS, \
    open('src/templates/card_back.html') as CARD_BACK, \
    open('src/templates/card1_front.html') as CARD1, \
    open('src/templates/card2_front.html') as CARD2, \
    open('src/templates/card3_front.html') as CARD3, \
    open('src/templates/card4_front.html') as CARD4, \
    open('src/data.json') as DATA:

        css = CSS.read()
        card_back = CARD_BACK.read()
        card1 = CARD1.read()
        card2 = CARD2.read()
        card3 = CARD3.read()
        card4 = CARD4.read()
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
        templates=[
            {
                'name': 'Card 1',
                'qfmt': card1,
                'afmt': card_back,
            },
            {
                'name': 'Card 2',
                'qfmt': card2,
                'afmt': card_back,
            },
            {
                'name': 'Card 3',
                'qfmt': card3,
                'afmt': card_back,
            },
            {
                'name': 'Card 4',
                'qfmt': card4,
                'afmt': card_back,
            }
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

    phrase_html = mk.convert(phrase)

    medias.append('src/{}'.format(media))
    media_html = '<IMG SRC="{}">'.format(media.split('/')[-1])

    note = genanki.Note(
            model=model,
            fields=[media_html, name, number, symbol, phrase_html, ''],
            sort_field=2)
    note.guid = guid

    deck.add_note(note)

package = genanki.Package(deck)
package.media_files = medias
package.write_to_file('output.apkg')
