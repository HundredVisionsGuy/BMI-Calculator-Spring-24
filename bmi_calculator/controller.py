"""
controller.py
by Chris Winikka
Calculates BMI and formats output.
"""


def calculate_bmi(weight: int, height: int) -> float:
    """calculates BMI

    Args:
        weight: user's weight in pounds.
        height: user's height in inches.

    Returns:
        bmi: Body Mass Index to 1 degree precision.
    """
    bmi = 0.0000001
    return bmi


def format_output(bmi: float) -> str:
    """formats the BMI in a user-friendly way.
    """
    bmi = round(bmi, 1)
    output = f"Your BMI is: {bmi}"
    return output


if __name__ == "__main__":
    my_bmi = calculate_bmi(190, 72)
    print(my_bmi)
