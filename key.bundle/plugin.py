def results(fields, original_query):
  return {
    "title": original_query,
    "run_args": [fields, original_query],
    "html": "<h1 style='font-family: sans-serif; padding: 2em'>{0}</h1>".format('emmmm ...')
  }

def run(fields, original_query):
  import os, pipes
  if original_query == 'key':
    os.system('osascript cvs2keychain.applescript')
  else:
    domain = fields['~domain']
    name = fields['~name']
    os.system('osascript -l JavaScript clipkeychain.applescript {domain} {name}'.format(domain=domain, name=name))

