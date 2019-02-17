
-- getting safari version
set SAFARI_V to get version of application "Safari"



-- select the csv to import to iCloud keychain
set theFile to (choose file with prompt "Select the CSV file")

-- read csv file
set f to read theFile

-- split lines into records
set recs to paragraphs of f

-- open safari passwords screen, check it is unlocked, do not allow to proceed until it is unlocked or user clicks cancel.
tell application "Safari"
	activate
end tell

tell application "System Events"
	tell application process "Safari"
		set frontmost to true
		keystroke "," using command down
		tell window 1
			click button "Passwords" of toolbar 1 of it
			repeat until (exists button "Add" of group 1 of group 1 of it)
				if name is not "Passwords" then
					exit repeat
				end if
			end repeat
			set AppleScript's text item delimiters to ","
			repeat with i from 1 to length of recs
				if name is not "Passwords" then
					exit repeat
				end if
				set currentitem to (item i of recs)
				if (count of currentitem) is not equal to 0 then
					set kcURL to text item 1 of currentitem
					set kcUsername to text item 3 of currentitem
					set kcPassword to text item 4 of currentitem
					click button "Add" of group 1 of group 1 of it
					if (SAFARI_V < 11) then
						tell last row of table 1 of scroll area of group 1 of group 1 of it
							set value of text field 1 of it to kcURL
							keystroke tab
							set value of text field 2 of it to kcUsername
							keystroke tab
							set value of text field 3 of it to kcPassword
							keystroke return
						end tell
					else
						tell sheet 1 of it
							set value of text field 1 of it to kcURL
							keystroke tab
							set value of text field 2 of it to kcUsername
							keystroke tab
							set value of text field 3 of it to kcPassword
							keystroke tab
							click UI element "Add Password"
						end tell
					end if
				end if
			end repeat
			
		end tell
	end tell
end tell

tell application "Safari"
	quit
end tell
