import numpy as np
import matplotlib.transforms as transforms
from matplotlib.patches import Ellipse
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score, roc_curve


def confidence_ellipse(mu, cov, ax, n_std=3.0, facecolor='none', **kwargs):
    """
    Create a plot of the covariance confidence ellipse of *x* and *y*.

    Parameters
    ----------
    mu : vector of means

    cov: covariance matrix

    ax : matplotlib.axes.Axes
        The axes object to draw the ellipse into.

    n_std : float
        The number of standard deviations to determine the ellipse's radiuses.

    Returns
    -------
    matplotlib.patches.Ellipse

    Other parameters
    ----------------
    kwargs : `~matplotlib.patches.Patch` properties
    """

    pearson = cov[0, 1] / np.sqrt(cov[0, 0] * cov[1, 1])
    # Using a special case to obtain the eigenvalues of this
    # two-dimensionl dataset.
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0),
                      width=ell_radius_x * 2,
                      height=ell_radius_y * 2,
                      facecolor=facecolor,
                      **kwargs)

    # Calculating the stdandard deviation of x from
    # the squareroot of the variance and multiplying
    # with the given number of standard deviations.
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = mu[0]

    # calculating the stdandard deviation of y ...
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = mu[1]

    transf = transforms.Affine2D() \
        .rotate_deg(45) \
        .scale(scale_x, scale_y) \
        .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)


def grid(xs, ys, f):
    """x and y coordinate descriptions as returns a 2D grid  of function f  evaluated on
    every xy combination.

    Takes grid
    :param xs: 1D array of x grid point coordinates
    :param ys: 1D array of y grid point coordinate
    :param f: function  taking a  lenght two array (xy) as argument, that  can thread automatically ver a Nx2 array.
    :return: xs, ys, f evaluated on xy.
    """
    grid = np.stack(np.meshgrid(xs, ys), axis=2).reshape(-1, 2)
    fs = f(grid).reshape(len(xs), len(ys))
    return xs, ys, fs


def roc_plot(figsize=[8, 8]):
    """Returns figure and axes object for plotting ROC curve
    setting aspect ration to one and labeling the axes.
    """
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_aspect(1)
    ax.set_xlabel('FPR')
    ax.set_ylabel('TPR')
    ax.plot([0, 1], [0, 1], linewidth=1, linestyle='--', color='grey')
    return fig, ax


def add_roc_curve(y_true, y_score, name, ax=plt.gca, **kwargs):
    if not ax:
        ax = plt.gca()
    fprs, tprs, thds = roc_curve(y_true, y_score)
    auc = roc_auc_score(y_true, y_score)
    ax.plot(fprs, tprs, label="{1:5.3f} {0:s} ".format(name, auc), **kwargs);
    return fprs, tprs, thds, auc


def decision_mask(xs, ys, proba, decision, colors):
    grid = np.stack(np.meshgrid(xs, ys), axis=2)
    p = proba(grid.reshape(-1, 2)).reshape(len(xs), len(ys), -1)
    pc = np.apply_along_axis(decision, 2, p)
    return colors[pc]


def decision_plot(data, lbls, colors, xs, ys, proba, decision, ax=None):
    if ax is None:
        ax = plt.gca()
    msk = decision_mask(xs, ys, proba, decision, colors)
    ax.imshow(msk, extent=(xs.min(), xs.max(), ys.min(), ys.max()), origin='lower', aspect='auto', alpha=0.2)
    max_l = np.max(lbls)
    min_l = np.min(lbls)
    labels = lbls - min_l
    n_lbls = max_l - min_l + 1
    for l in range(n_lbls):
        ax.scatter(data[labels == l, 0], data[labels == l, 1], c=[colors[l]], alpha=0.3)
