on run argv
	set task to item 1 of argv
	set cost to (item 2 of argv) as integer
	tell application "Focus"
		focus task for cost
	end tell
  tell application "Reminders"
    set duedate to (current date)
    set minutes of duedate to ((minutes of duedate) + cost)
    set targetlist to list (item 3 of argv)
    tell targetlist
      make new reminder at end with properties {name: task, due date:duedate}
    end tell
  end tell
end run
