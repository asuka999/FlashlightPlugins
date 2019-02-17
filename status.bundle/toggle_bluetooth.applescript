tell application "System Preferences"
  activate
	reveal pane "com.apple.preferences.Bluetooth"
end tell
tell application "System Events" to tell process "System Preferences"
	repeat until exists window "Bluetooth"
	end repeat
	try
		click button "Turn Bluetooth Off" of window "Bluetooth"
	on error
		click button "Turn Bluetooth On" of window "Bluetooth"
	end try
end tell
tell application "System Preferences" to quit
