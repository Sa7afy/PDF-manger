from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2 import PdfFileMerger


# Start the program
def start():
    print("Welcome to pdf manager")
    print('''
    by 
    Yousef Abdalla
    20210475
    Mohand Magdy
    20210412
    Mohamed Kamal
    20210350 ''')

    # choose what do you want
    print("choose 1, 2, 3 or 4:")
    print()
    print('1-Extract pages')
    print('2-Merge pdf files')
    print('3-split')
    print('4-Exit')
    global job
    job = int(input())


# Extracting pages from one file
def Extract():
    # take file name
    input_pdf = PdfFileReader(input('Enter file name with".pdf": '))
    # New file to write in it
    output = PdfFileWriter()
    # take pages
    
    choose = int(input("Please tell if you want a whole part of the pdf (1) or just specific pages (2): "))
    if choose == 1:
        limit1, limit2 = map(int, input("please enter the limits of the part (in one line): ").split())
        pages = []
        for i in range(limit1, (limit2)+1):
            pages.append(i)
    elif choose == 2:
        print("Enter pages (in one line): ")
        pages = list(map(int, input().split()))
    # add pages to file
    for page in pages:
        output.addPage(input_pdf.getPage(page - 1))
    # take name of the new file
    print("Enter the name of the result pdf with .pdf ")
    name = str(input())

    # save the file
    with open(name, "wb") as output_stream:
        output.write(output_stream)
    # End
    print("Done")


# merging two files which is adding two pdfs together and combine them in a single pdf
def merge():
    # create a list of pdf files
    pdf_list = []
    # take names
    number_of_pdfs = int(input("Enter the number of pdfs you want to merge: "))
    # add it into list
    for i in range(number_of_pdfs):
        pdf_list.append(str(input("Enter the name of the pdfs with '.pdf': ")))
    # call merge function
    merger = PdfFileMerger()
    # merge files
    for pdf in pdf_list:
        merger.append(pdf)
    # take name of the new  merged file
    print("Enter the name of the merged pdf with'.pdf': ")
    name = str(input())

    print("Merged file name is: ", name)
    # save new merged file
    merger.write(name)
    # End
    print("Done")

    merger.close()


# split one pdf file to into separate files
# you can split a pdf how many times depending on the user's need
def split():
    # take name of pdf file
    input_pdf = PdfFileReader(input('Enter file name with".pdf": '))
    # take number of files
    num = int(input("Enter the number of pdf files you want to split it into: "))

    for i in range(num):
        # create new file
        output = PdfFileWriter()
        # take name of the new file
        print("Enter the name of the splitted pdf with .pdf")
        name = str(input())
        # take pages
        choose = int(input("Please tell if you want a whole part of the pdf (1) or just specific pages (2): "))
        if choose == 1:
            limit1, limit2 = map(int, input("please enter the limits of the part (in one line): ").split())
            pages = []
            for i in range(limit1, (limit2)+1):
                pages.append(i)
        elif choose == 2:
            print("Enter pages (in one line): ")
            pages = list(map(int, input().split()))
        # add pages to new file
        for page in pages:
            output.addPage(input_pdf.getPage(page - 1))

        # save file
        with open(name, "wb") as output_stream:
            output.write(output_stream)


# starting the application loop

start()
global job
if job == 1:
    Extract()
    print("Thanks for using our program")

if job == 2:
    merge()
    print("Thanks for using our program")

if job == 3:
    split()
    print("Thanks for using our program")

if job == 4:
    print("Thanks for using our program")
