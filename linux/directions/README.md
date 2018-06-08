# Linux_Directions
## `uname a`
- 作用: 查看Linux的版本;

## `uname a`(example)
```
[root@bogon ~]# uname -a
Linux bogon 2.6.32-696.30.1.el6.x86_64 #1 SMP Tue May 22 03:28:18 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
```

## `uname --help`
- 作用: 查看`uname`的指令参数以及`uname`指令加指令参数的作用;

## `uname --help`(example)
- CN:
```
[root@bogon ~]# uname --help
用法：uname [选项]...
输出一组系统信息。如果不跟随选项，则视为只附加-s 选项。

  -a, --all         以如下次序输出所有信息。其中若-p 和
                -i 的探测结果不可知则被省略：
  -s, --kernel-name     输出内核名称
  -n, --nodename        输出网络节点上的主机名
  -r, --kernel-release      输出内核发行号
  -v, --kernel-version      输出内核版本
  -m, --machine     输出主机的硬件架构名称
  -p, --processor       输出处理器类型或"unknown"
  -i, --hardware-platform   输出硬件平台或"unknown"
  -o, --operating-system    输出操作系统名称
      --help        显示此帮助信息并退出
      --version     显示版本信息并退出
```
- ES:
```
jackdan@Docker06:~$ uname --help
Usage: uname [OPTION]...
Print certain system information.  With no OPTION, same as -s.

  -a, --all                print all information, in the following order,
                             except omit -p and -i if unknown:
  -s, --kernel-name        print the kernel name
  -n, --nodename           print the network node hostname
  -r, --kernel-release     print the kernel release
  -v, --kernel-version     print the kernel version
  -m, --machine            print the machine hardware name
  -p, --processor          print the processor type (non-portable)
  -i, --hardware-platform  print the hardware platform (non-portable)
  -o, --operating-system   print the operating system
      --help     display this help and exit
      --version  output version information and exit
```

## `cat /etc/*-release`
- `/ect/*-release`是系统安装时默认的发行版本信息, 通常安装好系统后文件内容不会发生变化. 
- 用法: `cat [OPTION]... [FILE]...`
- 作用: 将[文件]或标准输入组合输出到标准输出.

## `cat --help`
- 作用: 查看`cat`的指令参数以及`cat`指令加指令参数的作用;

## `cat --help`(example)
- CN:
```
用法：cat [选项]... [文件]...
将[文件]或标准输入组合输出到标准输出。

  -A, --show-all           等于-vET
  -b, --number-nonblank    对非空输出行编号
  -e                       等于-vE
  -E, --show-ends          在每行结束处显示"$"
  -n, --number             对输出的所有行编号
  -s, --squeeze-blank      不输出多行空行
  -t                       与-vT 等价
  -T, --show-tabs          将跳格字符显示为^I
  -u                       (被忽略)
  -v, --show-nonprinting   使用^ 和M- 引用，除了LFD和 TAB 之外
      --help        显示此帮助信息并退出
      --version     显示版本信息并退出

如果没有指定文件, 或者文件为"-", 则从标准输入读取.

示例:
  cat f - g  先输出f的内容, 然后输出标准输入的内容, 最后输出g的内容.
  cat        将标准输入的内容复制到标准输出.

```
- ES:
```
Usage: cat [OPTION]... [FILE]...
Concatenate FILE(s) to standard output.

With no FILE, or when FILE is -, read standard input.

  -A, --show-all           equivalent to -vET
  -b, --number-nonblank    number nonempty output lines, overrides -n
  -e                       equivalent to -vE
  -E, --show-ends          display $ at end of each line
  -n, --number             number all output lines
  -s, --squeeze-blank      suppress repeated empty output lines
  -t                       equivalent to -vT
  -T, --show-tabs          display TAB characters as ^I
  -u                       (ignored)
  -v, --show-nonprinting   use ^ and M- notation, except for LFD and TAB
      --help     display this help and exit
      --version  output version information and exit

Examples:
  cat f - g  Output f's contents, then standard input, then g's contents.
  cat        Copy standard input to standard output.

```

## `lsb_release -a`
- 作用: FSG(Free Standards Group)组织开发的LSB(Linux Standard Base)标准的一个命令, 用来查看linux兼容性的发行版信息.

## `lsb_release --help`
- Centos
```
[root@bogon ~]# lsb_release --help
FSG lsb_release v2.0 prints certain LSB (Linux Standard Base) and
Distribution information.

Usage: lsb_release [OPTION]...
With no OPTION specified defaults to -v.

Options:
  -v, --version
    Display the version of the LSB specification against which the distribution is compliant.
  -i, --id
    Display the string id of the distributor.
  -d, --description
    Display the single line text description of the distribution.
  -r, --release
    Display the release number of the distribution.
  -c, --codename
    Display the codename according to the distribution release.
  -a, --all
    Display all of the above information.
  -s, --short
    Use short output format for information requested by other options (or version if none).
  -h, --help
    Display this message.
```
- Ubuntu
```
jackdan@Docker06:~$ lsb_release --help
Usage: lsb_release [options]

Options:
  -h, --help         show this help message and exit
  -v, --version      show LSB modules this system supports
  -i, --id           show distributor ID
  -d, --description  show description of this distribution
  -r, --release      show release number of this distribution
  -c, --codename     show code name of this distribution
  -a, --all          show all of the above information
  -s, --short        show requested information in short format

```

