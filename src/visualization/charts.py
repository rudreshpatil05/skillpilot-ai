import plotly.express as px


def role_match_chart(results):

    roles = [r["Role"] for r in results[:5]]

    scores = [r["Score"] for r in results[:5]]

    fig = px.bar(
        x=scores,
        y=roles,
        orientation="h",
        text=scores,
        title="Top Matching Roles"
    )

    fig.update_layout(
        xaxis_title="Match Score",
        yaxis_title=""
    )

    return fig