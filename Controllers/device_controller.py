from DB.query import execute_query
# from DB.extract_from_db import select_filter_devices


# how do i get the name of the filter and the value,
# maybe as:{ip:123.456.777}
# maybe as:2 params (ip,1234.566.677
mac=223,
mac:123

# def view_filter_devices(input_network_id, **kwargs):
def view_filter_devices(input_network_id, condition=''):
    # is_athorized
    match condition:
        case 'ip':
            print("ip")
            device_by_ip = """
            SELECT * 
            FROM Device
            WHERE ip = condition
            """
            a = execute_query(device_by_ip).fetchall()
            for i in a:
                print(a[i])
            # select_filter_devices(ip)
        case 'mac':
            print("mac")
            device_by_mac = """
                       SELECT * 
                       FROM Device
                       WHERE mac = condition
                       """
            a = execute_query(device_by_mac).fetchall()
            for i in a:
                print(a[i])
            # select_filter_devices(mac)
        case 'protocol':
            print("protocol")
            device_by_protocol = """
                       SELECT * 
                       FROM Device
                       WHERE protocol = condition
                       """
            a = execute_query(device_by_protocol).fetchall()
            for i in a:
                print(a[i])
            # select_filter_devices(protocol)
        case 'vendor':
            print("vendor")
            device_by_vendor = """
                               SELECT * 
                               FROM Device
                               WHERE mac.contains = condition
                               """
            a = execute_query(device_by_vendor).fetchall()
            for i in a:
                print(a[i])
            # select_filter_devices(vendor or mac)
        case _:
            all_network_devices = """
            SELECT * 
            FROM Device 
            WHERE network_id = input_network_id
            """

            #WHERE network_id = network_id
            a = execute_query(all_network_devices).fetchall()
            for i in a:
                print(a[i])
            # results = cursor.fetchall()
            # select_filter_devices(network_id)




# NTH
def view_client_devices(client_id):
    pass
