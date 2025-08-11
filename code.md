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
# 直接复制脚本, 配置要运行的命令到/vault/myscript.sh
# r
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
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0NDE3NzIwMCw2NjcwNTQwNjFdfQ==
-->