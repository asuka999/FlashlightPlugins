on run argv
	tell application "iTunes"
    activate
		set trk to (item 1 of argv)
		if track trk exists then
			play track trk
		end if
	end tell
end run
