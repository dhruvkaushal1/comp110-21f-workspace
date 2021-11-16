"""Some helpful utility functinos for working with CSV Files."""\

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str,str]]:
    """REad the rows of a csv into a 'table'."""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    # Read that file

    csv_reader = DictReader(file_handle)
#read each row of the CSV line-by line
    for row in csv_reader:
        result.append(row)

    #Close the file when we're done, to free its resources
    return result

def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all the values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result