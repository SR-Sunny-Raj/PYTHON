target = input("Enter The IP address (separate by ,)")
port   = int(input("Enter The Number of Ports You would like to scan "))
if ',' in target:
    print(termcolor.colored(("[*] Scanning Multiple Targets"),'green'))
    for ip in target.split(','):
        scan(ip.strip(' '),port)
else:
    scan(target,port)
