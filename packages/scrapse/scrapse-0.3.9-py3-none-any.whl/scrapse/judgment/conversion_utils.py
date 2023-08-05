from scrapse.judgment.general_utils import *
import win32com.client

DOCX_FORMAT = 16


def get_all_file_from_directory(directory_file_path, convert_file):
    """Function used to retrieve the file list for each file .docx in the file path passed by argument"""

    allFiles = [[directory_file_path + "/", f] for f in listdir(directory_file_path) if
                isfile(join(directory_file_path, f)) and '~' not in f]
    allDocxFiles = [[file[0], file[1]] for file in allFiles if ".docx" in file[1]]

    if convert_file:
        allOtherFiles = [[file[0], file[1]] for file in allFiles if not (".docx" in file[1]) and (
                    (".docm" in file[1]) or (".doc" in file[1]) or (".pdf" in file[1]))]
        convert_pdf_doc_to_docx(allOtherFiles, directory_file_path)
        allDocxFiles += allOtherFiles

    return allDocxFiles




def convert_pdf_doc_to_docx(allOtherFiles, directory_input_path):
    """ Function used to convert all .doc, .docm and .pdf files in .docx format """

    print("Start conversion...")
    directory_output_path = directory_input_path + "/converted_files"
    print("------------------------ Output in: " + directory_output_path + "------------------------\n")

    # checking if the directory_output_path exists
    if not os.path.exists(directory_output_path):
        os.makedirs(directory_output_path)

    directory_output_path += "/"
    # run MICROSOFT WORD application
    word = win32com.client.Dispatch("Word.Application")
    if word is None:
        print("Conversion cannot be applied beacuse Word.application not exists")
        return

    for file in allOtherFiles:

        format_replace = ''
        if '.docm' in file[1]:
            format_replace = '.docm'
        elif '.doc' in file[1]:
            format_replace = '.doc'
        else:
            format_replace = '.pdf'

        source_file = (file[0] + file[1]).strip()
        novus_file = file[1].replace(format_replace, '.docx').strip()
        output_file = directory_output_path + novus_file

        windows_path = source_file.replace("/", "\\")
        doc = None
        try:
            doc = word.Documents.Open(windows_path)
        except Exception as error:
            print(error)
            if doc is not None:
                doc.Close()
            continue

        if doc is not None:
            doc.SaveAs(output_file, DOCX_FORMAT)
            doc.Close()
            file[0] = directory_output_path
            file[1] = novus_file

    word.Quit()
    print("End conversion...")
