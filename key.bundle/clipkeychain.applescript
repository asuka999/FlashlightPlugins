function run(argv) {
  const domain = argv[0]
  const name = argv[1]
  const KeyAccess = Application('Keychain Access')
	KeyAccess.activate()

	const SystemEvents = Application("System Events")
	const keychainAccess = SystemEvents.processes["Keychain Access"]
	
	const window = keychainAccess.windows["Keychain Access"]
	window.toolbars[0].groups[0].textFields[0].value = domain
	window.toolbars[0].groups[0].textFields[0].buttons[0].click()

	const rows = [].slice.call(window.splitterGroups[0].scrollAreas[0].outlines[0].rows)
	if (!name) {
		return rows.map(row => row.textFields[0].value())
	}
	
	rows.find(row => new RegExp(name).test(row.textFields[0].value())).select()
	keychainAccess.menuBars[0].menuBarItems["Edit"].menus[0].menuItems["Copy Password to Clipboard"].click()
	
	KeyAccess.quit()
}
