timedatectl set-ntp true
lsblk
cfdisk /dev/sda
# Select gpt
#sda1 - 500M - FAT32 EFI
#sda2 - 18.5G - ext4
#sda3 - 1G - swap -> Write
mkswap /dev/sda3
swapon /dev/sda3
mkfs.ext4 /dev/sda2
mkfs.fat -F32 /dev/sda1
mount /dev/sda2 /mnt
mkdir /mnt/boot
mount /dev/sda1 /mnt/boot
pacstrap /mnt base linux linux-firmware
genfstab -U /mnt >> /mnt/etc/fstab
arch-chroot /mnt
ln -sf /usr/share/zoneinfo/Region/City /etc/localtime