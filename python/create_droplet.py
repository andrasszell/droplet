#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 19:17:14 2023

@author: szellandras
"""

import requests
import json

# DigitalOcean API endpoint for creating a Droplet
url = 'https://api.digitalocean.com/v2/droplets'

# API token for authentication (replace with your own token)
api_token = 'dop_v1_4d1dae6c36dac40a30a7263839e50f74b20552f5de258a46ec00922d1ebfa072'

# Snapshot ID of the snapshot you want to use
snapshot_id = '140744802'

# Droplet configuration
droplet_name = 'ubuntu-andras-1'
region = 'FRA1'
size = 's-1vcpu-1gb'

# Create Droplet payload
payload = {
    'name': droplet_name,
    'region': region,
    'size': size,
    'image': snapshot_id,
    'ssh_keys': None,  # Replace with your SSH keys if needed
    'backups': False,
    'ipv6': False,
    'user_data': None,
    'private_networking': None,
    'volumes': None,
    'tags': []
}

# Set headers and authentication
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_token}'
}

# Send POST request to create the Droplet
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Check if the request was successful
if response.status_code == 202:
    print('Droplet creation successful!')
else:
    print('Droplet creation failed. Status code:', response.status_code)
    print('Response:', response.text)
