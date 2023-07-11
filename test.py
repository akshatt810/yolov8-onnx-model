import onnx

model_path = 'yolov8n.onnx'
onnx_model = onnx.load(model_path)
print(onnx_model)

onnx.checker.check_model(onnx_model)
