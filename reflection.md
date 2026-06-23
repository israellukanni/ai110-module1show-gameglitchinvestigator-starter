# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
At first the game look simple and didn't seem to have bugs, but once it started there were many bugs to find. The hints did not actually help and actually were backwards. Also the ranges for the different modes were strange, with easy being 1-20, medium being 1-100, and hard being 1-50 it doesn't really make sense why hard would have less options than medium.
- List at least two concrete bugs you noticed at the start  
  - The hints were backwards
  - The attempt counter is off

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|

|  56   |  "Go higher hint" | "Go lower hint" |        "none"          |
|-------|-------------------|-----------------|------------------------|

|  56   |  history : [56]   | history : []    |        "none"          |
|-------|-------------------|-----------------|------------------------|

|  70   |  "Go higher hint" | "Go lower hint" |        "none"          |
|-------|-------------------|-----------------|------------------------|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). The AI was correct when suggesting how to fix the bug with hints. It then correctly fixed the inverted hints. I verified by testing inputs that were higher and lower than the secret number, ensuring that it was giving the right hints.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
The AI was misleading when it decided to try and make the range for hard 1-200 instead of just swapping the ranges of hard(1-50) and normal(1-100). I told it to just swap the ranges and verified by checking the ranges for each mode in the game.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided by verifying with the pytest and then also checking the actual functionality of the game.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I checked to see if it would give me a lower hint for inputing a higher number. For example, with a secret number 23, I inputed 58 to make sure it would give me a lower hint.
- Did AI help you design or understand any tests? How?
AI helped me design my test because instead of having to manually figure exactly which test I had to run, I used AI to generate test based off of the function and features that I needed to test.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit doesn't run like a tradition webapp and wipes the variables each it is ran, recaculating everything. This results in a need for state, because otherwise varibles that require multiple operation over different runs will likely show incorrect values.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
