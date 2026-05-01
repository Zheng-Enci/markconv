# Mermaid 图表自定义背景色示例
# Mermaid Diagram Custom Background Color Example

"""
本示例演示如何设置 Mermaid 图表的背景色

This example demonstrates how to set the background color of Mermaid diagrams
"""

from markconv.tools import MermaidProcessor


def mermaid_custom_background_example():
    """
    自定义 Mermaid 图表背景色示例
    
    方式 1：通过 MermaidProcessor 设置背景色
    Method 1: Set background color via MermaidProcessor
    """
    print("Mermaid 图表自定义背景色示例")
    print("=" * 50)
    
    # 示例 1：透明背景（默认）
    # Example 1: Transparent background (default)
    print("\n1. 透明背景 Transparent background:")
    processor_transparent = MermaidProcessor(
        output_dir='./mermaid_images',
        background_color='transparent'  # 透明背景
    )
    print("   创建 MermaidProcessor，背景色：transparent")
    
    # 示例 2：白色背景
    # Example 2: White background
    print("\n2. 白色背景 White background:")
    processor_white = MermaidProcessor(
        output_dir='./mermaid_images',
        background_color='white'  # 白色背景
    )
    print("   创建 MermaidProcessor，背景色：white")
    
    # 示例 3：自定义颜色背景
    # Example 3: Custom color background
    print("\n3. 自定义颜色背景 Custom color background:")
    processor_custom = MermaidProcessor(
        output_dir='./mermaid_images',
        background_color='#f0f8ff'  # 爱丽丝蓝
    )
    print("   创建 MermaidProcessor，背景色：#f0f8ff")
    
    # 示例 4：深色背景
    # Example 4: Dark background
    print("\n4. 深色背景 Dark background:")
    processor_dark = MermaidProcessor(
        output_dir='./mermaid_images',
        background_color='#2d2d2d'  # 深灰色
    )
    print("   创建 MermaidProcessor，背景色：#2d2d2d")
    
    print("\n" + "=" * 50)
    print("提示：目前 MermaidProcessor 主要在 markconv 内部使用")
    print("Tip: MermaidProcessor is mainly used internally in markconv")
    print("如需修改 PDF 输出中的背景色，需要修改 pdf_exporter.py 中的代码")
    print("To change background color in PDF output, modify pdf_exporter.py")


def mermaid_inline_config_example():
    """
    方式 2：在 Markdown 中使用 Mermaid 配置
    Method 2: Use Mermaid configuration in Markdown
    """
    print("\n\n方式 2：在 Markdown 中配置背景色")
    print("Method 2: Configure background color in Markdown")
    print("=" * 50)
    
    mermaid_code = '''
%%{init: {'theme': 'base', 'themeVariables': { 'background': '#ffffff' }}}%%
graph TD
    A[开始 Start] --> B{判断 Decision}
    B -->|条件1| C[处理1 Process 1]
    B -->|条件2| D[处理2 Process 2]
    C --> E[结束 End]
    D --> E
'''
    
    print("\n在 Markdown 文件中这样写：")
    print("Write this in your Markdown file:")
    print("-" * 40)
    print("```mermaid")
    print(mermaid_code.strip())
    print("```")
    print("-" * 40)
    
    print("\n这种方式可以为单个图表设置特定的背景色")
    print("This method can set specific background color for individual diagrams")


if __name__ == '__main__':
    mermaid_custom_background_example()
    mermaid_inline_config_example()
