.. image:: https://raw.githubusercontent.com/PtPrashantTripathi/markdown-server/master/markdownserver-logo.webp
   :alt: "Markdown Server Logo"
   :width: 300px
   :align: center

===============
Markdown Server
===============

Markdown-server is a simple web application.
It converts markdown files to HTML and responds with `text/html`.

How to use
==========

--------------------
Runtime Environment
--------------------

:Python:        3.7
:pip:           19.1.1


--------------------
Library Dependencies
--------------------

See `requirements.txt`.

--------
Just try
--------

Start server
------------

You can install `markdown-server` from **PyPi** or run it directly from the repository.

### Install from PyPi:
::

    (.venv)$ pip install markdown-server
    (.venv)$ markdownserver --host localhost --port 8009 --debug

    Bottle v0.12.8 server starting up (using WSGIRefServer())...
    Listening on http://localhost:8009/

### Install from GitHub:
::

    $ git clone https://github.com/ohbarye/markdown-server
    $ cd markdown-server
    $ virtualenv .venv
    $ source .venv/bin/activate
    (.venv)$ pip install -r requirements.txt
    (.venv)$ markdownserver --host localhost --port 8009 --debug
        Bottle v0.12.8 server starting up (using WSGIRefServer())...
        Listening on http://localhost:8009/

If the server starts up successfully, browse the below URL and check the converted result.

::

    $ open http://localhost:8009/sample.md

MarkdownServer CLI
------------------

You can run the `markdownserver` command to start the server with the following examples:

### Example 1: Using Default Arguments
::

    (.venv)$ markdownserver

This will run the server on the default host (`localhost`) and port (`8009`), with debugging disabled.

### Example 2: Custom Host, Port, and Debug
::

    (.venv)$ markdownserver --host 0.0.0.0 --port 8080 --debug

This will run the server on `0.0.0.0:8080` with debugging enabled, allowing you to access the server from any device on your local network.

**Arguments:**
- `--host`: Specify the host to run the server on (default is `localhost`).
- `--port`: Specify the port to run the server on (default is `8009`).
- `--debug`: Enable or disable debugging mode (default is `False`).

Only Conversion
---------------

Additionally, you can use the conversion function alone from the command line.

::

    (.venv)$ markdownconvert source_md_file target_html_file

This will convert the provided markdown file (`source_md_file`) into an HTML file (`target_html_file`).

MarkdownConverter CLI
---------------------

The `markdownconvert` command can be used with the following options:

::

    $ markdownconvert source_md_file target_html_file

**Arguments:**
- `source_md_file`: The markdown file you want to convert to HTML.
- `target_html_file`: The output HTML file to save the converted content.

Example:

::

    $ markdownconvert sample.md sample.md.html

This will convert the `sample.md` file into a `sample.md.html` file in the current directory.

--------------
Do as you like
--------------

- The Markdown server provides `http://host/[file_name]` URL. You can place any markdown file here.

- The converted HTML file will be placed in the `resources/html` directory. The generated HTML file includes CSS for easy distribution.

Developers Information
======================

1. **Masato Ohba**
   - GitHub: `@ohbarye <https://github.com/ohbarye>`
   .. image:: https://avatars.githubusercontent.com/u/1811616
      :alt: "Masato Ohba"
      :width: 200px

2. **Pt. Prashant Tripathi**
   - GitHub: `@ptprashanttripathi <https://github.com/ptprashanttripathi>`
   .. image:: https://avatars.githubusercontent.com/u/26687933
      :alt: "Pt. Prashant Tripathi"
      :width: 200px


