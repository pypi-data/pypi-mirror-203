from typing import List


class Column:
    def __init__(self, name: str, data_type: str, nullable: bool = False):
        self.name = name
        self.data_type = data_type
        self.nullable = nullable


class Table:
    def __init__(self, name: str, columns: List[Column]):
        self.name = name
        self.columns = columns


class Schema:
    def __init__(self):
        self.tables = []

    def add_table(self, table: Table):
        self.tables.append(table)
