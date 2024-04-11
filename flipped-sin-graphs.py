import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def sinplot(n=10, flip=1):
    plt.switch_backend('TkAgg')  # Or any other backend that works for you
    x = np.linspace(0, 14, 100)
    for i in range(1, n + 1):
        plt.plot(x, np.sin(x + i * .5) * (n + 2 - i) * flip)
    plt.gca().set(xlabel='Time/s', ylabel='Amplitude/m')
    plt.show()

sinplot()

# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt

# def sinplot(n=10, flip=1):
#     plt.switch_backend('TkAgg')  # Or any other backend that works for you
#     x = np.linspace(0, 14, 100)
#     for i in range(1, n + 1):
#         ax=plt.plot(x, np.sin(x + i * .5) * (n + 2 - i) * flip)
#     ax.set(xlabel='common xlabel', ylabel='common ylabel')
#     plt.show()

# sinplot()
