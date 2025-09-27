---
aliases: []
category: LANG
date modified: 27-09-2025
tags: []
---
```python
import spacy
# Load spaCy model for NER
!python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")
# ===============================================
# 6. EXTRACT COMPANY NAMES (NER)
# ===============================================
def extract_companies(text):
    doc = nlp(text)
    return [ent.text for ent in doc.ents if ent.label_ == 'ORG']

df['companies'] = df['headline'].apply(extract_companies)
```