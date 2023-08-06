"""
If this suite of tests is not run as a module, need to run the following additional code: 
# add the root project directory to the system path:
>>> import sys
>>> import pathlib
>>> parent_dir_path = pathlib.Path(__file__).parent.parent
>>> sys.path.append(str(parent_dir_path))
>>> sys.path.append(f"{str(parent_dir_path)}/joes_giant_toolbox/")
"""

# import the function to be tested:
from joes_giant_toolbox.longest_sentence_subsequence_plagiarism_detector import (
    longest_sentence_subsequence_plagiarism_detector,
)

# run the tests:
def test_known_output_example():
    result = longest_sentence_subsequence_plagiarism_detector(
        doc1_str="cd efg opq rs ab cd efg az by opq rs tu vw xy af gq errty h ijk l mn a b c d e",
        doc2_str="ab cd efg h ijk l mn opq rs tu vw xy z",
        min_seq_len=3,
    )
    assert result == [
        "opq rs tu vw xy",
        "h ijk l mn",
        "ab cd efg",
    ], f"unexpected result on known example: expected=['opq rs tu vw xy','h ijk l mn','ab cd efg'] but received={result}"
