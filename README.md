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
    
Special thanks to @CoolerVoid for helping with the sandboxing part <3

## Security Considerations

This script will render possibly malicious PDFs to generate the sanitized file using MuPDF, which has had exploits in the past:
https://www.cvedetails.com/vulnerability-list/vendor_id-10846/product_id-20840/Artifex-Mupdf.html
Therefore, assume the machine this runs on will be pwned eventually.
  
To mitigate this risk, I recommend two techinques:

### Running the script on a Sandbox

#### Firejail

This sandbox will restrict all network access, unnecessary syscalls and reading/writing from unexpected files/folders. I recommend this method.

Install it using:

    sudo apt-get install firejail

The profile is already included in this repo, but it assumes you're running from ~/PDFSanitizer. Setup and use it by running the following commands:

    cd ~
    git clone https://github.com/lacioffi/PDFSanitizer
    cd ~/PDFSanitizer/ 
    firejail --profile=pdfsanitizer.profile python3 ~/PDFSanitizer/pdfsanitizer.py file.pdf ~/PDFSanitizer/out

Plase note that the input file must be located in ~/PDFSanitizer.
The output folder can have any name, but it must already exist and also be inside ~/PDFSanitizer.

If you want to run PDFSanitizer from another folder, change the following line in "pdfsanitizer.profile":

    whitelist ${HOME}/PDFSanitizer/
    
To wherever you're running the program from.
   

If you want the output folder or the input file to be outside of PDFSanitizer's folder, simply add a line in "pdfsanitizer.profile":
    
    whitelist /full/path/to/output/folder
    whitelist /full/path/to/file.pdf
    
Again, please note that the output folder must already exist.
 

#### CloudFlare Sandbox

This sandbox will restrict all network access and unnecessary syscalls, but will not restrict reading/writing to arbitrary files/folders.

Download and build it from here: https://github.com/cloudflare/sandbox
Take the generated "libsandbox.so" file, put it in this PDFSanitizer's folder and run the following command:

    LD_PRELOAD=./libsandbox.so SECCOMP_SYSCALL_ALLOW="read:write:lseek:close:openat:brk:stat:munmap:fstat:getdents64:ioctl:rt_sigaction:mmap:mprotect:pread64:lstat:dup:mremap:futex:getegid:getuid:getgid:geteuid:sigaltstack:rt_sigprocmask:access:uname:fcntl:getcwd:readlink:sysinfo:arch_prctl:gettid:set_tid_address:set_robust_list:prlimit64:getrandom:exit_group" python3 pdfsanitizer.py file.pdf ./output


### Running the script on an isolated environment

For maximum security, run this script on an isolated, ephemeral instance or even a serverless environment. 
Block all network communications, maybe kill the instance after the job is done, and only allow reading from an input folder/bucket
and writing to an output folder/bucket.

I didn't try this method, but I believe you can do it with some Cloud Majyks.

## To-do
This method removes EVERYTHING from the PDF. It would be nice to at least keep the text copy-pasteable.
