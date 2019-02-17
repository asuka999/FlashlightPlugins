tell application "Tunnelblick"
	get autoconnect of every configuration
	set result to the name of every configuration whose state is "CONNECTED"
	if (count of result) is not equal to 0 then
		disconnect all
	else
		set target to the name of the first configuration whose autoconnect is not "NO"
		connect target
	end if
end tell