import torch
import torch.nn as nn
import torch.optim as optim

# 定义简单的全连接网络
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(784, 128)  # 28x28 image -> 128 neurons
        self.fc2 = nn.Linear(128, 10)   # 128 -> 10 classes (output)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# 创建模型、损失函数和优化器
model = SimpleNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.001)

# 生成一个随机输入和标签，模拟 MNIST 数据集
inputs = torch.randn(64, 784)  # 64 samples of 28x28 flattened images
labels = torch.randint(0, 10, (64,))  # 64 random labels (0-9)

# 训练模型（简单的单步训练）
outputs = model(inputs)
loss = criterion(outputs, labels)
loss.backward()
optimizer.step()

print("训练完成，模型输出损失值:", loss.item())

torch.save(model.state_dict(), "model.pth")

print("模型保存成功")

""""


"""

# Hello World

第一阶段：

examples相关的样例全部看懂，examples里边的代码虽然麻雀虽小五脏俱全，看懂非常多

支撑文档： 龙书、还有小福推荐的基本C++书、、或者干脆把小福推荐的书都放在这里吧

考核点：可以快速添加一个新的token的处理、添加一种方言、添加一种pass、添加一种dialect的op、实现并执行一种的OP操作

# 优化一个模型

# 针对RK3588进行硬件定制的优化、特别是针对NPU、架构等之类的优化

# LLVM Committer

前期尽量做一些可以写在简历上的事情