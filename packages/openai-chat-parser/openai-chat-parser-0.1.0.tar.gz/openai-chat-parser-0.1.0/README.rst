
OpenAI Chat Parser is a command-line tool that downloads, extracts, and parses OpenAI chat conversation archives. The tool organizes conversations into separate folders with appropriate file formats based on the conversation content.

Installation
------------

You can install the OpenAI Chat Parser package from PyPI using pip:

.. code-block:: bash

   pip install openai-chat-parser

Usage
-----

After installing the package, you can use the `openai-chat-parser` command-line tool to process chat archives. 

To run the OpenAI Chat Parser, execute the following command:

.. code-block:: bash

   openai-chat-parser

The script will prompt you to enter the ZIP URL of the chat archive:

.. code-block:: text

   Enter the zip URL:

Enter the URL and press `Enter`. The tool will download, extract, and parse the chat conversations, organizing them into separate folders.

Configuration
-------------

Before using the OpenAI Chat Parser, you can configure the package by modifying the `config.json` file. This file contains settings like the destination path, archive folder, export folder, and download retries.

Here's an example of the `config.json` file:

.. code-block:: json

   {
      "chats_home": "~/Chats",
      "downloads_folder": "downloads",
      "archive_folder": "archive",
      "conversations_folder": "conversations",
      "zip_download_retries": 3,
      "retry_wait_time_seconds": 5
   }

You can customize the settings in the `config.json` file to suit your needs.

License
-------

This project is licensed under the MIT License.


