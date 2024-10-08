import os

def get_proxies_from_file():
    # Get the directory of the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    proxies_file_path = os.path.join(current_directory, 'proxies.txt')
    
    # Or simply use a fixed path 
    file_path = "xxxxxx/GitHub/Rumble-Likes-Bot/utils/files/proxies.txt"
    # Read proxies from the file
    with open(proxies_file_path, 'r') as file:
        proxies = [line.strip() for line in file if line.strip()]  # Strip whitespace and ignore empty lines

    return proxies
