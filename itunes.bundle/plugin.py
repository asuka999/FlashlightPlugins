def results(fields, original_query):
  if '~song' in fields:
    song = fields['~song']
    return {
      'title': 'Play "{0}"'.format(song),
      'run_args': [song],
    }
  else:
    return {
      'title': 'toggle itunes',
      'run_args': [''],
    }

def run(song):
  import os, pipes
  if song == '':
    os.system('osascript toggle_itunes.applescript')
  else:
    os.system('osascript play_song.applescript "{}"'.format(song.encode('utf8')))
