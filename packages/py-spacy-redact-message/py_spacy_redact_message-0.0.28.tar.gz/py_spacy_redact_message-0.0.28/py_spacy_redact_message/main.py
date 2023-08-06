import typer
import spacy

nlp = spacy.load('en_core_web_sm')
ent_labels_to_redact = ['ORDINAL', 'CARDINAL', 'DATE', 'EVENT', 'FAC', 'GPE', 'LANGUAGE', 'LAW', 'LOC', 'MONEY', 'NORP', 'ORG', 'PERCENT', 'PERSON', 'PRODUCT', 'QUANTITY', 'TIME', 'WORK_OF_ART']

def spacy_replace_entities_with_labels(text):
    spacy_doc = nlp(text)
    spacy_entities = spacy_doc.ents
    if len(spacy_entities) > 0:
        for ent in spacy_entities:
            if ent.label_ in ent_labels_to_redact:
                text = text.replace(ent.text, f"[{ent.label_}]")

    return text

def main(
    input: str = typer.Argument(..., exists=True),
    ):

    result = spacy_replace_entities_with_labels(input)

    print(result)

def run():
    typer.run(main)

if __name__ == "__main__":
    run()
