###  

## 一行代码

### 自动归档或解压 `.tar.xz` 文件

本脚本可以自动判断输入路径是**目录**还是**压缩包**，并执行相应的压缩或解压操作。  
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
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM1MDgxNjI3MSwtMjY1ODE2Mzg3XX0=
-->