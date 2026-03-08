## 一行代码

### 自动归档或解压 `.tar.xz` 文件

> 本脚本可以自动判断输入路径是**目录**还是**压缩包**，并执行相应的压缩或解压操作。  
适用于 Linux / macOS（`zsh` 环境）。
```bash
# 压缩
./archive.sh my_folder
# 解压
./archive.sh my_archive.tar.xz

# -完整脚本
#! /bin/zsh
# 自动归档文件夹或解压gz.tar文件
# tar -caf archive.tar.xz directory 压缩
# tar -xaf archive.tar.xz #解压

function compress(){
	tar -caf "$1".tar.xz "$1"
	[[ $? -eq 0 ]] && rm -rf "$1"
}
function uncompress(){
	tar -xvf "$1"
}
cd $(dirname $0)
if [[ $# -eq 0 ]]; then
	echo "input Compress dir or uncompress archive file"
	read dpath
else
	dpath="$1"
fi
dname=$(basename "$dpath")
if [[ -d "$dpath" ]];then
	compress "$dname"
else
	uncompress "$dname"
fi
```

### macos 下设置自动运行脚本

> 用于在macOS下创建自动运行脚本
```bash

# 定时任务开始命令: 
# launchctl load "$HOME/Library/LaunchAgents/com.user.myscript.plist" 

# 定时任务结束命令: 
# launchctl unload "$HOME/Library/LaunchAgents/com.user.myscript.plist" 

# 直接复制脚本, 配置要运行的命令到/vault/myscript.sh
# 定时任务设置为固定时间运行 6:55
# 定时任务log输出位置为$HOME/myscript.log

mkdir -p "$HOME/Library/LaunchAgents"
cat > "$HOME/Library/LaunchAgents/com.user.myscript.plist" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
 "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.myscript</string>

    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>/vault/myscript.sh</string>
    </array>

    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>6</integer>
        <key>Minute</key>
        <integer>55</integer>
    </dict>

    <key>RunAtLoad</key>
    <true/>

    <key>StandardOutPath</key>
    <string>$HOME/myscript.log</string>

    <key>StandardErrorPath</key>
    <string>$HOME/myscript.log</string>
</dict>
</plist>
EOF

chmod +x /vault/myscript.sh
launchctl unload "$HOME/Library/LaunchAgents/com.user.myscript.plist" 2>/dev/null
launchctl load "$HOME/Library/LaunchAgents/com.user.myscript.plist"

```

### RF 常用维护工具
```bash
#! /bin/zsh
program=("<Program>Diags-RAT-POR-Switch-FreeRunMeasure-Combo-OneShot</Program>" "<Program>01.Omnia-OTA-LAT-MP</Program>" "<Program>02.Omnia-OTA-UAT-MP</Program>")
stationname=("RAT" "RF-OTA-1" "WIFI-OTA2")
rmpath=("WiPASXNext_0_1/test_station_output_blob/" "WiPASXNext_0_1/test_station_output_logs/" "WiPASXNext_0_1/test_station_output_csv_v2/" "WiPASXNext_0_1/test_station_output_wipas/" "WiPASXNext_1_1/test_station_output_blob/" "WiPASXNext_1_1/test_station_output_csv_v2/" "WiPASXNext_1_1/test_station_output_wipas/" "WiPASXNext_1_1/test_station_output_logs/")
# main
function showmenu(){
	echo "============ 菜单选项 ============"
	echo "0. Exit"
    echo "1. Get asset number: macmini、T677、T536、StationID"
    echo "2. Get T677 MLB-Lid SN: MLBSN、LidSN"
    echo "3. Check Station Program"
    echo "4. Clear Log when Wipas is running"
    echo "5. Clear Log when Wipas is closing"
    echo "6. Re-open WiPAXNext"
    echo "7. Get Volume Avail Size"
    echo "================================"
}
function main(){
	choose="$1"
	if [[ "$1" == "" ]];then
		showmenu
		echo "Pls input the choose [0 - 6]"
		read choose
	fi
	case $choose in
		0)
			exit 0
			;;
		1)
			asset
			;;
		2)
			getLid
			;;
		3)
			checkScript
			;;
		4)
			cleanlog
			;;
		5)
			cleanlog2
			;;
		6)
			reopen
			;;
		7)
			getvolumesize
			;;
		*)
			log error "Invaild Value, Pls re-input"
			;;
	esac
}
# get volume size
function getvolumesize(){
	res=$(df -h ~/ | tail -1 | awk -F ' ' '{print $4,$5}')
	log ok "$res"
}
# reopen WiPASX
function reopen(){
	killall WiPASXNext
	sleep 0.5
	open /Applications/WiPAS/WiPASXNext.app &
}
# asset function
function asset(){
	host=$(gethost)
	macmini=$(ioreg -l | grep IOPlatformSerialNumber | egrep -o "[A-Z0-9]{12}")
	t677=$(getT677SN)
	t536=$(getT536SN)
	echo "$macmini,$t677,$t536,$host"
}
# get T677 MLBSN-LidSN
function getLid(){
	log=$(curl --connect-timeout 3 -s 10.0.0.10/devinfo.cgi | egrep -e "T677 serial number" -e "Lid serial number")
	sn=$(echo $log | sed 's/<[^>]*>//g; s/T677 serial number//g; s/Lid serial number//g')
	echo $(echo "$sn" | tr '\r\n' ',')
}
# clean log 
function cleanlog(){
	cd /Users/gdlocal/RFSAC/
	for i in ${rmpath[@]};do
		find "$i" -mtime +1 | xargs -P 4 -I {} rm -f {}
		#/bin/rm -rf "$i"*
	done
	log ok "the Big log and folder were removed"
}
# clean log2 all
function cleanlog2(){
	cd /Users/gdlocal/RFSAC/
	# find . -mtime 0 | xargs -P 4 -I {} rm -f {}
	/bin/rm -rf WiPASXNext_0_1
	r1=$?
	/bin/rm -rf WiPASXNext_1_1
	r2=$?
	if [[ $r1 == 0 && $r2 == 0 ]];then
		log ok "All Cleaned"
	fi
}
function getT677SN(){
	log=$(curl --connect-timeout 3 -s 10.0.0.10/devinfo.cgi)
	if [[ $? == 0 ]]; then
		t677=$(echo "$log" | grep "T677 serial number" | egrep -o "[0-9A-Z]{17}")
	else
		t677="T677 Not Ok"
	fi
	echo "$t677"
}
function getT536SN(){
	# open WIPASXNext
	# osascript -e 'tell application "System Events" to keystroke return using command down'
	log="/vault/caldata.txt"
	if [[ ! -f "$log" ]];then
		log=/Users/gdlocal/RFSAC/WiPASXNext_0_0/temp/log.log
		t536=$(grep -A2 "SerialNumber()" "$log" | egrep -o "[A-Z0-9]{17}")
	else
		t536=$(egrep -o "[A-Z0-9]{17}" "$log")
	fi
	
	if [[ -z "$t536" ]];then
		t536="T536 Not Ok"
	fi
	echo "$t536"
}
function gethost(){
	host=$(hostname | sed 's/\.local$//')
	echo "$host"
}
function log(){
	if [[ "$1" == "ok" ]]; then
		# echo -e "\e[32mOK      ]:$2\e[0m"
		echo "OK      ]:$2"
	elif [[ "$1" == "error" ]]; then
		# echo -e "\e[31mERROR   ]:$2\e[0m"
		echo "ERROR   ]:$2"
	else
		echo -e "\e[30mERROR   ]:$2\e[0m"
		echo "ERROR   ]:$2"
	fi
}
function getStation(){
	station=$(hostname | egrep -o "RAT|WIFI-OTA2|RF-OTA-1")
	echo "$station"
}
# check scenario
function checkScript() {
    local s=$(getStation)
    local index=-1  # 初始化为-1，表示未找到
    local len=${#stationname[*]}
    # 查找匹配的站点名称
    for i in $(seq 0 $len); do
	echo "${stationname[$i]}"
        if [[ "$s" == "${stationname[$i]}" ]]; then
		
            index=$i
            break
        fi
    done
    
    # 检查是否找到匹配项
    if [[ $index -lt 0 ]]; then
        log error "Not Found this Station Name: $s"
        exit 1
    fi
    
    # 检查两个文件
    grep "${program[$index]}" "/vault/wipas_0_1.xml"
    r1=$?
    
    grep "${program[$index]}" "/vault/wipas_1_1.xml"
    r2=$?
    
    # 判断结果
    if [[ $r1 == 0 && $r2 == 0 ]]; then
        log ok "All is Ok"
    elif [[ $r1 != 0 && $r2 == 0 ]]; then
        log error "Slot 1 is NG"
    elif [[ $r1 == 0 && $r2 != 0 ]]; then
        log error "Slot 2 is NG"
    else
        log error "Slot 1 & 2 are NG"
    fi
}
# function dialog(){
# 	PASSWORD=$(osascript -e '
#     tell application "System Events"
#         activate
#         display dialog "请输入密码：" default answer "" with hidden answer
#     end tell
#     return text returned of result
# 	')
# 	echo "输入的密码是: $PASSWORD"
# }
main "$1"
```


### APP-python 
### Python 改模式
```py
import tkinter as tk
import json
from re import search
from time import sleep
from os import remove,rename,path,makedirs
from subprocess import run,PIPE,STDOUT
from tkinter import ttk
from tkinter import messagebox,filedialog
from tkinter import scrolledtext
from pathlib import Path
from datetime import datetime
import pexpect
import serial
from pexpect_serial import SerialSpawn
class ClientGUI:
    def __init__(self, master):
        self.user= path.expanduser('~')+'/'
        self.logpath= self.user + "ChangeMode" +'/'
        self.port='/dev/'
        with open('config.json', 'r') as f:
            self.cfg=json.load(f)['config']
            self.cmdlist=self.cfg['testlist']
            self.maxcnt= int(self.cfg['maxcnt'])
            self.wifi= self.cfg['WIFI']
            self.cell= self.cfg['CELL']
            self.login= self.cfg['login']
            self.passwd= self.cfg['passwd']
            self.gusn=self.cfg['gusn']
            self.bandrate= int(self.cfg['bandrate'])
            self.defaultsw= self.cfg['defaultsw']
            self.autotest= self.cfg['autotest']
            self.savelog= False if int(self.cfg['savelog']) == 0 else True
        self.explist= ['login:', ':-)', 'root#', pexpect.EOF, pexpect.TIMEOUT]
        if not path.exists(self.logpath):
            makedirs(self.logpath,0o755)
        self.master = master
        self.master.geometry("600x450+300+300")
        self.master.title("CHange Mode")
        self.sn = ''
        self.mode= ''
        self.sku= ''
        self.cmdvar= tk.StringVar()
        self.resultvar= tk.StringVar()
        self.resultvar.set("Ready")
        settingBtn= ttk.Button(self.master, text="set",width=5, command=self.getPasswd)
        settingBtn.pack(anchor='ne', pady=5, padx=5)
        top= tk.Frame(self.master)
        top.pack(fill=tk.X,expand=True,pady=10)
        top.grid_columnconfigure(0,weight=5)
        top.grid_columnconfigure(1,weight=1)
        ttk.Label(top, text="Change Mode",width=30, font=("Times New Roman", 24), justify=tk.CENTER).grid(column=1,row=0,sticky="nsew")
        self.resL=ttk.Label(top, textvariable=self.resultvar,width=10, font=("Times New Roman", 24))
        self.resL.grid(column=2, row=0,sticky="nsew")
        self.resL.config(foreground="gray")
        ttk.Separator(self.master,orient=tk.HORIZONTAL).pack()
        style= ttk.Style()
        style.configure("My.TButton",width=15, font=("Arial", 16), padding=(0,5))
        func= tk.Frame(self.master)
        func.pack()
        ttk.Button(func, text="IOS",command=self.turn2ios, style="My.TButton" ).grid(column=0,row=1,padx=10)
        ttk.Button(func, text="Diags",command=self.turn2diags, style="My.TButton").grid(column=1,row=1,padx=10)
        ttk.Button(func, text="Recovery",command=self.turn2rec, style="My.TButton").grid(column=2,row=1,padx=10)
        ttk.Button(func, text="check bootargs", command=self.chkbootargs, style="My.TButton").grid(column=0,row=2)
        ttk.Button(func, text="get SN", command=self.getsn, style="My.TButton").grid(column=1,row=2)
        ttk.Button(func, text="Clean Logs",command=self.cleanlog, style="My.TButton").grid(column=2,row=2)
        ttk.Button(func, text="MakeGU", command=self.makegu, style="My.TButton").grid(column=0,row=3)
        ttk.Button(func, text="MakeCal",command=self.makecal, style="My.TButton").grid(column=1,row=3)
        self.log_text = scrolledtext.ScrolledText(master, wrap=tk.WORD,  height=20,state=tk.DISABLED)
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=10)
        self.client_socket = None
        self.receive_thread = None
        self.connected = False
    def initialize(self):
        self.log_text.configure(state=tk.NORMAL)
        self.log_text.delete('1.0', tk.END)
        self.log_text.configure(state=tk.DISABLED)
    def slog(self):
        if self.savelog :
            rename(self.logpath+'log.log', self.logpath+self.sn+'.log')
        else :
            remove(self.logpath+'log.log')
            
    def set2pass(self):
        self.resultvar.set("Pass")
        self.resL.config(foreground="green")
    def set2fail(self):
        self.resultvar.set("Fail")
        self.resL.config(foreground="red")
    def set2ready(self):
        self.resultvar.set("Ready")
        self.resL.config(foreground="gray")
    def turn2ios(self):
        self.initialize()
        port=self.getport()
        if not port:
            self.log("Cant find Port, Pls check Spartan")
            self.set2fail()
        self.updateinfo()
        if self.mode == ':-)':
            cmdname=self.sku+"diags2ios"
            logs=self.cmd(cmdname)
            self.set2pass()
        elif self.mode == 'root#':
            cmdname=self.sku+"ios2ios"
            logs=self.cmd(cmdname)
            self.set2pass()
        else :
            self.log("Unknown mode, Pls reboot and re-try")
            self.set2fail()
        self.slog()
    def turn2diags(self):
        self.initialize()
        port=self.getport()
        if not port:
            self.log("Cant find Port, Pls check Spartan")
            self.set2fail()
        self.updateinfo()
        if self.mode == ':-)':
            self.log("Already in diags mode")
            self.set2pass()
        elif self.mode == 'root#':
            cmdname="ios2diags"
            logs=self.cmd(cmdname)
            self.set2pass()
        else :
            self.log("Unknown mode, Pls reboot and re-try")
            self.set2fail()
        self.slog()
    def turn2rec(self):
        self.initialize()
        self.set2fail()
        # port=self.getport()
        # if not port:
        #     self.log("Cant find Port, Pls check Spartan")
        #     self.set2fail()
        # self.updateinfo()
        # if self.mode == ':-)':
        #     self.log("Already in diags mode")
        #     self.set2pass()
        # elif self.mode == 'root#':
        #     cmdname=self.sku+"ios2ios"
        #     logs=self.cmd(cmdname)
        #     self.set2pass()
        # else :
        #     self.log("Unknown mode, Pls reboot and re-try")
        #     self.set2fail()
        # self.slog()
    def chkbootargs(self):
        self.initialize()
        port=self.getport()
        if not port:
            self.log("Cant find Port, Pls check Spartan")
            self.set2fail()
        self.updateinfo()
        if self.mode == ':-)':
            logs=self.cmd("diagschkargs")
            argsname=self.sku+"bootargs"
            res=search(self.cfg[argsname], logs,flags=0)
            if res:
                self.set2pass()
            else:
                self.set2fail()
            
        elif self.mode == 'root#':
            logs=self.cmd("ioschkargs")
            argsname=self.sku+"bootargs"
            print(argsname)
            res=search(self.cfg[argsname], logs,flags=0)
            print(res)
            if res:
                self.set2pass()
            else:
                self.set2fail()
        else :
            self.log("Unknown mode, Pls reboot and re-try")
            self.set2fail()
        self.slog()
    def getsn(self):
        self.initialize()
        if self.sn:
            messagebox.showinfo("P", f"unit SN: {self.sn}")
            self.log("Unit SN: "+self.sn)
            return
        port=self.getport()
        if not port:
            self.log("Cant find Port, Pls check Spartan")
            self.set2fail()
        self.updateinfo()
        messagebox.showinfo("P", f"unit SN: {self.sn}")
        self.log("Unit SN: "+self.sn)
        self.slog()
    def cleanlog(self):
        self.initialize()
        port=self.getport()
        if not port:
            self.log("Cant find Port, Pls check Spartan")
            self.set2fail()
        self.updateinfo()
        if self.mode == ':-)':
            self.log("Pls change to IOS at first")
            self.set2fail()
        elif self.mode == 'root#':
            cmdname='rmlogs'
            logs=self.cmd(cmdname)
            self.set2pass()
        else :
            self.log("Unknown mode, Pls reboot and re-try")
            self.set2fail()
        self.slog()
    def makecom(self,tag=0):
        self.initialize()
        #  _mkgu(self, fpath,  target):
        port=self.getport()
        if not port:
            self.log("Cant find Port, Pls check Spartan")
            self.set2fail()
        self.updateinfo()
        if self.mode == ':-)':
            self.log("Pls change to IOS at first")
            self.set2fail()
        elif self.mode == 'root#':
            # check SN in GUSN list
            if self.sn not in self.gusn:
                self.log("This unit isnt GU")
                self.set2fail()
                return
            dp=self.choosefolder()
            cmd='find "'+dp+'" -type d -name "'+self.sn+'"'
            snpath=run(cmd,shell=True,stdout=PIPE,stderr=PIPE,encoding="utf-8").stdout.split('\n')[0]
            fpath=snpath+"/"
            print(fpath)
            if tag == 1:
                self.cmd("mkcal")
                mkname="mkcal"
            else:
                mkname="mk"+self.sku
            print(self.cfg[mkname])
            for i in iter(self.cfg[mkname]):
                self._mkgu(fpath,i[0],i[1])
                sleep(1)
            self.set2pass()
        else :
            self.log("Unknown mode, Pls reboot and re-try")
            self.set2fail()
        self.slog()
    # def mytest(self,tag=0):
    #     if tag == 1:
    #         # self.cmd("mkcal")
    #         mkname="mkcal"
    #     else:
    #         mkname="mkCELL"
    #     for i in iter(self.cfg[mkname]):
    #         self._mkgu(i[0],i[1])
    #         sleep(1)
    def makegu(self):
        self.makecom()
    def makecal(self):
        self.makecom(1)
        
    # def getHostPort(self):
    #     self.frame2 = tk.Toplevel(self.master)
    #     self.frame2.title("Config")
    #     parent_x = self.master.winfo_rootx()
    #     parent_y = self.master.winfo_rooty()
    #     parent_width = self.master.winfo_width()
    #     parent_height = self.master.winfo_height()
    #     print(parent_y,parent_x,parent_width,parent_height)
    #     x = 0
    #     y = 0
    #     self.frame2.geometry(f"{parent_width}x{parent_height}+{x}+{y}")
    #     self.hostvar= tk.StringVar()
    #     self.portvar= tk.StringVar()
    #     ttk.Label(self.frame2, text="Host", width=10).grid(column=0,row=0)
    #     hostE= ttk.Entry(self.frame2,textvariable=self.hostvar, width=20)
    #     hostE.grid(column=1, row=0)
    #     ttk.Label(self.frame2, text="Port", width=10).grid(column=0,row=1)
    #     portE= ttk.Entry(self.frame2,textvariable=self.portvar, width=20)
    #     portE.grid(column=1, row=1)
    #     ttk.Button(self.frame2, text="submit", command=self.updateHost).grid(column=0,row=2,columnspan=2)
    def getPasswd(self):
        # get passwd
        self.dialog= tk.Toplevel(self.master)
        self.dialog.title("Enter Password")
        parent_x = self.master.winfo_rootx()
        parent_y = self.master.winfo_rooty()
        parent_width = self.master.winfo_width()
        parent_height = self.master.winfo_height()
        dialog_width = 200
        dialog_height = 100
        x = parent_x + (parent_width - dialog_width) // 2
        y = parent_y + (parent_height - dialog_height) // 2
        self.dialog.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")
        self.pswdvar= tk.StringVar()
        pswdEntry= ttk.Entry(self.dialog, show="*", textvariable=self.pswdvar)
        pswdEntry.focus_set()
        pswdEntry.bind('<Return>',self.checkPswd)
        pswdEntry.pack(padx=(5,5), pady=(5,5))
        sb=ttk.Button(self.dialog, text="submit", command=self.checkPswd)
        sb.pack(pady=(5,5))
    def choosefolder(self):
        directory = filedialog.askdirectory(
            initialdir="~/Desktop",
            title="选择一个目录"
        )
        if directory:
            print(f"选择的目录：{directory}")
            self.log(directory)
            return directory
    def checkPswd(self, event=None):
        enterpswd=self.pswdvar.get()
        self.dialog.destroy()
        if enterpswd == self.config['password']:
            self.getHostPort()
        else:
            messagebox.showinfo("P", f"Password was wrong,You entered: {enterpswd}")
            self.getPasswd()
    def log(self, message):
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message)
        self.log_text.config(state=tk.DISABLED)
        self.log_text.see(tk.END)
    def getport(self):
        cnt=0
        while cnt < self.maxcnt:
            if self.port == '/dev/' :
                port=run('ls /dev/ | grep cu.usb | head -1',shell=True,stdout=PIPE,stderr=PIPE,encoding="utf-8").stdout.split('\n')[0]
                self.port= '/dev/'+port
                cnt+=1
                sleep(1)
            else :
                break
        return False if self.port == '/dev/' else self.port
   
    def cmd(self, cmdname):
        logs=''
        with serial.Serial(self.port, self.bandrate, timeout=1) as ser:
            ss=SerialSpawn(ser)
            fout= open(self.logpath+'log.log', 'ab')
            ss.logfile=fout
            ss.buffer=b''
            cmd2run=self.cmdlist[cmdname]
            cmdlen=len(cmd2run)
            for i in iter(cmd2run):
                ss.sendline(i[0])
                sleep(i[2])
                ss.expect_exact(i[1])
                tmp=ss.before.decode()
                self.log(tmp)
                logs+=tmp
            sleep(0.5)
            ss.close()
            return logs
    def _mkgu(self,dpath, fpath, target):
        cmd='system_profiler SPUSBDataType | fgrep -A 10 "iPad" | fgrep "Location ID" | egrep -o "0x[0-9]{8}"'
        ipadport=run(cmd,shell=True,stdout=PIPE,stderr=PIPE,encoding="utf-8").stdout.split('\n')[0]
        cmd='./copyUnrestricted -w -u '+ipadport+' -s "'+dpath+fpath+'" -t "'+target+'"'
        print(cmd)
        logs=run(cmd,shell=True,stdout=PIPE,stderr=STDOUT,encoding="utf-8").stdout
        self.log(logs)
        return logs
    def updateinfo(self):
        with serial.Serial(self.port, self.bandrate, timeout=1) as ser:
            ss=SerialSpawn(ser)
            fout= open(self.logpath+'log.log', 'ab')
            ss.logfile=fout
            cnt= 0
            while cnt < self.maxcnt :
                ss.sendline()
                i=ss.expect_exact(self.explist)
                if i == 0:
                    ss.sendline(self.login)
                    sleep(0.5)
                    ss.sendline(self.passwd)
                    cnt+=1
                elif i <= 2:
                    self.mode= self.explist[i]
                    break
                else:
                    pass
            cnt=0
            mode=self.mode
            logs=''
            if mode == ':-)':
                cmdname='diagsgetinfo'
                self.cmd(cmdname)
                logs=self.cmd(cmdname)
            elif mode == 'root#':
                cmdname='iosgetinfo'
                logs=self.cmd(cmdname)
            # elif mode == '] \r\n':
            #     cmdname='recoverygetinfo'
            #     print(cmdname)
            #     logs=self.cmd(cmdname,mode,5)
            else :
                return False
            sn= search('[A-Z0-9]{10}', logs,flags=0).group(0)
            sku= search('[jJ][0-9]{3}', logs,flags=0).group(0).upper()
            print("sn: ",sn)
            print("sku: ",sku)
            if sn :
                self.sn= sn
            if sku == self.wifi:
                self.sku = "WIFI"
            elif sku == self.cell:
                self.sku = "CELL"
            else :
                # cant identify project code
                pass
            ss.close()
def main():
    root = tk.Tk()
    client_gui = ClientGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()
```
```json
{"config":{
	"WIFI":"J481",
	"CELL":"J482",
	"login":"root",
	"passwd":"alpine",
	"bandrate": 115200,
	"defaultsw":"WIFIdiags2ios",
	"autotest":"False",
	"maxcnt": 3,
	"savelog":1,
	"WIFIbootargs":"debug=0x104146 serial=0x13 gpu_panic_on_recovery=1 apfs_edt_rw_mount=1 wlan-olyhal-abort=1 amfi_get_out_of_my_way=1 launchctl_enforce_codesign=0 amfi_unrestrict_task_for_pid=1 amfi_allow_any_signature=1 dk=0x8001 wdt=-1 cc.debug.enable=1 max_task_pmem=0 wlan.debug.abort-init=2 mtk.wlan.manufacture=1 wlan.factory=0x93 ota ioimageloader.debug.csr-access=1",
	"CELLbootargs":"debug=0x104146 serial=0x13 gpu_panic_on_recovery=1 apfs_edt_rw_mount=1 ota wdt=-1 wlan.factory=0x93",
	"gusn":["K6R2F6N4Y6","MG9XW1VQ2M", "LGKJV0RWX1", "G6FPV7PMQQ", "JNJKQX9VMW", "MQ6X7K0F2T", "HJ6L0G0WR3", "RFNQCJ4NVC", "CT2MHHG2WC", "GMCPXPWVVR"],
	"mkWIFI":[["Alchemy.csv","/var/logs/WiPASmini/"]],
	"mkCELL":[["Alchemy.csv","/var/logs/WiPASmini/"],
		["factoryota/Rprad.txt","/var/logs/WiPASmini/factoryota/"]],
	"mkcal":[
		["factoryota/BCAL.bin","/var/root/CALfiles/"],
		["factoryota/OCA3.bin","/var/root/CALfiles/"],
		["factoryota/OCAL.bin","/var/root/CALfiles/"],
		["factoryota/WCAL.bin","/var/root/CALfiles/"]
	],
	"testlist":{
		"WIFIdiags2ios":[
			["nvram --set boot-command fsboot", ":-)", 0.5],
			["nvram --set boot-args 'debug=0x104146 serial=0x13 gpu_panic_on_recovery=1 apfs_edt_rw_mount=1 wlan-olyhal-abort=1 amfi_get_out_of_my_way=1 launchctl_enforce_codesign=0 amfi_unrestrict_task_for_pid=1 amfi_allow_any_signature=1 dk=0x8001 wdt=-1 cc.debug.enable=1 max_task_pmem=0 wlan.debug.abort-init=2 mtk.wlan.manufacture=1 wlan.factory=0x93 ota ioimageloader.debug.csr-access=1'", ":-)", 0.5],
			["nvram --save", ":-)", 0.5],
			["reset", "reset", 0.5]
		],
		"CELLdiags2ios":[
			["nvram --set boot-command fsboot", ":-)", 0.5],
			["nvram --set boot-args 'debug=0x104146 serial=0x13 gpu_panic_on_recovery=1 apfs_edt_rw_mount=1 ota wdt=-1 wlan.factory=0x93'", ":-)", 0.5],
			["nvram --save", ":-)", 0.5],
			["reset", "reset", 0.5]
		],
		"WIFIios2ios":[
			["nvram boot-command=fsboot", "root#", 0.5],
			["nvram boot-args='debug=0x104146 serial=0x13 gpu_panic_on_recovery=1 apfs_edt_rw_mount=1 wlan-olyhal-abort=1 amfi_get_out_of_my_way=1 launchctl_enforce_codesign=0 amfi_unrestrict_task_for_pid=1 amfi_allow_any_signature=1 dk=0x8001 wdt=-1 cc.debug.enable=1 max_task_pmem=0 wlan.debug.abort-init=2 mtk.wlan.manufacture=1 wlan.factory=0x93 ota ioimageloader.debug.csr-access=1'", "root#", 0.5],
			["reboot", "Kext", 0.5]
		],
		"CELLios2ios":[
			["nvram boot-command=fsboot", "root#", 0.5],
			["nvram boot-args='debug=0x104146 serial=0x13 gpu_panic_on_recovery=1 apfs_edt_rw_mount=1 ota wdt=-1 wlan.factory=0x93'", "root#", 0.5],
			["reboot", "Kext", 0.5]
		],
		"ios2diags":[
			["nvram boot-command=diags", "root#", 0.5],
			["reboot", "Kext", 0.5]
		],
		"iosgetinfo":[
			["cat /var/logs/WiPASmini/factoryota/info.wipasmini", "root#", 0.5]
		],
		"diagsgetinfo":[
			["sn", ":-)", 0.5],
			["system", ":-)", 0.5]
		],
		"recoverygetinfo":[
			["diags", ":-)", 5],
			["sn", ":-)", 0.5],
			["system", ":-)", 0.5]
		],
		"rmlogs":[
			["cp -r /var/logs/WiPASmini /tmp", "root#", 0.5],
			["rm -rf /var/logs/", "root#", 0.5],
			["mkdir /var/logs", "root#", 0.5],
			["cp -r /tmp/WiPASmini /var/logs", "root#", 0.5]
		],
		"mkcal":[
			["mkdir /var/root/CALfiles/", "root#", 0.5]
		],
		"diagschkargs":[
			["nvram --get boot-args", ":-)", 0.5]
		],
		"ioschkargs":[
			["nvram boot-args", "root#", 0.5]
		]
	}
}
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTM5MTQ1ODI0OF19
-->