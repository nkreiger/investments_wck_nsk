# This class will house the api call to retrieve both fixture and general data about a given team.
import wrds

def getConnection():
    return wrds.Connection(wrds_username = 'kleiwc15');

def closeConnection():
    #putConn(conn);
    return

def getAllLibraries():
    conn = getConnection()

    libraries = conn.list_libraries()

    closeConnection()
        
    return libraries

def getTables(library):
    conn = getConnection()

    data = conn.list_tables(library=library)

    closeConnection()
    
    return data

def getTableData(library, table):
    conn = getConnection()

    data = conn.get_table(library=library, table=table)

    closeConnection()

    return data

def executeQuery(query):
    conn = getConenction()

    data = conn.raw_sql(query)

    closeConnection()

    return data




        
