
# SECTION 1: DEMOGRAPHIC INFORMATION
QUESTION_1 = {
    "text": "How old are you?",
    "options": None,
    "answer_type": "numerical"
}

QUESTION_2 = {
    "text": "What is your gender?",
    "options": [
        "Male",
        "Female",
        "I prefer not to answer",
        "Other"
    ],
    "answer_type": "categorical"
}

QUESTION_3 = {
    "text": "What country are you from?",
    "options": [
        "United States",
        "China",
        "Singapore",
        ""
    ],
    "answer_type": "categorical"
}

QUESTION_4 = {
    "text": "What is your Ethnicity/Race?",
    "options": [
        "Asian",
        "Hispanic or Latino/a",
        "Black or African American",
        "Native American or Alaska Native",
        "Native Hawaiian or other Pacific islander",
        "White",
        "I prefer not to answer",
        "Other"
    ],
    "answer_type": "categorical"
}

QUESTION_5 = {
    "text": "What is your education level?",
    "options": [
        "Some High School",
        "High School",
        "Some College",
        "Associate's Degree",
        "Bachelor's Degree",
        "Master's Degree",
        "Doctorate or professional degree"
    ],
    "answer_type": "categorical"
}

QUESTION_6 = {
    "text": "What is your annual income range?",
    "options": [
        "<$25,000",
        "$25,000-$49,999",
        "$50,000-$74,999",
        "$75,000-$99,999",
        "$100,000-$124,999",
        "$125,000-$149,999",
        "$150,000-$174,999",
        "$175,000-$199,999",
        "$200,000+"
    ],
    "answer_type": "categorical"
}

QUESTION_7 = {
    "text": "What is your employment status?",
    "options": [
        "Employed Full-time",
        "Employed Part-time",
        "Self-employed",
        "Unemployed",
        "Retired",
        "Student",
        "Other"
    ],
    "answer_type": "categorical"
}

QUESTION_8 = {
    "text": "What is your marital status?",
    "options": [
        "Single/Never Married",
        "Married",
        "Widowed",
        "Divorced",
        "Separated"
    ],
    "answer_type": "categorical"
}


# SECTION 3: STATE
QUESTION_9 = {
    "text": "What State are you from?",
    "options": [
        "",
    ],
    "answer_type": "categorical"
}


# SECTION 4: FINANCIAL EDUCATION AND KNOWLEDGE
QUESTION_10 = {
    "text": "Have you ever taken any formal financial education courses?",
    "options": [
        "Yes",
        "No"
    ],
    "answer_type": "categorical"
}

QUESTION_11 = {
    "text": "From which of the following sources have you gained financial knowledge? (Select all that apply)",
    "options": [
        "Formal financial education courses",
        "Academic Courses",
        "Books or articles",
        "Workshops or seminars",
        "Trading apps (e.g., Robinhood, Webull)",
        "Social media platforms (e.g., Instagram, TikTok, Reddit)",
        "Financial advisors",
        "Family or friends",
        "General Internet Research",
        "Podcast",
        "Other"
    ],
    "answer_type": "multi_select"
}

QUESTION_12 = {
    "text": "How would you rate your overall financial knowledge?",
    "options": [1, 2, 3, 4, 5],
    "answer_type": "numerical"
}


# SECTION 5: PUBLIC MARKET PARTICIPATION
QUESTION_13 = {
    "text": "Have you previously or do you currently invest in any public markets?",
    "options": [
        "Yes",
        "No"
    ],
    "answer_type": "categorical"
}

# SECTION 6: INVESTOR BEHAVIOR AND ATTITUDES
QUESTION_14 = {
    "text": "How long have you been involved in retail trading?",
    "options": [
        "<1 year",
        "1-3 years",
        "3-5 years",
        "5-9 years",
        "10+ years"
    ],
    "answer_type": "categorical"
}

QUESTION_15 = {
    "text": "What is your primary motivation for investing?",
    "options": [
        "Long-term wealth building",
        "Short-term Gains",
        "Retirement Savings",
        "Hobby"
    ],
    "answer_type": "categorical"
}

QUESTION_16 = {
    "text": "What types of assets do you trade?",
    "options": [
        "Stocks",
        "Bonds",
        "Mutual Funds",
        "ETFs",
        "Options",
        "Cryptocurrencies",
        "NFTs"
    ],
    "answer_type": "multi_select"
}

QUESTION_17 = {
    "text": "Which trading apps, if any, do you use for investing? (Select all that apply)",
    "options": [
        "Robinhood",
        "Webull",
        "eToro",
        "E-Trade",
        "Fidelity",
        "Interactive Brokers",
        "TD Ameritrade",
        "Charles Schwab",
        "None",
        "Other"
    ],
    "answer_type": "multi_select"
}

QUESTION_18 = {
    "text": "How often do you make trades?",
    "options": [
        "Daily",
        "Weekly",
        "Monthly",
        "Quarterly",
        "Annually"
    ],
    "answer_type": "categorical"
}

QUESTION_19 = {
    "text": "Which of the following best describes your primary source of financial information for investment decisions?",
    "options": [
        "Traditional sources (e.g., financial education courses, books, workshops)",
        "Modern platforms (e.g., trading apps, social media)",
        "A combination of both traditional sources and modern platforms",
        "Other"
    ],
    "answer_type": "categorical"
}

QUESTION_20 = {
    "text": "How much time do you spend on investment research and analysis per week?",
    "options": [
        "Less than 1 hour",
        "1-2 hours",
        "2-5 hours",
        "5-10 hours",
        "10-20 hours",
        "More than 20 hours"
    ],
    "answer_type": "categorical"
}

QUESTION_21 = {
    "text": "What is your typical investment time horizon? (e.g. How long do you typically hold a position?)",
    "options": [
        "Less than 1 month",
        "1-3 months",
        "3-6 months",
        "6 months to 1 year",
        "1-3 years",
        "3-5 years",
        "More than 5 years"
    ],
    "answer_type": "categorical"
}

QUESTION_22 = {
    "text": "How would you describe your investment strategy?",
    "options": [
        "Passive",
        "Active",
        "Value-oriented",
        "Growth-oriented",
        "Technical analysis"
    ],
    "answer_type": "categorical"
}

QUESTION_23 = {
    "text": "How much of your total savings is invested in the market?",
    "options": [
        "<10%",
        "10-24%",
        "25-49%",
        "50-74%",
        "75%+"
    ],
    "answer_type": "categorical"
}

QUESTION_24 = {
    "text": "How confident are you in your ability to make investment decisions?",
    "options": [1, 2, 3, 4, 5],
    "answer_type": "numerical"
}


# SECTION 7: RISK PERCEPTION AND TOLERANCE
QUESTION_25 = {
    "text": "What percentage of your investment portfolio is allocated to high-risk assets? (High-risk assets typically include investments such as individual stocks, cryptocurrencies, or small-cap companies, which have higher volatility and potential for loss but may offer higher returns.)",
    "options": [
        "<10%",
        "10-24%",
        "25-49%",
        "50-74%",
        "75-99%",
        "100%"
    ],
    "answer_type": "categorical"
}

QUESTION_26 = {
    "text": "When making investment decisions, which factor is most important to you?",
    "options": [
        "Potential return",
        "Risk minimization",
        "Diversification",
        "Company fundamentals",
        "Market trends",
        "Other"
    ],
    "answer_type": "categorical"
}

QUESTION_27 = {
    "text": "How would you describe your risk tolerance?",
    "options": [1, 2, 3, 4, 5],
    "answer_type": "numerical"
}


# SECTION 8: SOCIAL MEDIA USAGE
QUESTION_28 = {
    "text": "How often do you use social media for investment information?",
    "options": [1, 2, 3, 4, 5],
    "answer_type": "numerical"
}

QUESTION_29 = {
    "text": "What types of assets do you trade?",
    "options": [
        "Facebook",
        "TikTok",
        "Twitter",
        "Reddit",
        "YouTube",
        "Instagram",
        "LinkedIn",
        "Financial Blogs",
        "Discord",
        "StockTwits",
        "Other"
    ],
    "answer_type": "multi_select"
}

QUESTION_30 = {
    "text": "Have you ever made an investment decision based on information found on social media?",
    "options": [
        "Yes",
        "No"
    ],
    "answer_type": "categorical"
}

QUESTION_31 = {
    "text": "How reliable do you find the financial information obtained from social media platforms?",
    "options": [1, 2, 3, 4, 5],
    "answer_type": "numerical"
}


# SECTION 9: INVESTMENT OUTCOMES
QUESTION_32 = {
    "text": "What was your average annual return on investment in the past year?",
    "options": [
        "0-5%",
        "6-10%",
        "11-15%",
        "16-20%",
        "20%+"
    ],
    "answer_type": "categorical"
}

QUESTION_33 = {
    "text": "How satisfied are you with your investment performance?",
    "options": [1, 2, 3, 4, 5],
    "answer_type": "numerical"
}



QUESTIONS = [
    QUESTION_1,
    QUESTION_2,
    QUESTION_3,
    QUESTION_4,
    QUESTION_5,
    QUESTION_6,
    QUESTION_7,
    QUESTION_8,
    QUESTION_9,
    QUESTION_10,
    QUESTION_11,
    QUESTION_12,
    QUESTION_13,
    QUESTION_14,
    QUESTION_15,
    QUESTION_16,
    QUESTION_17,
    QUESTION_18,
    QUESTION_19,
    QUESTION_20,
    QUESTION_21,
    QUESTION_22,
    QUESTION_23,
    QUESTION_24,
    QUESTION_25,
    QUESTION_26,
    QUESTION_27,
    QUESTION_28,
    QUESTION_29,
    QUESTION_30,
    QUESTION_31,
    QUESTION_32,
    QUESTION_33
]
