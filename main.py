import pyttsx3
import PyPDF2
book = open('Rework ( PDFDrive.com ).pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
friend = pyttsx3.init()
friend.say('The book name is Rework & it has total pages: ' + str(pages))
for num in range(1, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    friend.say(text)
    friend.runAndWait()