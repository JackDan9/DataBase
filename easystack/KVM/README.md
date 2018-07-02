# KVM(Kernel-based Virtual Machine)

## 虚拟化的简史

![virtual_history][1]

------

## KVM的简史
- 在上图中, KVM全程是基于内核的虚拟机(Kernel-based Virtual Machine), 它是Linux的一个内核模块, 该内核模块使得Linux变成了一个`Hypervisor`。
    - 它是由`Quramnet`开发, 该公司于2008年被`Red Hat`收购;
    - 它支持x86(32 and 64位), s390, Powerpc等CPU;
    - 它从Linux 2.6.20 起就作为一模块被包含在Linux内核中;
    - 它需要支持虚拟化扩展的CPU;
    - 它是完全开源的。[官网地址][2]。

------

## KVM架构
- `KVM`是基于虚拟化扩展(Intel VT或者AMD-V)的x86硬件的开源的Linux原生的全虚拟化解决方案。KVM中, 虚拟机被实现为常规的Linux进程, 由标准Linux调度程序进行调度; 虚机的每个虚拟CPU被实现为一个常规的Linux线程。这使得`KVM`能够使用Linux内核的已有功能。
- 但是, `KVM`本身不执行任何硬件模拟, 需要用户空间程序通过`/dev/kvm`接口设置一个客户机虚拟服务器的地址空间, 向它提供模拟I/O, 并将它的视频显示映射回宿主的显示屏。目前这个应用程序是`QEMU`。
- Linux上的用户空间、内核空间和虚机:

![user_cpu_virtual_space][3]

- `Guest`: 客户机系统, 包括CPU(vCPU)、内存、驱动(Console、网卡、I/O设备驱动等), 被KVM置于一种受限制的CPU模式下运行。
- `KVM`: 运行在内核空间, 提供CPU和内存的虚拟化, 以及客户机的I/O拦截。`Guest`的I/O被KVM拦截后, 交给`QEMU`处理。
- `QEMU`: 修改过的被`KVM`虚机使用的`QEMU`代码, 运行在用户空间, 提供硬件`I/O`虚拟化, 通过`IOCTL /dev/kvm`设备和`KVM`进行交互。

### KVM是实现拦截虚机的I/O请求的原理
- 现代CPU本身实现了对**特殊指令的截获**和**重定向的硬件**支持, 甚至新硬件会提供额外的资源来帮助软件实现对于关键硬件资源的虚拟化从而提高性能。
- 以x86平台为例, 支持虚拟机技术的CPU带有特别优化过的指令集来控制虚拟化过程。通过这些指令集, VMM(Virtual Machine Monitor/虚拟机监控器)很容易将客户置于一种受限制的模式下运行, 一旦客户机试图访问物理资源, 硬件会暂停客户机运行, 将控制权交回给VMM处理。
- VMM还可以利用硬件的虚拟化增强机制, 将客户机在受限的模式下对一些特定资源的访问, 完全由硬件重定向VMM指定的虚拟资源, 整个过程不需要暂停客户机的运行和VMM的参与。
- 由于虚拟化硬件提供全新的架构, 支持操作系统直接在上面运行, 无需进行二进制转换, 减少了相关的性能开销, 极大简化了VMM的设计, 使得VMM性能更加强大。
- 从2005年起, Intel在其处理器产品线中推广`Intel Virtualization Technology`即`IntelVT`技术。

### QEMU-KVM
- 其实QEMU原本不是KVM中的一部分, 它自己就是一个纯软件实现的虚拟化系统, 所以其性能低下。
- 但是, QEMU代码中包含整套的虚拟机实现, 包括处理器虚拟化、内存虚拟化, 以及KVM需要使用到的虚拟设备模拟(网卡、显卡、存储控制器和硬盘等)。 
- 为了简化代码, KVM在QEMU的基础上修改。VM运行期间, QEMU会通过KVM模块提供的系统调用进入内核, 由KVM负责将虚拟机置于处理的特殊模式运行。
- 当虚机进行I/O操作时, KVM会从上次系统调用出口处返回QEMU, 由QEMU来负责解析和模拟这些设备。从QEMU角度看, 也可以说是QEMU使用了KVM模块的虚拟化功能, 为自己的虚机提供了硬件虚拟化加速。除此之外, 虚机的配置和创建、虚机运行所依赖的虚拟设备、虚拟运行时的用户提供一定的支持。以在一些虚机的特定技术比如动态迁移, 都是QEMU自己实现的。

### KVM
- KVM内核模块在运行时按需加载内核空间运行。KVM本身不执行任何设备模拟, 需要QEMU通过`/dev/kvm`接口设置一个`GUEST OS`的地址空间, 向它提供模拟的I/O设备, 并将它的视频显示映射回宿主机的显示屏。它是KVM虚机的核心部分, 其主要功能是初始化CPU硬件, 打开虚拟化模式, 然后将虚拟客户机运行在虚拟机模式下, 并对虚机的运行提供一定的支持。以在Intel上运行为例, KVM模块被加载的时候, 它:
    - 首先初始化内部的数据结构;
    - 做好准备后, KVM模块检测当前的CPU, 然后打开CPU控制以及存取CR4的虚拟化模式开关, 并通过执行`VMXON`指令将宿主操作系统置于虚拟化模式的根模式;
    - 最后, KVM模块创建特殊设备文件`/dev/kvm`并等待来自用户空间的指令。
- 接下来的虚机的创建和运行将是`QEMU`和`KVM`相互配合的过程。两者的通信接口主要是一系列针对特殊设备文件`/dev/kvm`的IOCTL调用。其中最重要的是创建虚机。它可以理解成`KVM`为了某个特定的虚机创建对应的内核数据结构, 同时, `KVM`返回一个文件句柄来代表所创建的虚机。
- 针对该句柄的调用可以对虚机做相应的管理, 比如创建用户空间虚拟地址和客户机物理管理、真实物理地址之间的映射关系, 再比如创建多个`vCPU`。`KVM`为每一个`vCPU`生成对应的文件句柄, 对其相应地IOCTL调用, 就可以对`vCPU`进行管理。其中最重要的就是"执行虚拟处理器"。通过它, 虚机在`KVM`的支持下, 被置于虚拟机模式的非根模式下, 开始执行二进制指令。在非根模式下, 所有敏感的二进制指令都被CPU捕捉到, CPU在保存现场之后自动切换到根模式, 由`KVM`决定如何处理。
- 除了CPU的虚拟化, 内存的虚拟化也由`KVM`实现。实际上, **内存虚拟化**往往是一个虚机实现中最复杂的部分。CPU中的内存管理单元`MMU`是通过**页表的形式**将程序运行的虚拟地址转换成实际物理地址。在虚拟地址模式下, `MMU`的页表则必须在一次查询的时候完成两次地址转换。因为除了将客户机程序的虚拟地址转换了客户机的物理地址外, 还要将客户机物理地址转换成真实物理地址。

------

## KVM的功能列表
- KVM所支持的功能包括:
    - 支持CPU和memory的超分(Overcommit);
    - 支持半虚拟化`I/O` (virtio);
    - 支持热插拔(cpu、块设备、网络设备等);
    - 支持对称多处理(Symmetric Multi-Processing, 缩写为SMP);
    - 支持实时迁移(Live Migation);
    - 支持PCI设备直接分配和单根I/O虚拟化(SR-IOV);
    - 支持内核同页(KSM);
    - 支持NUMA(Non-Uniform Memory Accss, 非一致存储访问结构)。

------

## KVM工具集合
- libvirt: 操作和管理KVM虚机的虚拟化API, 使用C语言编写, 可以由Python、Ruby、Perl、PHP、Java
等语言调用。可以操作包括KVM、vmware、XEN、Hyper-v、LXC等在内的多种Hypervisor。
- Virsh: 基于libvirt的命令行工具(CLI)。
- Virsh-Manager: 基于libvirt的GUI工具。
- virt-v2v: 虚机格式迁移工具。
- virt-* 工具: 包括Virt-install (创建KVM的命令行工具)、Virt-viewer(连接到虚机屏幕的工具、Virt-clone(虚拟克隆工具)、Virt-top等)。 
- sVirt: 安全工具。

------

## 为什么需要CPU虚拟化
- x86操作系统

------


## KVM的安装
- http://www.cnblogs.com/sammyliu/p/4543110.html


  [1]: ./images/virtual_history.jpg "virtual_history.jpg"
  [2]: http://www.linux-kvm.org/page/Main_Page
  [3]: ./images/user_cpu_virtual_space.jpg "user_cpu_virtual_space.jpg"