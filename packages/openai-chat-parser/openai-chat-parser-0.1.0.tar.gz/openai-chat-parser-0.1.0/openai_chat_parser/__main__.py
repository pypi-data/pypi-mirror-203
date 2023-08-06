#!/usr/bin/env python3
"""
openai_chat_parser

A script to download, extract, and parse OpenAI chat conversation archives.
The script takes a ZIP URL as input and processes the conversations, organizing them
into separate folders with appropriate file formats based on the conversation content.
"""
import json
import os
import re
import zipfile
import urllib.request
from datetime import datetime
from slugify import slugify

config_file_path = os.path.join(os.path.dirname(__file__), 'config.json')

with open(config_file_path) as f:
    config = json.load(f)

chats_home = os.path.expanduser(config["chats_home"])
downloads_folder = config["downloads_folder"]
archive_folder = config["archive_folder"]
conversations_folder = config["conversations_folder"]
zip_download_retries = config["zip_download_retries"]
retry_wait_time_seconds = config["retry_wait_time_seconds"]


def parse_conversation(export_path, conv_num, conversation):
    """
    Parse a conversation and save its content into separate files.

    :param export_path: The folder where parsed conversations should be saved.
    :param conv_num: The conversation number.
    :param conversation: The conversation data as a dictionary.
    """
    title = conversation["title"]
    messages = []
    for node_id, node in conversation['mapping'].items():
        if node['message'] is not None:
            role = node['message']['author']['role']
            content = node['message']['content']['parts'][0]
            messages.append((role, content))

    folder_slug = slugify(title)
    folder_path = f"{export_path}/{conv_num:03}-{folder_slug}"
    os.makedirs(folder_path, exist_ok=True)

    # Save the conversation node as a JSON dump
    with open(os.path.join(folder_path, f'000-original.json'), 'w') as f:
        json.dump(conversation, f, indent=2)

    for i, (role, content) in enumerate(messages):
        i += 1
        with open(os.path.join(folder_path, f'{i:03}-{role}.md'), 'w') as f:
            f.write(content)

        code_blocks = re.findall(r'```(.*?)\n(.*?)```', content, re.DOTALL)

        for j, (code_type, code_block) in enumerate(code_blocks):
            if code_type == 'python':
                extension = '.py'
            elif code_type == 'bash':
                extension = '.sh'
            elif code_type == 'html':
                extension = '.html'
            elif code_type == 'css':
                extension = '.css'
            elif code_type == 'rst':
                extension = '.rst'
            else:
                extension = '.txt'  # Default file extension for unknown code types

            if code_block.strip() == '' and content.endswith('```'):
                content = content.rstrip('`')
                code_block = content.split('```')[-1]

            with open(os.path.join(folder_path, f'{i:03}-{role}_code_{j}{extension}'), 'w') as f:
                f.write(code_block.strip())

    with open(os.path.join(folder_path, '000-full_transcript.md'), 'w') as f:
        for i, (role, content) in enumerate(messages):
            f.write(f"**{role.capitalize()}**\n\n")
            f.write(f"{content}\n\n")


def unzip_and_parse_conversations(zip_file_path, archive_path):
    """
    Unzip and parse the conversations from the ZIP file.

    The function extracts the contents of the ZIP file, reads the
    'conversations.json' file, reverses the conversations order, and then calls
    the `parse_conversation` function for each conversation to parse and save
    its content.

    :param zip_file_path: The file path of the ZIP file containing the conversations.
    """
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        file_name = zip_file_path.replace(".zip", "")
        userid, timestamp = file_name.split('-', 1)
        
        conversation_path = os.path.join(archive_path, timestamp)
        os.makedirs(conversation_path, exist_ok=True)
        zip_file.extractall(conversation_path)

        with open(os.path.join(conversation_path, 'conversations.json')) as f:
            conversations = json.load(f)

        conversations.reverse()

        export_path = os.path.join(conversation_path, "conversations")
        os.makedirs(export_path, exist_ok=True)

        for conv_num, conversation in enumerate(conversations):
            parse_conversation(export_path, conv_num, conversation)


def download_zip(zip_url, destination_path):
    """
    Download a ZIP file from the given URL and save it to the specified destination path.

    :param zip_url: The URL of the ZIP file.
    :param destination_path: The folder where the ZIP file should be saved.
    :return: The file path of the downloaded ZIP file.
    """
    filename = zip_url.split('/')[-1].split('?')[0]
    file_path = os.path.join(destination_path, filename)

    urllib.request.urlretrieve(zip_url, file_path)
    return file_path


def main():
    print("OpenAI Chat Parser")
    print("This script downloads, extracts, and parses OpenAI chat conversation archives.")
    print("It organizes conversations into separate folders with appropriate file formats based on the conversation content.")
    print()

    zip_url = input('Enter the zip URL: ')
    #  destination_path = 'downloads'
    os.makedirs(chats_home, exist_ok=True)
    downloads_path = os.path.join(chats_home, downloads_folder)
    os.makedirs(downloads_path, exist_ok=True)
    downloaded_zip_path = download_zip(zip_url, downloads_path)
    archive_path = os.path.join(chats_home, archive_folder)
    os.makedirs(archive_path, exist_ok=True)
    unzip_and_parse_conversations(downloaded_zip_path, archive_path)

if __name__ == '__main__':
    main()

