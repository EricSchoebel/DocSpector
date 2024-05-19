import pandas as pd
#def load_from_pickle(pickle_file):
#    return pd.read_pickle(pickle_file)

def search_documents_old(df, search_words):
    # Suche nach Dokumenten, die mindestens eines der Suchwörter enthalten
    mask = df['content'].apply(lambda text: any(word.lower() in text.lower() for word in search_words)) # gibt True/False
    return df[mask] # gibt die jeweiligen Zeilen des Dataframes wieder

def search_documents(df, search_words):
    # Suche nach Dokumenten, die mindestens eines der Suchwörter enthalten
    def find_keywords(text):
        found = [word for word in search_words if word.lower() in text.lower()]
        return ', '.join(found) if found else None

    df['Gefundene Suchwörter'] = df['content'].apply(find_keywords)
    return df.dropna(subset=['Gefundene Suchwörter'])

# Pickle-Datei laden
#df_loaded = load_from_pickle('documents.pkl')

# Suchwörter INPUT
#earch_words = ['Python', 'Personal', 'Knotenpunkt', 'Übung']


#results = search_documents(df_loaded, search_words)
#print("Gefundene Dokumente:")
#print(results[['filename']])
