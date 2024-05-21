import os
import pandas as pd
from PyPDF2 import PdfReader

def extract_text_from_txt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except:
        return None

#extrahiert "nur" die eingefügte Kommentare der PDF
def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ''.join([page.extract_text() or '' for page in reader.pages])
        return text
    except:
        return None


#def extract_text_from_docx(docx_path):
#    try:
#        doc = Document(docx_path)
#        text = '\n'.join([paragraph.text for paragraph in doc.paragraphs if paragraph.text])
#        return text
#    except:
#        return None


def load_documents(directory):
    data = {'filename': [], 'content': []}
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            text = None
            if filename.endswith('.pdf'):
                text = extract_text_from_pdf(filepath)
            elif filename.endswith('.txt'):
                text = extract_text_from_txt(filepath)
            if text:
                data['filename'].append(filename)
                data['content'].append(text)
    return pd.DataFrame(data)


def search_documents(df, search_words):

    # gibt für einen Text (=Input), die gefundenen Suchwörter zurück (String als Output)
    def find_keywords(text):
        found = [word for word in search_words if word.lower() in text.lower()]
        return ', '.join(found) if found else None

    # wendet für jeden Text in Content-Spalte find_keywords an
    df['Gefundene Suchwörter'] = df['content'].apply(find_keywords)

    # entfernt die Zeilen, die keinen Eintrag bei Gefundende Suchwörter haben
    return df.dropna(subset=['Gefundene Suchwörter'])

# INPUT:
# Verzeichnis mit Dokumenten
#directory = r'D:\\Programmierung\PyCharm\eigeneProjekte\Dokumentenfilter'


#print(df)

