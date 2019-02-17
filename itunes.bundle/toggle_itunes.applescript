tell application "iTunes"
	run
	if (player state) is playing then
		set expect to paused
	else
		set expect to playing
	end if
	log expect
	repeat while (expect is not (player state))
		playpause
	end repeat
end tell
