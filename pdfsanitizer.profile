############################################
# python3 profile
############################################

# This file was generated using the following command:
# firejail --build python3 pdfsanitizer.py file.pdf out

### basic blacklisting
include /etc/firejail/disable-common.inc
include /etc/firejail/disable-devel.inc
include /etc/firejail/disable-passwdmgr.inc
include /etc/firejail/disable-programs.inc


### home directory whitelisting
whitelist ~/.local/lib/python3.8/site-packages
whitelist ${HOME}/PDFSanitizer/
#include /etc/firejail/whitelist-common.inc


### filesystem

blacklist /var
blacklist /usr/share

### security filters
caps.drop all
nonewprivs
seccomp
seccomp.keep write,read,lseek,brk,stat,openat,fstat,getdents64,close,mmap,ioctl,munmap,mprotect,lstat,pread64,readlink,futex,fcntl,mremap,rt_sigaction,access,getcwd,set_tid_address,prlimit64,getrandom,rt_sigprocmask,getpid,arch_prctl,set_robust_list,sigaltstack,dup,execve,uname,sysinfo,getuid,getgid,geteuid,getegid,gettid
# 39 syscalls total
# Probably you will need to add more syscalls to seccomp.keep. Look for
# seccomp errors in /var/log/syslog or /var/log/audit/audit.log while
# running your sandbox.

### network
net none

### environment
shell none
