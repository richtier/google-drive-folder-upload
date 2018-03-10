Google Drive Folder Upload
==========================

**Python Client for uploading files to Google Drive**

--------------

Installation
------------

.. code:: sh
    
    git clone git@github.com:richtier/google-drive-folder-upload.git
    cd google-drive-folder-upload

.. code:: py
    
    pip install requirements.txt


Authentication
--------------

Login to https://console.developers.google.com and generate an Oauth client id file. Set the "Authorized redirect URIs" to http://localhost:8080/

Then download the credentials file and save it under `config/client_secrets.json`.

You will be prompted to authenticate the application the first time you run the script.


Usage
-----

Upload single file
~~~~~~~~~~~~~~~~~~
Run the following code to upload a file to to Google Drive:

.. code:: sh

    python google_drive_folder_upload/main.py /path/to/file.png



Upload new files in a directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`inotifywait <https://github.com/rvoicilas/inotify-tools/wiki>`_ can be used to monitor a folder for new files and upload them to Google Drive. Run the following command to do that:


.. code:: sh

    sudo chmod +x monitor.sh
    monitor.sh /path/to/folder

Follow `this tutorial <http://www.diegoacuna.me/how-to-run-a-script-as-a-service-in-raspberry-pi-raspbian-jessie/>`_ to run the monitor.sh as a service.

