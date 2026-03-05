###  

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


### Python
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTUxMjQwMzIyLC0yMDAzNjA0ODc2XX0=
-->