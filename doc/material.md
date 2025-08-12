[MLIR doc](https://mlir.llvm.org/docs/)

[LLVM doc](https://llvm.org/docs/)


# 教科书

超标量处理器设计

[2020 LLVM Developers’ Meeting: M. Amini & R. Riddle “MLIR Tutorial”](https://www.youtube.com/watch?v=Y4SvqTtOIDk)

https://mlir.llvm.org/OpenMeetings/2021-10-07-The-Torch-MLIR-project.pdf

[如何学习LLVM才能找到一份编译器研发的工作？ - 开心的小福的回答 - 知乎](https://www.zhihu.com/question/471200593/answer/2880145488)

[编译原理中的抽象语法树(AST)为什么而存在？ - 开心的小福的回答 - 知乎](https://www.zhihu.com/question/363445606/answer/2868757254)

[八千里路云和月 - 开心的小福的文章 - 知乎](https://zhuanlan.zhihu.com/p/1901963200481695106)

https://godbolt.org/

[A Gentle Introduction to LLVM IR](https://mcyoung.xyz/2023/08/01/llvm-ir/)


# 网课

[CS143 | Compliers](https://web.stanford.edu/class/cs143/)

# CPP

<Effective C++>

<More Effective C++>

<深度探索C++对象模型>，选读

# System Pogramming

<Operating System Concepts>

MIT 6.828

Operating Systems: Three Easy Pieces

# 高性能计算

<Computer Systems: A Programmer's Perspective><CUDA C++ Programming Guide> + GEMM + LSTM，选读，且建议有一定体系结构积累后再读。<A Primer on Memory Consistency and Cache Coherence>

# 体系结构

1. <Computer Organization and Design: The Hardware/Software Interface>2. <General Purpose Graphics Processor Architectures>，选读3. <Computer Architecture: A Quantitative Approach>，选读部分章节

超标量处理器设计

# Complier


作者：开心的小福
链接：https://zhuanlan.zhihu.com/p/1901963200481695106
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

1. <Compiler Construction: Principles and Practice>，我心中最适合0基础入门的教材，手把手教写了一个玩具编译器。2. <Engineering A Compiler>, 工业级编译器该有的五脏六腑。5. <Compilers: Principles, Techniques, and Tools>，经典，但我认为适合有一定开发经验后再看，且前端部分有点太多了。6. <Optimizing Compilers for Modern Architectures,A Dependence-Based Approach>，本书升华之处在于，一是将编译器与数学结合，虽然数学在工业编译器中还是鲜有出现，但在当时还是开拓了眼界，成为我理解多面体优化的基础；二是将原先学到的"平台无关优化"和体系结构结合，使我摒弃了"平台无关"的观念，转而相信"没有优化是彻底平台无关的"，在实践时也会考虑中端PASS的整体影响。3. <Getting Started with LLVM Core Libraries>，介绍LLVM的基础概念，LLVM各组件命名几乎都对应于<Engineering a Compiler>，令人不仅感慨"原来如此"。4. <深入理解LLVM：代码生成>，介绍了后端优的各类优化，覆盖API，数据结构和算法，且成书于2024年，所用LLVM版本也较新，我用作字典。

CS143

# 训练技巧

以上是我在无竞赛和无实习机会的年代摸索出来的学习方法，如果有条件开展毕升杯，龙芯杯，GSOC和找到实习，可以跳过一些书籍。当年，我通过两个项目来自行训练:在LLVM上实现图着色寄存器分配在LLVM IR层实现<Optimizing Compilers for Modern Architectures,A Dependence-Based Approach>中的若干优化




