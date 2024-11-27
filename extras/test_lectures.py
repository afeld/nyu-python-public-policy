from glob import glob
import re

import pytest

from .lib.nb_helper import get_tags, is_code_cell, read_notebook


lecture_notebooks = glob("lecture_?.ipynb")
lecture_notebooks.sort()


def slide_type(cell):
    return cell.metadata.get("slideshow", {}).get("slide_type")


def is_slide(cell):
    SLIDE_TYPES = ["slide", "subslide"]
    return slide_type(cell) in SLIDE_TYPES


def num_slides(cells):
    """Return a weighted number of slides"""

    slides = [cell for cell in cells if is_slide(cell)]
    count = len(slides)

    has_intro = any("# Introductions" in slide.source for slide in slides)
    if has_intro:
        count += 5

    num_exercises = sum(
        1 for slide in slides if re.match("#.+exercise", slide.source, re.IGNORECASE)
    )
    # let's say that each exercise is worth ten slides
    count += num_exercises * 10

    return count


def num_slides_without_tag(cells, tag):
    tagged_cells = [cell for cell in cells if tag not in get_tags(cell)]
    return num_slides(tagged_cells)


@pytest.mark.parametrize("file", lecture_notebooks)
def test_num_slides(file):
    """Ensure there are a reasonable number of slides for each school"""

    notebook = read_notebook(file)

    if file == "lecture_1.ipynb":
        pytest.xfail("Known issue that these lectures have too many slides")
    if file == "lecture_6.ipynb":
        pytest.xfail("The various pieces of the lecture can be scaled appropriately")

    num_columbia = num_slides_without_tag(notebook.cells, "nyu-only")
    assert num_columbia >= 42, "Too few slides for Columbia"
    assert num_columbia <= 63, "Too many slides for Columbia"

    num_nyu = num_slides_without_tag(notebook.cells, "columbia-only")
    assert num_nyu >= 39, "Too few slides for NYU"
    assert num_nyu <= 51, "Too many slides for NYU"

    assert (
        num_nyu <= num_columbia
    ), "NYU should have fewer slides than Columbia, since the class sessions are shorter"


@pytest.mark.parametrize("file", lecture_notebooks)
def test_attendance_reminder(file):
    notebook = read_notebook(file)

    start_cells = notebook.cells[:3]
    assert any("attendance" in cell.source for cell in start_cells)


@pytest.mark.parametrize("file", lecture_notebooks)
def test_hidden_imports(file):
    if file == "lecture_1.ipynb":
        pytest.skip("Introducing pandas")

    notebook = read_notebook(file)

    for cell in notebook.cells:
        if is_code_cell(cell):
            lines = cell.source.splitlines()

            imports_only = all(line.startswith("import ") for line in lines)
            if imports_only:
                assert slide_type(cell) == "skip", f"imports should be hidden:\n\n{cell.source}\n"
