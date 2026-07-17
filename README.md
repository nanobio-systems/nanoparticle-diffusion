# Nanoparticle Diffusion Simulation

A Python-based computational research project investigating Brownian motion and nanoparticle diffusion through simulation, analysis, and theoretical modelling.

This repository was developed as a first scientific computing project while learning Python for computational biology and nanobiotechnology. It demonstrates how theoretical diffusion models can be implemented, analysed and compared with simulation results using reusable Python modules and Jupyter notebooks.

The project is inspired by the methods presented in the following publication:

> *Simulation study of nanoparticle diffusion...* (2025), *International Journal of Heat and Mass Transfer*.

Rather than reproducing the paper exactly, this repository recreates many of the underlying computational ideas using an educational implementation designed to build reusable scientific programming skills.

---

# Objectives

The goals of this project are to:

* Learn Python for scientific research.
* Develop reusable scientific software rather than standalone scripts.
* Simulate Brownian motion of nanoparticle populations.
* Estimate diffusion coefficients from simulated trajectories.
* Compare simulated diffusion coefficients with theoretical predictions from the Stokes–Einstein equation.
* Produce publication-quality figures.
* Build a portfolio-quality GitHub project.

---

# Repository Structure

```text
nanoparticle-diffusion-104337/

├── notebooks/
│   ├── 01_project_setup.ipynb
│   ├── 02_random_walk.ipynb
│   ├── 03_brownian_motion.ipynb
│   ├── 04_population_simulation.ipynb
│   ├── 05_msd_analysis.ipynb
│   ├── 06_diffusion_coefficient.ipynb
│   ├── 07_parameter_study.ipynb
│   ├── 08_paper_reproduction.ipynb
│   └── 09_discussion.ipynb
│
├── src/
│   ├── __init__.py
│   ├── constants.py
│   ├── physics.py
│   ├── simulation.py
│   ├── analysis.py
│   ├── validation.py
│   └── plotting.py
│
├── tests/
├── figures/
├── data/
├── references/
│
├── environment.yml
├── README.md
├── LICENSE
└── .gitignore
```

---

# Scientific Background

Nanoparticles suspended in fluids experience continual random collisions with surrounding molecules. This process, known as **Brownian motion**, leads to diffusion.

The theoretical diffusion coefficient for spherical particles is given by the **Stokes–Einstein equation**:

$$
D = \frac{k_B T}{6\pi \eta r}
$$

where:

* (D) = diffusion coefficient
* (k_B) = Boltzmann constant
* (T) = temperature
* (\eta) = fluid viscosity
* (r) = particle radius

This project simulates Brownian motion, measures the mean squared displacement (MSD), estimates the diffusion coefficient from simulated trajectories, and compares those estimates with theoretical predictions.

---

# Installation

Clone the repository.

```bash
git clone https://github.com/<username>/nanoparticle-diffusion-104337.git
```

Move into the project directory.

```bash
cd nanoparticle-diffusion-104337
```

Create the Conda environment.

```bash
conda env create -f environment.yml
```

Activate the environment.

```bash
conda activate research
conda env list
```

Launch Jupyter.

```bash
jupyter lab
```

or

```bash
jupyter notebook
```

---

# Running the Project

The notebooks are designed to be completed in order.

1. Project setup
2. Random walks
3. Brownian motion
4. Population simulation
5. Mean squared displacement
6. Diffusion coefficient estimation
7. Parameter study
8. Main paper-inspired reproduction
9. Summary of results and visualises outputs

Each notebook builds on reusable code contained in the `src/` package.

---

# Software Architecture

The repository separates reusable scientific code from analysis notebooks.

The `src/` package contains reusable functions for:

* physical equations
* simulation
* data analysis
* plotting
* validation

The notebooks demonstrate how those functions are used in scientific investigations.

This separation mirrors the structure used in many research codebases.

---

# Outputs

Running the notebooks will generate:

* Brownian motion trajectories
* Mean squared displacement curves
* Diffusion coefficient estimates
* Parameter studies
* Comparison plots between simulation and theory
* Publication-quality figures saved in the `figures/` directory

Example outputs include:

- `figures/figure_radius_vs_diffusion.png`

---

# Testing

Automated tests are provided in the `tests/` directory. The tests verify that core scientific functions behave correctly, including:
- diffusion calculations
- Brownian simulation outputs
- MSD analysis

Run them using:

```bash
pytest
```

---

# Future Development

Possible future improvements include:

* Three-dimensional diffusion
* Constrained diffusion environments
* Extracellular matrix simulations
* Experimental dataset comparison
* Particle–particle interactions
* Variable viscosity environments
* Temperature-dependent diffusion studies
* Performance optimisation using NumPy vectorisation

---

# References

Primary inspirations:

* Yang et al. (2025) *[Pore-scale analysis of nanoparticle diffusion in brain tumours]
* International Journal of Heat and Mass Transfer (2025).

This project implements a simplified educational reproduction of the computational concepts presented in the paper, including Brownian motion simulation, diffusion modelling, and analysis of nanoparticle transport behaviour.

Additional references:

* Berg, H.C. (1993). *Random Walks in Biology.*
* Allen, M.P. & Tildesley, D.J. (2017). *Computer Simulation of Liquids.*
* NumPy documentation
* Matplotlib documentation

---

# License

This project is released under the MIT License.

---

# Acknowledgements

This repository was developed as a self-directed scientific programming project to build practical skills in computational biology, nanobiotechnology and research software development while reproducing concepts from the scientific literature.
