import matplotlib.pyplot as plt


def png(generator, target_path):
    plt.imsave(target_path, generator())
