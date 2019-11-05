# Extracting SPOs.
# python -m spacy download en -> To donwload the en model of spacy.

import spacy
import textacy

# Subject Verb Object detection


class KnowledgeExtraction:

    def retrieveKnowledge(self, textInput):
        nlp = spacy.load('en')
        text = nlp(textInput)
        text_ext = textacy.extract.subject_verb_object_triples(text)
        return list(text_ext)
