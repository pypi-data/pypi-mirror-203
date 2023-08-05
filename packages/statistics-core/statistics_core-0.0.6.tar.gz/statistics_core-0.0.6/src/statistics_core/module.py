import os

import pymysql
import pywikibot
from pywikibot import config as _config


class Database:
    """
    A class to handle connections to a MySQL database and execute queries.

    Attributes:
    _connection: pymysql.connections.Connection
        The connection object for the database.
    _query: str
        The query to be executed on the database.
    result: list
        The result of the executed query.

    Methods:
    connection:
        A property to get the database connection.
    query:
        A property to get and set the query to be executed on the database.
    get_content_from_database():
        Executes the query on the database and fetches the result.
    """

    def __init__(self):
        self._connection = None
        self._query = ""
        self.result = []

    @property
    def connection(self):
        """
        Get the database connection object.

        If the connection object exists, return it. Otherwise, establish a new
        connection and return it.

        Returns:
        pymysql.connections.Connection
            The connection object for the database.
        """
        if self._connection is not None:
            return self._connection
        else:
            return pymysql.connect(
                host=_config.db_hostname_format.format("arwiki"),
                read_default_file=_config.db_connect_file,
                db=_config.db_name_format.format("arwiki"),
                charset='utf8mb4',
                port=_config.db_port,
                cursorclass=pymysql.cursors.DictCursor,
            )

    @property
    def query(self):
        """
        Get the query to be executed on the database.

        Returns:
        str
            The query to be executed on the database.
        """
        return self._query

    @query.setter
    def query(self, value):
        """
        Set the query to be executed on the database.

        Args:
        value: str
            The query to be executed on the database.
        """
        self._query = value

    def get_content_from_database(self):
        """
        Execute the query on the database and fetch the result.

        Returns:
        list
            The result of the executed query.
        """
        try:
            # Create a cursor object
            with self.connection.cursor() as cursor:
                # Execute the SELECT statement
                cursor.execute(self._query)
                # Fetch all the rows of the result
                self.result = cursor.fetchall()
        finally:
            # Close the connection
            self.connection.close()

    @connection.setter
    def connection(self, value):
        """
        Set the database connection object.

        Args:
        value: pymysql.connections.Connection
            The connection object for the database.
        """
        self._connection = value

class Page:
    """
    A class for handling a MediaWiki page.

    Attributes:
        site (pywikibot.Site): The site object for the wiki where the page exists.
        _page_name (str): The name of the page.
        contents (str): The contents of the page.
        _summary (str): The edit summary to use when saving the page.

    """

    def __init__(self):
        """
        Initializes a Page object.
        """
        self.site = pywikibot.Site()
        self._page_name = ""
        self.contents = ""
        self._summary = "بوت:إحصاءات V2.2.1"

    @property
    def page_name(self):
        """
        Gets the name of the page.

        Returns:
            str: The name of the page.

        """
        return self._page_name

    @page_name.setter
    def page_name(self, value):
        """
        Sets the name of the page.

        Args:
            value (str): The new name of the page.

        """
        self._page_name = value

    @property
    def summary(self):
        """
        Gets the edit summary.

        Returns:
            str: The edit summary.

        """
        return self._summary

    @summary.setter
    def summary(self, value):
        """
        Sets the edit summary.

        Args:
            value (str): The new edit summary.

        """
        self._summary = value

    def make_new_text(self):
        """
        Replaces some placeholders in the contents of the page with actual values.
        """
        # Get the username of the bot account
        username_bot = self.site.username()
        self.contents = self.contents.replace(
            'BOT_USER_NAME', f"[[مستخدم:{username_bot}|{username_bot}]]"
        ).replace(
            "BOT_TIME_NOW", "{{نسخ:#time:H:i، j F Y}}"
        )

    def set_contents(self, content):
        """
        Sets the contents of the page.

        Args:
            content (str): The new contents of the page.

        """
        self.contents = content

    def save_page(self):
        """
        Saves the page with the new contents.
        """
        # Get a Page object for the page
        page = pywikibot.Page(self.site, self.page_name)
        self.make_new_text()
        # Set the text of the page
        page.text = self.contents
        # Save the page
        page.save(summary=self.summary)

class File:
    """
    A class for interacting with files.

    Attributes:
    -----------
    script_dir : str
        The directory of the current script.
    file_path : str
        The path of the file to interact with.
    contents : str
        The contents of the file.
    """

    def __init__(self):
        self.script_dir = os.path.dirname(__file__)
        self.file_path = ""
        self.contents = ""

    def set_stub_path(self, name):
        """
        Set the file path based on the given name.

        Parameters:
        -----------
        name : str
            The name of the file to interact with.
        """
        self.file_path = os.path.join(self.script_dir, name)

    def get_file_content(self):
        """
        Get the contents of the file.
        """
        with open(self.file_path) as file:
            self.contents = file.read()




class ArticleTable:
    """
    A utility class for building wikitable markup from a list of data.
    """
    def __init__(self):
        """
         Initializes an instance of the ArticleTable class.
         """
        self.columns = []
        self.add_header_text = None
        self.add_footer_text = None
        self.add_table_name = None
        self.add_end_row_to_table = None
        self.sort_column = None

    def add_column(self, name, value_index, clause=None):
        """
        Adds a column to the table.

        Args:
            name (str): The name of the column.
            value_index (int): The index of the value to display in the column.
            clause (function, optional): A function to generate the column value. The function must take three arguments:
                the row being processed, the list of all rows, and the index of the row being processed. Defaults to None.
        """

        self.columns.append((name, value_index, clause))

    def set_sort_column(self, column_name):
        """
        Sets the column to sort the table by.

        Args:
            column_name (str): The name of the column to sort by.
        """

        self.sort_column = column_name

    def build_table(self, result, end_row_in_table=None, header_text=None, footer_text=None):
        """
        Builds the wikitable markup for the given data.

        Args:
            result (list): The data to display in the table.
            end_row_in_table (function, optional): A function to generate additional rows at the end of the table.
                The function must take a single argument, the list of all rows. Defaults to None.
            header_text (function, optional): A function to generate header text for the table.
                The function must take a single argument, the list of all rows. Defaults to None.
            footer_text (function, optional): A function to generate footer text for the table.
                The function must take a single argument, the list of all rows. Defaults to None.

        Returns:
            str: The wikitable markup for the data.
        """
        if self.sort_column:
            result = sorted(result, key=lambda x: x[self.sort_column], reverse=True)

        table_header = ""
        if header_text is not None:
            table_header += header_text(result)

        # create the table header
        header = '{| class="wikitable sortable"\n'
        for column_name, _, _ in self.columns:
            header += f'!style="background-color:#808080" align="center"|{column_name}\n'

        # create the table body
        body = header

        for index, row in enumerate(result):
            body += '|-\n'
            for _, value_index, clause in self.columns:
                if clause:
                    cell_value = clause(row, result, index)
                else:
                    if isinstance(row[value_index], (str, bytes)):
                        cell_value = str(row[value_index], 'utf-8')
                    else:
                        cell_value = str(row[value_index])
                body += f'|{cell_value}\n'
            body += '\n'
        if end_row_in_table is not None:
            body += end_row_in_table(result)

        # create the table footer
        footer = '|}\n'

        if footer_text is not None:
            footer += footer_text(result)

        # return the full table
        return str(table_header + body + footer).replace("TABLE_NAME", str(self.add_table_name))


class UpdatePage:
    """
    A class to update a wiki page with data from a database.

    Attributes:
    -----------
    query : str
        The SQL query to fetch the data from the database.
    file_path : str
        The path to the file containing the wiki page content.
    page_name : str
        The name of the wiki page to update.
    tables : ArticleTable
        An instance of the ArticleTable class, which defines the structure of the tables to be inserted in the page.
    connection : Connection, optional
        The database connection object to use. If not provided, a new connection object will be created.

    Methods:
    --------
    update()
        Update the wiki page with the data from the database and the defined tables.
    """
    def __init__(self, query, file_path, page_name, tables, connection=None):
        """
        Initialize the UpdatePage class.

        Parameters:
        -----------
        query : str
            The SQL query to fetch the data from the database.
        file_path : str
            The path to the file containing the wiki page content.
        page_name : str
            The name of the wiki page to update.
        tables : ArticleTable
            An instance of the ArticleTable class, which defines the structure of the tables to be inserted in the page.
        connection : Connection, optional
            The database connection object to use. If not provided, a new connection object will be created.
        """
        self.database = Database()
        self.file = File()
        self.tables = tables
        self.page = Page()
        if connection is not None:
            self.database.connection = connection
        self.database.query = query
        self.database.get_content_from_database()

        self.file.set_stub_path(file_path)
        self.file.get_file_content()

        self.page.page_name = page_name

    def update(self):
        """
        Update the wiki page with the data from the database and the defined tables.
        """
        content = self.file.contents
        table_body = ""
        for table in self.tables.tables:
            table_body += table.build_table(result=self.database.result, end_row_in_table=table.add_end_row_to_table,
                                            header_text=table.add_header_text, footer_text=table.add_footer_text)

        content = content.replace("BOT_TABLE_BODY", table_body)
        self.page.set_contents(content)
        self.page.save_page()


class ArticleTables:
    """
    A class for managing multiple ArticleTable objects and creating tables for a Wikipedia page.

    Attributes:
        tables (list): A list of ArticleTable objects.

    Methods:
        add_table(name, columns, header_text=None, footer_text=None, end_row_text=None, sort_column=None):
            Adds a new ArticleTable object to the list of tables with the specified name, columns, and optional attributes.
    """


    def __init__(self):
        self.tables = []

    def add_table(self, name, columns, header_text=None, footer_text=None, end_row_text=None, sort_column=None):
        """
        Adds a new ArticleTable object to the list of tables with the specified name, columns, and optional attributes.

        Args:
            name (str): The name of the table.
            columns (list): A list of tuples representing the columns of the table. Each tuple should have two or three
                            elements: the name of the column, the index of the value in each row, and optionally a
                            clause for transforming the value.
            header_text (function, optional): A function that takes a list of rows as input and returns a string
                                              representing the header of the table.
            footer_text (function, optional): A function that takes a list of rows as input and returns a string
                                              representing the footer of the table.
            end_row_text (function, optional): A function that takes a list of rows as input and returns a string
                                               representing the last row of the table.
            sort_column (str, optional): The name of the column to sort the table by.

        Returns:
            None
        """
        table = ArticleTable()
        if header_text is not None:
            table.add_header_text = header_text

        if footer_text is not None:
            table.add_footer_text = footer_text

        if end_row_text is not None:
            table.add_end_row_to_table = end_row_text

        if name is not None:
            table.add_table_name = name

        if sort_column is not None:
            table.set_sort_column(sort_column)

        for column in columns:
            column_name = column[0]
            value_index = column[1]
            clause = None
            if len(column) > 2:
                clause = column[2]
            table.add_column(column_name, value_index, clause=clause)
        self.tables.append(table)

def index(row, result, index):
    """
    Returns the 1-based index of the current row in the result set.

    :param row: A dictionary representing the current row in the result set.
    :param result: A list of dictionaries representing the entire result set.
    :param index: The 0-based index of the current row in the result set.
    :return: The 1-based index of the current row in the result set.
    """
    return index + 1


if __name__ == "__main__":
    pass