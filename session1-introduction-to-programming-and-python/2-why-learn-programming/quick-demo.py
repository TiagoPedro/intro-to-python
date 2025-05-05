import requests
import re
import tkinter as tk
from tkinter import messagebox

# APS token and folder URN (already obtained beforehand)
token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IlhrUFpfSmhoXzlTYzNZS01oRERBZFBWeFowOF9SUzI1NiIsInBpLmF0bSI6ImFzc2MifQ.eyJzY29wZSI6WyJidWNrZXQ6Y3JlYXRlIiwiYnVja2V0OnJlYWQiLCJkYXRhOnJlYWQiLCJkYXRhOmNyZWF0ZSIsImRhdGE6d3JpdGUiXSwiY2xpZW50X2lkIjoiMXZ2SjVBcUdFMFlKSkJ6S1ZMcUdHUXZuYlZlYXgxWG4iLCJpc3MiOiJodHRwczovL2RldmVsb3Blci5hcGkuYXV0b2Rlc2suY29tIiwiYXVkIjoiaHR0cHM6Ly9hdXRvZGVzay5jb20iLCJqdGkiOiJCanVvUGt0Sm1mT29ZRmdaRDVsbUpMY2psMWJaOUlwaVdRemRLT1BKZ0c5U1J1MmF4elhEdklnalcyNFBvQkJnIiwiZXhwIjoxNzQyODM5ODI4fQ.QGYmMUN3YZcREYzrrKSWMIf6rFJ8s6XFFgKLwou7kx-hRfbr-rVAauSameGca8dwkKJ2D_YX7TKWf29QpuYSmZ-fhlgASsya0XicMfARC2TtGcwBDcfoaNF-jLisF55rvVxfHDSWM9LyJ8QIQPGdE3cR1oVETzBWfMgq5SvY68PZTpMi76WF6SSrn7oIXwADpXKzwzzdGkqnGSpbImrXZrqmKJLudftFGK026uAvdILMftInpfKf107TLBN3QtM_7lalmdxx4blgGsUkYy-Cf2ipQQKEWrvA_gRdUZ3VeRV73YMSH76hNKVeTXkrdQWr_Acwzb5Irk0nsvv4wbWQeQ"
folder_urn = "urn:adsk.wipprod:fs.folder:co.WHzig8wHQryaLmLBdvlx-A"
project_id = "09baab9a-2390-4a93-9fb0-1e8c121a5139"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# Regex pattern based on naming convention
naming_pattern = re.compile(r"^[A-Z]{3}-[A-Z]{3}-ZZ-ZZ-[A-Z0-9]{2}-[A-Z]{1}-\d{6}\.rvt$")

# List all items (models) in the folder
url = f"https://developer.api.autodesk.com/data/v1/projects/b.{project_id}/folders/{folder_urn}/contents"
response = requests.get(url, headers=headers)
items = response.json()["data"]

# Validate names and prepare dialog message
dialog_message = "File Name Validation Results:\n\n"
for item in items:
    name = item["attributes"]["displayName"]
    if name.endswith(".rvt"):
        if naming_pattern.match(name):
            dialog_message += f"[✅] Valid: {name}\n"
        else:
            dialog_message += f"[❌] Invalid: {name}\n"

# Create root window but keep it hidden
root = tk.Tk()
root.withdraw()

# Show message box dialog
messagebox.showinfo("Filename Validation Results", dialog_message)

# Cleanup
root.destroy()
