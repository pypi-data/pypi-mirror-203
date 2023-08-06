import os
import cProfile
import pstats
from tsstp.datatemplate import DataTemplate

# 获取当前脚本所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))

def test_match():
    match_template1 = """
    loop
    {{ key }} = {{ value }}
    {{ key1 }} = {{ value1 }}
    {{ key2 }} = {{ value2 }}
    end
    """

    final_energy = """
    Free energy of the ion-electron system (eV)
    {{ separator1 }} ~ n
    alpha Z PSCENC = {{ PSCENC }}
    Ewald energy TEWEN  =  {{ TEWEN }}
    -Hartree energ DENC = {{ DENC }}
    -exchange EXHF = {{ EXHF }}
    -V(xc)+E(xc)  XCENC  = {{ XCENC }}
    PAW double counting  =  {{ PAW }}
    entropy T*S EENTRO = {{ EENTRO }}
    eigenvalues  EBANDS =  {{ EBANDS }}
    atomic energy  EATOM  = {{ EATOM }}
    Solvation  Ediel_sol  = {{ Ediel_sol }}
    {{ separator2 }} ~ n
    free energy  TOTEN  =  {{ TOTEN }} eV
    energy without entropy =  {{ entropy }} energy(sigma->0) =  {{ energy }} 
    """
    basepath = os.path.join(current_dir, 'testdata\\')
    text_file = basepath + 'text_file.txt'
    outcar = basepath + 'OUTCAR'
    outcar_t = basepath + 'outcar_template.txt'

    parser = DataTemplate(outcar_t, outcar)
    result = parser.match()
    # print(f'--result:{result}')

# run the function with profiling enabled
cProfile.run('test_match()', 'profile_stats')

# create a pstats object from the stats file
p = pstats.Stats('profile_stats')

# sort the stats by cumulative time spent in each function
p.sort_stats('cumulative')

# print out the top 10 functions by cumulative time spent
p.print_stats(10)