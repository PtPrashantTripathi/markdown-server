import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
from markdownserver.markdown_converter import MarkdownConverter
from markdownserver.env import ms_host, ms_port, ms_debug


class MarkdownServerHandler(SimpleHTTPRequestHandler):
    """
    Custom HTTP request handler that dynamically converts Markdown (.md) files to HTML
    when accessed via a browser. Non-Markdown files are served as-is.
    """

    def do_GET(self):
        """
        Handle GET requests.
        - If the requested file is a Markdown file, convert it to HTML and serve it.
        - Otherwise, serve the file normally.
        """
        # Get the file path
        filepath = self.translate_path(self.path)

        # Check if the requested file is a Markdown file
        if os.path.isfile(filepath) and filepath.endswith(".md"):
            self.serve_markdown(filepath)
        else:
            super().do_GET()

    def serve_markdown(self, filepath):
        """
        Serve a Markdown file as HTML content.

        Args:
            filepath (str): The path to the Markdown file.
        """
        try:
            # Create an instance of the MarkdownConverter
            converter = MarkdownConverter()

            # Convert the Markdown file to HTML
            html_path = converter.convert(filepath)

            # Read the generated HTML content
            with open(html_path, "r", encoding="utf-8") as html_file:
                html_content = html_file.read()

            # Send the response headers
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()

            # Write the HTML content to the response
            self.wfile.write(html_content.encode("utf-8"))

        except Exception as e:
            self.send_error(500, f"Error processing Markdown file: {e}")


class MarkdownServer:
    """
    A simple HTTP server for serving files, with special handling for Markdown files.
    """

    def __init__(self, host=None, port=None, debug=False):
        """
        Initialize the server.

        Args:
            host (str): Hostname to bind the server to. Default is 'localhost'.
            port (int): Port to bind the server to. Default is 8000.
            debug (bool): Enable/Disable debug mode. Default is False.
        """
        # Use environment variables or defaults for host and port
        self.host = host or ms_host
        self.port = int(port or ms_port)
        self.debug = debug or ms_debug
        self.server_address = (self.host, self.port)
        self.httpd = HTTPServer(self.server_address, MarkdownServerHandler)

    def start(self):
        """
        Start the HTTP server and begin serving requests.
        """
        print(f"Markdown server is running on http://{self.host}:{self.port}")
        self.httpd.serve_forever()

    def stop(self):
        """
        Stop the HTTP server.
        """
        print("Shutting down the server...")
        self.httpd.server_close()


def main():
    """
    Main function to run the server with command-line arguments for host, port, and debug.
    """
    import argparse

    # Setup CLI arguments
    parser = argparse.ArgumentParser(description="Start the markdown HTTP server.")
    parser.add_argument("--host", help="Host to bind the server (default: localhost)")
    parser.add_argument(
        "--port", type=int, help="Port to bind the server (default: 8000)"
    )
    parser.add_argument(
        "--debug", action="store_true", help="Enable debug mode (default: False)"
    )

    args = parser.parse_args()

    # Create an instance of the server with provided or default arguments
    server = MarkdownServer(host=args.host, port=args.port, debug=args.debug)

    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()


if __name__ == "__main__":
    main()
