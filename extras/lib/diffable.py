from nbconvert.preprocessors import Preprocessor
from nbformat import NotebookNode


def is_system_command(source: str):
    return source.startswith("!")


def is_ipytest(source: str):
    return source.startswith("%%ipytest")


def has_html(output):
    return "text/html" in output.get("data", {})


def has_html_output(cell: NotebookNode):
    return any(has_html(output) for output in cell["outputs"])


def contains_memory_address(text: str):
    return text.startswith("<") and text.endswith(">")


def has_memory_address(cell: NotebookNode):
    return any(
        contains_memory_address(output.get("data", {}).get("text/plain", ""))
        for output in cell["outputs"]
    )


def should_clear_output(cell: NotebookNode):
    """Ignore any system command and ipytest output, since things like package paths shown in warnings/errors can change between different systems. Also clear HTML output, since it often has generated IDs (from displacy, plotly, etc.) that change with each execution."""
    source = cell["source"]
    return (
        is_system_command(source)
        or is_ipytest(source)
        or has_html_output(cell)
        or has_memory_address(cell)
    )


# based off of
# https://github.com/jupyter/nbconvert/blob/master/nbconvert/preprocessors/tagremove.py
class Diffable(Preprocessor):
    def preprocess_cell(self, cell: NotebookNode, resources, cell_index):
        if cell["cell_type"] != "code":
            return cell, resources

        if should_clear_output(cell):
            cell["outputs"] = []

        # filter out warnings
        cell["outputs"] = [
            output for output in cell["outputs"] if output.get("name", None) != "stderr"
        ]

        return cell, resources
