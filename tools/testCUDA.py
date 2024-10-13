import torch

class MyModel(torch.nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.fc = torch.nn.Linear(10, 10)

    def forward(self, x):
        x = x.to(device)  # 确保输入张量在 GPU 上
        return self.fc(x)
    
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")
model = MyModel().to(device)  # 确保模型在 GPU 上
input = torch.randn(1, 10).to(device)  # 确保输入张量在 GPU 上


output = model(input)
print(output)

# 检查是否有可用的 GPU
print(f"Available GPUs: {torch.cuda.device_count()}")

# 输出所有可用的 GPU 设备 ID
for i in range(torch.cuda.device_count()):
    print(f"Device {i}: {torch.cuda.get_device_name(i)}")