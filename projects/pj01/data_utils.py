from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Product a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(SET_DATA: dict[str, list[str]], result_rows: int) -> dict[str, list[str]]:
    """Return the first value in the column."""
    result: dict[str, list[str]] = {}
    if result_rows > len(SET_DATA):
        result_rows = len(SET_DATA)
    for column in SET_DATA: 
        first_n: list[str] = []
        i: int = 0
        while i < result_rows:
            first_n.append(SET_DATA[column][i])
            i += 1
        result[column] = first_n
    return result


def select(SET_DATA: dict[str, list[str]], result_column: list[str]) -> dict[str, list[str]]:
    """Returns only a few select columns."""
    select_dict: dict[str, list[str]] = {}
    for column in result_column:
        for key in result_column:
            if key == column:
                select_dict[key] = SET_DATA[key]
    return select_dict


def concat(COLUMN_TABLE: dict[str, list[str]], TABLE_TWO: dict[str, list[str]]) -> dict[str, list[str]]:
    """This concatenates two tables."""
    together_dict: dict[str, list[str]] = {}
    for column in COLUMN_TABLE:
        together_dict[column] = COLUMN_TABLE[column]
    for column_two in TABLE_TWO:
        if column_two in together_dict:
            together_dict[column_two] = together_dict[column_two] + TABLE_TWO[column_two]
        else:
            together_dict[column_two] = TABLE_TWO[column_two]
    return together_dict


def count(value_list: list[str]) -> dict[str, int]:
    """This will count the values in the data set."""
    result: dict[str, int] = {}
    for item in value_list: 
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result