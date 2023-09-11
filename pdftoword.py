# from pdf2docx import Converter

# pdf_file = 'STA 312 EXPERIMENTAL DESIGNS I.pdf'
# docx_file = 'FailList_KCABAC_MAY19_MAIN.docx'
# # convert pdf to docx
# cv = Converter(pdf_file)
# cv.convert(docx_file, start=0, end=None)
# cv.close()

#  cv.convert(path_output+file+'.docx', start=0, end=None)
# cv.close()
# print(file)

# /home/kim/Documents/pdftoword/input
# #/home/kim/Documents/pdftoword/output/
from pdf2docx import Converter
import os

# # # dir_path for input reading and output files & a for loop # # #

path_input = 'path to your input'
path_output = 'path to your output'
files = os.listdir(path_input)

for file in files[0:]:
    full_pdf_path = os.path.join(path_input, file)
    cv = Converter(full_pdf_path)
    name = file.split(".")
    cv.convert(path_output+name[0]+'.docx', start=0, end=None)
    cv.close()
