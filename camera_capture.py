import cv2
import numpy as np
import math
from pathlib import Path

# ==================== 路径配置 ====================
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
FIXED_CODE_DIR = DATA_DIR / "fixed_code"
OUTPUT_DIR = PROJECT_ROOT / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


class CameraSketchToCadQuery:
    """基于摄像头草图的CadQuery代码生成器（自动导出STL）"""
    
    def __init__(self, template_dir=None):
        if template_dir is None:
            template_dir = FIXED_CODE_DIR
        self.template_dir = Path(template_dir)
        self.cap = None
        self.load_templates()
    
    def load_templates(self):
        self.templates = []
        if self.template_dir.exists():
            for code_file in self.template_dir.glob("*.py"):
                with open(code_file, 'r', encoding='utf-8') as f:
                    code = f.read()
                self.templates.append({
                    'filename': code_file.name,
                    'code': code
                })
            print(f"已加载 {len(self.templates)} 个代码模板")
        else:
            print(f"警告: 模板目录不存在: {self.template_dir}")
    
    def open_camera(self):
        """打开摄像头（修复版）"""
        for camera_id in [0, 1]:
            backends = [
                (cv2.CAP_DSHOW, "DSHOW"),
                (cv2.CAP_MSMF, "MSMF"),
                (cv2.CAP_ANY, "ANY")
            ]
            for backend, backend_name in backends:
                try:
                    cap = cv2.VideoCapture(camera_id, backend)
                    if cap.isOpened():
                        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
                        print(f"✓ 成功打开摄像头 {camera_id} (后端: {backend_name})")
                        return cap
                except Exception:
                    continue
        return None
    
    def capture_from_camera(self):
        """从摄像头采集图像"""
        self.cap = self.open_camera()
        
        if self.cap is None:
            print("\n" + "="*50)
            print("【错误】无法打开摄像头！")
            print("="*50)
            print("\n请尝试以下解决方法：")
            print("1. 检查摄像头是否被其他程序占用")
            print("2. 在Windows设置中检查摄像头权限")
            print("3. 重启电脑后重试")
            print("\n按回车键退出...")
            input()
            return None
        
        print("\n摄像头已打开！")
        print("请在摄像头前的手写板上绘制草图")
        print("按 [空格键] 拍照识别")
        print("按 [ESC] 退出\n")
        
        for _ in range(10):
            self.cap.read()
        
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            
            frame = cv2.flip(frame, 1)
            h, w = frame.shape[:2]
            
            margin = 80
            draw_area = (margin, margin, w - 2*margin, h - 2*margin)
            
            cv2.rectangle(frame, 
                         (draw_area[0], draw_area[1]), 
                         (draw_area[0] + draw_area[2], draw_area[1] + draw_area[3]), 
                         (0, 255, 0), 3)
            
            cv2.putText(frame, "SKETCH TO CAD", 
                       (w//2 - 100, 40), cv2.FONT_HERSHEY_SIMPLEX, 
                       0.8, (0, 255, 255), 2)
            cv2.putText(frame, "Place your drawing inside the GREEN box", 
                       (w//2 - 180, 70), cv2.FONT_HERSHEY_SIMPLEX, 
                       0.5, (255, 255, 255), 1)
            cv2.putText(frame, "SPACE: Capture | ESC: Exit", 
                       (w//2 - 150, h - 20), cv2.FONT_HERSHEY_SIMPLEX, 
                       0.5, (200, 200, 200), 1)
            
            center_x = w // 2
            center_y = h // 2
            cv2.line(frame, (center_x - 20, center_y), (center_x + 20, center_y), (100, 100, 100), 1)
            cv2.line(frame, (center_x, center_y - 20), (center_x, center_y + 20), (100, 100, 100), 1)
            
            cv2.imshow("Sketch Capture - Camera Ready", frame)
            
            key = cv2.waitKey(1) & 0xFF
            if key == 27:
                return None
            elif key == 32:
                sketch = frame[draw_area[1]:draw_area[1] + draw_area[3], 
                              draw_area[0]:draw_area[0] + draw_area[2]]
                cv2.imwrite(str(OUTPUT_DIR / "captured_raw.jpg"), sketch)
                print("\n✓ 已捕获图像，正在处理...")
                return sketch
        
        return None
    
    def preprocess_sketch(self, image):
        """预处理草图图像"""
        print("  - 转换为灰度图...")
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        print("  - 高斯滤波去噪...")
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        print("  - 自适应二值化...")
        binary = cv2.adaptiveThreshold(blurred, 255, 
                                       cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY_INV, 11, 2)
        
        print("  - 形态学处理...")
        kernel = np.ones((3, 3), np.uint8)
        closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
        denoised = cv2.medianBlur(closed, 3)
        
        cv2.imwrite(str(OUTPUT_DIR / "processed_binary.jpg"), denoised)
        
        return denoised
    
    def analyze_shape(self, binary_image):
        """分析形状类型和参数"""
        print("  - 查找轮廓...")
        contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, 
                                       cv2.CHAIN_APPROX_SIMPLE)
        
        if not contours:
            return None, None
        
        main_contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(main_contour)
        
        if area < 500:
            print(f"    警告: 轮廓面积太小 ({area})")
            return None, None
        
        print(f"    检测到轮廓面积: {area}")
        
        perimeter = cv2.arcLength(main_contour, True)
        epsilon = 0.02 * perimeter
        approx = cv2.approxPolyDP(main_contour, epsilon, True)
        num_vertices = len(approx)
        print(f"    顶点数: {num_vertices}")
        
        rect = cv2.minAreaRect(main_contour)
        (cx, cy), (width, height), angle = rect
        
        if width < height:
            width, height = height, width
        
        if perimeter > 0:
            circularity = 4 * math.pi * area / (perimeter * perimeter)
        else:
            circularity = 0
        print(f"    圆度: {circularity:.3f}")
        
        # 形状分类
        if circularity > 0.7 and num_vertices > 8:
            shape_type = 'sphere'
            shape_name = '圆形/球体'
        elif num_vertices == 4:
            aspect_ratio = width / height if height > 0 else 1
            if 0.8 < aspect_ratio < 1.2:
                shape_type = 'cube'
                shape_name = '正方形/立方体'
            else:
                shape_type = 'rectangle'
                shape_name = '长方形/长方体'
        elif num_vertices == 3:
            shape_type = 'cone'
            shape_name = '三角形/圆锥'
        elif 5 <= num_vertices <= 8 and circularity > 0.6:
            shape_type = 'cylinder'
            shape_name = '椭圆形/圆柱'
        else:
            shape_type = 'cube'
            shape_name = '未识别，默认立方体'
        
        # 估算尺寸
        size = max(5, min(50, math.sqrt(area) / 5))
        
        print(f"    识别形状: {shape_name}")
        print(f"    估算尺寸: {size:.1f}")
        
        params = {
            'size': size,
            'width': width,
            'height': height,
            'circularity': circularity,
            'num_vertices': num_vertices
        }
        
        return shape_type, params
    
    def generate_and_save_stl(self, shape_type, params):
        """生成CadQuery模型并直接保存为STL文件"""
        size = params.get('size', 10)
        
        import cadquery as cq
        
        # 根据形状创建模型
        if shape_type == 'cube':
            result = cq.Workplane("XY").box(size, size, size)
            shape_name = "立方体"
        elif shape_type == 'sphere':
            result = cq.Workplane("XY").sphere(size/2)
            shape_name = "球体"
        elif shape_type == 'cylinder':
            result = cq.Workplane("XY").cylinder(size, size/3)
            shape_name = "圆柱体"
        elif shape_type == 'cone':
            result = cq.Workplane("XY").circle(size/3).workplane(offset=size).circle(5).loft()
            shape_name = "圆锥体"
        elif shape_type == 'rectangle':
            result = cq.Workplane("XY").box(params.get('width', size), params.get('height', size), size/2)
            shape_name = "长方体"
        else:
            result = cq.Workplane("XY").box(size, size, size)
            shape_name = "立方体"
        
        # 生成STL文件名
        stl_filename = f"{shape_type}_{int(size)}_{int(size*100)%100}.stl"
        stl_path = OUTPUT_DIR / stl_filename
        
        # 导出STL
        cq.exporters.export(result, str(stl_path))
        print(f"\n✓ STL文件已保存: {stl_path}")
        
        # 同时保存CadQuery代码
        code = self.generate_cadquery_code(shape_type, params)
        py_filename = f"generated_{shape_type}_{int(size)}.py"
        py_path = OUTPUT_DIR / py_filename
        with open(py_path, 'w', encoding='utf-8') as f:
            f.write(code)
        print(f"✓ CadQuery代码已保存: {py_path}")
        
        return stl_path
    
    def generate_cadquery_code(self, shape_type, params):
        """生成CadQuery代码（仅用于保存文本）"""
        size = params.get('size', 10)
        
        imports = '''import cadquery as cq

'''
        
        codes = {
            'cube': f'''{imports}# 立方体
result = cq.Workplane("XY").box({size}, {size}, {size})

# 导出STL（可选）
# result.export("output.stl")
''',
            'sphere': f'''{imports}# 球体
result = cq.Workplane("XY").sphere({size/2})
''',
            'cylinder': f'''{imports}# 圆柱体
result = cq.Workplane("XY").cylinder({size}, {size/3})
''',
            'cone': f'''{imports}# 圆锥体
result = cq.Workplane("XY").circle({size/3}).workplane(offset={size}).circle(5).loft()
''',
            'rectangle': f'''{imports}# 长方体
result = cq.Workplane("XY").box({params.get('width', size)}, {params.get('height', size)}, {size/2})
'''
        }
        
        return codes.get(shape_type, codes['cube'])
    
    def run(self):
        """主流程"""
        print("\n" + "="*60)
        print("    摄像头草图 → STL 3D模型生成系统")
        print("="*60)
        print(f"输出目录: {OUTPUT_DIR}")
        print("="*60)
        
        # 步骤1：摄像头采集
        print("\n【步骤1】摄像头采集")
        print("-" * 40)
        sketch = self.capture_from_camera()
        
        if sketch is None:
            print("\n用户退出")
            return
        
        if self.cap:
            self.cap.release()
        cv2.destroyAllWindows()
        
        # 步骤2：图像预处理
        print("\n【步骤2】图像预处理")
        print("-" * 40)
        binary = self.preprocess_sketch(sketch)
        
        # 步骤3：形状分析
        print("\n【步骤3】形状分析")
        print("-" * 40)
        shape_type, params = self.analyze_shape(binary)
        
        if shape_type is None:
            print("\n❌ 未能识别形状，请确保:")
            print("   1. 图形轮廓清晰（用黑色笔绘制）")
            print("   2. 图形位于绿色框内")
            print("   3. 光照充足，避免阴影")
            return
        
        # 步骤4：生成并保存STL
        print("\n【步骤4】生成STL模型")
        print("-" * 40)
        stl_path = self.generate_and_save_stl(shape_type, params)
        
        print("\n" + "="*60)
        print("✓ 处理完成！")
        print(f"STL文件位置: {stl_path}")
        print(f"输出文件夹: {OUTPUT_DIR}")
        print("="*60)
        
        # 尝试用系统默认程序打开STL文件
        try:
            import os
            os.startfile(str(stl_path))
            print("\n已自动打开STL文件（Windows 3D查看器）")
        except Exception:
            print(f"\n请手动打开STL文件: {stl_path}")


# ==================== 运行入口 ====================
if __name__ == "__main__":
    print("\n正在启动系统...")
    generator = CameraSketchToCadQuery()
    generator.run()
    
    print("\n按回车键退出...")
    input()