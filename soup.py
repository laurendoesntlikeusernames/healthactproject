import html5lib
with open("index.html", "rb") as f:
    lxml_etree_document = html5lib.parse(f, treebuilder="lxml")