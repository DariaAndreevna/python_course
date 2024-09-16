import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open("draft.html", "r", "utf-8") as file:
        html = file.read()
    cleaned_text = []
    inside_tag = False
    for sym in html:
        if sym == "<":
            inside_tag = True
        elif sym == ">":
            inside_tag = False
        elif not inside_tag:
            cleaned_text.append(sym)
    cleaned_text = "".join(cleaned_text)

    with codecs.open("cleaned.txt", "w", "utf-8") as output:
        lines = cleaned_text.splitlines()
        non_empty_lines = [line for line in lines if line.strip()]
        output.write("\n".join(non_empty_lines))


delete_html_tags("draft.html")
