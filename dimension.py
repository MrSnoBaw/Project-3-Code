import matplotlib.pyplot as plt
from sampler import *
from mlpack import emst
from math import log10
from sklearn.linear_model import LinearRegression as linreg

# We always work in n-dimensional Euclidean space.

def get_distances(points, ptnum):
    lp = len(points)
    for n in np.logspace(3, log10(lp), ptnum, base=10):
        print(f"Computing intervals: {round((n/lp)**2*100, 2)} %")
        yield emst(points[:int(n + 1)])['output'][:, 2]

def PH_dim(pts, alpha_range, ptnum = 100):
    dimension_values = []
    x, ys = np.linspace(3, log10(len(pts)), ptnum), [np.zeros(ptnum) for _ in range(len(alpha_range))]
    for ind, distances in enumerate(get_distances(pts, ptnum)):
        for ind1, alpha in enumerate(alpha_range):
            ys[ind1][ind] = log10(np.sum(distances**alpha))

    for alpha, y in zip(alpha_range, ys):
        reg = linreg().fit(x.reshape((-1, 1)), y)
        if reg.score(x.reshape((-1, 1)), y) > 0.95:
            dimension_values.append(alpha / (1 - reg.coef_))
    return sum(dimension_values)/len(dimension_values)

def compute_dimrange(alpha, E_values, sample_sizes, ptnum):
    dim_values = np.zeros(ptnum)
    for n in range(ptnum):
        reg = linreg().fit(sample_sizes[:n + 1].reshape((-1, 1)), E_values[:n + 1])
        dim_values[n] = alpha / (1 - reg.coef_) 
    return dim_values

def plot_dim_vs_samples(pts, alpha_range, fractal_name, true_dim, ptnum = 100):
    sample_sizes = np.linspace(3, log10(len(pts)), ptnum)
    E_values = [np.zeros(ptnum) for _ in range(len(alpha_range))]

    for ind, intervals in enumerate(get_distances(pts, ptnum)):
        for ind1, alpha in enumerate(alpha_range):
            E_values[ind1][ind] = log10(np.sum(intervals ** alpha))
    fig, ax = plt.subplots()
    plt.title(fractal_name)
    ax.plot([1000, len(pts)], [true_dim, true_dim], '--', color = "black", label = f"Hausdorff dimension {round(true_dim, 4)}")

    for alpha, E_values in zip(alpha_range, E_values):
        dim_estimates = compute_dimrange(alpha, E_values, sample_sizes, ptnum)
        ax.plot(10**sample_sizes, dim_estimates)
    plt.ylim(true_dim-0.5, true_dim + 0.5)
    plt.xlabel("Sample size")
    plt.ylabel("Dimension estimate")
    plt.show()

sampler = {
    "Dragon curve" : dragon_sample,
    "Sierpinski triangle" : sierpinski_triangle_sample, 
    "Sierpinski carpet" : sierpinski_carpet_sample,  
    "Cantor set cross an interval" : cantor_interval_sample, 
    "Square" : square_sample, 
    "Circle" : circle_sample
    }

dims = [2, log10(3)/log10(2), log10(8)/log10(3), 1 + log10(2)/log10(3), 2, 2]

alpha_num = 10

alpha_ranges = [
    np.linspace(0.1, 2 - 0.001, alpha_num),
    np.linspace(0.1, log10(3)/log10(2) - 0.001, alpha_num),
    np.linspace(0.1, log10(8)/log10(3) - 0.001, alpha_num),
    np.linspace(0.1, 1 + log10(2)/log10(3) - 0.001, alpha_num),
    np.linspace(0.1, 2 - 0.001, alpha_num),
    np.linspace(0.1, 2 - 0.001, alpha_num)
]

for fractal_name, true_dim, arange in zip(sampler, dims, alpha_ranges):
    plot_dim_vs_samples(sampler[fractal_name](10**6), arange, fractal_name, true_dim, ptnum=100)
    
