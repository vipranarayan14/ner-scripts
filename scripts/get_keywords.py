import csv
import spacy

from indic_transliteration.sanscript import transliterate, DEVANAGARI, IAST

from simplify_diacritics import simplify_diacritics


def prepare_comments(list_file_path):
    list_file = open(list_file_path)
    reader = csv.DictReader(list_file)

    comments = []

    for row in reader:
        slno = row["Serial No."]
        category = row["Catagory"]
        source = row["Source"]

        comment_raw = " ".join([category, source])
        comment_without_deva = transliterate(comment_raw, DEVANAGARI, IAST)
        comment_clean = simplify_diacritics(comment_without_deva)
        comment = comment_without_deva + " " + comment_clean

        comments.append((comment, slno))

    return comments


def extract_keywords(docs):
    all_keywords = []

    for doc, context in docs:
        keywords = [token.text for token in doc if token.pos_ == "NOUN"]
        uniq_keywords = list(set(keywords))
        all_keywords.append([context, ",".join(uniq_keywords)])

    return all_keywords


list_file_path = "data/list_clean.csv"
out_file_path = "notes/keywords/keywords_in_comments.csv"

nlp = spacy.load("en_core_web_md")

comments_data = prepare_comments(list_file_path)
docs = nlp.pipe(comments_data, as_tuples=True, batch_size=100, n_process=2)
keywords_by_slno = extract_keywords(docs)


with open(out_file_path, mode="w") as out_file:
    fieldnames = ["slno", "keywords_in_comments"]
    csv_writer = csv.writer(out_file)
    csv_writer.writerow(fieldnames)
    csv_writer.writerows(keywords_by_slno)


# for row in reader:
#     slno = row["Serial No."]
#     category = row["Catagory"]
#     source = row["Source"]

#     category_doc = nlp(category)

#     keywords_in_category = [
#         token.text for token in category_doc if token.pos_ == "VERB"
#     ]
#     keywords.append([slno, ",".join(keywords_in_category)])
