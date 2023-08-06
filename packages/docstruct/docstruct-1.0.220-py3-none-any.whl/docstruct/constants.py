"""Constants for the docstruct package.

The delimiter between pages / paragraphs / lines / words  
is represented by the `PAGE_DELIMITER` / `PARAGRAPH_DELIMITER` /  `LINE_DELIMITER`  / `WORD_DELIMITER` constant.
"""

PAGE_DELIMITER = "\f"
PARAGRAPH_DELIMITER = "\v"
LINE_DELIMITER = "\n"
WORD_DELIMITER = " "
AREA_DELIMITER = "\t"
CELL_DELIMITER = "\n"
COLUMN_DELIMITER = "\n"

DELIMITERS = {
    "PAGE": PAGE_DELIMITER,
    "PARAGRAPH": PARAGRAPH_DELIMITER,
    "LINE": LINE_DELIMITER,
    "WORD": WORD_DELIMITER,
    "AREA": AREA_DELIMITER,
    "CELL": CELL_DELIMITER,
    "COLUMN": COLUMN_DELIMITER,
}


PAGE = "PAGE"
LINE = "LINE"
WORD = "WORD"

BBOX_PATTERN = "\s*bbox\s+([0-9]+)\s+([0-9]+)\s+([0-9]+)\s+([0-9]+)"

# The factor of which we'll multiply the paragraph bounding box when looking for intersections with other paragraphs.
PARAGRAPH_VERTICAL_SCALE = 1.1
PARAGRAPH_HORIZONTAL_SCALE = 1
PARAGRAPH_HORIZONTAL_SCALE_FOR_LINES = 100
PARAGRAPH_VERTICAL_SCALE_FOR_LINES = 0.5

THIN_CHARS = {".", ",", ":", ";", "!"}
CHARACTER_WIDTH_MAP = {"lower": 1, "upper": 1.2, "thin": 0.5, "default": 1}
