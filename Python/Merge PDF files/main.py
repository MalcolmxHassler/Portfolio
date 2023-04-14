import glob 
from PyPDF2 import PdfFileMerger

def main_code():
    files = glob.glob('input/*.pdf')
    merger=PdfFileMerger()

    for pdf_file in files:
        merger.append(pdf_file)

    ##write the output of the merged PDF file
    merger.write("CertificationsV3.pdf")
    merger.close()


    print('The Merge PDF file is available now...\n')
    print('By Malcolmx Gninghaye')
    print('LinkedIn: https://www.linkedin.com/in/malcolmx-hassler-gninghaye-guemandeu')

if __name__ == "__main__":
    main_code()
