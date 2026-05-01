"""
Mermaid 图表处理器模块
"""

import os
import re
import uuid


class MermaidProcessor:
    def __init__(self, output_dir: str = './mermaid_images'):
        self.output_dir = output_dir
        self.mermaid_pattern = re.compile(r'```mermaid\n(.*?)```', re.DOTALL)
    
    def render_to_image(self, mermaid_code: str, output_format: str = 'png') -> str:
        os.makedirs(self.output_dir, exist_ok=True)
        
        file_id = str(uuid.uuid4())[:8]
        temp_file = os.path.join(self.output_dir, f'temp_{file_id}.mmd')
        output_file = os.path.join(self.output_dir, f'mermaid_{file_id}.{output_format}')
        
        try:
            with open(temp_file, 'w', encoding='utf-8') as f:
                f.write(mermaid_code)
            
            # 使用 mermaid_cli 库
            from mermaid_cli import render_mermaid_file_sync
            render_mermaid_file_sync(
                input_file=temp_file,
                output_file=output_file,
                output_format=output_format
            )
            
            return output_file
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)
