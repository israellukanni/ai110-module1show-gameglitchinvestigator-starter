from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# Bug fix: win formula was 100 - 10 * (attempt_number + 1), penalising one extra attempt.
# A first-attempt win should award 90 points (100 - 10*1), not 80 (100 - 10*2).
def test_win_score_uses_actual_attempt_number():
    score = update_score(0, "Win", attempt_number=1)
    assert score == 90, f"Expected 90, got {score}"


# Bug fix: "Too High" on an even attempt_number was awarding +5 instead of deducting 5.
def test_too_high_always_deducts_on_even_attempt():
    score = update_score(50, "Too High", attempt_number=2)
    assert score == 45, f"Expected 45, got {score}"


# Bug fix: int(float("3.7")) silently truncated "3.7" to 3 instead of rejecting it.
# parse_guess must reject non-integer decimals as invalid input.
def test_parse_guess_rejects_decimal_string():
    ok, value, err = parse_guess("3.7")
    assert not ok, "Expected parse_guess to reject a decimal string"
    assert value is None
    assert err is not None


# Bug fix: Hard returned (1, 50) and Normal returned (1, 100), making Hard easier than Normal.
# Correct order: Easy 1-20, Normal 1-50, Hard 1-100.
def test_difficulty_ranges_increase_with_difficulty():
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert easy_high < normal_high < hard_high, (
        f"Expected Easy({easy_high}) < Normal({normal_high}) < Hard({hard_high})"
    )
