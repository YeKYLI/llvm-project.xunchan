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
