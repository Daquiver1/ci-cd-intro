"""Test file."""
import sys
sys.path.append("src")
from main import main


def test_main() -> None:
    assert main() == "Hello, World!"
