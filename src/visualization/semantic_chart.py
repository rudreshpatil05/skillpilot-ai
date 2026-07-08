import plotly.express as px
import pandas as pd


def semantic_chart(results):

    df = pd.DataFrame(results)

    fig = px.bar(
        df,
        x="Score",
        y="Role",
        orientation="h",
        title="AI Semantic Role Matching",
        color="Score",
        text="Score",
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),
        height=450
    )

    return fig