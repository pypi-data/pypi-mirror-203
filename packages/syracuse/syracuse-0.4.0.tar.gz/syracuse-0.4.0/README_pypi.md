![PyPI - Python Version](https://img.shields.io/pypi/pyversions/syracuse)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/devfred78/syracuse)
![GitHub](https://img.shields.io/github/license/devfred78/syracuse)
![GitHub issues](https://img.shields.io/github/issues/devfred78/syracuse)
![GitHub pull requests](https://img.shields.io/github/issues-pr/devfred78/syracuse)

![Graph of the first 26 compressed Collatz sequences](https://github.com/devfred78/syracuse/blob/main/assets/graph_compressed_syracuse_26.png?raw=True)
*(Graph of the first 26 compressed Collatz sequences)*

# Syracuse

syracuse, The Syracuse problem (aka Collatz conjecture) library.

## About the project

The syracuse library provides a way to generate Collatz sequences (either "normal" or compressed forms) and some functions to deal with.

### The Collatz conjecture

The Collatz conjecture, also known as the "3n + 1 problem" or the "Syracuse problem", is an unsolved hypothesis in mathematics that concerns a sequence of operations applied to a positive integer. The conjecture states that no matter what the starting value of this integer is, the sequence will always eventually reach the value 1.

More specifically, the Collatz conjecture states that if one takes a positive integer n and applies the following function:

- If n is even, divide it by 2.
- If n is odd, multiply it by 3 and add 1.

Then, repeat the process with the resulting value, applying the function over and over again until the value of n eventually reaches 1.

> For example, if one takes n = 6, the sequence for the Collatz conjecture would be:
> 6, 3, 10, 5, 16, 8, 4, 2, 1.

Although the conjecture has been computationally tested for extremely large values, it remains unproven to this day.

### The compressed form

*(definition partially inspired by the [relevant article on Wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture))*

Since 3n+1 is even whenever n is odd, one may instead use the "compressed" form of the Collatz function:

- if n is even, divide it by 2.
- if n is odd, multiply it by 3, add 1 **and divide the result by 2**.

This definition yields smaller values for the stopping time and total stopping time without changing the overall dynamics of the process. 

> For example, consider the Collatz sequence for the number 17:
> 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1
>
> The compressed form of this sequence would be:
> 17, 26, 13, 20, 10, 5, 8, 4, 2, 1

The compressed form of the Collatz sequence has been the subject of much research, as it provides insights into the behavior of the original sequence and can be used to search for cycles and other patterns. However, the Collatz conjecture itself remains unproven, and the compressed form of the sequence does not provide a proof or disproof of the conjecture.

### Why the name "syracuse" ?

The Collatz conjecture is also known as the Syracuse problem because it was first introduced by Lothar Collatz in a 1950 paper, where he credited his colleague, mathematician Helmut Hasse, with calling it the Syracuse problem. The name "Syracuse" refers to the University of Syracuse, where Collatz was working at the time.

The name "Syracuse problem" has since become a common alternative to "Collatz conjecture", especially in French and Italian-speaking countries, where it is often referred to as the "problème de Syracuse" or "problema di Syracuse", respectively.

Regardless of the name used, the conjecture remains one of the most famous and challenging open problems in mathematics, and it continues to attract the attention of mathematicians and computer scientists around the world.

## Getting started

### Prerequisites

Of course, syracuse cannot run without Python ! More precisely, it requires at least the 3.11 version of our beloved language.

syracuse depends on the following packages. The installation of syracuse should install automatically those packages if they are missing on your system. If it fails, you can install them individually:

* networkx: version 3.0.0 or above

	```sh
	pip install networkx["default"]
	```

* matplotlib: version 3.6.0 or above

	```sh
	pip install matplotlib
	```

* numpy: version 1.24.0 or above

	```sh
	pip install numpy
	```

* pydot: version 1.4.2 or above

	```sh
	pip install pydot
	```

* more-itertools: version 9.1.0 or above

	```sh
	pip install more-itertools
	```

### Installation

Install from PyPi with:

```sh
pip install syracuse
```

As an alternative, you can download the `*.whl` file from the last [release on the syracuse Github repository](https://github.com/devfred78/syracuse/releases), and execute the following command (replace "X.Y.Z" by the right version number):

```sh
pip install syracuse-X.Y.Z-py3-none-any.whl
```

## Usage

Basic usage:

```pycon
>>> # Import the core library
>>> import syracuse

>>> # Create a Syracuse sequence with 27 as initial value
>>> my_sequence = syracuse.Syracuse(27)

>>> # Stopping time
>>> my_sequence.stopping_time
96
>>> # Total stopping time
>>> my_sequence.total_stopping_time
111
>>> # Maximum reached value
>>> my_sequence.max
9232
>>> # Full sequence (until 1)
>>> my_sequence.total_stopping_sequence
(27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161,
 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155,
 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780,
 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566,
 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079,
 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102,
 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433,
 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35,
 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1)

>>> # Import the sequences library
>>> import syracuse.sequences

>>> # Create an iterator over the records of the max values (A006884)
>>> # with all possible optimizations
>>> max_records = syracuse.sequences.max_value_records(15)

>>> # Iterate over the first 30 records
>>> for _ in range(30):
...		print(f"{next(max_records)}, ", end="", flush=True)
...
1, 2, 3, 7, 15, 27, 255, 447, 639, 703, 1819, 4255, 4591, 9663,
20895, 26623, 31911, 60975, 77671, 113383, 138367, 159487, 270271,
665215, 704511, 1042431, 1212415, 1441407, 1875711, 1988859,

>>> # Import the drawing library
>>> import syracuse.drawing

>>> # Display the full sequence in a Matplotlib window
>>> syracuse.drawing.single_sequence_to_matplotlib_figure(my_sequence, test=True)
```

![Matplotlib graphical view of the successive values of the sequence Syracuse(27)](https://github.com/devfred78/syracuse/blob/main/assets/graph_sequence_27_reduced.png?raw=True)

For deeper explanations, please refer to the [documentation](https://devfred78.github.io/syracuse/).

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement" or "bug", according to whether you want to share a proposal of a new function, or to record an anomaly.

Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. Check out [LICENSE.md](https://github.com/devfred78/syracuse/blob/main/LICENSE.md) file for more information.

## Acknowledgments

I would like greatfully to thank:

Graphviz [authors](https://graphviz.org/) for this impressive graph visualization software, especially for the creation of the useful [DOT Langage](https://graphviz.org/doc/info/lang.html).

[The Matplotlib development team](https://matplotlib.org/) for providing a very powerful library "for creating static, animated, and interactive visualizations in Python".

NumPy [community](https://numpy.org/) for this fundamental tool to be used as a priority if you want make serious scientific computations with Python.

[MkDocs](https://www.mkdocs.org/), [mkdocstrings](https://mkdocstrings.github.io/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) for giving the ability to create in a very simple way an accessible documentation for either tiny or big projects.

[Make a README](https://www.makeareadme.com/), [Sayan Mondal](https://medium.com/swlh/how-to-make-the-perfect-readme-md-on-github-92ed5771c061), [Hillary Nyakundi](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/) and [othneildrew](https://github.com/othneildrew/Best-README-Template) for providing very interesting materials to write good README files (far better than I can write by myself !).

[Choose an open source license](https://choosealicense.com/) for helping to choose the best suitable license for this project.

[Semantic Versioning](https://semver.org/) for providing clear specifications for versioning projects.

[Real Python](https://realpython.com/) for contributing really increasing skills in Python for everyone, novices or veterans.

[GitHub](https://github.com/) for hosting this project, and helping to share it.

[Pypi](https://pypi.org/) for providing a very convenient way to share modules and package to the entire Python community.

And, of course, all the former, current and further contributors of this project !