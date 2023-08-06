from tsstp.datatemplate import DataTemplate
import cProfile
import pstats
import os

# 获取当前脚本所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))

def test_xdatcar_parse():
    xdatacar_template = """
    {{ head }}
    {{ Scaling }}
    {% loop 3 %}
        {{ lattice_vector }} ~ 3
    {% endloop %}
    {{ elements }} ~ 3
    {{ element_num }} ~ 3
    {% loop n %}
        Direct configuration= {{ loop_index }}
        {% loop sum(element_num) %}
            {{ Coordinates }} ~ 3
        {% endloop %}
    {% endloop %}
    """

    basepath = os.path.join(current_dir, 'testdata\\')
    xdatacar_file = basepath + 'XDATCAR'
    xdatacar_t = basepath + 'xdatcar_template.txt'

    parser = DataTemplate(xdatacar_t, xdatacar_file)

    parser.parse()
    result = parser.result()
    # print(f'--result:{result}')

# run the function with profiling enabled
cProfile.run('test_xdatcar_parse()', 'profile_stats')

# create a pstats object from the stats file
p = pstats.Stats('profile_stats')

# sort the stats by cumulative time spent in each function
p.sort_stats('cumulative')

# print out the top 10 functions by cumulative time spent
p.print_stats(10)
