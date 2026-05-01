# Mermaid 图表使用示例

本目录包含 Mermaid 图表在 markconv 中的使用示例。

## 文件说明

### 1. mermaid_basic_example.py
基础使用示例，演示如何将包含 Mermaid 图表的 Markdown 文件转换为 PDF 和 HTML。

**运行方式：**
```bash
cd examples/mermaid_example
python mermaid_basic_example.py
```

### 2. mermaid_custom_bg_example.py
自定义背景色示例，演示三种设置 Mermaid 图表背景色的方式：
- 方式 1：通过 MermaidProcessor 设置背景色
- 方式 2：在 Markdown 中使用 Mermaid 配置
- 方式 3：通过 CSS 设置背景色

**运行方式：**
```bash
cd examples/mermaid_example
python mermaid_custom_bg_example.py
```

### 3. mermaid_css_bg_example.css
CSS 样式文件，演示如何通过 CSS 为透明背景的 Mermaid 图片添加背景色。

**使用方式：**
```python
from markconv import MDConverter

converter = MDConverter(css_file="mermaid_css_bg_example.css")
converter.to_pdf("input.md", "output.pdf")
```

### 4. sample_with_mermaid.md
包含各种 Mermaid 图表的示例 Markdown 文件，包括：
- 流程图 (Flowchart)
- 时序图 (Sequence Diagram)
- 类图 (Class Diagram)
- 状态图 (State Diagram)
- 饼图 (Pie Chart)
- 甘特图 (Gantt Chart)
- 实体关系图 (ER Diagram)
- 用户旅程图 (User Journey)

## 背景色设置方法详解

### 方法 1：修改 MermaidProcessor（推荐用于全局设置）

在 `pdf_exporter.py` 中修改：

```python
# 在 _replace_mermaid_with_images 函数中
mermaid_images_dir = os.path.join(output_dir, 'mermaid_images')

# 设置为白色背景
processor = MermaidProcessor(
    output_dir=mermaid_images_dir,
    background_color='white'  # 或 'transparent', '#f0f0f0' 等
)
```

**支持的背景色值：**
- `'transparent'` - 透明背景（默认）
- `'white'` - 白色
- `'#FFFFFF'` - 十六进制颜色
- 其他 CSS 颜色值

### 方法 2：在 Markdown 中配置（推荐用于单个图表）

在 Markdown 文件中：

```markdown
```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'background': '#ffffff' }}}%%
graph TD
    A[开始] --> B[结束]
```
```

### 方法 3：通过 CSS 设置（推荐用于 PDF/HTML 显示效果）

使用 `mermaid_css_bg_example.css` 文件：

```css
div[style*="text-align: center"] {
    background-color: #f5f5f5;
    padding: 20px;
    border-radius: 8px;
}
```

**注意：** 此方法需要 Mermaid 图片使用透明背景才能看到效果。

## 三种方法对比

| 方法 | 适用场景 | 优点 | 缺点 |
|------|---------|------|------|
| 方法 1 | 全局修改所有图表 | 统一控制，一次修改全局生效 | 需要修改源代码 |
| 方法 2 | 单个图表特殊设置 | 灵活，不影响其他图表 | 需要在 Markdown 中添加配置 |
| 方法 3 | PDF/HTML 显示效果 | 不影响图片本身，可随时调整 | 需要图片有透明背景 |

## 推荐使用场景

1. **所有图表统一背景色** → 使用 **方法 1**
2. **个别图表特殊背景** → 使用 **方法 2**
3. **仅调整显示效果** → 使用 **方法 3**

## 注意事项

1. Mermaid 图表渲染需要安装 `mermaid-cli` 依赖：
   ```bash
   pip install mermaid-cli>=0.1.3
   ```

2. 首次运行可能需要下载 Chromium 浏览器（由 Playwright 自动管理）

3. 透明背景的图片在 PDF 中可以通过 CSS 设置背景色，但白色背景的图片无法通过 CSS 改变背景

4. 如果 Mermaid 渲染失败，请检查：
   - 是否安装了 mermaid-cli
   - 网络连接是否正常（需要下载 Chromium）
   - Mermaid 代码语法是否正确
