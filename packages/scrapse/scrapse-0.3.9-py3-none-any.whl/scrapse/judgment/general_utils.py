from pathlib import Path
import re
from os import listdir
from os.path import isfile, join,exists
import os
import json
import docx
import docx2txt
import spacy
nlp = spacy.load('it_core_news_md')

splitWords_ordinanza = ['ordinanza']
splitWords_oggetto = ['oggetto :', 'oggetto:'] # apply of "Metodo_racca"
splitWords_conclusioni = ["conclusioni"]
splitWords_fatto = ['fattidicausa','motiviinfattoeindirittodelladecisione', 'svolgimentodelprocesso', "fattoediritto", 'fattoedritto']
splitWords_decisione = ['motivodelladecisione','motividelladecisione', 'ragionidelladecisione', 'ragionidelladecisionefattoediritto']
splitWords_PQM = ['p.q.m', 'p.q.m.']
splitWords_end = ["ilpresidente", 'lapresidente', 'presidenteest', 'presidente']

main_directory_path = '/'.join([str(Path.home()), 'scrapse', 'judgment'])