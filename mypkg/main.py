#from pdfparser import PDFParser
#from docxparser import DocxParser
#from docoleparser import DocOleParser
#from docconverterparser import DocConverterParser
from htmlparser import HTMLParser
#from pdfminerparser import PDFMinerParser
#from docxxmlparser import DocxXMLParser
import csv
import requests
from datetime import datetime
import  time


# def pdfminer():
#     pdf_parser = PDFMinerParser()
#     pdf_parser.parse(r'files/Test3.pdf')
#     print('pdfminer parser', pdf_parser.get_processed_stems(), len(pdf_parser.get_processed_stems()))
#
#
# def pdf():
#     pdf_parser = PDFParser()
#     pdf_parser.parse(r'files/Test3.pdf')
#     print('pdf parser', pdf_parser.get_processed_stems(), len(pdf_parser.get_processed_stems()))
#
#
# def docx():
#     docx_parser = DocxParser()
#     docx_parser.parse(r'files/Test2.docx')
#     print('docx parser', docx_parser.get_processed_stems(), len(docx_parser.get_processed_stems()))
#
#
# def docx_xml():
#     docx_xml_parser = DocxXMLParser()
#     docx_xml_parser.parse(r'files/Test2.docx')
#     print('docx_xml parser', docx_xml_parser.get_processed_stems(), len(docx_xml_parser.get_processed_stems()))
#
#
# def doc_ole():
#     doc_ole_parser = DocOleParser()
#     doc_ole_parser.parse(r'files/Test2.doc')
#     print('doc_ole parser', doc_ole_parser.get_processed_stems(), len(doc_ole_parser.get_processed_stems()))
#
#
# def doc_converter():
#     doc_parser = DocConverterParser()
#     doc_parser.parse(r'files/Test2.doc')
#     print('doc_converter parser', doc_parser.get_processed_stems(), len(doc_parser.get_processed_stems()))


def html(link):
    html_parser = HTMLParser()
    html_parser.parse(link)
    word_list = html_parser.get_processed_stems()
    return  word_list

def get_links(file_all_links):
    with open(file_all_links, "r") as file:
        reader = csv.reader(file)
        link_list = list(reader)
    return link_list

def get_map_list(file_map_words):
    with open(file_map_words, "w") as file:
        for link in all_links:
            try:
                word_list = html(",".join(link).replace(",", ""))
                writer = csv.writer(file)
                for word in word_list:
                    writer.writerow([word, ",".join(link).replace(",", "")])
            except requests.exceptions.RequestException:
                pass

def sort_list(file_read, file_write):
    with open(file_read, "r") as file_read:
        reader = csv.reader(file_read)
        unsorted_list = list(reader)
    sorted_list = sorted(unsorted_list, key = lambda x: (x[0], x[1]))
    with open(file_write, "w") as file:
        writer = csv.writer(file)
        for row in sorted_list:
            writer.writerow(row)

def build_index(file_read, file_write):
    list = []
    with open(file_read, "r") as file_read:
        reader = csv.reader(file_read)
        with open(file_write, "w") as file:
            writer = csv.writer(file)
            row_1 = next(reader)
            list = row_1
            j = 0
            a=list[0]
            b=list[1]
            for row in reader:
                if (a == row[0]):
                    list.append(row[1])
                else:
                    writer.writerow(list)
                    list = []
                    list = row
                a = row[0]
                b = row[1]


def find_word(word, filename):
    f = 0
    with open(filename, "r") as file_read:
        reader = csv.reader(file_read)
        for row in reader:
            if (row[0] == word):
                print(row)
                print(len(row) - 1)
                f = 1
                break
    if (f == 0):
        print('Nothing was found')


if __name__ == '__main__':

    start_time = datetime.now()

    # file_all_links = '/home/elavelina/PycharmProjects/parsers-master/mypkg/files/all_links_msu.csv'
    # all_links = get_links(file_all_links)
    #
    # file_map_words = '/home/elavelina/PycharmProjects/parsers-master/mypkg/files/map_words_msu.csv'
    # get_map_list(file_map_words)

    # сортировка для тестирования на маленьких файлах
    # file_read = '/home/elavelina/PycharmProjects/parsers-master/mypkg/files/map_words_msu.csv'
    # file_write = '/home/elavelina/PycharmProjects/parsers-master/mypkg/files/sorted_map_words_msu.csv'
    # sort_list(file_read, file_write)

    # file_read = '/home/elavelina/PycharmProjects/parsers-master/mypkg/files/msu/sorted_map_words_msu.csv'
    # file_write = '/home/elavelina/PycharmProjects/parsers-master/mypkg/files/msu/index_msu.csv'
    # build_index(file_read, file_write)

    used_index = '/home/elavelina/PycharmProjects/parsers-master/mypkg/files/spbu/index_spbu.csv'
    # find_word('kropachev', used_index)
    find_word('лавелина', used_index)
    # find_word('садовничий', used_index)
    # find_word('sadovnichy', used_index)

    # filename = '/home/elavelina/PycharmProjects/parsers-master/mypkg/files/test/index_test.csv'
    # with open(filename, "r") as file_read:
    #     reader = csv.reader(file_read)
    #     for row in reader:
    #         print(row)

    print(datetime.now() - start_time)
