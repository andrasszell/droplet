#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 19:16:14 2023

@author: szellandras
"""

import requests

def get_snapshot_id_by_name(api_token, snapshot_name):
    print(f"Bearer {api_token}")
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }

    url = "https://api.digitalocean.com/v2/snapshots"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        snapshots = response.json()["snapshots"]
        for snapshot in snapshots:
            if snapshot["name"] == snapshot_name:
                return snapshot["id"]
        return None
    else:
        print(f"Failed to get snapshots. Status Code: {response.status_code}")
        return None

# Replace 'YOUR_API_TOKEN' with your actual DigitalOcean API token
api_token = 'dop_v1_4d1dae6c36dac40a30a7263839e50f74b20552f5de258a46ec00922d1ebfa072'
snapshot_name = "ubuntu-andras-1"

snapshot_id = get_snapshot_id_by_name(api_token, snapshot_name)

if snapshot_id:
    print(f"Snapshot ID for '{snapshot_name}': {snapshot_id}")
else:
    print(f"Snapshot '{snapshot_name}' not found.")
