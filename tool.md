## 编程相关
- [VS Code](https://code.visualstudio.com)
- [GitHub](https://github.com)

## 在线工具
- [JSON Formatter](https://jsonformatter.org)
- [RegEx101](https://regex101.com)

## Tool
- [md img url 2 base64](https://mzrf.github.io/url2base64.html)

## 一行代码
```shell
#! /bin/zsh
# 自动归档文件夹、解压
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
eyJoaXN0b3J5IjpbMTcxNjk3NDQ4MSwxNzgwMjcwMjQ2XX0=
-->