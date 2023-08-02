# from DB.query import execute_query
def get_network_dict(network_id):
    # return {1:[2,3,4],2:[5,6]}

    network_devices = f"""
    SELECT mac 
    FROM Device
    WHERE network_id = {network_id}
    """
    network_dict = {}
    for device in network_devices:
        device_connections = f"""
        SELECT dest_mac FROM Device_Connections_table
        WHERE src_mac = {device}
        """
        # network_dict.append(key = device,value = device_connections:[])

        network_dict[device] = [device_connections]
        # network_dict[device] = device_connections


# def match_filter():
#     pass
def select_filter_devices(condition):
    q = """
    SELECT * 
    FROM Device 
    WHERE condition = condition
    """
    query_result = execute_query(q).fetchall()
    # results = cursor.fetchall()
    for i in query_result:
        print(query_result[i])


# NTH
def get_client_devices_from_db():
    pass
