import pytest
from project import play_game

def test_play_game():
    mock_weights = [0.5, -0.5, 0.3, 0.1]
    size = 1
    speed = 0
    habitat = 1
    result = play_game(mock_weights, size, speed, habitat)
    assert result in ["Tiger", "Rabbit", "Fish", "Turtle"]
