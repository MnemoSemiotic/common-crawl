import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_mds_dist(names, pos):
    xs, ys = pos[:, 0], pos[:, 1]

    fig = plt.figure()
    ax = fig.add_subplot()

    for x, y, name in zip(xs, ys, names):
        if names[0] == name:
            color = 'orange'
        elif names[1] == name:
            color = 'red'
        else:
            color = 'green'


        ax = plt.scatter(x, y, c=color)
        ax = plt.text(x, y, name)
    plt.savefig('temp_mds2d.png')
    plt.show()


def plot_mds_dist3d(names, pos):
    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2])

    for x, y, z, s in zip(pos[:, 0], pos[:, 1], pos[:, 2], names):
        ax.text(x, y, z, s)

    plt.savefig('temp_mds3d.png')
    plt.show()

if __name__ == '__main__':
    pass
