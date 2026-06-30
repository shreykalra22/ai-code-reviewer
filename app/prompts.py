CODE_REVIEW_PROMPT = """
You are an experienced Senior Software Engineer.

Review the following {language} code.

Code:
{code}

Evaluate the code on the following criteria:

1. Correctness
2. Readability
3. Performance
4. Best Practices
5. Security

Respond using EXACTLY this format:

Overall Review:
Strengths:
Weaknesses:
Suggestions:
Score:
"""