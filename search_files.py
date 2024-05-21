import pandas as pd

def search_documents(df, search_words):
    
    def find_keywords(text): #gibt für einen Text (=Input), die gefundenen Suchwörter zurück (String als Optuput)
        found = [word for word in search_words if word.lower() in text.lower()]
        return ', '.join(found) if found else None

    df['Gefundene Suchwörter'] = df['content'].apply(find_keywords) # wendet für jeden Text in Content-Spalte find_keywords an
    return df.dropna(subset=['Gefundene Suchwörter']) # entfernt die Zeilen, die keinen Eintrag bei Gefundende Suchwörter haben
