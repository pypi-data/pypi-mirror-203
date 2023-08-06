import pytest
from tsstp.datatemplate import DataTemplate


@pytest.mark.benchmark
def test_match_performance(benchmark):
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
    basepath = 'D:\\workspace\\MDI\\datatemplate\\test\\testdata\\'
    outcar = basepath + 'OUTCAR'

    def run_parser():

        parser = DataTemplate(final_energy, outcar)
        result = parser.match()

    benchmark(run_parser)

@pytest.mark.benchmark
def test_poscar_parse_performance(benchmark):
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
    basepath = 'D:\\workspace\\MDI\\datatemplate\\test\\testdata\\'
    poscar_file = basepath + 'POSCAR'

    def run_parser():
        parser = DataTemplate(poscar_template, poscar_file)
        parser.parse()
        result = parser.result()

    benchmark(run_parser)

@pytest.mark.benchmark
def test_xdatcar_parse_performance(benchmark):
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

    basepath = 'D:\\workspace\\MDI\\datatemplate\\test\\testdata\\'
    xdatacar_file = basepath + 'XDATCAR'

    def run_parser():
        parser = DataTemplate(xdatacar_template, xdatacar_file)
        parser.parse()
        result = parser.result()

    benchmark(run_parser)

@pytest.mark.benchmark
def test_incar_search_performance(benchmark):
    search_template1 = """
    {{ key }} = {{ value }}
    """

    basepath = 'D:\\workspace\\MDI\\datatemplate\\test\\testdata\\'
    incar = basepath + 'INCAR'
    def run_parser():
        parser = DataTemplate(search_template1, incar)
        result = parser.search()

    benchmark(run_parser)