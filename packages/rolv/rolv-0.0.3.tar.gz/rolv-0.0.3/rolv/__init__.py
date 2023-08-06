from . import rc, executables, package


def help_text():

    print(f"""
                  dP          
                  88          
88d888b. .d8888b. 88 dP   .dP 
88'  `88 88'  `88 88 88   d8' 
88       88.  .88 88 88 .88'  
dP       `88888P' dP 8888P'   v{package.get_version()}            
""")
    print("\"\"\"A simple tool to synchronize all my \nquality of life scripts between servers.\"\"\"\n")
    print("rolv.install    - install/update executables, aliases, etc")
    print("rolv.version    - get version of package")
    print("rolv.disclaimer - get a short list of things you need to know before using this package")
    print("\n")

def disclaimer():
    print("""
8888888b.  d8b                   888          d8b                                         
888  "Y88b Y8P                   888          Y8P                                         
888    888                       888                                                      
888    888 888 .d8888b   .d8888b 888  8888b.  888 88888b.d88b.   .d88b.  888d888 .d8888b  
888    888 888 88K      d88P"    888     "88b 888 888 "888 "88b d8P  Y8b 888P"   88K      
888    888 888 "Y8888b. 888      888 .d888888 888 888  888  888 88888888 888     "Y8888b. 
888  .d88P 888      X88 Y88b.    888 888  888 888 888  888  888 Y8b.     888          X88 
8888888P"  888  88888P'  "Y8888P 888 "Y888888 888 888  888  888  "Y8888  888      88888P' 

This package is written by me, for me. Best not to use this package at all if you are not me.

Will add/update the  ` # <rolv config> ... # </rolv config> `  block in any rc it can find.
  * Unless the ROLV_RC_FILE_PATH environment variable is set.
  
Will delete any file under  ` $HOME/.local/bin `  that starts with  ` __rolv_ `  .   
    """)

def version():
    print(package.get_version())


def install():
    print("\n")
    rc.set_rc_files()
    executables.sync_executables()

    print("\nTo make sure the ENV is up to date, be sure to open a new terminal window, or run (one of) the following command(s):")
    for path in rc.get_rc_file_paths():
        print(f"  source {path.as_posix()}")
    print("\nDone.")
    print("\n")
