set pager=1
ls 
"Get the partition with boot"
"Set root to that partition"
linux vm root=/dev/sda2
"Initiate init image" 
"Boot"
"If error with root : reboot to grub"