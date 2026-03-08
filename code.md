---


---

<h3 id="section"><span class="prefix"></span><span class="content"></span><span class="suffix"></span></h3>
<h2 id="一行代码"><span class="prefix"></span><span class="content">一行代码</span><span class="suffix"></span></h2>
<h3 id="自动归档或解压-.tar.xz-文件"><span class="prefix"></span><span class="content">自动归档或解压 <code>.tar.xz</code> 文件</span><span class="suffix"></span></h3>
<blockquote>
<p>本脚本可以自动判断输入路径是<strong>目录</strong>还是<strong>压缩包</strong>，并执行相应的压缩或解压操作。<br>
适用于 Linux / macOS（<code>zsh</code> 环境）。</p>
</blockquote>
<pre class=" language-bash"><code class="prism  language-bash"><span class="token comment"># 压缩</span>
./archive.sh my_folder
<span class="token comment"># 解压</span>
./archive.sh my_archive.tar.xz

<span class="token comment"># -完整脚本</span>
<span class="token comment">#! /bin/zsh</span>
<span class="token comment"># 自动归档文件夹或解压gz.tar文件</span>
<span class="token comment"># tar -caf archive.tar.xz directory 压缩</span>
<span class="token comment"># tar -xaf archive.tar.xz #解压</span>

<span class="token keyword">function</span> compress<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
	<span class="token function">tar</span> -caf <span class="token string">"<span class="token variable">$1</span>"</span>.tar.xz <span class="token string">"<span class="token variable">$1</span>"</span>
	<span class="token punctuation">[</span><span class="token punctuation">[</span> <span class="token variable">$?</span> -eq 0 <span class="token punctuation">]</span><span class="token punctuation">]</span> <span class="token operator">&amp;&amp;</span> <span class="token function">rm</span> -rf <span class="token string">"<span class="token variable">$1</span>"</span>
<span class="token punctuation">}</span>
<span class="token keyword">function</span> uncompress<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
	<span class="token function">tar</span> -xvf <span class="token string">"<span class="token variable">$1</span>"</span>
<span class="token punctuation">}</span>
<span class="token function">cd</span> <span class="token variable"><span class="token variable">$(</span><span class="token function">dirname</span> $0<span class="token variable">)</span></span>
<span class="token keyword">if</span> <span class="token punctuation">[</span><span class="token punctuation">[</span> $<span class="token comment"># -eq 0 ]]; then</span>
	<span class="token keyword">echo</span> <span class="token string">"input Compress dir or uncompress archive file"</span>
	<span class="token function">read</span> dpath
<span class="token keyword">else</span>
	dpath<span class="token operator">=</span><span class="token string">"<span class="token variable">$1</span>"</span>
<span class="token keyword">fi</span>
dname<span class="token operator">=</span><span class="token punctuation">$(</span>basename <span class="token string">"<span class="token variable">$dpath</span>"</span><span class="token punctuation">)</span>
<span class="token keyword">if</span> <span class="token punctuation">[</span><span class="token punctuation">[</span> -d <span class="token string">"<span class="token variable">$dpath</span>"</span> <span class="token punctuation">]</span><span class="token punctuation">]</span><span class="token punctuation">;</span><span class="token keyword">then</span>
	compress <span class="token string">"<span class="token variable">$dname</span>"</span>
<span class="token keyword">else</span>
	uncompress <span class="token string">"<span class="token variable">$dname</span>"</span>
<span class="token keyword">fi</span>
</code></pre>
<h3 id="macos-下设置自动运行脚本"><span class="prefix"></span><span class="content">macos 下设置自动运行脚本</span><span class="suffix"></span></h3>
<blockquote>
<p>用于在macOS下创建自动运行脚本</p>
</blockquote>
<pre class=" language-bash"><code class="prism  language-bash">
<span class="token comment"># 定时任务开始命令: </span>
<span class="token comment"># launchctl load "$HOME/Library/LaunchAgents/com.user.myscript.plist" </span>

<span class="token comment"># 定时任务结束命令: </span>
<span class="token comment"># launchctl unload "$HOME/Library/LaunchAgents/com.user.myscript.plist" </span>

<span class="token comment"># 直接复制脚本, 配置要运行的命令到/vault/myscript.sh</span>
<span class="token comment"># 定时任务设置为固定时间运行 6:55</span>
<span class="token comment"># 定时任务log输出位置为$HOME/myscript.log</span>

<span class="token function">mkdir</span> -p <span class="token string">"<span class="token variable">$HOME</span>/Library/LaunchAgents"</span>
<span class="token function">cat</span> <span class="token operator">&gt;</span> <span class="token string">"<span class="token variable">$HOME</span>/Library/LaunchAgents/com.user.myscript.plist"</span> <span class="token operator">&lt;&lt;</span><span class="token string">EOF
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
 "http://www.apple.com/DTDs/PropertyList-1.0.dtd"&gt;
&lt;plist version="1.0"&gt;
&lt;dict&gt;
    &lt;key&gt;Label&lt;/key&gt;
    &lt;string&gt;com.user.myscript&lt;/string&gt;

    &lt;key&gt;ProgramArguments&lt;/key&gt;
    &lt;array&gt;
        &lt;string&gt;/bin/bash&lt;/string&gt;
        &lt;string&gt;/vault/myscript.sh&lt;/string&gt;
    &lt;/array&gt;

    &lt;key&gt;StartCalendarInterval&lt;/key&gt;
    &lt;dict&gt;
        &lt;key&gt;Hour&lt;/key&gt;
        &lt;integer&gt;6&lt;/integer&gt;
        &lt;key&gt;Minute&lt;/key&gt;
        &lt;integer&gt;55&lt;/integer&gt;
    &lt;/dict&gt;

    &lt;key&gt;RunAtLoad&lt;/key&gt;
    &lt;true/&gt;

    &lt;key&gt;StandardOutPath&lt;/key&gt;
    &lt;string&gt;<span class="token variable">$HOME</span>/myscript.log&lt;/string&gt;

    &lt;key&gt;StandardErrorPath&lt;/key&gt;
    &lt;string&gt;<span class="token variable">$HOME</span>/myscript.log&lt;/string&gt;
&lt;/dict&gt;
&lt;/plist&gt;
EOF</span>

<span class="token function">chmod</span> +x /vault/myscript.sh
launchctl unload <span class="token string">"<span class="token variable">$HOME</span>/Library/LaunchAgents/com.user.myscript.plist"</span> 2<span class="token operator">&gt;</span>/dev/null
launchctl load <span class="token string">"<span class="token variable">$HOME</span>/Library/LaunchAgents/com.user.myscript.plist"</span>

</code></pre>
<h3 id="rf-常用维护工具"><span class="prefix"></span><span class="content">RF 常用维护工具</span><span class="suffix"></span></h3>
<pre class=" language-bash"><code class="prism  language-bash"><span class="token comment">#! /bin/zsh</span>
program<span class="token operator">=</span><span class="token punctuation">(</span><span class="token string">"&lt;Program&gt;Diags-RAT-POR-Switch-FreeRunMeasure-Combo-OneShot&lt;/Program&gt;"</span> <span class="token string">"&lt;Program&gt;01.Omnia-OTA-LAT-MP&lt;/Program&gt;"</span> <span class="token string">"&lt;Program&gt;02.Omnia-OTA-UAT-MP&lt;/Program&gt;"</span><span class="token punctuation">)</span>
stationname<span class="token operator">=</span><span class="token punctuation">(</span><span class="token string">"RAT"</span> <span class="token string">"RF-OTA-1"</span> <span class="token string">"WIFI-OTA2"</span><span class="token punctuation">)</span>
rmpath<span class="token operator">=</span><span class="token punctuation">(</span><span class="token string">"WiPASXNext_0_1/test_station_output_blob/"</span> <span class="token string">"WiPASXNext_0_1/test_station_output_logs/"</span> <span class="token string">"WiPASXNext_0_1/test_station_output_csv_v2/"</span> <span class="token string">"WiPASXNext_0_1/test_station_output_wipas/"</span> <span class="token string">"WiPASXNext_1_1/test_station_output_blob/"</span> <span class="token string">"WiPASXNext_1_1/test_station_output_csv_v2/"</span> <span class="token string">"WiPASXNext_1_1/test_station_output_wipas/"</span> <span class="token string">"WiPASXNext_1_1/test_station_output_logs/"</span><span class="token punctuation">)</span>
<span class="token comment"># main</span>
<span class="token keyword">function</span> showmenu<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
	<span class="token keyword">echo</span> <span class="token string">"============ 菜单选项 ============"</span>
	<span class="token keyword">echo</span> <span class="token string">"0. Exit"</span>
    <span class="token keyword">echo</span> <span class="token string">"1. Get asset number: macmini、T677、T536、StationID"</span>
    <span class="token keyword">echo</span> <span class="token string">"2. Get T677 MLB-Lid SN: MLBSN、LidSN"</span>
    <span class="token keyword">echo</span> <span class="token string">"3. Check Station Program"</span>
    <span class="token keyword">echo</span> <span class="token string">"4. Clear Log when Wipas is running"</span>
    <span class="token keyword">echo</span> <span class="token string">"5. Clear Log when Wipas is closing"</span>
    <span class="token keyword">echo</span> <span class="token string">"6. Re-open WiPAXNext"</span>
    <span class="token keyword">echo</span> <span class="token string">"7. Get Volume Avail Size"</span>
    <span class="token keyword">echo</span> <span class="token string">"================================"</span>
<span class="token punctuation">}</span>
<span class="token keyword">function</span> main<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
	choose<span class="token operator">=</span><span class="token string">"<span class="token variable">$1</span>"</span>
	<span class="token keyword">if</span> <span class="token punctuation">[</span><span class="token punctuation">[</span> <span class="token string">"<span class="token variable">$1</span>"</span> <span class="token operator">==</span> <span class="token string">""</span> <span class="token punctuation">]</span><span class="token punctuation">]</span><span class="token punctuation">;</span><span class="token keyword">then</span>
		showmenu
		<span class="token keyword">echo</span> <span class="token string">"Pls input the choose [0 - 6]"</span>
		<span class="token function">read</span> choose
	<span class="token keyword">fi</span>
	<span class="token keyword">case</span> <span class="token variable">$choose</span> <span class="token keyword">in</span>
		0<span class="token punctuation">)</span>
			<span class="token keyword">exit</span> 0
			<span class="token punctuation">;</span><span class="token punctuation">;</span>
		1<span class="token punctuation">)</span>
			asset
			<span class="token punctuation">;</span><span class="token punctuation">;</span>
		2<span class="token punctuation">)</span>
			getLid
			<span class="token punctuation">;</span><span class="token punctuation">;</span>
		3<span class="token punctuation">)</span>
			checkScript
			<span class="token punctuation">;</span><span class="token punctuation">;</span>
		4<span class="token punctuation">)</span>
			cleanlog
			<span class="token punctuation">;</span><span class="token punctuation">;</span>
		5<span class="token punctuation">)</span>
			cleanlog2
			<span class="token punctuation">;</span><span class="token punctuation">;</span>
		6<span class="token punctuation">)</span>
			reopen
			<span class="token punctuation">;</span><span class="token punctuation">;</span>
		7<span class="token punctuation">)</span>
			getvolumesize
			<span class="token punctuation">;</span><span class="token punctuation">;</span>
		*<span class="token punctuation">)</span>
			log error <span class="token string">"Invaild Value, Pls re-input"</span>
			<span class="token punctuation">;</span><span class="token punctuation">;</span>
	esac
<span class="token punctuation">}</span>
<span class="token comment"># get volume size</span>
<span class="token keyword">function</span> getvolumesize<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
	res<span class="token operator">=</span><span class="token punctuation">$(</span>df -h ~/ <span class="token operator">|</span> <span class="token function">tail</span> -1 <span class="token operator">|</span> <span class="token function">awk</span> -F <span class="token string">' '</span> <span class="token string">'{print <span class="token variable">$4</span>,<span class="token variable">$5</span>}'</span><span class="token punctuation">)</span>
	log ok <span class="token string">"<span class="token variable">$res</span>"</span>
<span class="token punctuation">}</span>
<span class="token comment"># reopen WiPASX</span>
<span class="token keyword">function</span> reopen<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
	<span class="token function">killall</span> WiPASXNext
	<span class="token function">sleep</span> 0.5
	<span class="token function">open</span> /Applications/WiPAS/WiPASXNext.app <span class="token operator">&amp;</span>
<span class="token punctuation">}</span>
<span class="token comment"># asset function</span>
<span class="token keyword">function</span> asset<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
	host<span class="token operator">=</span><span class="token variable"><span class="token variable">$(</span>gethost<span class="token variable">)</span></span>
	macmini<span class="token operator">=</span><span class="token punctuation">$(</span>ioreg -l <span class="token operator">|</span> <span class="token function">grep</span> IOPlatformSerialNumber <span class="token operator">|</span> <span class="token function">egrep</span> -o <span class="token string">"[A-Z0-9]{12}"</span><span class="token punctuation">)</span>
	t677<span class="token operator">=</span><span class="token variable"><span class="token variable">$(</span>getT677SN<span class="token variable">)</span></span>
	t536<span class="token operator">=</span><span class="token variable"><span class="token variable">$(</span>getT536SN<span class="token variable">)</span></span>
	<span class="token keyword">echo</span> <span class="token string">"<span class="token variable">$macmini</span>,<span class="token variable">$t677</span>,<span class="token variable">$t536</span>,<span class="token variable">$host</span>"</span>
<span class="token punctuation">}</span>
<span class="token comment"># get T677 MLBSN-LidSN</span>
<span class="token keyword">function</span> getLid<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
	log<span class="token operator">=</span><span class="token punctuation">$(</span>curl --connect-timeout 3 -s 10.0.0.10/devinfo.cgi <span class="token operator">|</span> <span class="token function">egrep</span> -e <span class="token string">"T677 serial number"</span> -e <span class="token string">"Lid serial number"</span><span class="token punctuation">)</span>
	sn<span class="token operator">=</span><span class="token punctuation">$(</span>echo <span class="token variable">$log</span> <span class="token operator">|</span> <span class="token function">sed</span> <span class="token string">'s/&lt;[^&gt;]*&gt;//g; s/T677 serial number//g; s/Lid serial number//g'</span><span class="token punctuation">)</span>
	<span class="token keyword">echo</span> <span class="token punctuation">$(</span>echo <span class="token string">"<span class="token variable">$sn</span>"</span> <span class="token operator">|</span> <span class="token function">tr</span> <span class="token string">'\r\n'</span> <span class="token string">','</span><span class="token punctuation">)</span>
<span class="token punctuation">}</span>
<span class="token comment"># clean log </span>
<span class="token keyword">function</span> cleanlog<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
	<span class="token function">cd</span> /Users/gdlocal/RFSAC/
	<span class="token keyword">for</span> i <span class="token keyword">in</span> <span class="token variable">${rmpath[@]}</span><span class="token punctuation">;</span><span class="token keyword">do</span>
		<span class="token function">find</span> <span class="token string">"<span class="token variable">$i</span>"</span> -mtime +1 <span class="token operator">|</span> <span class="token function">xargs</span> -P 4 -I <span class="token punctuation">{</span><span class="token punctuation">}</span> <span class="token function">rm</span> -f <span class="token punctuation">{</span><span class="token punctuation">}</span>
		<span class="token comment">#/bin/rm -rf "$i"*</span>
	<span class="token keyword">done</span>
	log ok <span class="token string">"the Big log and folder were removed"</span>
<span class="token punctuation">}</span>
<span class="token comment"># clean log2 all</span>
<span class="token keyword">function</span> cleanlog2<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
	<span class="token function">cd</span> /Users/gdlocal/RFSAC/
	<span class="token comment"># find . -mtime 0 | xargs -P 4 -I {} rm -f {}</span>
	/bin/rm -rf WiPASXNext_0_1
	r1<span class="token operator">=</span><span class="token variable">$?</span>
	/bin/rm -rf WiPASXNext_1_1
	r2<span class="token operator">=</span><span class="token variable">$?</span>
	<span class="token keyword">if</span> <span class="token punctuation">[</span><span class="token punctuation">[</span> <span class="token variable">$r1</span> <span class="token operator">==</span> 0 <span class="token operator">&amp;&amp;</span> <span class="token variable">$r2</span> <span class="token operator">==</span> 0 <span class="token punctuation">]</span><span class="token punctuation">]</span><span class="token punctuation">;</span><span class="token keyword">then</span>
		log ok <span class="token string">"All Cleaned"</span>
	<span class="token keyword">fi</span>
<span class="token punctuation">}</span>
<span class="token keyword">function</span> getT677SN<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
	log<span class="token operator">=</span><span class="token variable"><span class="token variable">$(</span>curl --connect-timeout 3 -s 10.0.0.10/devinfo.cgi<span class="token variable">)</span></span>
	<span class="token keyword">if</span> <span class="token punctuation">[</span><span class="token punctuation">[</span> <span class="token variable">$?</span> <span class="token operator">==</span> 0 <span class="token punctuation">]</span><span class="token punctuation">]</span><span class="token punctuation">;</span> <span class="token keyword">then</span>
		t677<span class="token operator">=</span><span class="token punctuation">$(</span>echo <span class="token string">"<span class="token variable">$log</span>"</span> <span class="token operator">|</span> <span class="token function">grep</span> <span class="token string">"T677 serial number"</span> <span class="token operator">|</span> <span class="token function">egrep</span> -o <span class="token string">"[0-9A-Z]{17}"</span><span class="token punctuation">)</span>
	<span class="token keyword">else</span>
		t677<span class="token operator">=</span><span class="token string">"T677 Not Ok"</span>
	<span class="token keyword">fi</span>
	<span class="token keyword">echo</span> <span class="token string">"<span class="token variable">$t677</span>"</span>
<span class="token punctuation">}</span>
<span class="token keyword">function</span> getT536SN<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
	<span class="token comment"># open WIPASXNext</span>
	<span class="token comment"># osascript -e 'tell application "System Events" to keystroke return using command down'</span>
	log<span class="token operator">=</span><span class="token string">"/vault/caldata.txt"</span>
	<span class="token keyword">if</span> <span class="token punctuation">[</span><span class="token punctuation">[</span> <span class="token operator">!</span> -f <span class="token string">"<span class="token variable">$log</span>"</span> <span class="token punctuation">]</span><span class="token punctuation">]</span><span class="token punctuation">;</span><span class="token keyword">then</span>
		log<span class="token operator">=</span>/Users/gdlocal/RFSAC/WiPASXNext_0_0/temp/log.log
		t536<span class="token operator">=</span><span class="token punctuation">$(</span>grep -A2 <span class="token string">"SerialNumber()"</span> <span class="token string">"<span class="token variable">$log</span>"</span> <span class="token operator">|</span> <span class="token function">egrep</span> -o <span class="token string">"[A-Z0-9]{17}"</span><span class="token punctuation">)</span>
	<span class="token keyword">else</span>
		t536<span class="token operator">=</span><span class="token punctuation">$(</span>egrep -o <span class="token string">"[A-Z0-9]{17}"</span> <span class="token string">"<span class="token variable">$log</span>"</span><span class="token punctuation">)</span>
	<span class="token keyword">fi</span>
	
	<span class="token keyword">if</span> <span class="token punctuation">[</span><span class="token punctuation">[</span> -z <span class="token string">"<span class="token variable">$t536</span>"</span> <span class="token punctuation">]</span><span class="token punctuation">]</span><span class="token punctuation">;</span><span class="token keyword">then</span>
		t536<span class="token operator">=</span><span class="token string">"T536 Not Ok"</span>
	<span class="token keyword">fi</span>
	<span class="token keyword">echo</span> <span class="token string">"<span class="token variable">$t536</span>"</span>
<span class="token punctuation">}</span>
<span class="token keyword">function</span> gethost<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
	host<span class="token operator">=</span><span class="token punctuation">$(</span>hostname <span class="token operator">|</span> <span class="token function">sed</span> <span class="token string">'s/\.local$//'</span><span class="token punctuation">)</span>
	<span class="token keyword">echo</span> <span class="token string">"<span class="token variable">$host</span>"</span>
<span class="token punctuation">}</span>
<span class="token keyword">function</span> log<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
	<span class="token keyword">if</span> <span class="token punctuation">[</span><span class="token punctuation">[</span> <span class="token string">"<span class="token variable">$1</span>"</span> <span class="token operator">==</span> <span class="token string">"ok"</span> <span class="token punctuation">]</span><span class="token punctuation">]</span><span class="token punctuation">;</span> <span class="token keyword">then</span>
		<span class="token comment"># echo -e "\e[32mOK      ]:$2\e[0m"</span>
		<span class="token keyword">echo</span> <span class="token string">"OK      ]:<span class="token variable">$2</span>"</span>
	<span class="token keyword">elif</span> <span class="token punctuation">[</span><span class="token punctuation">[</span> <span class="token string">"<span class="token variable">$1</span>"</span> <span class="token operator">==</span> <span class="token string">"error"</span> <span class="token punctuation">]</span><span class="token punctuation">]</span><span class="token punctuation">;</span> <span class="token keyword">then</span>
		<span class="token comment"># echo -e "\e[31mERROR   ]:$2\e[0m"</span>
		<span class="token keyword">echo</span> <span class="token string">"ERROR   ]:<span class="token variable">$2</span>"</span>
	<span class="token keyword">else</span>
		<span class="token keyword">echo</span> -e <span class="token string">"\e[30mERROR   ]:<span class="token variable">$2</span>\e[0m"</span>
		<span class="token keyword">echo</span> <span class="token string">"ERROR   ]:<span class="token variable">$2</span>"</span>
	<span class="token keyword">fi</span>
<span class="token punctuation">}</span>
<span class="token keyword">function</span> getStation<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
	station<span class="token operator">=</span><span class="token punctuation">$(</span>hostname <span class="token operator">|</span> <span class="token function">egrep</span> -o <span class="token string">"RAT|WIFI-OTA2|RF-OTA-1"</span><span class="token punctuation">)</span>
	<span class="token keyword">echo</span> <span class="token string">"<span class="token variable">$station</span>"</span>
<span class="token punctuation">}</span>
<span class="token comment"># check scenario</span>
<span class="token keyword">function</span> checkScript<span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    local s<span class="token operator">=</span><span class="token variable"><span class="token variable">$(</span>getStation<span class="token variable">)</span></span>
    local index<span class="token operator">=</span>-1  <span class="token comment"># 初始化为-1，表示未找到</span>
    local len<span class="token operator">=</span><span class="token variable">${#stationname[*]}</span>
    <span class="token comment"># 查找匹配的站点名称</span>
    <span class="token keyword">for</span> i <span class="token keyword">in</span> <span class="token variable"><span class="token variable">$(</span><span class="token function">seq</span> 0 $len<span class="token variable">)</span></span><span class="token punctuation">;</span> <span class="token keyword">do</span>
	<span class="token keyword">echo</span> <span class="token string">"<span class="token variable">${stationname[$i]}</span>"</span>
        <span class="token keyword">if</span> <span class="token punctuation">[</span><span class="token punctuation">[</span> <span class="token string">"<span class="token variable">$s</span>"</span> <span class="token operator">==</span> <span class="token string">"<span class="token variable">${stationname[$i]}</span>"</span> <span class="token punctuation">]</span><span class="token punctuation">]</span><span class="token punctuation">;</span> <span class="token keyword">then</span>
		
            index<span class="token operator">=</span><span class="token variable">$i</span>
            <span class="token keyword">break</span>
        <span class="token keyword">fi</span>
    <span class="token keyword">done</span>
    
    <span class="token comment"># 检查是否找到匹配项</span>
    <span class="token keyword">if</span> <span class="token punctuation">[</span><span class="token punctuation">[</span> <span class="token variable">$index</span> -lt 0 <span class="token punctuation">]</span><span class="token punctuation">]</span><span class="token punctuation">;</span> <span class="token keyword">then</span>
        log error <span class="token string">"Not Found this Station Name: <span class="token variable">$s</span>"</span>
        <span class="token keyword">exit</span> 1
    <span class="token keyword">fi</span>
    
    <span class="token comment"># 检查两个文件</span>
    <span class="token function">grep</span> <span class="token string">"<span class="token variable">${program[$index]}</span>"</span> <span class="token string">"/vault/wipas_0_1.xml"</span>
    r1<span class="token operator">=</span><span class="token variable">$?</span>
    
    <span class="token function">grep</span> <span class="token string">"<span class="token variable">${program[$index]}</span>"</span> <span class="token string">"/vault/wipas_1_1.xml"</span>
    r2<span class="token operator">=</span><span class="token variable">$?</span>
    
    <span class="token comment"># 判断结果</span>
    <span class="token keyword">if</span> <span class="token punctuation">[</span><span class="token punctuation">[</span> <span class="token variable">$r1</span> <span class="token operator">==</span> 0 <span class="token operator">&amp;&amp;</span> <span class="token variable">$r2</span> <span class="token operator">==</span> 0 <span class="token punctuation">]</span><span class="token punctuation">]</span><span class="token punctuation">;</span> <span class="token keyword">then</span>
        log ok <span class="token string">"All is Ok"</span>
    <span class="token keyword">elif</span> <span class="token punctuation">[</span><span class="token punctuation">[</span> <span class="token variable">$r1</span> <span class="token operator">!=</span> 0 <span class="token operator">&amp;&amp;</span> <span class="token variable">$r2</span> <span class="token operator">==</span> 0 <span class="token punctuation">]</span><span class="token punctuation">]</span><span class="token punctuation">;</span> <span class="token keyword">then</span>
        log error <span class="token string">"Slot 1 is NG"</span>
    <span class="token keyword">elif</span> <span class="token punctuation">[</span><span class="token punctuation">[</span> <span class="token variable">$r1</span> <span class="token operator">==</span> 0 <span class="token operator">&amp;&amp;</span> <span class="token variable">$r2</span> <span class="token operator">!=</span> 0 <span class="token punctuation">]</span><span class="token punctuation">]</span><span class="token punctuation">;</span> <span class="token keyword">then</span>
        log error <span class="token string">"Slot 2 is NG"</span>
    <span class="token keyword">else</span>
        log error <span class="token string">"Slot 1 &amp; 2 are NG"</span>
    <span class="token keyword">fi</span>
<span class="token punctuation">}</span>
<span class="token comment"># function dialog(){</span>
<span class="token comment"># 	PASSWORD=$(osascript -e '</span>
<span class="token comment">#     tell application "System Events"</span>
<span class="token comment">#         activate</span>
<span class="token comment">#         display dialog "请输入密码：" default answer "" with hidden answer</span>
<span class="token comment">#     end tell</span>
<span class="token comment">#     return text returned of result</span>
<span class="token comment"># 	')</span>
<span class="token comment"># 	echo "输入的密码是: $PASSWORD"</span>
<span class="token comment"># }</span>
main <span class="token string">"<span class="token variable">$1</span>"</span>
</code></pre>
<h3 id="app-python"><span class="prefix"></span><span class="content">APP-python</span><span class="suffix"></span></h3>
<h3 id="python-改模式"><span class="prefix"></span><span class="content">Python 改模式</span><span class="suffix"></span></h3>
<pre class=" language-py"><code class="prism  language-py"><span class="token keyword">import</span> tkinter <span class="token keyword">as</span> tk
<span class="token keyword">import</span> json
<span class="token keyword">from</span> re <span class="token keyword">import</span> search
<span class="token keyword">from</span> time <span class="token keyword">import</span> sleep
<span class="token keyword">from</span> os <span class="token keyword">import</span> remove<span class="token punctuation">,</span>rename<span class="token punctuation">,</span>path<span class="token punctuation">,</span>makedirs
<span class="token keyword">from</span> subprocess <span class="token keyword">import</span> run<span class="token punctuation">,</span>PIPE<span class="token punctuation">,</span>STDOUT
<span class="token keyword">from</span> tkinter <span class="token keyword">import</span> ttk
<span class="token keyword">from</span> tkinter <span class="token keyword">import</span> messagebox<span class="token punctuation">,</span>filedialog
<span class="token keyword">from</span> tkinter <span class="token keyword">import</span> scrolledtext
<span class="token keyword">from</span> pathlib <span class="token keyword">import</span> Path
<span class="token keyword">from</span> datetime <span class="token keyword">import</span> datetime
<span class="token keyword">import</span> pexpect
<span class="token keyword">import</span> serial
<span class="token keyword">from</span> pexpect_serial <span class="token keyword">import</span> SerialSpawn
<span class="token keyword">class</span> <span class="token class-name">ClientGUI</span><span class="token punctuation">:</span>
    <span class="token keyword">def</span> <span class="token function">__init__</span><span class="token punctuation">(</span>self<span class="token punctuation">,</span> master<span class="token punctuation">)</span><span class="token punctuation">:</span>
        self<span class="token punctuation">.</span>user<span class="token operator">=</span> path<span class="token punctuation">.</span>expanduser<span class="token punctuation">(</span><span class="token string">'~'</span><span class="token punctuation">)</span><span class="token operator">+</span><span class="token string">'/'</span>
        self<span class="token punctuation">.</span>logpath<span class="token operator">=</span> self<span class="token punctuation">.</span>user <span class="token operator">+</span> <span class="token string">"ChangeMode"</span> <span class="token operator">+</span><span class="token string">'/'</span>
        self<span class="token punctuation">.</span>port<span class="token operator">=</span><span class="token string">'/dev/'</span>
        <span class="token keyword">with</span> <span class="token builtin">open</span><span class="token punctuation">(</span><span class="token string">'config.json'</span><span class="token punctuation">,</span> <span class="token string">'r'</span><span class="token punctuation">)</span> <span class="token keyword">as</span> f<span class="token punctuation">:</span>
            self<span class="token punctuation">.</span>cfg<span class="token operator">=</span>json<span class="token punctuation">.</span>load<span class="token punctuation">(</span>f<span class="token punctuation">)</span><span class="token punctuation">[</span><span class="token string">'config'</span><span class="token punctuation">]</span>
            self<span class="token punctuation">.</span>cmdlist<span class="token operator">=</span>self<span class="token punctuation">.</span>cfg<span class="token punctuation">[</span><span class="token string">'testlist'</span><span class="token punctuation">]</span>
            self<span class="token punctuation">.</span>maxcnt<span class="token operator">=</span> <span class="token builtin">int</span><span class="token punctuation">(</span>self<span class="token punctuation">.</span>cfg<span class="token punctuation">[</span><span class="token string">'maxcnt'</span><span class="token punctuation">]</span><span class="token punctuation">)</span>
            self<span class="token punctuation">.</span>wifi<span class="token operator">=</span> self<span class="token punctuation">.</span>cfg<span class="token punctuation">[</span><span class="token string">'WIFI'</span><span class="token punctuation">]</span>
            self<span class="token punctuation">.</span>cell<span class="token operator">=</span> self<span class="token punctuation">.</span>cfg<span class="token punctuation">[</span><span class="token string">'CELL'</span><span class="token punctuation">]</span>
            self<span class="token punctuation">.</span>login<span class="token operator">=</span> self<span class="token punctuation">.</span>cfg<span class="token punctuation">[</span><span class="token string">'login'</span><span class="token punctuation">]</span>
            self<span class="token punctuation">.</span>passwd<span class="token operator">=</span> self<span class="token punctuation">.</span>cfg<span class="token punctuation">[</span><span class="token string">'passwd'</span><span class="token punctuation">]</span>
            self<span class="token punctuation">.</span>gusn<span class="token operator">=</span>self<span class="token punctuation">.</span>cfg<span class="token punctuation">[</span><span class="token string">'gusn'</span><span class="token punctuation">]</span>
            self<span class="token punctuation">.</span>bandrate<span class="token operator">=</span> <span class="token builtin">int</span><span class="token punctuation">(</span>self<span class="token punctuation">.</span>cfg<span class="token punctuation">[</span><span class="token string">'bandrate'</span><span class="token punctuation">]</span><span class="token punctuation">)</span>
            self<span class="token punctuation">.</span>defaultsw<span class="token operator">=</span> self<span class="token punctuation">.</span>cfg<span class="token punctuation">[</span><span class="token string">'defaultsw'</span><span class="token punctuation">]</span>
            self<span class="token punctuation">.</span>autotest<span class="token operator">=</span> self<span class="token punctuation">.</span>cfg<span class="token punctuation">[</span><span class="token string">'autotest'</span><span class="token punctuation">]</span>
            self<span class="token punctuation">.</span>savelog<span class="token operator">=</span> <span class="token boolean">False</span> <span class="token keyword">if</span> <span class="token builtin">int</span><span class="token punctuation">(</span>self<span class="token punctuation">.</span>cfg<span class="token punctuation">[</span><span class="token string">'savelog'</span><span class="token punctuation">]</span><span class="token punctuation">)</span> <span class="token operator">==</span> <span class="token number">0</span> <span class="token keyword">else</span> <span class="token boolean">True</span>
        self<span class="token punctuation">.</span>explist<span class="token operator">=</span> <span class="token punctuation">[</span><span class="token string">'login:'</span><span class="token punctuation">,</span> <span class="token string">':-)'</span><span class="token punctuation">,</span> <span class="token string">'root#'</span><span class="token punctuation">,</span> pexpect<span class="token punctuation">.</span>EOF<span class="token punctuation">,</span> pexpect<span class="token punctuation">.</span>TIMEOUT<span class="token punctuation">]</span>
        <span class="token keyword">if</span> <span class="token operator">not</span> path<span class="token punctuation">.</span>exists<span class="token punctuation">(</span>self<span class="token punctuation">.</span>logpath<span class="token punctuation">)</span><span class="token punctuation">:</span>
            makedirs<span class="token punctuation">(</span>self<span class="token punctuation">.</span>logpath<span class="token punctuation">,</span><span class="token number">0o755</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>master <span class="token operator">=</span> master
        self<span class="token punctuation">.</span>master<span class="token punctuation">.</span>geometry<span class="token punctuation">(</span><span class="token string">"600x450+300+300"</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>master<span class="token punctuation">.</span>title<span class="token punctuation">(</span><span class="token string">"CHange Mode"</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>sn <span class="token operator">=</span> <span class="token string">''</span>
        self<span class="token punctuation">.</span>mode<span class="token operator">=</span> <span class="token string">''</span>
        self<span class="token punctuation">.</span>sku<span class="token operator">=</span> <span class="token string">''</span>
        self<span class="token punctuation">.</span>cmdvar<span class="token operator">=</span> tk<span class="token punctuation">.</span>StringVar<span class="token punctuation">(</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>resultvar<span class="token operator">=</span> tk<span class="token punctuation">.</span>StringVar<span class="token punctuation">(</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>resultvar<span class="token punctuation">.</span><span class="token builtin">set</span><span class="token punctuation">(</span><span class="token string">"Ready"</span><span class="token punctuation">)</span>
        settingBtn<span class="token operator">=</span> ttk<span class="token punctuation">.</span>Button<span class="token punctuation">(</span>self<span class="token punctuation">.</span>master<span class="token punctuation">,</span> text<span class="token operator">=</span><span class="token string">"set"</span><span class="token punctuation">,</span>width<span class="token operator">=</span><span class="token number">5</span><span class="token punctuation">,</span> command<span class="token operator">=</span>self<span class="token punctuation">.</span>getPasswd<span class="token punctuation">)</span>
        settingBtn<span class="token punctuation">.</span>pack<span class="token punctuation">(</span>anchor<span class="token operator">=</span><span class="token string">'ne'</span><span class="token punctuation">,</span> pady<span class="token operator">=</span><span class="token number">5</span><span class="token punctuation">,</span> padx<span class="token operator">=</span><span class="token number">5</span><span class="token punctuation">)</span>
        top<span class="token operator">=</span> tk<span class="token punctuation">.</span>Frame<span class="token punctuation">(</span>self<span class="token punctuation">.</span>master<span class="token punctuation">)</span>
        top<span class="token punctuation">.</span>pack<span class="token punctuation">(</span>fill<span class="token operator">=</span>tk<span class="token punctuation">.</span>X<span class="token punctuation">,</span>expand<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">,</span>pady<span class="token operator">=</span><span class="token number">10</span><span class="token punctuation">)</span>
        top<span class="token punctuation">.</span>grid_columnconfigure<span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">,</span>weight<span class="token operator">=</span><span class="token number">5</span><span class="token punctuation">)</span>
        top<span class="token punctuation">.</span>grid_columnconfigure<span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">,</span>weight<span class="token operator">=</span><span class="token number">1</span><span class="token punctuation">)</span>
        ttk<span class="token punctuation">.</span>Label<span class="token punctuation">(</span>top<span class="token punctuation">,</span> text<span class="token operator">=</span><span class="token string">"Change Mode"</span><span class="token punctuation">,</span>width<span class="token operator">=</span><span class="token number">30</span><span class="token punctuation">,</span> font<span class="token operator">=</span><span class="token punctuation">(</span><span class="token string">"Times New Roman"</span><span class="token punctuation">,</span> <span class="token number">24</span><span class="token punctuation">)</span><span class="token punctuation">,</span> justify<span class="token operator">=</span>tk<span class="token punctuation">.</span>CENTER<span class="token punctuation">)</span><span class="token punctuation">.</span>grid<span class="token punctuation">(</span>column<span class="token operator">=</span><span class="token number">1</span><span class="token punctuation">,</span>row<span class="token operator">=</span><span class="token number">0</span><span class="token punctuation">,</span>sticky<span class="token operator">=</span><span class="token string">"nsew"</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>resL<span class="token operator">=</span>ttk<span class="token punctuation">.</span>Label<span class="token punctuation">(</span>top<span class="token punctuation">,</span> textvariable<span class="token operator">=</span>self<span class="token punctuation">.</span>resultvar<span class="token punctuation">,</span>width<span class="token operator">=</span><span class="token number">10</span><span class="token punctuation">,</span> font<span class="token operator">=</span><span class="token punctuation">(</span><span class="token string">"Times New Roman"</span><span class="token punctuation">,</span> <span class="token number">24</span><span class="token punctuation">)</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>resL<span class="token punctuation">.</span>grid<span class="token punctuation">(</span>column<span class="token operator">=</span><span class="token number">2</span><span class="token punctuation">,</span> row<span class="token operator">=</span><span class="token number">0</span><span class="token punctuation">,</span>sticky<span class="token operator">=</span><span class="token string">"nsew"</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>resL<span class="token punctuation">.</span>config<span class="token punctuation">(</span>foreground<span class="token operator">=</span><span class="token string">"gray"</span><span class="token punctuation">)</span>
        ttk<span class="token punctuation">.</span>Separator<span class="token punctuation">(</span>self<span class="token punctuation">.</span>master<span class="token punctuation">,</span>orient<span class="token operator">=</span>tk<span class="token punctuation">.</span>HORIZONTAL<span class="token punctuation">)</span><span class="token punctuation">.</span>pack<span class="token punctuation">(</span><span class="token punctuation">)</span>
        style<span class="token operator">=</span> ttk<span class="token punctuation">.</span>Style<span class="token punctuation">(</span><span class="token punctuation">)</span>
        style<span class="token punctuation">.</span>configure<span class="token punctuation">(</span><span class="token string">"My.TButton"</span><span class="token punctuation">,</span>width<span class="token operator">=</span><span class="token number">15</span><span class="token punctuation">,</span> font<span class="token operator">=</span><span class="token punctuation">(</span><span class="token string">"Arial"</span><span class="token punctuation">,</span> <span class="token number">16</span><span class="token punctuation">)</span><span class="token punctuation">,</span> padding<span class="token operator">=</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">,</span><span class="token number">5</span><span class="token punctuation">)</span><span class="token punctuation">)</span>
        func<span class="token operator">=</span> tk<span class="token punctuation">.</span>Frame<span class="token punctuation">(</span>self<span class="token punctuation">.</span>master<span class="token punctuation">)</span>
        func<span class="token punctuation">.</span>pack<span class="token punctuation">(</span><span class="token punctuation">)</span>
        ttk<span class="token punctuation">.</span>Button<span class="token punctuation">(</span>func<span class="token punctuation">,</span> text<span class="token operator">=</span><span class="token string">"IOS"</span><span class="token punctuation">,</span>command<span class="token operator">=</span>self<span class="token punctuation">.</span>turn2ios<span class="token punctuation">,</span> style<span class="token operator">=</span><span class="token string">"My.TButton"</span> <span class="token punctuation">)</span><span class="token punctuation">.</span>grid<span class="token punctuation">(</span>column<span class="token operator">=</span><span class="token number">0</span><span class="token punctuation">,</span>row<span class="token operator">=</span><span class="token number">1</span><span class="token punctuation">,</span>padx<span class="token operator">=</span><span class="token number">10</span><span class="token punctuation">)</span>
        ttk<span class="token punctuation">.</span>Button<span class="token punctuation">(</span>func<span class="token punctuation">,</span> text<span class="token operator">=</span><span class="token string">"Diags"</span><span class="token punctuation">,</span>command<span class="token operator">=</span>self<span class="token punctuation">.</span>turn2diags<span class="token punctuation">,</span> style<span class="token operator">=</span><span class="token string">"My.TButton"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>grid<span class="token punctuation">(</span>column<span class="token operator">=</span><span class="token number">1</span><span class="token punctuation">,</span>row<span class="token operator">=</span><span class="token number">1</span><span class="token punctuation">,</span>padx<span class="token operator">=</span><span class="token number">10</span><span class="token punctuation">)</span>
        ttk<span class="token punctuation">.</span>Button<span class="token punctuation">(</span>func<span class="token punctuation">,</span> text<span class="token operator">=</span><span class="token string">"Recovery"</span><span class="token punctuation">,</span>command<span class="token operator">=</span>self<span class="token punctuation">.</span>turn2rec<span class="token punctuation">,</span> style<span class="token operator">=</span><span class="token string">"My.TButton"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>grid<span class="token punctuation">(</span>column<span class="token operator">=</span><span class="token number">2</span><span class="token punctuation">,</span>row<span class="token operator">=</span><span class="token number">1</span><span class="token punctuation">,</span>padx<span class="token operator">=</span><span class="token number">10</span><span class="token punctuation">)</span>
        ttk<span class="token punctuation">.</span>Button<span class="token punctuation">(</span>func<span class="token punctuation">,</span> text<span class="token operator">=</span><span class="token string">"check bootargs"</span><span class="token punctuation">,</span> command<span class="token operator">=</span>self<span class="token punctuation">.</span>chkbootargs<span class="token punctuation">,</span> style<span class="token operator">=</span><span class="token string">"My.TButton"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>grid<span class="token punctuation">(</span>column<span class="token operator">=</span><span class="token number">0</span><span class="token punctuation">,</span>row<span class="token operator">=</span><span class="token number">2</span><span class="token punctuation">)</span>
        ttk<span class="token punctuation">.</span>Button<span class="token punctuation">(</span>func<span class="token punctuation">,</span> text<span class="token operator">=</span><span class="token string">"get SN"</span><span class="token punctuation">,</span> command<span class="token operator">=</span>self<span class="token punctuation">.</span>getsn<span class="token punctuation">,</span> style<span class="token operator">=</span><span class="token string">"My.TButton"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>grid<span class="token punctuation">(</span>column<span class="token operator">=</span><span class="token number">1</span><span class="token punctuation">,</span>row<span class="token operator">=</span><span class="token number">2</span><span class="token punctuation">)</span>
        ttk<span class="token punctuation">.</span>Button<span class="token punctuation">(</span>func<span class="token punctuation">,</span> text<span class="token operator">=</span><span class="token string">"Clean Logs"</span><span class="token punctuation">,</span>command<span class="token operator">=</span>self<span class="token punctuation">.</span>cleanlog<span class="token punctuation">,</span> style<span class="token operator">=</span><span class="token string">"My.TButton"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>grid<span class="token punctuation">(</span>column<span class="token operator">=</span><span class="token number">2</span><span class="token punctuation">,</span>row<span class="token operator">=</span><span class="token number">2</span><span class="token punctuation">)</span>
        ttk<span class="token punctuation">.</span>Button<span class="token punctuation">(</span>func<span class="token punctuation">,</span> text<span class="token operator">=</span><span class="token string">"MakeGU"</span><span class="token punctuation">,</span> command<span class="token operator">=</span>self<span class="token punctuation">.</span>makegu<span class="token punctuation">,</span> style<span class="token operator">=</span><span class="token string">"My.TButton"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>grid<span class="token punctuation">(</span>column<span class="token operator">=</span><span class="token number">0</span><span class="token punctuation">,</span>row<span class="token operator">=</span><span class="token number">3</span><span class="token punctuation">)</span>
        ttk<span class="token punctuation">.</span>Button<span class="token punctuation">(</span>func<span class="token punctuation">,</span> text<span class="token operator">=</span><span class="token string">"MakeCal"</span><span class="token punctuation">,</span>command<span class="token operator">=</span>self<span class="token punctuation">.</span>makecal<span class="token punctuation">,</span> style<span class="token operator">=</span><span class="token string">"My.TButton"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>grid<span class="token punctuation">(</span>column<span class="token operator">=</span><span class="token number">1</span><span class="token punctuation">,</span>row<span class="token operator">=</span><span class="token number">3</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>log_text <span class="token operator">=</span> scrolledtext<span class="token punctuation">.</span>ScrolledText<span class="token punctuation">(</span>master<span class="token punctuation">,</span> wrap<span class="token operator">=</span>tk<span class="token punctuation">.</span>WORD<span class="token punctuation">,</span>  height<span class="token operator">=</span><span class="token number">20</span><span class="token punctuation">,</span>state<span class="token operator">=</span>tk<span class="token punctuation">.</span>DISABLED<span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>log_text<span class="token punctuation">.</span>pack<span class="token punctuation">(</span>fill<span class="token operator">=</span>tk<span class="token punctuation">.</span>BOTH<span class="token punctuation">,</span> expand<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">,</span> padx<span class="token operator">=</span><span class="token number">5</span><span class="token punctuation">,</span> pady<span class="token operator">=</span><span class="token number">10</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>client_socket <span class="token operator">=</span> <span class="token boolean">None</span>
        self<span class="token punctuation">.</span>receive_thread <span class="token operator">=</span> <span class="token boolean">None</span>
        self<span class="token punctuation">.</span>connected <span class="token operator">=</span> <span class="token boolean">False</span>
    <span class="token keyword">def</span> <span class="token function">initialize</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
        self<span class="token punctuation">.</span>log_text<span class="token punctuation">.</span>configure<span class="token punctuation">(</span>state<span class="token operator">=</span>tk<span class="token punctuation">.</span>NORMAL<span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>log_text<span class="token punctuation">.</span>delete<span class="token punctuation">(</span><span class="token string">'1.0'</span><span class="token punctuation">,</span> tk<span class="token punctuation">.</span>END<span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>log_text<span class="token punctuation">.</span>configure<span class="token punctuation">(</span>state<span class="token operator">=</span>tk<span class="token punctuation">.</span>DISABLED<span class="token punctuation">)</span>
    <span class="token keyword">def</span> <span class="token function">slog</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
        <span class="token keyword">if</span> self<span class="token punctuation">.</span>savelog <span class="token punctuation">:</span>
            rename<span class="token punctuation">(</span>self<span class="token punctuation">.</span>logpath<span class="token operator">+</span><span class="token string">'log.log'</span><span class="token punctuation">,</span> self<span class="token punctuation">.</span>logpath<span class="token operator">+</span>self<span class="token punctuation">.</span>sn<span class="token operator">+</span><span class="token string">'.log'</span><span class="token punctuation">)</span>
        <span class="token keyword">else</span> <span class="token punctuation">:</span>
            remove<span class="token punctuation">(</span>self<span class="token punctuation">.</span>logpath<span class="token operator">+</span><span class="token string">'log.log'</span><span class="token punctuation">)</span>
            
    <span class="token keyword">def</span> <span class="token function">set2pass</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
        self<span class="token punctuation">.</span>resultvar<span class="token punctuation">.</span><span class="token builtin">set</span><span class="token punctuation">(</span><span class="token string">"Pass"</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>resL<span class="token punctuation">.</span>config<span class="token punctuation">(</span>foreground<span class="token operator">=</span><span class="token string">"green"</span><span class="token punctuation">)</span>
    <span class="token keyword">def</span> <span class="token function">set2fail</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
        self<span class="token punctuation">.</span>resultvar<span class="token punctuation">.</span><span class="token builtin">set</span><span class="token punctuation">(</span><span class="token string">"Fail"</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>resL<span class="token punctuation">.</span>config<span class="token punctuation">(</span>foreground<span class="token operator">=</span><span class="token string">"red"</span><span class="token punctuation">)</span>
    <span class="token keyword">def</span> <span class="token function">set2ready</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
        self<span class="token punctuation">.</span>resultvar<span class="token punctuation">.</span><span class="token builtin">set</span><span class="token punctuation">(</span><span class="token string">"Ready"</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>resL<span class="token punctuation">.</span>config<span class="token punctuation">(</span>foreground<span class="token operator">=</span><span class="token string">"gray"</span><span class="token punctuation">)</span>
    <span class="token keyword">def</span> <span class="token function">turn2ios</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
        self<span class="token punctuation">.</span>initialize<span class="token punctuation">(</span><span class="token punctuation">)</span>
        port<span class="token operator">=</span>self<span class="token punctuation">.</span>getport<span class="token punctuation">(</span><span class="token punctuation">)</span>
        <span class="token keyword">if</span> <span class="token operator">not</span> port<span class="token punctuation">:</span>
            self<span class="token punctuation">.</span>log<span class="token punctuation">(</span><span class="token string">"Cant find Port, Pls check Spartan"</span><span class="token punctuation">)</span>
            self<span class="token punctuation">.</span>set2fail<span class="token punctuation">(</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>updateinfo<span class="token punctuation">(</span><span class="token punctuation">)</span>
        <span class="token keyword">if</span> self<span class="token punctuation">.</span>mode <span class="token operator">==</span> <span class="token string">':-)'</span><span class="token punctuation">:</span>
            cmdname<span class="token operator">=</span>self<span class="token punctuation">.</span>sku<span class="token operator">+</span><span class="token string">"diags2ios"</span>
            logs<span class="token operator">=</span>self<span class="token punctuation">.</span>cmd<span class="token punctuation">(</span>cmdname<span class="token punctuation">)</span>
            self<span class="token punctuation">.</span>set2pass<span class="token punctuation">(</span><span class="token punctuation">)</span>
        <span class="token keyword">elif</span> self<span class="token punctuation">.</span>mode <span class="token operator">==</span> <span class="token string">'root#'</span><span class="token punctuation">:</span>
            cmdname<span class="token operator">=</span>self<span class="token punctuation">.</span>sku<span class="token operator">+</span><span class="token string">"ios2ios"</span>
            logs<span class="token operator">=</span>self<span class="token punctuation">.</span>cmd<span class="token punctuation">(</span>cmdname<span class="token punctuation">)</span>
            self<span class="token punctuation">.</span>set2pass<span class="token punctuation">(</span><span class="token punctuation">)</span>
        <span class="token keyword">else</span> <span class="token punctuation">:</span>
            self<span class="token punctuation">.</span>log<span class="token punctuation">(</span><span class="token string">"Unknown mode, Pls reboot and re-try"</span><span class="token punctuation">)</span>
            self<span class="token punctuation">.</span>set2fail<span class="token punctuation">(</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>slog<span class="token punctuation">(</span><span class="token punctuation">)</span>
    <span class="token keyword">def</span> <span class="token function">turn2diags</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
        self<span class="token punctuation">.</span>initialize<span class="token punctuation">(</span><span class="token punctuation">)</span>
        port<span class="token operator">=</span>self<span class="token punctuation">.</span>getport<span class="token punctuation">(</span><span class="token punctuation">)</span>
        <span class="token keyword">if</span> <span class="token operator">not</span> port<span class="token punctuation">:</span>
            self<span class="token punctuation">.</span>log<span class="token punctuation">(</span><span class="token string">"Cant find Port, Pls check Spartan"</span><span class="token punctuation">)</span>
            self<span class="token punctuation">.</span>set2fail<span class="token punctuation">(</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>updateinfo<span class="token punctuation">(</span><span class="token punctuation">)</span>
        <span class="token keyword">if</span> self<span class="token punctuation">.</span>mode <span class="token operator">==</span> <span class="token string">':-)'</span><span class="token punctuation">:</span>
            self<span class="token punctuation">.</span>log<span class="token punctuation">(</span><span class="token string">"Already in diags mode"</span><span class="token punctuation">)</span>
            self<span class="token punctuation">.</span>set2pass<span class="token punctuation">(</span><span class="token punctuation">)</span>
        <span class="token keyword">elif</span> self<span class="token punctuation">.</span>mode <span class="token operator">==</span> <span class="token string">'root#'</span><span class="token punctuation">:</span>
            cmdname<span class="token operator">=</span><span class="token string">"ios2diags"</span>
            logs<span class="token operator">=</span>self<span class="token punctuation">.</span>cmd<span class="token punctuation">(</span>cmdname<span class="token punctuation">)</span>
            self<span class="token punctuation">.</span>set2pass<span class="token punctuation">(</span><span class="token punctuation">)</span>
        <span class="token keyword">else</span> <span class="token punctuation">:</span>
            self<span class="token punctuation">.</span>log<span class="token punctuation">(</span><span class="token string">"Unknown mode, Pls reboot and re-try"</span><span class="token punctuation">)</span>
            self<span class="token punctuation">.</span>set2fail<span class="token punctuation">(</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>slog<span class="token punctuation">(</span><span class="token punctuation">)</span>
    <span class="token keyword">def</span> <span class="token function">turn2rec</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
        self<span class="token punctuation">.</span>initialize<span class="token punctuation">(</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>set2fail<span class="token punctuation">(</span><span class="token punctuation">)</span>
        <span class="token comment"># port=self.getport()</span>
        <span class="token comment"># if not port:</span>
        <span class="token comment">#     self.log("Cant find Port, Pls check Spartan")</span>
        <span class="token comment">#     self.set2fail()</span>
        <span class="token comment"># self.updateinfo()</span>
        <span class="token comment"># if self.mode == ':-)':</span>
        <span class="token comment">#     self.log("Already in diags mode")</span>
        <span class="token comment">#     self.set2pass()</span>
        <span class="token comment"># elif self.mode == 'root#':</span>
        <span class="token comment">#     cmdname=self.sku+"ios2ios"</span>
        <span class="token comment">#     logs=self.cmd(cmdname)</span>
        <span class="token comment">#     self.set2pass()</span>
        <span class="token comment"># else :</span>
        <span class="token comment">#     self.log("Unknown mode, Pls reboot and re-try")</span>
        <span class="token comment">#     self.set2fail()</span>
        <span class="token comment"># self.slog()</span>
    <span class="token keyword">def</span> <span class="token function">chkbootargs</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
        self<span class="token punctuation">.</span>initialize<span class="token punctuation">(</span><span class="token punctuation">)</span>
        port<span class="token operator">=</span>self<span class="token punctuation">.</span>getport<span class="token punctuation">(</span><span class="token punctuation">)</span>
        <span class="token keyword">if</span> <span class="token operator">not</span> port<span class="token punctuation">:</span>
            self<span class="token punctuation">.</span>log<span class="token punctuation">(</span><span class="token string">"Cant find Port, Pls check Spartan"</span><span class="token punctuation">)</span>
            self<span class="token punctuation">.</span>set2fail<span class="token punctuation">(</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>updateinfo<span class="token punctuation">(</span><span class="token punctuation">)</span>
        <span class="token keyword">if</span> self<span class="token punctuation">.</span>mode <span class="token operator">==</span> <span class="token string">':-)'</span><span class="token punctuation">:</span>
            logs<span class="token operator">=</span>self<span class="token punctuation">.</span>cmd<span class="token punctuation">(</span><span class="token string">"diagschkargs"</span><span class="token punctuation">)</span>
            argsname<span class="token operator">=</span>self<span class="token punctuation">.</span>sku<span class="token operator">+</span><span class="token string">"bootargs"</span>
            res<span class="token operator">=</span>search<span class="token punctuation">(</span>self<span class="token punctuation">.</span>cfg<span class="token punctuation">[</span>argsname<span class="token punctuation">]</span><span class="token punctuation">,</span> logs<span class="token punctuation">,</span>flags<span class="token operator">=</span><span class="token number">0</span><span class="token punctuation">)</span>
            <span class="token keyword">if</span> res<span class="token punctuation">:</span>
                self<span class="token punctuation">.</span>set2pass<span class="token punctuation">(</span><span class="token punctuation">)</span>
            <span class="token keyword">else</span><span class="token punctuation">:</span>
                self<span class="token punctuation">.</span>set2fail<span class="token punctuation">(</span><span class="token punctuation">)</span>
            
        <span class="token keyword">elif</span> self<span class="token punctuation">.</span>mode <span class="token operator">==</span> <span class="token string">'root#'</span><span class="token punctuation">:</span>
            logs<span class="token operator">=</span>self<span class="token punctuation">.</span>cmd<span class="token punctuation">(</span><span class="token string">"ioschkargs"</span><span class="token punctuation">)</span>
            argsname<span class="token operator">=</span>self<span class="token punctuation">.</span>sku<span class="token operator">+</span><span class="token string">"bootargs"</span>
            <span class="token keyword">print</span><span class="token punctuation">(</span>argsname<span class="token punctuation">)</span>
            res<span class="token operator">=</span>search<span class="token punctuation">(</span>self<span class="token punctuation">.</span>cfg<span class="token punctuation">[</span>argsname<span class="token punctuation">]</span><span class="token punctuation">,</span> logs<span class="token punctuation">,</span>flags<span class="token operator">=</span><span class="token number">0</span><span class="token punctuation">)</span>
            <span class="token keyword">print</span><span class="token punctuation">(</span>res<span class="token punctuation">)</span>
            <span class="token keyword">if</span> res<span class="token punctuation">:</span>
                self<span class="token punctuation">.</span>set2pass<span class="token punctuation">(</span><span class="token punctuation">)</span>
            <span class="token keyword">else</span><span class="token punctuation">:</span>
                self<span class="token punctuation">.</span>set2fail<span class="token punctuation">(</span><span class="token punctuation">)</span>
        <span class="token keyword">else</span> <span class="token punctuation">:</span>
            self<span class="token punctuation">.</span>log<span class="token punctuation">(</span><span class="token string">"Unknown mode, Pls reboot and re-try"</span><span class="token punctuation">)</span>
            self<span class="token punctuation">.</span>set2fail<span class="token punctuation">(</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>slog<span class="token punctuation">(</span><span class="token punctuation">)</span>
    <span class="token keyword">def</span> <span class="token function">getsn</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
        self<span class="token punctuation">.</span>initialize<span class="token punctuation">(</span><span class="token punctuation">)</span>
        <span class="token keyword">if</span> self<span class="token punctuation">.</span>sn<span class="token punctuation">:</span>
            messagebox<span class="token punctuation">.</span>showinfo<span class="token punctuation">(</span><span class="token string">"P"</span><span class="token punctuation">,</span> f<span class="token string">"unit SN: {self.sn}"</span><span class="token punctuation">)</span>
            self<span class="token punctuation">.</span>log<span class="token punctuation">(</span><span class="token string">"Unit SN: "</span><span class="token operator">+</span>self<span class="token punctuation">.</span>sn<span class="token punctuation">)</span>
            <span class="token keyword">return</span>
        port<span class="token operator">=</span>self<span class="token punctuation">.</span>getport<span class="token punctuation">(</span><span class="token punctuation">)</span>
        <span class="token keyword">if</span> <span class="token operator">not</span> port<span class="token punctuation">:</span>
            self<span class="token punctuation">.</span>log<span class="token punctuation">(</span><span class="token string">"Cant find Port, Pls check Spartan"</span><span class="token punctuation">)</span>
            self<span class="token punctuation">.</span>set2fail<span class="token punctuation">(</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>updateinfo<span class="token punctuation">(</span><span class="token punctuation">)</span>
        messagebox<span class="token punctuation">.</span>showinfo<span class="token punctuation">(</span><span class="token string">"P"</span><span class="token punctuation">,</span> f<span class="token string">"unit SN: {self.sn}"</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>log<span class="token punctuation">(</span><span class="token string">"Unit SN: "</span><span class="token operator">+</span>self<span class="token punctuation">.</span>sn<span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>slog<span class="token punctuation">(</span><span class="token punctuation">)</span>
    <span class="token keyword">def</span> <span class="token function">cleanlog</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
        self<span class="token punctuation">.</span>initialize<span class="token punctuation">(</span><span class="token punctuation">)</span>
        port<span class="token operator">=</span>self<span class="token punctuation">.</span>getport<span class="token punctuation">(</span><span class="token punctuation">)</span>
        <span class="token keyword">if</span> <span class="token operator">not</span> port<span class="token punctuation">:</span>
            self<span class="token punctuation">.</span>log<span class="token punctuation">(</span><span class="token string">"Cant find Port, Pls check Spartan"</span><span class="token punctuation">)</span>
            self<span class="token punctuation">.</span>set2fail<span class="token punctuation">(</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>updateinfo<span class="token punctuation">(</span><span class="token punctuation">)</span>
        <span class="token keyword">if</span> self<span class="token punctuation">.</span>mode <span class="token operator">==</span> <span class="token string">':-)'</span><span class="token punctuation">:</span>
            self<span class="token punctuation">.</span>log<span class="token punctuation">(</span><span class="token string">"Pls change to IOS at first"</span><span class="token punctuation">)</span>
            self<span class="token punctuation">.</span>set2fail<span class="token punctuation">(</span><span class="token punctuation">)</span>
        <span class="token keyword">elif</span> self<span class="token punctuation">.</span>mode <span class="token operator">==</span> <span class="token string">'root#'</span><span class="token punctuation">:</span>
            cmdname<span class="token operator">=</span><span class="token string">'rmlogs'</span>
            logs<span class="token operator">=</span>self<span class="token punctuation">.</span>cmd<span class="token punctuation">(</span>cmdname<span class="token punctuation">)</span>
            self<span class="token punctuation">.</span>set2pass<span class="token punctuation">(</span><span class="token punctuation">)</span>
        <span class="token keyword">else</span> <span class="token punctuation">:</span>
            self<span class="token punctuation">.</span>log<span class="token punctuation">(</span><span class="token string">"Unknown mode, Pls reboot and re-try"</span><span class="token punctuation">)</span>
            self<span class="token punctuation">.</span>set2fail<span class="token punctuation">(</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>slog<span class="token punctuation">(</span><span class="token punctuation">)</span>
    <span class="token keyword">def</span> <span class="token function">makecom</span><span class="token punctuation">(</span>self<span class="token punctuation">,</span>tag<span class="token operator">=</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
        self<span class="token punctuation">.</span>initialize<span class="token punctuation">(</span><span class="token punctuation">)</span>
        <span class="token comment">#  _mkgu(self, fpath,  target):</span>
        port<span class="token operator">=</span>self<span class="token punctuation">.</span>getport<span class="token punctuation">(</span><span class="token punctuation">)</span>
        <span class="token keyword">if</span> <span class="token operator">not</span> port<span class="token punctuation">:</span>
            self<span class="token punctuation">.</span>log<span class="token punctuation">(</span><span class="token string">"Cant find Port, Pls check Spartan"</span><span class="token punctuation">)</span>
            self<span class="token punctuation">.</span>set2fail<span class="token punctuation">(</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>updateinfo<span class="token punctuation">(</span><span class="token punctuation">)</span>
        <span class="token keyword">if</span> self<span class="token punctuation">.</span>mode <span class="token operator">==</span> <span class="token string">':-)'</span><span class="token punctuation">:</span>
            self<span class="token punctuation">.</span>log<span class="token punctuation">(</span><span class="token string">"Pls change to IOS at first"</span><span class="token punctuation">)</span>
            self<span class="token punctuation">.</span>set2fail<span class="token punctuation">(</span><span class="token punctuation">)</span>
        <span class="token keyword">elif</span> self<span class="token punctuation">.</span>mode <span class="token operator">==</span> <span class="token string">'root#'</span><span class="token punctuation">:</span>
            <span class="token comment"># check SN in GUSN list</span>
            <span class="token keyword">if</span> self<span class="token punctuation">.</span>sn <span class="token operator">not</span> <span class="token keyword">in</span> self<span class="token punctuation">.</span>gusn<span class="token punctuation">:</span>
                self<span class="token punctuation">.</span>log<span class="token punctuation">(</span><span class="token string">"This unit isnt GU"</span><span class="token punctuation">)</span>
                self<span class="token punctuation">.</span>set2fail<span class="token punctuation">(</span><span class="token punctuation">)</span>
                <span class="token keyword">return</span>
            dp<span class="token operator">=</span>self<span class="token punctuation">.</span>choosefolder<span class="token punctuation">(</span><span class="token punctuation">)</span>
            cmd<span class="token operator">=</span><span class="token string">'find "'</span><span class="token operator">+</span>dp<span class="token operator">+</span><span class="token string">'" -type d -name "'</span><span class="token operator">+</span>self<span class="token punctuation">.</span>sn<span class="token operator">+</span><span class="token string">'"'</span>
            snpath<span class="token operator">=</span>run<span class="token punctuation">(</span>cmd<span class="token punctuation">,</span>shell<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">,</span>stdout<span class="token operator">=</span>PIPE<span class="token punctuation">,</span>stderr<span class="token operator">=</span>PIPE<span class="token punctuation">,</span>encoding<span class="token operator">=</span><span class="token string">"utf-8"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>stdout<span class="token punctuation">.</span>split<span class="token punctuation">(</span><span class="token string">'\n'</span><span class="token punctuation">)</span><span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span>
            fpath<span class="token operator">=</span>snpath<span class="token operator">+</span><span class="token string">"/"</span>
            <span class="token keyword">print</span><span class="token punctuation">(</span>fpath<span class="token punctuation">)</span>
            <span class="token keyword">if</span> tag <span class="token operator">==</span> <span class="token number">1</span><span class="token punctuation">:</span>
                self<span class="token punctuation">.</span>cmd<span class="token punctuation">(</span><span class="token string">"mkcal"</span><span class="token punctuation">)</span>
                mkname<span class="token operator">=</span><span class="token string">"mkcal"</span>
            <span class="token keyword">else</span><span class="token punctuation">:</span>
                mkname<span class="token operator">=</span><span class="token string">"mk"</span><span class="token operator">+</span>self<span class="token punctuation">.</span>sku
            <span class="token keyword">print</span><span class="token punctuation">(</span>self<span class="token punctuation">.</span>cfg<span class="token punctuation">[</span>mkname<span class="token punctuation">]</span><span class="token punctuation">)</span>
            <span class="token keyword">for</span> i <span class="token keyword">in</span> <span class="token builtin">iter</span><span class="token punctuation">(</span>self<span class="token punctuation">.</span>cfg<span class="token punctuation">[</span>mkname<span class="token punctuation">]</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
                self<span class="token punctuation">.</span>_mkgu<span class="token punctuation">(</span>fpath<span class="token punctuation">,</span>i<span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span><span class="token punctuation">,</span>i<span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">]</span><span class="token punctuation">)</span>
                sleep<span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">)</span>
            self<span class="token punctuation">.</span>set2pass<span class="token punctuation">(</span><span class="token punctuation">)</span>
        <span class="token keyword">else</span> <span class="token punctuation">:</span>
            self<span class="token punctuation">.</span>log<span class="token punctuation">(</span><span class="token string">"Unknown mode, Pls reboot and re-try"</span><span class="token punctuation">)</span>
            self<span class="token punctuation">.</span>set2fail<span class="token punctuation">(</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>slog<span class="token punctuation">(</span><span class="token punctuation">)</span>
    <span class="token comment"># def mytest(self,tag=0):</span>
    <span class="token comment">#     if tag == 1:</span>
    <span class="token comment">#         # self.cmd("mkcal")</span>
    <span class="token comment">#         mkname="mkcal"</span>
    <span class="token comment">#     else:</span>
    <span class="token comment">#         mkname="mkCELL"</span>
    <span class="token comment">#     for i in iter(self.cfg[mkname]):</span>
    <span class="token comment">#         self._mkgu(i[0],i[1])</span>
    <span class="token comment">#         sleep(1)</span>
    <span class="token keyword">def</span> <span class="token function">makegu</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
        self<span class="token punctuation">.</span>makecom<span class="token punctuation">(</span><span class="token punctuation">)</span>
    <span class="token keyword">def</span> <span class="token function">makecal</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
        self<span class="token punctuation">.</span>makecom<span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">)</span>
        
    <span class="token comment"># def getHostPort(self):</span>
    <span class="token comment">#     self.frame2 = tk.Toplevel(self.master)</span>
    <span class="token comment">#     self.frame2.title("Config")</span>
    <span class="token comment">#     parent_x = self.master.winfo_rootx()</span>
    <span class="token comment">#     parent_y = self.master.winfo_rooty()</span>
    <span class="token comment">#     parent_width = self.master.winfo_width()</span>
    <span class="token comment">#     parent_height = self.master.winfo_height()</span>
    <span class="token comment">#     print(parent_y,parent_x,parent_width,parent_height)</span>
    <span class="token comment">#     x = 0</span>
    <span class="token comment">#     y = 0</span>
    <span class="token comment">#     self.frame2.geometry(f"{parent_width}x{parent_height}+{x}+{y}")</span>
    <span class="token comment">#     self.hostvar= tk.StringVar()</span>
    <span class="token comment">#     self.portvar= tk.StringVar()</span>
    <span class="token comment">#     ttk.Label(self.frame2, text="Host", width=10).grid(column=0,row=0)</span>
    <span class="token comment">#     hostE= ttk.Entry(self.frame2,textvariable=self.hostvar, width=20)</span>
    <span class="token comment">#     hostE.grid(column=1, row=0)</span>
    <span class="token comment">#     ttk.Label(self.frame2, text="Port", width=10).grid(column=0,row=1)</span>
    <span class="token comment">#     portE= ttk.Entry(self.frame2,textvariable=self.portvar, width=20)</span>
    <span class="token comment">#     portE.grid(column=1, row=1)</span>
    <span class="token comment">#     ttk.Button(self.frame2, text="submit", command=self.updateHost).grid(column=0,row=2,columnspan=2)</span>
    <span class="token keyword">def</span> <span class="token function">getPasswd</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
        <span class="token comment"># get passwd</span>
        self<span class="token punctuation">.</span>dialog<span class="token operator">=</span> tk<span class="token punctuation">.</span>Toplevel<span class="token punctuation">(</span>self<span class="token punctuation">.</span>master<span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>dialog<span class="token punctuation">.</span>title<span class="token punctuation">(</span><span class="token string">"Enter Password"</span><span class="token punctuation">)</span>
        parent_x <span class="token operator">=</span> self<span class="token punctuation">.</span>master<span class="token punctuation">.</span>winfo_rootx<span class="token punctuation">(</span><span class="token punctuation">)</span>
        parent_y <span class="token operator">=</span> self<span class="token punctuation">.</span>master<span class="token punctuation">.</span>winfo_rooty<span class="token punctuation">(</span><span class="token punctuation">)</span>
        parent_width <span class="token operator">=</span> self<span class="token punctuation">.</span>master<span class="token punctuation">.</span>winfo_width<span class="token punctuation">(</span><span class="token punctuation">)</span>
        parent_height <span class="token operator">=</span> self<span class="token punctuation">.</span>master<span class="token punctuation">.</span>winfo_height<span class="token punctuation">(</span><span class="token punctuation">)</span>
        dialog_width <span class="token operator">=</span> <span class="token number">200</span>
        dialog_height <span class="token operator">=</span> <span class="token number">100</span>
        x <span class="token operator">=</span> parent_x <span class="token operator">+</span> <span class="token punctuation">(</span>parent_width <span class="token operator">-</span> dialog_width<span class="token punctuation">)</span> <span class="token operator">//</span> <span class="token number">2</span>
        y <span class="token operator">=</span> parent_y <span class="token operator">+</span> <span class="token punctuation">(</span>parent_height <span class="token operator">-</span> dialog_height<span class="token punctuation">)</span> <span class="token operator">//</span> <span class="token number">2</span>
        self<span class="token punctuation">.</span>dialog<span class="token punctuation">.</span>geometry<span class="token punctuation">(</span>f<span class="token string">"{dialog_width}x{dialog_height}+{x}+{y}"</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>pswdvar<span class="token operator">=</span> tk<span class="token punctuation">.</span>StringVar<span class="token punctuation">(</span><span class="token punctuation">)</span>
        pswdEntry<span class="token operator">=</span> ttk<span class="token punctuation">.</span>Entry<span class="token punctuation">(</span>self<span class="token punctuation">.</span>dialog<span class="token punctuation">,</span> show<span class="token operator">=</span><span class="token string">"*"</span><span class="token punctuation">,</span> textvariable<span class="token operator">=</span>self<span class="token punctuation">.</span>pswdvar<span class="token punctuation">)</span>
        pswdEntry<span class="token punctuation">.</span>focus_set<span class="token punctuation">(</span><span class="token punctuation">)</span>
        pswdEntry<span class="token punctuation">.</span>bind<span class="token punctuation">(</span><span class="token string">'&lt;Return&gt;'</span><span class="token punctuation">,</span>self<span class="token punctuation">.</span>checkPswd<span class="token punctuation">)</span>
        pswdEntry<span class="token punctuation">.</span>pack<span class="token punctuation">(</span>padx<span class="token operator">=</span><span class="token punctuation">(</span><span class="token number">5</span><span class="token punctuation">,</span><span class="token number">5</span><span class="token punctuation">)</span><span class="token punctuation">,</span> pady<span class="token operator">=</span><span class="token punctuation">(</span><span class="token number">5</span><span class="token punctuation">,</span><span class="token number">5</span><span class="token punctuation">)</span><span class="token punctuation">)</span>
        sb<span class="token operator">=</span>ttk<span class="token punctuation">.</span>Button<span class="token punctuation">(</span>self<span class="token punctuation">.</span>dialog<span class="token punctuation">,</span> text<span class="token operator">=</span><span class="token string">"submit"</span><span class="token punctuation">,</span> command<span class="token operator">=</span>self<span class="token punctuation">.</span>checkPswd<span class="token punctuation">)</span>
        sb<span class="token punctuation">.</span>pack<span class="token punctuation">(</span>pady<span class="token operator">=</span><span class="token punctuation">(</span><span class="token number">5</span><span class="token punctuation">,</span><span class="token number">5</span><span class="token punctuation">)</span><span class="token punctuation">)</span>
    <span class="token keyword">def</span> <span class="token function">choosefolder</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
        directory <span class="token operator">=</span> filedialog<span class="token punctuation">.</span>askdirectory<span class="token punctuation">(</span>
            initialdir<span class="token operator">=</span><span class="token string">"~/Desktop"</span><span class="token punctuation">,</span>
            title<span class="token operator">=</span><span class="token string">"选择一个目录"</span>
        <span class="token punctuation">)</span>
        <span class="token keyword">if</span> directory<span class="token punctuation">:</span>
            <span class="token keyword">print</span><span class="token punctuation">(</span>f<span class="token string">"选择的目录：{directory}"</span><span class="token punctuation">)</span>
            self<span class="token punctuation">.</span>log<span class="token punctuation">(</span>directory<span class="token punctuation">)</span>
            <span class="token keyword">return</span> directory
    <span class="token keyword">def</span> <span class="token function">checkPswd</span><span class="token punctuation">(</span>self<span class="token punctuation">,</span> event<span class="token operator">=</span><span class="token boolean">None</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
        enterpswd<span class="token operator">=</span>self<span class="token punctuation">.</span>pswdvar<span class="token punctuation">.</span>get<span class="token punctuation">(</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>dialog<span class="token punctuation">.</span>destroy<span class="token punctuation">(</span><span class="token punctuation">)</span>
        <span class="token keyword">if</span> enterpswd <span class="token operator">==</span> self<span class="token punctuation">.</span>config<span class="token punctuation">[</span><span class="token string">'password'</span><span class="token punctuation">]</span><span class="token punctuation">:</span>
            self<span class="token punctuation">.</span>getHostPort<span class="token punctuation">(</span><span class="token punctuation">)</span>
        <span class="token keyword">else</span><span class="token punctuation">:</span>
            messagebox<span class="token punctuation">.</span>showinfo<span class="token punctuation">(</span><span class="token string">"P"</span><span class="token punctuation">,</span> f<span class="token string">"Password was wrong,You entered: {enterpswd}"</span><span class="token punctuation">)</span>
            self<span class="token punctuation">.</span>getPasswd<span class="token punctuation">(</span><span class="token punctuation">)</span>
    <span class="token keyword">def</span> <span class="token function">log</span><span class="token punctuation">(</span>self<span class="token punctuation">,</span> message<span class="token punctuation">)</span><span class="token punctuation">:</span>
        self<span class="token punctuation">.</span>log_text<span class="token punctuation">.</span>config<span class="token punctuation">(</span>state<span class="token operator">=</span>tk<span class="token punctuation">.</span>NORMAL<span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>log_text<span class="token punctuation">.</span>insert<span class="token punctuation">(</span>tk<span class="token punctuation">.</span>END<span class="token punctuation">,</span> message<span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>log_text<span class="token punctuation">.</span>config<span class="token punctuation">(</span>state<span class="token operator">=</span>tk<span class="token punctuation">.</span>DISABLED<span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>log_text<span class="token punctuation">.</span>see<span class="token punctuation">(</span>tk<span class="token punctuation">.</span>END<span class="token punctuation">)</span>
    <span class="token keyword">def</span> <span class="token function">getport</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
        cnt<span class="token operator">=</span><span class="token number">0</span>
        <span class="token keyword">while</span> cnt <span class="token operator">&lt;</span> self<span class="token punctuation">.</span>maxcnt<span class="token punctuation">:</span>
            <span class="token keyword">if</span> self<span class="token punctuation">.</span>port <span class="token operator">==</span> <span class="token string">'/dev/'</span> <span class="token punctuation">:</span>
                port<span class="token operator">=</span>run<span class="token punctuation">(</span><span class="token string">'ls /dev/ | grep cu.usb | head -1'</span><span class="token punctuation">,</span>shell<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">,</span>stdout<span class="token operator">=</span>PIPE<span class="token punctuation">,</span>stderr<span class="token operator">=</span>PIPE<span class="token punctuation">,</span>encoding<span class="token operator">=</span><span class="token string">"utf-8"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>stdout<span class="token punctuation">.</span>split<span class="token punctuation">(</span><span class="token string">'\n'</span><span class="token punctuation">)</span><span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span>
                self<span class="token punctuation">.</span>port<span class="token operator">=</span> <span class="token string">'/dev/'</span><span class="token operator">+</span>port
                cnt<span class="token operator">+=</span><span class="token number">1</span>
                sleep<span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">)</span>
            <span class="token keyword">else</span> <span class="token punctuation">:</span>
                <span class="token keyword">break</span>
        <span class="token keyword">return</span> <span class="token boolean">False</span> <span class="token keyword">if</span> self<span class="token punctuation">.</span>port <span class="token operator">==</span> <span class="token string">'/dev/'</span> <span class="token keyword">else</span> self<span class="token punctuation">.</span>port
   
    <span class="token keyword">def</span> <span class="token function">cmd</span><span class="token punctuation">(</span>self<span class="token punctuation">,</span> cmdname<span class="token punctuation">)</span><span class="token punctuation">:</span>
        logs<span class="token operator">=</span><span class="token string">''</span>
        <span class="token keyword">with</span> serial<span class="token punctuation">.</span>Serial<span class="token punctuation">(</span>self<span class="token punctuation">.</span>port<span class="token punctuation">,</span> self<span class="token punctuation">.</span>bandrate<span class="token punctuation">,</span> timeout<span class="token operator">=</span><span class="token number">1</span><span class="token punctuation">)</span> <span class="token keyword">as</span> ser<span class="token punctuation">:</span>
            ss<span class="token operator">=</span>SerialSpawn<span class="token punctuation">(</span>ser<span class="token punctuation">)</span>
            fout<span class="token operator">=</span> <span class="token builtin">open</span><span class="token punctuation">(</span>self<span class="token punctuation">.</span>logpath<span class="token operator">+</span><span class="token string">'log.log'</span><span class="token punctuation">,</span> <span class="token string">'ab'</span><span class="token punctuation">)</span>
            ss<span class="token punctuation">.</span>logfile<span class="token operator">=</span>fout
            ss<span class="token punctuation">.</span><span class="token builtin">buffer</span><span class="token operator">=</span>b<span class="token string">''</span>
            cmd2run<span class="token operator">=</span>self<span class="token punctuation">.</span>cmdlist<span class="token punctuation">[</span>cmdname<span class="token punctuation">]</span>
            cmdlen<span class="token operator">=</span><span class="token builtin">len</span><span class="token punctuation">(</span>cmd2run<span class="token punctuation">)</span>
            <span class="token keyword">for</span> i <span class="token keyword">in</span> <span class="token builtin">iter</span><span class="token punctuation">(</span>cmd2run<span class="token punctuation">)</span><span class="token punctuation">:</span>
                ss<span class="token punctuation">.</span>sendline<span class="token punctuation">(</span>i<span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span><span class="token punctuation">)</span>
                sleep<span class="token punctuation">(</span>i<span class="token punctuation">[</span><span class="token number">2</span><span class="token punctuation">]</span><span class="token punctuation">)</span>
                ss<span class="token punctuation">.</span>expect_exact<span class="token punctuation">(</span>i<span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">]</span><span class="token punctuation">)</span>
                tmp<span class="token operator">=</span>ss<span class="token punctuation">.</span>before<span class="token punctuation">.</span>decode<span class="token punctuation">(</span><span class="token punctuation">)</span>
                self<span class="token punctuation">.</span>log<span class="token punctuation">(</span>tmp<span class="token punctuation">)</span>
                logs<span class="token operator">+=</span>tmp
            sleep<span class="token punctuation">(</span><span class="token number">0.5</span><span class="token punctuation">)</span>
            ss<span class="token punctuation">.</span>close<span class="token punctuation">(</span><span class="token punctuation">)</span>
            <span class="token keyword">return</span> logs
    <span class="token keyword">def</span> <span class="token function">_mkgu</span><span class="token punctuation">(</span>self<span class="token punctuation">,</span>dpath<span class="token punctuation">,</span> fpath<span class="token punctuation">,</span> target<span class="token punctuation">)</span><span class="token punctuation">:</span>
        cmd<span class="token operator">=</span><span class="token string">'system_profiler SPUSBDataType | fgrep -A 10 "iPad" | fgrep "Location ID" | egrep -o "0x[0-9]{8}"'</span>
        ipadport<span class="token operator">=</span>run<span class="token punctuation">(</span>cmd<span class="token punctuation">,</span>shell<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">,</span>stdout<span class="token operator">=</span>PIPE<span class="token punctuation">,</span>stderr<span class="token operator">=</span>PIPE<span class="token punctuation">,</span>encoding<span class="token operator">=</span><span class="token string">"utf-8"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>stdout<span class="token punctuation">.</span>split<span class="token punctuation">(</span><span class="token string">'\n'</span><span class="token punctuation">)</span><span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span>
        cmd<span class="token operator">=</span><span class="token string">'./copyUnrestricted -w -u '</span><span class="token operator">+</span>ipadport<span class="token operator">+</span><span class="token string">' -s "'</span><span class="token operator">+</span>dpath<span class="token operator">+</span>fpath<span class="token operator">+</span><span class="token string">'" -t "'</span><span class="token operator">+</span>target<span class="token operator">+</span><span class="token string">'"'</span>
        <span class="token keyword">print</span><span class="token punctuation">(</span>cmd<span class="token punctuation">)</span>
        logs<span class="token operator">=</span>run<span class="token punctuation">(</span>cmd<span class="token punctuation">,</span>shell<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">,</span>stdout<span class="token operator">=</span>PIPE<span class="token punctuation">,</span>stderr<span class="token operator">=</span>STDOUT<span class="token punctuation">,</span>encoding<span class="token operator">=</span><span class="token string">"utf-8"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>stdout
        self<span class="token punctuation">.</span>log<span class="token punctuation">(</span>logs<span class="token punctuation">)</span>
        <span class="token keyword">return</span> logs
    <span class="token keyword">def</span> <span class="token function">updateinfo</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
        <span class="token keyword">with</span> serial<span class="token punctuation">.</span>Serial<span class="token punctuation">(</span>self<span class="token punctuation">.</span>port<span class="token punctuation">,</span> self<span class="token punctuation">.</span>bandrate<span class="token punctuation">,</span> timeout<span class="token operator">=</span><span class="token number">1</span><span class="token punctuation">)</span> <span class="token keyword">as</span> ser<span class="token punctuation">:</span>
            ss<span class="token operator">=</span>SerialSpawn<span class="token punctuation">(</span>ser<span class="token punctuation">)</span>
            fout<span class="token operator">=</span> <span class="token builtin">open</span><span class="token punctuation">(</span>self<span class="token punctuation">.</span>logpath<span class="token operator">+</span><span class="token string">'log.log'</span><span class="token punctuation">,</span> <span class="token string">'ab'</span><span class="token punctuation">)</span>
            ss<span class="token punctuation">.</span>logfile<span class="token operator">=</span>fout
            cnt<span class="token operator">=</span> <span class="token number">0</span>
            <span class="token keyword">while</span> cnt <span class="token operator">&lt;</span> self<span class="token punctuation">.</span>maxcnt <span class="token punctuation">:</span>
                ss<span class="token punctuation">.</span>sendline<span class="token punctuation">(</span><span class="token punctuation">)</span>
                i<span class="token operator">=</span>ss<span class="token punctuation">.</span>expect_exact<span class="token punctuation">(</span>self<span class="token punctuation">.</span>explist<span class="token punctuation">)</span>
                <span class="token keyword">if</span> i <span class="token operator">==</span> <span class="token number">0</span><span class="token punctuation">:</span>
                    ss<span class="token punctuation">.</span>sendline<span class="token punctuation">(</span>self<span class="token punctuation">.</span>login<span class="token punctuation">)</span>
                    sleep<span class="token punctuation">(</span><span class="token number">0.5</span><span class="token punctuation">)</span>
                    ss<span class="token punctuation">.</span>sendline<span class="token punctuation">(</span>self<span class="token punctuation">.</span>passwd<span class="token punctuation">)</span>
                    cnt<span class="token operator">+=</span><span class="token number">1</span>
                <span class="token keyword">elif</span> i <span class="token operator">&lt;=</span> <span class="token number">2</span><span class="token punctuation">:</span>
                    self<span class="token punctuation">.</span>mode<span class="token operator">=</span> self<span class="token punctuation">.</span>explist<span class="token punctuation">[</span>i<span class="token punctuation">]</span>
                    <span class="token keyword">break</span>
                <span class="token keyword">else</span><span class="token punctuation">:</span>
                    <span class="token keyword">pass</span>
            cnt<span class="token operator">=</span><span class="token number">0</span>
            mode<span class="token operator">=</span>self<span class="token punctuation">.</span>mode
            logs<span class="token operator">=</span><span class="token string">''</span>
            <span class="token keyword">if</span> mode <span class="token operator">==</span> <span class="token string">':-)'</span><span class="token punctuation">:</span>
                cmdname<span class="token operator">=</span><span class="token string">'diagsgetinfo'</span>
                self<span class="token punctuation">.</span>cmd<span class="token punctuation">(</span>cmdname<span class="token punctuation">)</span>
                logs<span class="token operator">=</span>self<span class="token punctuation">.</span>cmd<span class="token punctuation">(</span>cmdname<span class="token punctuation">)</span>
            <span class="token keyword">elif</span> mode <span class="token operator">==</span> <span class="token string">'root#'</span><span class="token punctuation">:</span>
                cmdname<span class="token operator">=</span><span class="token string">'iosgetinfo'</span>
                logs<span class="token operator">=</span>self<span class="token punctuation">.</span>cmd<span class="token punctuation">(</span>cmdname<span class="token punctuation">)</span>
            <span class="token comment"># elif mode == '] \r\n':</span>
            <span class="token comment">#     cmdname='recoverygetinfo'</span>
            <span class="token comment">#     print(cmdname)</span>
            <span class="token comment">#     logs=self.cmd(cmdname,mode,5)</span>
            <span class="token keyword">else</span> <span class="token punctuation">:</span>
                <span class="token keyword">return</span> <span class="token boolean">False</span>
            sn<span class="token operator">=</span> search<span class="token punctuation">(</span><span class="token string">'[A-Z0-9]{10}'</span><span class="token punctuation">,</span> logs<span class="token punctuation">,</span>flags<span class="token operator">=</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">.</span>group<span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span>
            sku<span class="token operator">=</span> search<span class="token punctuation">(</span><span class="token string">'[jJ][0-9]{3}'</span><span class="token punctuation">,</span> logs<span class="token punctuation">,</span>flags<span class="token operator">=</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">.</span>group<span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">.</span>upper<span class="token punctuation">(</span><span class="token punctuation">)</span>
            <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">"sn: "</span><span class="token punctuation">,</span>sn<span class="token punctuation">)</span>
            <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">"sku: "</span><span class="token punctuation">,</span>sku<span class="token punctuation">)</span>
            <span class="token keyword">if</span> sn <span class="token punctuation">:</span>
                self<span class="token punctuation">.</span>sn<span class="token operator">=</span> sn
            <span class="token keyword">if</span> sku <span class="token operator">==</span> self<span class="token punctuation">.</span>wifi<span class="token punctuation">:</span>
                self<span class="token punctuation">.</span>sku <span class="token operator">=</span> <span class="token string">"WIFI"</span>
            <span class="token keyword">elif</span> sku <span class="token operator">==</span> self<span class="token punctuation">.</span>cell<span class="token punctuation">:</span>
                self<span class="token punctuation">.</span>sku <span class="token operator">=</span> <span class="token string">"CELL"</span>
            <span class="token keyword">else</span> <span class="token punctuation">:</span>
                <span class="token comment"># cant identify project code</span>
                <span class="token keyword">pass</span>
            ss<span class="token punctuation">.</span>close<span class="token punctuation">(</span><span class="token punctuation">)</span>
<span class="token keyword">def</span> <span class="token function">main</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
    root <span class="token operator">=</span> tk<span class="token punctuation">.</span>Tk<span class="token punctuation">(</span><span class="token punctuation">)</span>
    client_gui <span class="token operator">=</span> ClientGUI<span class="token punctuation">(</span>root<span class="token punctuation">)</span>
    root<span class="token punctuation">.</span>mainloop<span class="token punctuation">(</span><span class="token punctuation">)</span>
<span class="token keyword">if</span> __name__ <span class="token operator">==</span> <span class="token string">"__main__"</span><span class="token punctuation">:</span>
    main<span class="token punctuation">(</span><span class="token punctuation">)</span>
</code></pre>
<pre class=" language-json"><code class="prism  language-json"><span class="token punctuation">{</span><span class="token string">"config"</span><span class="token punctuation">:</span><span class="token punctuation">{</span>
	<span class="token string">"WIFI"</span><span class="token punctuation">:</span><span class="token string">"J481"</span><span class="token punctuation">,</span>
	<span class="token string">"CELL"</span><span class="token punctuation">:</span><span class="token string">"J482"</span><span class="token punctuation">,</span>
	<span class="token string">"login"</span><span class="token punctuation">:</span><span class="token string">"root"</span><span class="token punctuation">,</span>
	<span class="token string">"passwd"</span><span class="token punctuation">:</span><span class="token string">"alpine"</span><span class="token punctuation">,</span>
	<span class="token string">"bandrate"</span><span class="token punctuation">:</span> <span class="token number">115200</span><span class="token punctuation">,</span>
	<span class="token string">"defaultsw"</span><span class="token punctuation">:</span><span class="token string">"WIFIdiags2ios"</span><span class="token punctuation">,</span>
	<span class="token string">"autotest"</span><span class="token punctuation">:</span><span class="token string">"False"</span><span class="token punctuation">,</span>
	<span class="token string">"maxcnt"</span><span class="token punctuation">:</span> <span class="token number">3</span><span class="token punctuation">,</span>
	<span class="token string">"savelog"</span><span class="token punctuation">:</span><span class="token number">1</span><span class="token punctuation">,</span>
	<span class="token string">"WIFIbootargs"</span><span class="token punctuation">:</span><span class="token string">"debug=0x104146 serial=0x13 gpu_panic_on_recovery=1 apfs_edt_rw_mount=1 wlan-olyhal-abort=1 amfi_get_out_of_my_way=1 launchctl_enforce_codesign=0 amfi_unrestrict_task_for_pid=1 amfi_allow_any_signature=1 dk=0x8001 wdt=-1 cc.debug.enable=1 max_task_pmem=0 wlan.debug.abort-init=2 mtk.wlan.manufacture=1 wlan.factory=0x93 ota ioimageloader.debug.csr-access=1"</span><span class="token punctuation">,</span>
	<span class="token string">"CELLbootargs"</span><span class="token punctuation">:</span><span class="token string">"debug=0x104146 serial=0x13 gpu_panic_on_recovery=1 apfs_edt_rw_mount=1 ota wdt=-1 wlan.factory=0x93"</span><span class="token punctuation">,</span>
	<span class="token string">"gusn"</span><span class="token punctuation">:</span><span class="token punctuation">[</span><span class="token string">"K6R2F6N4Y6"</span><span class="token punctuation">,</span><span class="token string">"MG9XW1VQ2M"</span><span class="token punctuation">,</span> <span class="token string">"LGKJV0RWX1"</span><span class="token punctuation">,</span> <span class="token string">"G6FPV7PMQQ"</span><span class="token punctuation">,</span> <span class="token string">"JNJKQX9VMW"</span><span class="token punctuation">,</span> <span class="token string">"MQ6X7K0F2T"</span><span class="token punctuation">,</span> <span class="token string">"HJ6L0G0WR3"</span><span class="token punctuation">,</span> <span class="token string">"RFNQCJ4NVC"</span><span class="token punctuation">,</span> <span class="token string">"CT2MHHG2WC"</span><span class="token punctuation">,</span> <span class="token string">"GMCPXPWVVR"</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
	<span class="token string">"mkWIFI"</span><span class="token punctuation">:</span><span class="token punctuation">[</span><span class="token punctuation">[</span><span class="token string">"Alchemy.csv"</span><span class="token punctuation">,</span><span class="token string">"/var/logs/WiPASmini/"</span><span class="token punctuation">]</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
	<span class="token string">"mkCELL"</span><span class="token punctuation">:</span><span class="token punctuation">[</span><span class="token punctuation">[</span><span class="token string">"Alchemy.csv"</span><span class="token punctuation">,</span><span class="token string">"/var/logs/WiPASmini/"</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
		<span class="token punctuation">[</span><span class="token string">"factoryota/Rprad.txt"</span><span class="token punctuation">,</span><span class="token string">"/var/logs/WiPASmini/factoryota/"</span><span class="token punctuation">]</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
	<span class="token string">"mkcal"</span><span class="token punctuation">:</span><span class="token punctuation">[</span>
		<span class="token punctuation">[</span><span class="token string">"factoryota/BCAL.bin"</span><span class="token punctuation">,</span><span class="token string">"/var/root/CALfiles/"</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
		<span class="token punctuation">[</span><span class="token string">"factoryota/OCA3.bin"</span><span class="token punctuation">,</span><span class="token string">"/var/root/CALfiles/"</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
		<span class="token punctuation">[</span><span class="token string">"factoryota/OCAL.bin"</span><span class="token punctuation">,</span><span class="token string">"/var/root/CALfiles/"</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
		<span class="token punctuation">[</span><span class="token string">"factoryota/WCAL.bin"</span><span class="token punctuation">,</span><span class="token string">"/var/root/CALfiles/"</span><span class="token punctuation">]</span>
	<span class="token punctuation">]</span><span class="token punctuation">,</span>
	<span class="token string">"testlist"</span><span class="token punctuation">:</span><span class="token punctuation">{</span>
		<span class="token string">"WIFIdiags2ios"</span><span class="token punctuation">:</span><span class="token punctuation">[</span>
			<span class="token punctuation">[</span><span class="token string">"nvram --set boot-command fsboot"</span><span class="token punctuation">,</span> <span class="token string">":-)"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
			<span class="token punctuation">[</span><span class="token string">"nvram --set boot-args 'debug=0x104146 serial=0x13 gpu_panic_on_recovery=1 apfs_edt_rw_mount=1 wlan-olyhal-abort=1 amfi_get_out_of_my_way=1 launchctl_enforce_codesign=0 amfi_unrestrict_task_for_pid=1 amfi_allow_any_signature=1 dk=0x8001 wdt=-1 cc.debug.enable=1 max_task_pmem=0 wlan.debug.abort-init=2 mtk.wlan.manufacture=1 wlan.factory=0x93 ota ioimageloader.debug.csr-access=1'"</span><span class="token punctuation">,</span> <span class="token string">":-)"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
			<span class="token punctuation">[</span><span class="token string">"nvram --save"</span><span class="token punctuation">,</span> <span class="token string">":-)"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
			<span class="token punctuation">[</span><span class="token string">"reset"</span><span class="token punctuation">,</span> <span class="token string">"reset"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span>
		<span class="token punctuation">]</span><span class="token punctuation">,</span>
		<span class="token string">"CELLdiags2ios"</span><span class="token punctuation">:</span><span class="token punctuation">[</span>
			<span class="token punctuation">[</span><span class="token string">"nvram --set boot-command fsboot"</span><span class="token punctuation">,</span> <span class="token string">":-)"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
			<span class="token punctuation">[</span><span class="token string">"nvram --set boot-args 'debug=0x104146 serial=0x13 gpu_panic_on_recovery=1 apfs_edt_rw_mount=1 ota wdt=-1 wlan.factory=0x93'"</span><span class="token punctuation">,</span> <span class="token string">":-)"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
			<span class="token punctuation">[</span><span class="token string">"nvram --save"</span><span class="token punctuation">,</span> <span class="token string">":-)"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
			<span class="token punctuation">[</span><span class="token string">"reset"</span><span class="token punctuation">,</span> <span class="token string">"reset"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span>
		<span class="token punctuation">]</span><span class="token punctuation">,</span>
		<span class="token string">"WIFIios2ios"</span><span class="token punctuation">:</span><span class="token punctuation">[</span>
			<span class="token punctuation">[</span><span class="token string">"nvram boot-command=fsboot"</span><span class="token punctuation">,</span> <span class="token string">"root#"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
			<span class="token punctuation">[</span><span class="token string">"nvram boot-args='debug=0x104146 serial=0x13 gpu_panic_on_recovery=1 apfs_edt_rw_mount=1 wlan-olyhal-abort=1 amfi_get_out_of_my_way=1 launchctl_enforce_codesign=0 amfi_unrestrict_task_for_pid=1 amfi_allow_any_signature=1 dk=0x8001 wdt=-1 cc.debug.enable=1 max_task_pmem=0 wlan.debug.abort-init=2 mtk.wlan.manufacture=1 wlan.factory=0x93 ota ioimageloader.debug.csr-access=1'"</span><span class="token punctuation">,</span> <span class="token string">"root#"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
			<span class="token punctuation">[</span><span class="token string">"reboot"</span><span class="token punctuation">,</span> <span class="token string">"Kext"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span>
		<span class="token punctuation">]</span><span class="token punctuation">,</span>
		<span class="token string">"CELLios2ios"</span><span class="token punctuation">:</span><span class="token punctuation">[</span>
			<span class="token punctuation">[</span><span class="token string">"nvram boot-command=fsboot"</span><span class="token punctuation">,</span> <span class="token string">"root#"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
			<span class="token punctuation">[</span><span class="token string">"nvram boot-args='debug=0x104146 serial=0x13 gpu_panic_on_recovery=1 apfs_edt_rw_mount=1 ota wdt=-1 wlan.factory=0x93'"</span><span class="token punctuation">,</span> <span class="token string">"root#"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
			<span class="token punctuation">[</span><span class="token string">"reboot"</span><span class="token punctuation">,</span> <span class="token string">"Kext"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span>
		<span class="token punctuation">]</span><span class="token punctuation">,</span>
		<span class="token string">"ios2diags"</span><span class="token punctuation">:</span><span class="token punctuation">[</span>
			<span class="token punctuation">[</span><span class="token string">"nvram boot-command=diags"</span><span class="token punctuation">,</span> <span class="token string">"root#"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
			<span class="token punctuation">[</span><span class="token string">"reboot"</span><span class="token punctuation">,</span> <span class="token string">"Kext"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span>
		<span class="token punctuation">]</span><span class="token punctuation">,</span>
		<span class="token string">"iosgetinfo"</span><span class="token punctuation">:</span><span class="token punctuation">[</span>
			<span class="token punctuation">[</span><span class="token string">"cat /var/logs/WiPASmini/factoryota/info.wipasmini"</span><span class="token punctuation">,</span> <span class="token string">"root#"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span>
		<span class="token punctuation">]</span><span class="token punctuation">,</span>
		<span class="token string">"diagsgetinfo"</span><span class="token punctuation">:</span><span class="token punctuation">[</span>
			<span class="token punctuation">[</span><span class="token string">"sn"</span><span class="token punctuation">,</span> <span class="token string">":-)"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
			<span class="token punctuation">[</span><span class="token string">"system"</span><span class="token punctuation">,</span> <span class="token string">":-)"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span>
		<span class="token punctuation">]</span><span class="token punctuation">,</span>
		<span class="token string">"recoverygetinfo"</span><span class="token punctuation">:</span><span class="token punctuation">[</span>
			<span class="token punctuation">[</span><span class="token string">"diags"</span><span class="token punctuation">,</span> <span class="token string">":-)"</span><span class="token punctuation">,</span> <span class="token number">5</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
			<span class="token punctuation">[</span><span class="token string">"sn"</span><span class="token punctuation">,</span> <span class="token string">":-)"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
			<span class="token punctuation">[</span><span class="token string">"system"</span><span class="token punctuation">,</span> <span class="token string">":-)"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span>
		<span class="token punctuation">]</span><span class="token punctuation">,</span>
		<span class="token string">"rmlogs"</span><span class="token punctuation">:</span><span class="token punctuation">[</span>
			<span class="token punctuation">[</span><span class="token string">"cp -r /var/logs/WiPASmini /tmp"</span><span class="token punctuation">,</span> <span class="token string">"root#"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
			<span class="token punctuation">[</span><span class="token string">"rm -rf /var/logs/"</span><span class="token punctuation">,</span> <span class="token string">"root#"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
			<span class="token punctuation">[</span><span class="token string">"mkdir /var/logs"</span><span class="token punctuation">,</span> <span class="token string">"root#"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
			<span class="token punctuation">[</span><span class="token string">"cp -r /tmp/WiPASmini /var/logs"</span><span class="token punctuation">,</span> <span class="token string">"root#"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span>
		<span class="token punctuation">]</span><span class="token punctuation">,</span>
		<span class="token string">"mkcal"</span><span class="token punctuation">:</span><span class="token punctuation">[</span>
			<span class="token punctuation">[</span><span class="token string">"mkdir /var/root/CALfiles/"</span><span class="token punctuation">,</span> <span class="token string">"root#"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span>
		<span class="token punctuation">]</span><span class="token punctuation">,</span>
		<span class="token string">"diagschkargs"</span><span class="token punctuation">:</span><span class="token punctuation">[</span>
			<span class="token punctuation">[</span><span class="token string">"nvram --get boot-args"</span><span class="token punctuation">,</span> <span class="token string">":-)"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span>
		<span class="token punctuation">]</span><span class="token punctuation">,</span>
		<span class="token string">"ioschkargs"</span><span class="token punctuation">:</span><span class="token punctuation">[</span>
			<span class="token punctuation">[</span><span class="token string">"nvram boot-args"</span><span class="token punctuation">,</span> <span class="token string">"root#"</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">]</span>
		<span class="token punctuation">]</span>
	<span class="token punctuation">}</span>
<span class="token punctuation">}</span>
<span class="token punctuation">}</span>
</code></pre>
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
eyJoaXN0b3J5IjpbLTE4MDQ1NjQxMDZdfQ==
-->