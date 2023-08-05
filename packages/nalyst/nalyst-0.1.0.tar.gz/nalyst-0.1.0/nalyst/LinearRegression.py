from typing import List, Tuple


class LinearRegression:
    """
    Class for building and analyzing a linear regression model.

    Attributes:
        x (List[float]): List of x values.
        y (List[float]): List of y values.
        x_mean (float): Mean of x values.
        y_mean (float): Mean of y values.
        x_value (List[float]): List of x values minus x_mean.
        y_value (List[float]): List of y values minus y_mean.
        x_value_square (List[float]): List of squared x values.
        x_value_square_total (float): Sum of x_value_square.
        x_y_value_square (List[float]): List of product of x_value and y_value.
        x_y_value_square_total (float): Sum of x_y_value_square.
        b1 (float): Regression coefficient b1.
        bo (float): Regression coefficient bo.
        n (int): Number of observations.

    Methods:
        predict(x: List[float]) -> List[float]: Generate predicted y values based on a list of x values.
        mse() -> float: Calculate the mean squared error of the model.
        rmse() -> float: Calculate the root mean squared error of the model.
        r_squared() -> float: Calculate the R-squared value of the model.
    """

    def __init__(self, x: List[float], y: List[float]):
        """
        Initialize the LinearRegressionModel class.

        Args:
            x (List[float]): List of x values.
            y (List[float]): List of y values.
        """
        self.x = x
        self.y = y
        self.x_mean = sum(x) / len(x)
        self.y_mean = sum(y) / len(y)
        self.x_value = list(map(lambda value: value - self.x_mean, x))
        self.y_value = list(map(lambda value: value - self.y_mean, y))
        self.x_value_square = list(map(lambda value: value**2, self.x_value))
        self.x_value_square_total = sum(self.x_value_square)
        self.x_y_value_square = list(
            map(lambda xv, yv: xv * yv, self.x_value, self.y_value))
        self.x_y_value_square_total = sum(self.x_y_value_square)
        self.b1 = self.x_y_value_square_total / self.x_value_square_total
        self.bo = self.y_mean - (self.b1 * self.x_mean)
        self.n = len(x)

    def predict(self, x: List[float]) -> List[float]:
        """
        Generate predicted y values based on a list of x values.

        Args:
            x (List[float]): List of x values.

        Returns:
            List[float]: List of predicted y values.
        """
        return list(map(lambda xi: self.bo + self.b1 * xi, x))

    def mse(self) -> float:
        """
        Calculate the mean squared error of the model.

        Returns:
            float: Mean squared error of the model.
        """
        y_pred = self.predict(self.x)
        return sum(list(map(lambda y_pred_i, y_i: (y_pred_i - y_i)**2, y_pred, self.y))) / self.n

    def rmse(self) -> float:
        """
        Calculate the root mean squared error of the model.

        Returns:
            float: Root mean squared error of the model.
        """
        return self.mse() ** 0.5

    def r_squared(self) -> float:
        """Compute the R-squared value of the linear regression model. 

       Returns:
           float: R-squared value.
       """
        y_mean_line = [self.y_mean for _ in self.y]
        total_sum_squares = sum(
            [(y - y_mean_line[idx])**2 for idx, y in enumerate(self.y)])
        residual_sum_squares = sum(
            [(self.y[idx] - self.predict([x])[0])**2 for idx, x in enumerate(self.x)])
        return 1 - (residual_sum_squares / total_sum_squares)
