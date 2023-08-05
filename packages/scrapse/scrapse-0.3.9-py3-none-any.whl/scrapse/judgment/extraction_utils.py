from scrapse.judgment.general_utils import *

def find_sentenza_number(docx_path):
    """ Find sentenza number and year"""

    text = docx2txt.process(docx_path)
    text = text.split("\n")
    text = [el.strip().lower().replace(' ', '') for el in text if el != ''][:4]
    for el in text:
        if 'n.' in el and not 'cron' in el and not "rgl" in el and not 'r.g.l' in el and not 'fasc' in el:
            el2 = el.split('n.')[1]
            if el2 and el2[0].isdigit() and '/' in el2[:5]:
                el2_split = el2.split("/")
                if el2_split[0].isdigit():
                    numero_sent = el2_split[0]
                    if el2_split[1][:4].isdigit():
                        anno_sent = el2_split[1][:4]
                        return numero_sent, anno_sent
                    elif el2_split[1][:2].isdigit():
                        anno_sent = el2_split[1][:2]
                        return numero_sent, anno_sent

    return 0, 0


def check_nrg(sentenza_meta, text, file):
    """ find and retrieve NRG code, if exists """

    if "r.g." in text.strip():
        splitted = text.split("r.g.l")[0]
        if "n.ro" in splitted:
            splitted2 = splitted.split("n.ro")[1].strip()
            if "/" in splitted2:
                splitted3 = splitted2.split("/")
                sentenza_meta["nrg_code"] = splitted3[0].strip()
                sentenza_meta["nrg_anno"] = splitted3[1].split()[0].strip()

        elif "n.ri" in splitted:
            splitted2 = splitted.split("n.ri")[1].strip()
            if "/" in splitted2:
                splitted3 = splitted2.split("/")
                last = splitted3[0].split()[len(splitted3[0].split()) - 1]
                sentenza_meta["nrg_code"] = last.strip()
                sentenza_meta["nrg_anno"] = splitted3[1].split()[0].strip()

        elif "n." in splitted:
            splitted2 = splitted.split("n.")[1].strip()
            if "/" in splitted2:
                splitted3 = splitted2.split("/")
                sentenza_meta["nrg_code"] = splitted3[0].strip()
                sentenza_meta["nrg_anno"] = splitted3[1].split()[0].strip()
        return True
    elif "rgl" in text.strip():
        splitted = text.split("rgl")[1]
        if "/" in splitted:
            splitted2 = splitted.split("/")
            sentenza_meta["nrg_code"] = splitted2[0].strip()
            sentenza_meta["nrg_anno"] = splitted2[1].split()[0]
        return True
    elif "rg" in text.strip():
        splitted = text.split("rg")[1]
        if "/" in splitted:
            splitted2 = splitted.split("/")
            sentenza_meta["nrg_code"] = splitted2[0].strip()
            sentenza_meta["nrg_anno"] = splitted2[1].split()[0]
        return True
    return False