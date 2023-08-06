#!/bin/python3
"""
"""

# Only import what we need from our base, just to keep it light.
from sqlite3 import connect

# Same with logging, only rename the members for readability.
from logging import getLogger, exception
from logging import info as information
from logging import debug as debugging


class Lab93DatabaseSystem:

    def __init__( self,
                  database: str="./sqlite3.db",
                  interactive_mode: bool=False  ) -> None:
        """
        """
        getLogger(); information(
            f"Initialized Lab-93 database system."
        )
        
        debugging(
            f"Beginning constants definition"
        )

        self.sql = SQLite3_Statements(
            database
        )


    class databaseConnection:
        """
        """

        def __init__( self,
                      database: str="./.sqlite3.db" ) -> None:

            getLogger(); information(
                f"Establishing database connection with {database}"
            )

            debugging(
                f"Attempting connection with sqlite3 database file."
            )
            try:
                self.connection = connect(
                    database
                ); self.cursor = self.connection\
                                     .cursor()

                debugging(
                    f"Database connection successful."
                )
            
            except Exception as error:
                exception(
                    f"There was an issue connecting to the {database} database;\n{error}"
                ); return error


    class SQLite3_Statements:
        """
        SQLite3 is the chosen method for data storage based on the
        fact that it comes included with Python; but despite it's
        simplicity and ubiquity it's still very powerful for our
        day to day use-case.

        The SQLite3_Statements class offers a library of pre-defined
        statements that are easily accessed by an api of functionality.
        """

        def __init__( self,
                      database: str="./test.db" ) -> None:
            """
            The class holds a self-referential list of myriad sqlite3 statements sans-
            formatting; customization of commands is offered through argumentative
            methods.
            """

            ''' (Linux) Filepath to an sqlite3.db file. '''
            self.database = database

            ''' Master dictionary of various sqlite3 statements. '''
            self.statements = {
                # Select a specific column from a row based on another column.
                'queryCompareColumns': "SELECT {} FROM {} WHERE  {}='{}';",

                # Add a new column to the database.
                'createNewColumn': "ALTER TABLE {} ADD {} {}",
            
                # Create a new new table within the database.
                'createNewTable': "CREATE TABLE IF NOT EXISTS {}({} {} PRIMARY KEY);",

                # Check if a specific table exists within the database.
                'queryTableExistence': "SELECT COUNT(name) FROM sqlite_master WHERE type='table' AND name='{}';",

                # Check a given table for a specific column.
                'queryColumnExistence': "SELECT COUNT(*) FROM pragma_table_info('{}') WHERE name='{}';",
            }


        def newColumn( self,
                       table: str="test_table_one",
                       column: str="test_column_one",
                       column_type: str="UNIQUE PRIMARY TEXT" ) -> None:

            db = databaseConnection(self.database)

            db.cursor\
              .execute( self.statements['createNewColumn']\
                            .format( table.lower()\
                                          .replace(" ", "-"),

                                     column.lower()\
                                           .replace(" ", "-"),

                                     column_type.upper()       ) )

            return db.connection\
                     .commit()


        def compareColumns( self,
                            column: str="test_column_one",
                            table: str="test_table_one",
                            comparator: str="test_column_two",
                            value: str="test_value_two") -> str:
            """
            """
            return databaseConnection(
                self.database
            ).cursor\
             .execute( self.statements['queryCompareColumns']\
                           .format( column,
                                    table,
                                    comparator,
                                    value       )
                                                               )\
             .fetchall()[0][0]


        def newTable( self,
                      table: str="test_table_one",
                      column: str="test_column_one",
                      column_type: str="UNIQUE PRIMARY TEXT" ) -> None:
            """
            Create a new table initialized with a PRIMARY KEY
            $column of $column_type.
            """

            ''' Establish database connection. '''
            db = databaseConnection(self.database)

            ''' Format command string with argument input. '''
            db.cursor\
              .execute( self.statements['createNewTable']\
                            .format ( table.lower()\
                                           .replace(" ", "_"),

                                      column.lower()\
                                            .replace(" ", "_"),

                                      column_type.upper()       ) )

            ''' Save your work. '''
            return db.connection\
                     .commit()


        def checkTable( self,
                        # A collection of records to be found.
                        table: str="test_table_one"            ) -> int:
            """
            """
            return databaseConnection.cursor\
                                     .execute( self.statements['queryTableExistence']\
                                                   .format( table.lower() )          )\
                                     .fetchall()[0][0]


        def checkColumn( self,
                         # Record collection being searched.
                         table: str="test_table_one",
                         # Column header being searched for.
                         column: str="test_column_one"       ) -> int:
            """
            Calls self.queryColumnExistence on a given $table and $column;
            if the return value is more than zero, then the column exists.
            """

            return databaseConnection.cursor\
                                     .execute( self.statements['queryColumnExistence']\
                                                   .format( table.lower(),
                                                            column.lower() )            )\
                                     .fetchall()[0][0]