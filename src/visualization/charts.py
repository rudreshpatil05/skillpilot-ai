import plotly.express as px


def role_match_chart(results):
    """
    Creates a professional horizontal bar chart
    for the top matching job roles.
    """

    # Take Top 5 Roles
    top_roles = sorted(
        results,
        key=lambda x: x["Score"],
        reverse=True
    )[:5]

    roles = [role["Role"] for role in top_roles]
    scores = [role["Score"] for role in top_roles]

    fig = px.bar(
        x=scores,
        y=roles,
        orientation="h",
        text=[f"{score}%" for score in scores],
        color=scores,
        color_continuous_scale="Blues",
        title="🎯 Top 5 Matching Career Roles"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        height=450,
        showlegend=False,
        coloraxis_showscale=False,
        xaxis_title="Match Score (%)",
        yaxis_title="",
        yaxis=dict(autorange="reversed"),
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig