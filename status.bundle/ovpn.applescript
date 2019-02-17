tell application "Tunnelblick"
	set result to the name of every configuration whose state is "CONNECTED"
	if (count of result) is not equal to 0 then
		get item 1 of result
	end if
end tell
