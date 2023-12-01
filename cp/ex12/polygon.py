import numpy as np
import matplotlib.pyplot as plt


class Polygon:
    def __init__(self, points):
        self.x = np.array([point[0] for point in points])
        self.y = np.array([point[1] for point in points])

    # def plot_polygon(self):
    #     plt.figure(figsize=(6, 6))
    #     plt.plot(np.append(self.x, self.x[0]), np.append(self.y, self.y[0]), marker="o")
    #     plt.xlabel("X-axis")
    #     plt.ylabel("Y-axis")
    #     plt.title("Polygon")
    #     plt.grid()
    #     plt.show()

    # def get_area(self):
    #     return 0.5 * np.abs(
    #         np.dot(self.x, np.roll(self.y, 1)) - np.dot(self.y, np.roll(self.x, 1))
    #     )

    def get_perimeter(self):
        return np.sum(
            np.sqrt(
                (np.roll(self.x, -1) - self.x) ** 2
                + (np.roll(self.y, -1) - self.y) ** 2
            )
        )

    def smooth_polygon(self, alpha):
        if len(self.x) < 3 or len(self.y) < 3:
            return

        num_points = len(self.x)
        smoothed_points = []

        for i in range(num_points):
            new_x = (1 - alpha) * self.x[i] + alpha * 0.5 * (
                self.x[i - 1] + self.x[(i + 1) % num_points]
            )
            new_y = (1 - alpha) * self.y[i] + alpha * 0.5 * (
                self.y[i - 1] + self.y[(i + 1) % num_points]
            )
            smoothed_points.append((new_x, new_y))

        self.x, self.y = zip(*smoothed_points)
