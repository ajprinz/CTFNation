import virtualbox
import time

# Create instance
vbox = virtualbox.VirtualBox()

# Create Session
session = virtualbox.Session()

# Find Virtualbox machineby name
vm = vbox.find_machine('Ubuntu')

# Launch virtualbox machine -> variable 'vm'
progress = vm.launch_vm_process(session, "gui", [])
progress.wait_for_completion()
time.sleep(60)

# Find and execute needed scripts
guest_session = session.console.guest.create_session("root", "ctfnation.com")
guest_session.directory_exists("/ctfnation")
proc, stdout, stderr = guest_session.execute("/ctfnation/spawn.py")
print(stdout)

# Get the IP Address
res = vm.enumerate_guest_properties('/VirtualBox/GuestInfo/Net/0/V4/IP')
ip = res[1][0]
print(ip)
