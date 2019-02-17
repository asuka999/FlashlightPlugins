def results(fields, original_query):
  import commands
  wifi = commands.getoutput("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | awk '/ SSID/ {print substr($0, index($0, $2))}'")
  ovpn = commands.getoutput("osascript ovpn.applescript")
  socks = commands.getoutput("""scutil --proxy | awk 'BEGIN {ORS=";"} {print}' |  awk '{ if (match($0, /SOCKSEnabled : 1/)) { split($0, kvs, ";"); domain=""; port=""; for (i in kvs) {kv = kvs[i]; if (match(kv, /SOCKSProxyServer : /)) domain = substr(kv, index(kv, ":") + 2); if (match(kv, /Port:/)) port = substr(kv, index(kv, ":") + 2); }; print sprintf("socks://%s:%s", domain, port); } else if (match($0, /ProxyAutoConfigEnable : 1/)) { print "auto configure"; } else { print "off"; }}'""")
  ip = commands.getoutput("ifconfig en0 | head -3 | grep 'inet ' | cut -d' ' -f 2")
  battery = commands.getoutput("pmset -g batt | awk '/%/ {print $3, $4}'")
  bluetooth = commands.getoutput("""system_profiler SPBluetoothDataType |awk '/Devices/,/^ {6}Services:/' | awk '/ {10}/ {print match($0, /^ {10}[^ ]+/) ? ";"$0 : $0;}' | awk 'BEGIN{RS=";";FS="\\n"} /Connected: Yes/ {gsub(" ", "", $1); gsub(":", "", $1); print $1}'""")
  return {
    "title": "toggle {}".format(original_query) if original_query != 'status' else 'status...',
    "run_args": [original_query, ip],
    "webview_transparent_background": True,
    "html": open("index.html").read().decode('utf-8').encode('utf-8').format(
      bluetooth=bluetooth,
      wifi=wifi,
      ovpn=ovpn,
      socks=socks,
      ip=ip,
      battery=battery
      # volume=volume,
      )
  }

def run(command, ip):
  import commands
  if command == 'wifi':
    commands.getoutput("(networksetup -getairportpower en0 | grep 'On') && (networksetup -setairportpower en0 off) || (networksetup -setairportpower en0 on)")
  if command == 'bluetooth':
    commands.getoutput("osascript toggle_bluetooth.applescript")
  if command == 'ovpn':
    commands.getoutput("osascript toggle_ovpn.applescript")
  if command == 'socks':
    commands.getoutput("osascript toggle_socks.applescript")
  if command == 'ip':
    import subprocess
    subprocess.call(['printf "'+ip+'" | LANG=en_US.UTF-8  pbcopy && osascript -e \'display notification "Copied!" with title "Flashlight"\''], shell=True)

