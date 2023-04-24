import pandas as pd
from data_loading import preprocess_data, split_data_by_investment_experience
from visualization import tex_to_pdf, create_pie_chart, create_histogram, create_age_histogram
from data_analysis import run_linear_regression, run_multiple_linear_regressions
from stargazer.stargazer import Stargazer


def main():

    # Preprocess the data
    preprocessed_data = preprocess_data()

    # Split the data based on investment experience
    investors_yes, investors_no = split_data_by_investment_experience(
        preprocessed_data)

    # if investors_yes.shape[0] > 0:
    #     # Define the dependent variable
    #     dependent_var = 'How confident are you in your ability to make investment decisions?'

    #     # Define different sets of independent variables
    #     independent_vars_list = [
    #         ['How old are you?', 'How would you rate your overall financial knowledge?'],
    #         ['How old are you?', 'How would you describe your risk tolerance?'],
    #         ['How would you rate your overall financial knowledge?', 'How would you describe your risk tolerance?']
    #     ]

    #     # Run multiple linear regressions
    #     results = run_multiple_linear_regressions(investors_yes, dependent_var, independent_vars_list)

    #     # Save the regression summaries to a PDF file
    #     for i, (independent_vars, model) in enumerate(results):
    #         summary = model.summary()
    #         save_regression_summary_to_pdf(summary, f'regression_summary_{i+1}.pdf')

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

        # Create stargazer object with the list of fitted models
        stargazer = Stargazer(fitted_models)

        # Render the LaTeX code
        latex_code = stargazer.render_latex()

        # Save the LaTeX code to a file
        with open('output/regression_summary.tex', 'w') as f:
            f.write(latex_code)
            
        tex_file = 'output/regression_summary.tex'
        pdf_file = tex_to_pdf(tex_file, 'output/')
        print("Regression summary saved to regression_summary.pdf")
    else:
        print("No data available for investors with investment experience.")

    #summary = model.summary()
    
    #save_regression_summary_to_pdf(summary, 'regression_summary.pdf')


    # run_data_analysis(preprocessed_data)

    # create_age_histogram(preprocessed_data, 'How old are you?',
   #                      'Age Distribution', 'age_histogram.png')

    # print("Visualizations created successfully!")


if __name__ == '__main__':
    main()
