#NEPYUNE i.e DATABASIC2

intro = '''

        ███╗   ██╗███████╗██████╗ ████████╗██╗   ██╗███╗   ██╗███████╗
        ████╗  ██║██╔════╝██╔══██╗╚══██╔══╝██║   ██║████╗  ██║██╔════╝
        ██╔██╗ ██║█████╗  ██████╔╝   ██║   ██║   ██║██╔██╗ ██║█████╗  
        ██║╚██╗██║██╔══╝  ██╔═══╝    ██║   ██║   ██║██║╚██╗██║██╔══╝  
        ██║ ╚████║███████╗██║        ██║   ╚██████╔╝██║ ╚████║███████╗
        ╚═╝  ╚═══╝╚══════╝╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚══════╝

'''.split("\n")                      

import tabulate
import os
from colorama import Fore, Back, Style
import getpass
import sys
from time import sleep
print('Run in cmd directly for best results.' if 'idlelib.run' in sys.modules else '\r')
os.system("cls")
os.system('color 0b')

center_table=True
tb_back=Back.WHITE
tb_fore=Fore.BLACK
pty=True

#if you already have color enabled in commandline
#, just delete enablecolor.reg and these two lines will not execute.
if os.path.exists("enablecolor.reg"):
    os.system('enablecolor.reg')

cmds=["BEGIN TABLE","CLS{TYPE:","CLS{NAME:","DATA{","END TABLE"]
curname=""
datatypes=[]
curhead=[]
curbase=[]
styles=['╭─', '─', '─┬─', '─╮','├─', '─', '─┼─', '─┤','│ ', '', ' │ ', ' │','╰─', '─', '─┴─', '─╯']
path="dbase\\"
loaded=False

def print_center(s):
    print(' ' * ((os.get_terminal_size().columns - len(s))//2) + s)

def gv_err(txt):
    print(Fore.RED + str(txt) + Style.RESET_ALL)
    
def load_data(fname):
    dbase=open(str(path+fname),"r")
    lb=dbase.readlines()
    rb=''.join(lb).strip("\n")
    cont=True
    for i in cmds:
        if i not in rb:
            cont=False    
    if cont==True:
        curname=lb[0][12:].strip("\n")
        dtypes = lb[1].strip("CLS{TYPE:").strip("}\n").split(";")
        datatypes.append(dtypes)
        chead=lb[2].strip("}\n")[9:].split(";")
        for i in chead:
            curhead.append(i)
        rows=lb[3].strip("DATA{").strip("}\n").split("|")
        for itm in rows:
            spitm=itm.strip("ROW{").strip("}").split(";")
            for i in range(0,len(spitm)):
                if datatypes[0][i] == "int":
                    spitm[i] = int(spitm[i])
            curbase.append(spitm)
    print("  set current table to '" + curname + "'\n")
    dbase.close()

# test command: dbase load-table offline tdata; table show *; table add-record {Abhay Tr,17,XII,J,14-04-03}; table show *

def showbase(pretty=True):
    if pretty == True:
        stable=str(tabulate.tabulate(curbase,headers=curhead)).split("\n")
        ptytable=[styles[0]+(styles[1]*(len(stable[1])))+styles[3]]
        for i in stable:
            ptytable.append(styles[8] + str(i) + " " * (len(stable[1])-len(str(i))) + styles[11])
        ptytable.append(styles[12] + (styles[13]*(len(stable[1]))) + styles[15])
        for ln in ptytable:
            if center_table==True:
                print_center(" "*12 + tb_fore + tb_back + ln + Style.RESET_ALL)
            else:
                print(tb_fore + tb_back + ln + Style.RESET_ALL)
    else:
        print(curhead,curbase)

def parse_cdtn(cdtn):
    print("  coming soon.")
    
#load_data("dbase.dbc")
#showbase()

def initialize_():
    for nln in range(0,len(intro)):
        if nln in [3,4,5]:
            print_center(Fore.CYAN + intro[nln] + Style.RESET_ALL)
        else:
            print_center(Fore.BLUE + intro[nln] + Style.RESET_ALL)
            
    print_center("        " + Fore.WHITE + "at-adityavikram 2020 • made in (python) heaven™ • input '?' for help" + Style.RESET_ALL)
    print("")

def reset_uncommited():
    print("  coming soon.")


    
initialize_()
ipstr=Fore.YELLOW + "$ command: " + Style.RESET_ALL
while True:
    uipt=input(ipstr).split("; ")
    print("")
    for t in uipt:
        if "dbase" in t.lower()[0:5]:
            if t.lower()[6:14] == "set-path":
                if t[15:] == "*":
                    path="dbase\\"
                    if os.path.exists("dbase\\") == False:
                        os.mkdir("dbase\\")
                    print("  path to database directory (dbase) set to current directory\n")
                elif t[15:].strip(" ") == "?":
                    print("  sets the directory in which the dbase folder is located\n")
                else:
                    if not "dbase" in t[15:]:
                        if os.path.exists(t[15:].rstrip("\\") + "\\" + "dbase\\"):
                            path= t[15:].rstrip("\\") + "\\" + "dbase\\"
                            print("  path to database directory (dbase) set to '" + path + "'")
                        else:
                            gv_err("  given path does not have the dbase folder!\n")
                            pt=input("  would you like to create it in this path? (y/n)> ").lower()
                            if pt=="y":
                                os.mkdir(t[15:].rstrip("\\") + "\\" + "dbase\\")
                                path= t[15:].rstrip("\\") + "\\" + "dbase\\"
                            else:
                                print("ok.\n")
                    else:
                        if os.path.exists(t[15:].rstrip("\\") + "\\" + "dbase\\"):
                            path= t[15:].rstrip("\\") + "\\"
                            print("  path to database directory (dbase) set to '" + path + "'")
                        else:
                            gv_err("  given path does not have the dbase folder!\n")
                            pt=input("  would you like to create it in this path? (y/n)> ").lower()
                            if pt=="y":
                                os.mkdir(t[15:].rstrip("\\") + "\\" + "dbase\\")
                                path= t[15:].rstrip("\\") + "\\" + "dbase\\"
                            else:
                                print("ok.\n")
            elif t.lower()[6:14] == "get-path":
                if t[15:].strip(" ") == "?":
                    print("  gets the current path to the dbase folder\n")
                else:
                    print("  current path is '" + path + "'")
            elif t.lower()[6:16] == "load-table" and loaded==False:
                if t.lower()[17:24] == "offline":
                    tname = t[24:].strip(" ").strip(".dbc")
                    if not tname == "":
                        if os.path.exists(path + tname + ".dbc"):
                            load_data(tname + ".dbc")
                            loaded=True
                        else:
                            gv_err("  given table not found in directory\n")
                elif t.lower()[17:20] == "ftp":
                    ftp_usname=input("  enter your username> ")
                    ftp_password = getpass.getpass("  password> ")
                    print("  coming soon")
                elif t.lower()[17:20] == "git":
                    print("  coming soon")
            elif t.lower()[6:16] == "load-table" and loaded==True:
                gv_err("  cannot load new table until previous table is unloaded\n")
                
            elif t.lower()[6:15] == "list-all":
                if t[16:].strip(" ") == "?":
                    print("  list all tables in directory\n")
                else:
                    tbv= [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
                    for i in range(0,len(tbv)):
                        print("  " + str(i+1) + ") " + tbv[i].strip(".dbc"))
        elif "table" in t.lower()[0:5]:
            if t.lower()[6:10] == "show":
                if t[11:].strip(" ") == "*":
                    print("")
                    showbase(pty)
                    print("")
                elif "* where" in t[11:]:
                    condition = t[19:].split(" and ")
                    parse_cdtn(condition)
            elif t.lower()[6:14] == "describe":
                print("")
                print(tabulate.tabulate(datatypes,headers=curhead))
                print("")
            elif t.lower()[6:16].strip(" ") == "add-record":
                if not t[17:].strip(" ") == "":
                    if t[17] == "{" and t[-1] == "}":
                        recrd=(t[18:].strip("}")).split(",")
                        if len(recrd)==len(datatypes[0]):
                            for i in range(0,len(recrd)):
                                if datatypes[0][i] == "int":
                                    recrd[i] = int(recrd[i])
                            curbase.append(recrd)
                            print("  row added successfully\n")
                    elif t[17] == "?":
                        print("  adds a row to the table. syntax: table add-record {some_str,some_int,..}\n")
            elif t.lower[6:16].strip(" ") == "add-column":
                print("adding column")
            elif t.lower[6:10].strip(" ") == "edit":
                print("editing")
        elif "nep" in t.lower()[0:3]:
            if t.lower() == "nep reset-tmp":
                print("  resetting uncommited channges")
                gv_err("  note that commited changes cannot be reset\n")
                reset_uncommited()
            elif t.lower()[4:7] == "set":
                if t.lower()[8:20] == "center-table":
                    if t.lower()[21:25] == "true":
                        center_table= True
                    elif t.lower()[21:26] == "false":
                        center_table=False
                        print("bruh")
                    elif t.lower()[21:] == "?":
                        print("  sets wether table should be centered or not (only if prettyprint is enabled)\n")
                elif t.lower()[8:20] == "pretty-print":
                    if t.lower()[21:25] == "true":
                        pty= True
                    elif t.lower()[21:26] == "false":
                        pty=False
                    elif t.lower()[21:] == "?":
                        print("  sets wether table should be pretty-printed\n")
                elif t.lower()[8:18] == "table-fore":
                    print("  coming soon.")
                elif t.lower()[8:18] == "table-back":
                    print("  coming soon.")
            elif t.lower() == "nep hide-intro":
                print("removing the awesome logo...")
                sleep(0.5)
                gv_err("warning - also removes all outputs until now. but rest assured, activities are untouched")
                sleep(2)
                os.system("cls")
                
        else:
            gv_err("  unknown command '" + t + "'\n")
extt=input("press enter to exit...")
                
            
        
