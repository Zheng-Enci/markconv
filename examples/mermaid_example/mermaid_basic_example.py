# Mermaid 图表基础使用示例
# Mermaid Diagram Basic Usage Example

"""
本示例演示如何在 Markdown 转 PDF/HTML 中使用 Mermaid 图表

This example demonstrates how to use Mermaid diagrams in Markdown to PDF/HTML conversion
"""

from markconv import MDConverter


def mermaid_basic_example():
    """
    Mermaid 图表基础示例
    
    演示如何将包含 Mermaid 图表的 Markdown 文件转换为 PDF
    """
    print("Mermaid 图表基础使用示例")
    print("=" * 50)
    
    # 创建 MDConverter 实例
    # Create MDConverter instance
    converter = MDConverter()
    
    # 定义输入的 Markdown 文件路径
    # Define input Markdown file path
    input_file = r'sample_with_mermaid.md'
    
    # 定义输出的 PDF 文件路径
    # Define output PDF file path
    output_pdf = 'examples/mermaid_output.pdf'
    
    # 定义输出的 HTML 文件路径
    # Define output HTML file path
    output_html = 'examples/mermaid_output.html'
    
    # 转换为 PDF（Mermaid 图表会自动渲染为图片）
    # Convert to PDF (Mermaid diagrams will be automatically rendered as images)
    print("正在生成 PDF...")
    converter.to_pdf(input_file, output_pdf)
    print(f"PDF 文件已生成: {output_pdf}")
    
    # 转换为 HTML（Mermaid 图表会使用 Mermaid.js 在浏览器中渲染）
    # Convert to HTML (Mermaid diagrams will use Mermaid.js to render in browser)
    print("\n正在生成 HTML...")
    converter.to_html(input_file, output_html)
    print(f"HTML 文件已生成: {output_html}")
    
    print("\n完成！Done!")


if __name__ == '__main__':
    mermaid_basic_example()
