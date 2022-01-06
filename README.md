# PDFSanitizer
Renders possibly malicious PDF files and outputs harmless PDF files

To do this, the PDF files are rendered and converted to images using PyMuPDF.
The images are then saved to a new PDF file using img2pdf. This ensures no visual data is lost,
but any scripts/external references/flash files are removed.

<b>Instalation</b>: pip install -r requirements.txt <br>
<b>Usage</b>: pdfsanitizer.py \<filename> \<output folder>

This project uses the following libraries:
    
    PyMuPDF - By Jorj X. McKie (@JorjMcKie)
    
    img2pdf - By Johannes Schauer Marin Rodrigues (josch@mister-muffin.de)

### Security Considerations

This script will render possibly malicious PDFs to generate the sanitized file using MuPDF, which has had exploits in the past: <br>
    https://www.cvedetails.com/vulnerability-list/vendor_id-10846/product_id-20840/Artifex-Mupdf.html 
<br>
Therefore, assume the machine this runs on will be pwned eventually. 
  
To mitigate this risk you can use CloudFlare's sandbox to filter the system calls this program can make.
Download and build it from here: https://github.com/cloudflare/sandbox
Take the generated "libsandbox.so" file, put it in this folder and run the following command:

    LD_PRELOAD=./libsandbox.so SECCOMP_SYSCALL_ALLOW="read:write:lseek:close:openat:brk:stat:munmap:fstat:getdents64:ioctl:rt_sigaction:mmap:mprotect:pread64:lstat:dup:mremap:futex:getegid:getuid:getgid:geteuid:sigaltstack:rt_sigprocmask:access:uname:fcntl:getcwd:readlink:sysinfo:arch_prctl:gettid:set_tid_address:set_robust_list:prlimit64:getrandom:exit_group" python3 pdfsanitizer.py file.pdf ./outFolder
    

Another (possibly safer) option would be to run this script in an ephemeral instance, 
reading the input and writing the output to external buckets or similar.

### To-do
This method removes EVERYTHING from the PDF. It would be nice to at least keep the text copy-pasteable.
