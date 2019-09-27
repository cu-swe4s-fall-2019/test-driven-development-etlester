# test-driven-dev
Test Driven Development

data_viz_update
- made the data_viz.py method that takes in an array of integers and
creates a boxplot, histogram, or both.
- created unittests for data_viz.py
- made viz.py that pulls everything together
- made sure everything conforms to pycode style


What this does:
  viz.py will plot data as either a histogram, boxplot, or both. It takes in
data via stdin along with the following parameters: --out_file (string),
--col_num (int), --plot_type(string).
The following plot_plot types are acceptable: boxplot, histogram, or combo.

How to use it
- The usage example below generates two columns of random data in gen_data.sh
and pipes it to viz.py. The following parameters are also passed to viz.py:
--out_file test_file.png, --col_num 0, --plot_type combo.
- This will generate both a histogram and a box plot of column 1 of the
randomly generated data passed via stdin
Usage Example: bash gen_data.sh | python viz.py --out_file combo_test.png --col_num 1 --plot_type combo

How to install it
- wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
- bash Miniconda3-latest-Linux-x86_64.sh -b
- . /home/travis/miniconda3/etc/profile.d/conda.sh
- conda update --yes conda
- conda config --add channels r
- conda create --yes -n test
- conda activate test
- conda install -y pycodestyle
- conda install --yes python=3.6
- git clone the repository
