import pandas as pd
from data_loading import preprocess_data, split_data_by_investment_experience
from visualization import generate_regression_summary, tex_to_pdf, create_pie_chart, create_histogram, create_age_histogram
from data_analysis import run_linear_regression, run_multiple_linear_regressions
from stargazer.stargazer import Stargazer


def main():

    # Preprocess the data
    preprocessed_data = preprocess_data()

    # Split the data based on investment experience
    investors_yes, investors_no = split_data_by_investment_experience(
        preprocessed_data)

    if investors_yes.shape[0] > 0:
        # Define the dependent variable
        dependent_var = 'How confident are you in your ability to make investment decisions?'

        # Define different sets of independent variables
        independent_vars_list = [
            ['How old are you?', 'How would you rate your overall financial knowledge?'],
            ['How old are you?', 'How would you describe your risk tolerance?'],
            ['How would you rate your overall financial knowledge?', 'How would you describe your risk tolerance?']
        ]

        # Run multiple linear regressions and get the list of fitted models
        fitted_models = run_multiple_linear_regressions(investors_yes, dependent_var, independent_vars_list)

        # Call the modified generate_regression_summary function
        generate_regression_summary(fitted_models, 'output/regression_summary.tex')
    else:
        print("No data available for investors with investment experience.")


if __name__ == '__main__':
    main()
