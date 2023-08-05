import typer
from scrapse.judgment.general_utils import *
from scrapse.judgment.extraction_utils import *
from scrapse.judgment.conversion_utils import *
from scrapse.judgment.anonimization_utils import *

# '/'.join([main_directory_path, 'judgments_dump']

def extraction(

        directory_file_path: str = typer.Option(
            None, '--path', '-p',
            help='Path to the directory containing all .docx judgments to extract',
            show_default=False),

        convert_file: bool = typer.Option(
            False, '--convert', '-c',
            show_default=True,
            help='Convert all .doc, .pdf and .docm files in .docx'),

        pseudo_anonim: bool = typer.Option(
            False, '--anonim', '-a',
            show_default=True,
            help='Perform a pseudo-anonymization on the extracted judgments'),
):
    """
        Read all .docx file in the directory at the 'path' variable.
        Write 2 jsons objects with all the information extracted.
        This function save the extracted jsons in directory_file_path,
        in a new folder called "output".

        - params: directory_file_path: str
        - params: pseudo_anonimization: bool
    """

    print("Init extraction...")
    print("directories_file_path:", directory_file_path)
    print("pseudo-anonimization:", pseudo_anonim)

    if pseudo_anonim: list_names = create_nITA(pseudo_anonim)

    sentenze_content_list = []
    sentenze_meta_list = []
    allDocxFiles = get_all_file_from_directory(directory_file_path, convert_file)

    for file in allDocxFiles:
        doc = docx.Document(file[0] + file[1])

        sentenza_content = {
            "nomefile": None,
            "oggetto": None,
            "conclusioni": None,
            "fatto": None,
            "decisione": None,
            "fatto_decisione": None,
            "pqm": None
        }

        sentenza_meta = {
            "nomefile": None,
            "origine": "sentenze_ciccarelli",
            "tribunale": "torino",
            "sezione": None,
            "voci": None,
            "sent_code": None,
            "sent_anno": None,
            "nrg_code": None,
            "nrg_anno": None,
            "tipo": None
        }

        sentenza_content['nomefile'] = file[1]
        sentenza_meta['nomefile'] = file[1]

        numero_sent, anno_sent = find_sentenza_number(file[0] + file[1])
        if numero_sent != 0 and anno_sent != 0:
            sentenza_meta["sent_code"] = numero_sent
            sentenza_meta["sent_anno"] = anno_sent

        lines = doc.paragraphs
        sezione_found = False
        oggetto_found = False
        nrg_found = False
        fatto_found = False
        conclusione_found = False
        decisione_found = False
        PQM_found = False
        end_found = False

        fatto_text = []
        conclusioni_text = []
        decisione_text = []
        PQM_text = []

        i = 0
        while (i < len(lines)):
            text = lines[i].text.lower().replace(' ', ' ').strip()
            text_final = lines[i].text.replace(' ', ' ').strip()

            # check is sezione found?
            if not sezione_found and not nrg_found:
                if "sezione" in text:
                    splitted = text.split("sezione")[1].strip()
                    splittd1 = splitted.split()[0]
                    sentenza_meta['sezione'] = "sez. " + splittd1
                    sezione_found = True

            # check is nrg found?
            if not nrg_found and not oggetto_found:
                if (check_nrg(sentenza_meta, text, file[0])):
                    if not sentenza_meta['nrg_code'] is None and not sentenza_meta['nrg_code'].isdigit():
                        print("Problema in " + sentenza_meta['nomefile'])
                    nrg_found = True

            # check is oggetto found?
            if not oggetto_found:
                for el in splitWords_oggetto:
                    if el in text.strip():
                        obj_splitted = text.split(el)[1].strip()
                        obj_splitted = obj_splitted.replace(":", ",")
                        sentenza_content['oggetto'] = obj_splitted
                        oggetto_found = True

            # check is conclusione found?
            if not conclusione_found:
                for el in splitWords_conclusioni:
                    if el in text.replace(" ", "").strip():
                        i += 1
                        text = lines[i].text.lower().strip()
                        text_final = lines[i].text.replace(' ', ' ').strip()
                        conclusione_found = True

            # check is fatto di causa found?
            if not fatto_found:
                for el in splitWords_fatto:
                    if el in text.replace(" ", "").strip():
                        i += 1
                        text = lines[i].text.lower().strip()
                        text_final = lines[i].text.replace(' ', ' ').strip()
                        sentenza_content['conclusioni'] = " ".join(conclusioni_text)
                        fatto_found = True

            if conclusione_found and not fatto_found:
                conclusioni_text.append(text_final)

            # check is ragioni della decisione found?
            if not decisione_found:
                for el in splitWords_decisione:
                    if el in text.replace(" ", "").strip():
                        i += 1
                        text = lines[i].text.lower().strip()
                        text_final = lines[i].text.replace(' ', ' ').strip()
                        decisione_found = True
                        sentenza_content['fatto'] = " ".join(fatto_text)

            if fatto_found and not decisione_found and not PQM_found:
                fatto_text.append(text_final)

            # check is PQM found?
            if not PQM_found:
                for el in splitWords_PQM:
                    if el in text.replace(" ", "").strip():
                        i += 1
                        text = lines[i].text.lower().strip()
                        text_final = lines[i].text.replace(' ', ' ').strip()
                        PQM_found = True
                        sentenza_content['decisione'] = " ".join(decisione_text)
                        if sentenza_content['decisione'] == "":
                            sentenza_content['decisione'] = None

            if decisione_found and not PQM_found:
                decisione_text.append(text_final)

            # check is end of file found?
            if not end_found:
                for el in splitWords_end:
                    if el in text.replace(" ", "").strip() and PQM_found:
                        i += 1
                        try:
                            text = lines[i].text.lower().strip()
                            text_final = lines[i].text.replace(' ', ' ').strip()
                            sentenza_content['pqm'] = " ".join(PQM_text)
                            end_found = True
                        except IndexError:
                            sentenza_content['pqm'] = " ".join(PQM_text)
                            end_found = True

            # print(sentenza["RG"] + " non ha le RAGIONI DELLA DECISIONE ")
            if PQM_found and not decisione_found:
                sentenza_content['fatto'] = " ".join(fatto_text)

            if PQM_found and not end_found:
                PQM_text.append(text_final)

            i += 1

        if (sentenza_content["decisione"] is None):
            sentenza_content["fatto_decisione"] = sentenza_content['fatto']
            sentenza_content['fatto'] = None
            if sentenza_content["fatto_decisione"] == "":
                sentenza_content["fatto_decisione"] = None

        if sentenza_content['oggetto'] is None and sentenza_content['fatto'] is None and sentenza_content[
            'fatto_decisione'] is None and sentenza_content['decisione'] is None:
            sentenza_meta['tipo'] = "ordinanza"
        else:
            sentenza_meta['tipo'] = "sentenza di merito"

        if pseudo_anonim: pseudo_anonimization(sentenza_content, list_names)

        sentenze_content_list.append(sentenza_content)
        sentenze_meta_list.append(sentenza_meta)

        # Print outputs
    output = directory_file_path + "/output"
    if not os.path.exists(output):
        os.makedirs(output)

    json_content_path = output + "/output_content.json"
    json_meta_path = output + "/output_metadata.json"

    with open(json_content_path, "w", encoding='utf8') as write_file:
        json.dump(sentenze_content_list, write_file, indent=4, ensure_ascii=False)

    with open(json_meta_path, "w", encoding='utf8') as write_file:
        json.dump(sentenze_meta_list, write_file, indent=4, ensure_ascii=False)

    print("All documents in " + directory_file_path + " has been extracted!")
    print("json content created at " + json_content_path)
    print("json metadata created at " + json_meta_path)
    print("End extraction...")