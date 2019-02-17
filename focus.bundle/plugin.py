
def results(fields, command):
  title = command
  args = None
  content = ''
  if command.startswith('focus'):
    task = fields['~task']
    what = fields['~what'] if '~what' in fields else 'working'
    cost = fields['~time'] if '~time' in fields else '30'
    title = 'start task...'
    content = "<div style='padding: 20px; font-family: Helvetica'><h4>{}</h4><h2><i>{}</i></h2><p>for {}</p><p>expected cost {}</p>".format(title, task, what, cost)
  return {
    "title": title,
    "run_args": [fields, command],
    "html": content,
    "webview_transparent_background": True
  }

def run(fields, command):
  import os
  if command.startswith('focus'):
    task = fields['~task']
    what = fields['~what'] if '~what' in fields else 'working'
    cost = fields['~time'] if '~time' in fields else '30'
    os.system('osascript focus.applescript "{task}" {cost} {what}'.format(task=task.encode('utf8'), cost=cost, what=what))
  if command.startswith('stop'):
    os.system('osascript stop.applescript')
  if command.startswith('pause'):
    os.system('osascript toggle.applescript')
  if command.startswith('continue'):
    os.system('osascript toggle.applescript')
