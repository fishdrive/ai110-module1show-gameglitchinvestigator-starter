from logic_utils import check_guess, get_temperature_indicator


def test_check_guess_returns_outcome_and_message():
    result = check_guess(50, 50)

    assert result == ("Win", "🎉 Correct!")


def test_check_guess_handles_integer_guess_and_string_secret():
    result = check_guess(50, "50")

    assert result == ("Win", "🎉 Correct!")


def test_check_guess_gives_lower_hint_for_high_guess():
    result = check_guess(60, "50")

    assert result == ("Too High", "📉 Go LOWER!")


def test_check_guess_compares_string_secret_numerically():
    result = check_guess(9, "10")

    assert result == ("Too Low", "📈 Go HIGHER!")


def test_temperature_indicator_boundaries():
    assert get_temperature_indicator(0, 50) == "🧊🧊"
    assert get_temperature_indicator(25, 50) == "🧊"
    assert get_temperature_indicator(37, 50) == "🔥"
    assert get_temperature_indicator(38, 50) == "🔥🔥"
