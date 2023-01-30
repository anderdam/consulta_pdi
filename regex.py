import re


def find_doc(row):
    match = re.search(r"[A-Z]{3}\d{11}", row)
    sequence = match.group()
    return str(sequence)


def find_emi(row):
    match = re.search(r"[A-Z]{3}\d{11}\s(\d{2}/\d{2}/\d{4})", row)
    sequence = match.group(1)
    return str(sequence)


def find_value(row):
    match = re.search(r"R\$\s([\d,]+(\.\d{2})?)", row)
    sequence = match.group()
    return str(sequence)


def find_venc(row):
    return str(re.findall(r"R\$\s([\d,]+(\.\d{2})?)\s(\d{2}/\d{2}/\d{4})", row))


def find_situation(row):
    match = re.search(r"([a-zA-Z]+\s[a-zA-Z]+)\s*$", row)
    sequence = match.group()
    return str(sequence)
