import subprocess
import re
from tabulate import tabulate

# Command to run to get Wi-Fi profiles
cmd_command = 'netsh wlan show profile'

# Run the command and capture the output
try:
    result = subprocess.check_output(cmd_command, shell=True, universal_newlines=True)

    # Extract the "All User Profile" names using regular expressions
    profile_names = re.findall(r'All User Profile\s+:\s+(.+)', result)

    # Initialize dictionaries to store profile data and password counts
    profile_data = {}
    password_counts = {}

    for profile_name in profile_names:
        # Escape any special characters within the profile name and enclose in double quotes
        escaped_profile_name = '"' + profile_name.replace('"', r'\"') + '"'

        # Run the command for each profile name
        cmd_command = f'netsh wlan show profile name={escaped_profile_name} key=clear'

        try:
            cmd_result = subprocess.check_output(cmd_command, shell=True, universal_newlines=True)

            # Extract the "Key Content" using regular expressions
            key_content = re.search(r'Key Content\s+:\s+(.+)', cmd_result)
            if key_content:
                key_content = key_content.group(1)
            else:
                key_content = "Key not found"

            # Store profile data
            profile_data[profile_name] = key_content

            # Count the number of profiles with the same password
            if key_content not in password_counts:
                password_counts[key_content] = 1
            else:
                password_counts[key_content] += 1

        except subprocess.CalledProcessError as e:
            print(f"Error executing command for '{profile_name}': {e}")

    # Ask the user for the sorting option
    print("Select a sorting option:")
    print("1. Print profiles in original order")
    print("2. Group profiles with the same password together")
    user_option = input("Enter your choice (1/2): ")

    if user_option == "1":
        # Display the table in original order
        headers = ["Wi-Fi Profile Name", "Key Content"]
        data = [[profile_name, key_content] for profile_name, key_content in profile_data.items()]
        print(f"Total Wi-Fi profiles: {len(profile_names)}")
        print(tabulate(data, headers, tablefmt="grid"))

    elif user_option == "2":
        # Group profiles with the same password together and display password counts
        grouped_profile_data = {}
        for profile_name, key_content in profile_data.items():
            if key_content not in grouped_profile_data:
                grouped_profile_data[key_content] = []
            grouped_profile_data[key_content].append(profile_name)

        headers = ["Key Content", "Wi-Fi Profile Names", "Count"]
        grouped_table_data = [
            [key, "\n".join(profile_names), password_counts[key]]
            for key, profile_names in grouped_profile_data.items()
        ]

        print(f"Total Wi-Fi profiles: {len(profile_names)}")
        print(tabulate(grouped_table_data, headers, tablefmt="grid"))

    else:
        print("Invalid option. Please enter '1' or '2'.")

except subprocess.CalledProcessError as e:
    print(f"Error executing command: {e}")
