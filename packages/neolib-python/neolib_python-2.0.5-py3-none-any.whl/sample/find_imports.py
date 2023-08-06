import os
import re
list_python_lib = ['string','re','difflib','textwrap','unicodedata','stringprep','readline','rlcompleter','struct','codecs','datetime','zoneinfo','calendar','collections','collections.abc','heapq','bisect','array','weakref','types','copy','pprint','reprlib','enum','graphlib','numbers','math','cmath','decimal','fractions','random','statistics','itertools','functools','operator','pathlib','os.path','fileinput','stat','filecmp','tempfile','glob','fnmatch','linecache','shutil','pickle','copyreg','shelve','marshal','dbm','sqlite3','zlib','gzip','bz2','lzma','zipfile','tarfile','csv','configparser','tomllib','netrc','plistlib','hashlib','hmac','secrets','os','io','time','argparse','getopt','logging','logging.config','logging.handlers','getpass','curses','curses.textpad','curses.ascii','curses.panel','platform','errno','ctypes','threading','multiprocessing','multiprocessing.shared_memory','concurrent.futures','subprocess','sched','queue','contextvars','_thread','asyncio','socket','ssl','select','selectors','signal','mmap','email','json','mailbox','mimetypes','base64','binascii','quopri','html','html.parser','html.entities','xml.etree.ElementTree','xml.dom','xml.dom.minidom','xml.dom.pulldom','xml.sax','xml.sax.handler','xml.sax.saxutils','xml.sax.xmlreader','xml.parsers.expat','webbrowser','wsgiref','urllib','urllib.request','urllib.response','urllib.parse','urllib.error','urllib.robotparser','http','http.client','ftplib','poplib','imaplib','smtplib','uuid','socketserver','http.server','http.cookies','http.cookiejar','xmlrpc','xmlrpc.client','xmlrpc.server','ipaddress','wave','colorsys','gettext','locale','turtle','cmd','shlex','tkinter','tkinter.colorchooser','tkinter.font','tkinter.messagebox','tkinter.scrolledtext','tkinter.dnd','tkinter.ttk','tkinter.tix','typing','pydoc','doctest','unittest','unittest.mock','unittest.mock','2to3','test','test.support','test.support.socket_helper','test.support.script_helper','test.support.bytecode_helper','test.support.threading_helper','test.support.os_helper','test.support.import_helper','test.support.warnings_helper','bdb','faulthandler','pdb','timeit','trace','tracemalloc','distutils','ensurepip','venv','zipapp','sys','sysconfig','builtins','__main__','warnings','dataclasses','contextlib','abc','atexit','traceback','__future__','gc','inspect','site','code','codeop','zipimport','pkgutil','modulefinder','runpy','importlib','ast','symtable','token','keyword','tokenize','tabnanny','pyclbr','py_compile','compileall','dis','pickletools','msvcrt','winreg','winsound','posix','pwd','grp','termios','tty','pty','fcntl','resource','syslog','aifc','asynchat','asyncore','audioop','cgi','cgitb','chunk','crypt','imghdr','imp','mailcap','msilib','nis','nntplib','optparse','ossaudiodev','pipes','smtpd','sndhdr','spwd','sunau','telnetlib','uu','xdrlib',]

def find_imports_in_file(file_path):
    with open(file_path, 'r',encoding='utf-8') as file:
        content = file.read()
        imports = re.findall(r'^\s*(?:import|from)\s+(\S+)', content, flags=re.MULTILINE)
        return imports

def find_imports_in_directory(directory_path):
    imports = set()

    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                imports_in_file = find_imports_in_file(file_path)
                imports.update(imports_in_file)

    return imports

project_directory = os.path.join(os.path.dirname(__file__),"..","neolib")
imports = find_imports_in_directory(project_directory)

print("Libraries used in your project:")
for imported_library in sorted(set(imports)):
    if imported_library not in list_python_lib:
        print(imported_library)
