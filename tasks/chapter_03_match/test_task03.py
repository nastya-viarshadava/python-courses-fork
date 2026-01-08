import pytest
from tasks.chapter_03_match.task03 import process_command


def test_move():
    assert process_command(("move", 10, 20)) == "Moving to (10, 20)", "Move command should return 'Moving to (10, 20)'"


def test_draw_circle():
    assert process_command(("draw", "circle", 5)) == "Drawing circle with radius 5", "Draw circle command should return 'Drawing circle with radius 5'"


def test_draw_rectangle():
    assert process_command(("draw", "rectangle", 10, 20)) == "Drawing rectangle 10x20", "Draw rectangle command should return 'Drawing rectangle 10x20'"


def test_unknown():
    assert process_command(("unknown", 1)) == "Unknown command", "Unknown command should return 'Unknown command'"
    assert process_command(("draw", "square", 5)) == "Unknown command", "Unknown draw shape should return 'Unknown command'"