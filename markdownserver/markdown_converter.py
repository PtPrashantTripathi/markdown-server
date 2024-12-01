import sys
import os
import markdown as md
import codecs
import argparse
from .env import css_path, ms_encoding, markdown_type, html_dir, html_extension


class MarkdownConverter:
    def __init__(self):
        """Initialize the converter with the CSS header and footer."""
        css = codecs.open(css_path, encoding=ms_encoding, mode="r")
        self.html_header = (
            """
            <html>
            <head>
            <style type='text/css'>
            <!--
            """
            + css.read()
            + """
            //-->
            </style>
            </head>
            <body>
            <div class='markdown-body'>
            """
        )
        self.html_footer = """
            </div>
            </body>
            </html>
            """

    def convert(self, src, dst=""):
        """Convert a Markdown file to HTML."""
        code = md.markdown(self.read_md(src), extensions=[markdown_type])
        return self.write_html(code, src, dst)

    def read_md(self, file_name):
        """Read the contents of a Markdown file."""
        workingdir = os.getcwd()
        md_file = codecs.open(
            os.path.join(workingdir, file_name), encoding=ms_encoding, mode="r"
        )
        return md_file.read()

    def write_html(self, body, file_name, dst):
        """Write HTML content to a file."""
        html_path = os.path.join(html_dir, file_name + html_extension)
        if dst != "":
            html_path = dst
        try:
            os.makedirs("/".join(html_path.replace("\\", "/").split("/")[:-1]))
        except OSError:
            pass

        html_file = codecs.open(html_path, encoding=ms_encoding, mode="w")
        html_file.write(self.html_header + body + self.html_footer)
        return html_path


def main():
    """CLI entry point to convert a Markdown file to HTML using argparse."""
    parser = argparse.ArgumentParser(
        description="Convert a Markdown file to an HTML file with styling."
    )
    parser.add_argument(
        "source_md_file",
        metavar="SOURCE_MD_FILE",
        help="The source Markdown file to convert",
    )
    parser.add_argument(
        "target_html_file",
        metavar="TARGET_HTML_FILE",
        help="The destination HTML file to save",
    )

    args = parser.parse_args()

    # Convert the given Markdown file to HTML
    converter = MarkdownConverter()
    html_path = converter.convert(args.source_md_file, args.target_html_file)
    print(
        f"Markdown file '{args.source_md_file}' converted to HTML and saved as '{html_path}'"
    )


if __name__ == "__main__":
    main()
