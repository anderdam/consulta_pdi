import re


def find_doc(row):
    match = re.search(r"[A-Z]{3}\d{11}", row)
    if match:
        sequence = match.group()
        return str(sequence)
    else:
        return 'N/D'


def find_emi(row):
    match = re.search(r"[A-Z]{3}\d{11}\s(\d{2}/\d{2}/\d{4})", row)
    if match:
        sequence = match.group(1)
        return str(sequence)
    else:
        return 'N/D'


def find_value(row):
    match = re.search(r"R\$\s([\d,]+(\.\d{2})?)", row)
    if match:
        sequence = match.group()
        return str(sequence)
    else:
        return 'N/D'


def find_venc(row):
    matches = re.findall(r"R\$\s([\d,]+(\.\d{2})?)\s(\d{2}/\d{2}/\d{4})", row)
    if matches:
        dates = [match[2] for match in matches]
        return str(dates[0])
    else:
        return 'N/D'


def find_situation(row):
    match = re.search(r"([a-zA-Z]+\s[a-zA-Z]+)\s*$", row)
    if match:
        sequence = match.group()
        return str(sequence)
    else:
        return 'N/D'
