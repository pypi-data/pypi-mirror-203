from scrapse.judgment.general_utils import *

##### special chars P . Q . M . 
CHECK_DUPLICATES = "[(][0-9][)]"
CF_CHECK = "([A-Z]{6})([0-9]{2})([A-Z]{1})([0-9]{2})([A-Z]{1})([0-9]{3})([A-Z]{1})"
TITLE = "(?:[A-Z][a-z]*\.\s*)?"
NAME1 = "[A-Z][a-z]+,?\s+"
MIDDLE_I = "(?:[A-Z][a-z]*\.?\s*)?"
NAME2 = "[A-Z][a-z]+"
NOMETITOLO = NAME1 + MIDDLE_I + NAME2


def create_nITA(file_path):
    """create a list of all italian names, gets in input a txt list"""
    file = open(file_path, 'r', encoding="utf8")
    file_content = file.readlines()
    list_names = []
    for line in file_content:
        line = line.replace('\n', '')
        list_names.append(line.lower())
    file.close()
    return list_names


def ps_CF(text):
    """Find and replace all CF in the document"""
    return re.sub(CF_CHECK, "entity_cf", text)


def ps_names(line, tag, list_names):
    """analyzes the pos tagging of a single line"""

    doc = nlp(line)
    newline = str(line)
    newline = re.sub(NOMETITOLO, "entity_person", newline)
    for token in doc:
        word = token.text
        pos = token.pos_
        if pos == tag:
            if str(word) in list_names:
                newline = newline.replace(word, "entity_person")
    return newline


def pseudo_anonimization(json_object, list_names):
    """ Apply a simple form of anonimization on text"""

    list_indexJ = ["conclusioni", "fatto", "decisione", "fatto_decisione", "pqm"]

    for field in json_object:
        if field in list_indexJ:
            if not json_object[field] is None:
                line = ps_CF(json_object[field])
                line = ps_names(line, "PROPN", list_names)
                line = str(line)
                json_object[field] = line
