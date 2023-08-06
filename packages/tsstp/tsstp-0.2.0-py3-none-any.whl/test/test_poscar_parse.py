from tsstp.datatemplate import DataTemplate
import cProfile
import pstats
import os

# 获取当前脚本所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
def test_poscar_parse():
    poscar_template = """
    {{ head }}
    {{ Scaling }}
    {% loop 3 %}
        {{ lattice_vector }} ~ 3
    {% endloop %}
    {{ elements }} ~ 3
    {{ element_num }} ~ 3
    {{ model }}
    {% if direct %}
        {% loop sum(element_num) %}
          {{ Coordinates }} ~ 3
        {% endloop %}
    {% else %}
        {{ Direct }}
        {% loop sum(element_num) %}
          {{ Coordinates }} ~ 6
        {% endloop %}
    {% endif %}
    {% loop n %}
        {{ other }}
    {% endloop %}
    """
    basepath = os.path.join(current_dir, 'testdata\\')
    poscar_file = basepath + 'POSCAR'
    poscar_t = basepath + 'poscar_template.txt'

    parser = DataTemplate(poscar_template, poscar_file)
    parser.parse()
    result = parser.result()
    print(f'--result:{result}')

test_poscar_parse()
# # run the function with profiling enabled
# cProfile.run('test_poscar_parse()', 'profile_stats')
#
# # create a pstats object from the stats file
# p = pstats.Stats('profile_stats')
#
# # sort the stats by cumulative time spent in each function
# p.sort_stats('cumulative')
#
# # print out the top 10 functions by cumulative time spent
# p.print_stats(10)

