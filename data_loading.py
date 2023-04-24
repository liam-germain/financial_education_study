import pandas as pd
from config import QUESTIONS, QUESTION_13
pd.set_option("display.max_columns", None)

def load_data():
    csv_file = 'data/IS_responses.csv'
    return pd.read_csv(csv_file)


def convert_categorical_data(data):
    # Convert categorical columns to numeric using one-hot encoding
    categorical_columns = []

    # Loop through the questions and add the ones with "categorical" answer_type to the list
    for question in QUESTIONS:
        if question["answer_type"] == "categorical":
            categorical_columns.append(question["text"])

    data = pd.get_dummies(data, columns=categorical_columns, drop_first=True)

    return data


def convert_numerical_data(data, numerical_columns=None):
    if numerical_columns is None:
        numerical_columns = [
            question["text"] for question in QUESTIONS if question["answer_type"] == "numerical"
        ]

    available_columns = set(data.columns)

    for column in numerical_columns:
        column = column.strip()
        if column not in available_columns:
            print(f"Column '{column}' not found in DataFrame.")
            continue

        min_value = data[column].min()
        max_value = data[column].max()
        data[column] = (data[column] - min_value) / (max_value - min_value)

    return data


def convert_option_data(data):
    option_columns = [
        question for question in QUESTIONS if question["answer_type"] == "multi_select"
    ]

    for question in option_columns:
        column_name = question["text"]
        options = question["options"]

        for option in options:
            data[f"{column_name}_{option}"] = data[column_name].apply(
                lambda x: 1 if isinstance(x, str) and option in x else 0
            )

    return data



def preprocess_data():
    # Your data preprocessing code here
    data = load_data()

    data = convert_categorical_data(data)
    data = convert_option_data(data)
    data = convert_numerical_data(data)
     
    data = data.select_dtypes(exclude=['object'])

    #print(data.columns)
    #print(data.info())
    # print([col for col in data.columns if "Have you previously or do you currently invest in any public markets?" in col])

    return data



# def split_data_by_investment_experience(data):
#     question_text = QUESTION_13["text"]
#     options = QUESTION_13["options"]

#     # Identify the columns representing the options for the question
#     investment_experience_cols = [f"{question_text}_{option}" for option in options]

#     # Filter rows based on the option "Yes"
#     investors_yes = data[data[investment_experience_cols[0]] == 1]

#     # Filter rows based on the option "No"
#     investors_no = data[data[investment_experience_cols[1]] == 1]

#     return investors_yes, investors_no



def split_data_by_investment_experience(data):
    yes_column = 'Have you previously or do you currently invest in any public markets?_Yes'

    # Filter rows based on the "Yes" option
    investors_yes = data[data[yes_column] == 1]

    # Filter rows based on the "No" option
    investors_no = data[data[yes_column] == 0]

    return investors_yes, investors_no
