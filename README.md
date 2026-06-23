# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

The game is a number guessing game where you try to guess a secret number within a set number of attempts. Each guess gives you a hint telling you to go higher or lower, and your score goes up when you win depending on how fast you guessed.

When I first ran it the game looked fine but once I started playing I noticed a lot of things were off. The hints were completely backwards, so if I guessed too high it would tell me to go higher which made it impossible to win. The difficulty ranges also didn't make sense because Hard was 1-50 and Normal was 1-100, so Hard was actually easier. On top of that the scoring had a bug where it was penalizing one extra attempt and guessing Too High on even attempts was somehow giving you points instead of taking them away.

To fix everything I moved all the logic into `logic_utils.py`, swapped the hints so they're correct, fixed the difficulty ranges so they actually get harder, fixed the score formula, and made sure Too High always deducts points. I also used Claude to help generate tests for the functions so I could verify each fix was actually working.

## 📸 Demo Walkthrough

1. Player selects Normal difficulty (range: 1–50, 8 attempts allowed)
2. Player guesses 25, game returns "📉 Go LOWER!" and score drops by 5
3. Player guesses 10, game returns "📈 Go HIGHER!" and score drops by 5
4. Player guesses 18, game returns "📉 Go LOWER!" and score drops by 5
5. Player guesses 14, game returns "📈 Go HIGHER!" and score drops by 5
6. Player guesses 16, game returns "🎉 Correct!" on attempt 5
7. Score updates: 100 - 10×5 = 50 points awarded on top of current score
8. Balloons pop and the game shows "You won! The secret was 16. Final score: 30"

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
============================= test session starts ==============================
platform darwin -- Python 3.13.7, pytest-9.0.3, pluggy-1.6.0
rootdir: /Users/israelolukanni/Desktop/codepath-aiengineering/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collecting ... collected 7 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 14%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 28%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 42%]
tests/test_game_logic.py::test_win_score_uses_actual_attempt_number PASSED [ 57%]
tests/test_game_logic.py::test_too_high_always_deducts_on_even_attempt PASSED [ 71%]
tests/test_game_logic.py::test_parse_guess_rejects_decimal_string PASSED [ 85%]
tests/test_game_logic.py::test_difficulty_ranges_increase_with_difficulty PASSED [100%]

============================== 7 passed in 0.03s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
