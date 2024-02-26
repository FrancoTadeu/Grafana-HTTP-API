import os
import json
import requests

grafana_url = "http://your-grafana-instance"  # Replace with your Grafana instance URL
api_key = "YOUR_API_KEY"  # Replace with your Grafana API key
folder_name = "YourFolder"  # Replace with the desired folder name

# Function to read JSON files from a folder
def read_dashboard_files(folder_path):
    dashboard_files = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".json"):
            dashboard_files.append(os.path.join(folder_path, file_name))
    return dashboard_files

# Function to upload a dashboard to Grafana
def upload_dashboard(file_path):
    with open(file_path, 'r') as file:
        dashboard_content = json.load(file)

    url = f"{grafana_url}/api/dashboards/db"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {api_key}"
    }

    payload = {
        "dashboard": dashboard_content,
        "folderId": 0,  # Set to 0 for the General folder, or specify a folder ID if needed
        "overwrite": True  # Set to True to overwrite if the dashboard already exists
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print(f"Dashboard from {file_path} uploaded successfully.")
    else:
        print(f"Error uploading dashboard from {file_path}. Status code: {response.status_code}")

# Main script
if __name__ == "__main__":
    # Get a list of JSON files in the "dashboards" subfolder
    dashboards_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dashboards")
    dashboard_files = read_dashboard_files(dashboards_folder)

    # Upload each dashboard to Grafana
    for dashboard_file in dashboard_files:
        upload_dashboard(dashboard_file)
