# Section 5: The "Unbreakable" Script # 

## Secuirty Robustness Checklist 

For any future automation project, I will: 

1. Enforce virtual environments - never install packages system-wide
2. Mask secrets and environment variables in any printed output or logs. 
3. Store all secrets in `.env` files, never hardcoded, and confirm `.gitignore` excludes them before ever running `git add`.
4. Order exception handling from most specific to most general. 
5. Always use a `finally` block for cleanup steps that must run regardless of success or failure.
6. Replace `print()` with the `logging` module for anything long-running or production-facing, and set the logging level explicitly.
7. Audit resource usage for scripts that process large amounts of data, to catch leaks before they hit production.
8. Never track auto-generated or constantly-growing files in git — add them to `.gitignore` instead.

## Reflection 

Section 3 was solid for most of it. Regex clicked faster than I expected once I sat down with Regex101 and tested patterns before dropping them into code, and the JSON/YAML swap made sense pretty quick too. Where I actually got stuck was Task 5, the dashboard. I could get subprocess to run who (or last) fine and see the raw output was there, but the second I tried cleaning it up with regex and formatting it into a table, the numbers wouldn't line up, garbage stats, fields shifted a column over from where they should've been. Turned out the raw output doesn't split as cleanly as I assumed, extra whitespace and inconsistent spacing between columns were throwing off my regex groups. Eventually I slowed down and just printed the raw output line by line before trying to parse anything, so I could see exactly what I was working with instead of guessing, and once I could see where the whitespace was messing things up, I could fix the pattern to match what was actually there.
