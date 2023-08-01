from Authentication.login import UserInDB
from query_DB import db_connection, execute_query
from mysql.connector import Error


def create_device(ip, mac, network_id):
    connection = db_connection()
    new_device = """
    INSERT INTO Device (ip,mac,network_id)
    VALUES (ip,mac,network_id);
    """
    insert_device = execute_query(connection, new_device)
    return insert_device


def create_network(client_id, premise, date_taken):
    connection = db_connection()
    new_network = """
        INSERT INTO Network (client_id,premise,date_taken)
        VALUES (client_id,premise,date_taken);
        """
    insert_network = execute_query(connection, new_network)
    return insert_network


def create_device_connections(src, destination, protocol, network_id):
    connection = db_connection()
    new_device_connections = """
           INSERT INTO Device_Connections_table (src,dest,protocol,network_id)
           VALUES (src,destination,protocol,network_id);
           """
    insert_device_connections = execute_query(connection, new_device_connections)
    return insert_device_connections


def create_user_client(user_id, client_id):
    connection = db_connection()
    new_user_client = """
            INSERT INTO User_Client (user_id,client_id)
            VALUES (user_id,client_id);
            """
    insert_user_client = execute_query(connection, new_user_client)
    return insert_user_client


# def get_all_users():
#     connection = db_connection()
#     get_users_query = "SELECT id, name, password FROM user_table;"
#     users = execute_query(connection, get_users_query).fetchall()
#     return users


def get_password_by_name(username):
    try:
        connection = db_connection()
        get_password_query = "SELECT password FROM user_table WHERE name = %s"
        cursor = connection.cursor()
        cursor.execute(get_password_query, username)
        user_data = cursor.fetchone()
        if user_data:
            user_id, username, password = user_data
            return UserInDB(name=username, id=user_id, hashed_password=password)
        else:
            return None
    except Error as e:
        print("Error:", e)
        return None


