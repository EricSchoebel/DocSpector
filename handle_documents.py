"""
DocSpector
Copyright (C) 2024 Eric Schöbel

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import os
import pandas as pd
from PyPDF2 import PdfReader
from docx import Document

def extract_text_from_txt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except:
        return None

def extract_text_from_docx(docx_path):
    try:
        doc = Document(docx_path)
        text = '\n'.join([paragraph.text for paragraph in doc.paragraphs if paragraph.text])
        return text
    except:
        return None

#extrahiert "nur" die eingefügten Kommentare der PDF
def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ''.join([page.extract_text() or '' for page in reader.pages])
        return text
    except:
        return None

def load_documents(directory):
    data = {'filename': [], 'content': []}
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            text = None
            if filename.endswith('.txt'):
                text = extract_text_from_txt(filepath)
            elif filename.endswith('.docx'):
                text = extract_text_from_docx(filepath)
            elif filename.endswith('.pdf'):
                text = extract_text_from_pdf(filepath)
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

