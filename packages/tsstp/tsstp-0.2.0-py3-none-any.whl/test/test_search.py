from tsstp.datatemplate import DataTemplate
import os

# 获取当前脚本所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))

def test_search():
    search_template1 = """
    {{ key }} = {{ value }}
    """

    basepath = os.path.join(current_dir, 'testdata\\')
    text_file = basepath + 'text_file.txt'
    incar = basepath + 'INCAR'
    incar_t = basepath + 'incar_template.txt'

    parser = DataTemplate(incar_t, incar)
    result = parser.search()
    print(f'--result:{result}')

test_search()
