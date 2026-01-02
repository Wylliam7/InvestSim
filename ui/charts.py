import plotly.graph_objects as go

def plot_capital_interactive(capital_no_fee, capital_with_fee, years):
    months_count = years * 12
    years_x = [round(m / 12, 1) for m in range(months_count)]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=years_x,
        y=capital_no_fee,
        mode="lines",
        name="Sans frais de gestion",
        hovertemplate="Capital sans frais: %{y:,.0f} $<extra></extra>"
    ))

    fig.add_trace(go.Scatter(
        x=years_x,
        y=capital_with_fee,
        mode="lines",
        name="Avec frais de gestion",
        hovertemplate="Capital avec frais: %{y:,.0f} $<extra></extra>"
    ))

    difference = [a - b for a, b in zip(capital_no_fee, capital_with_fee)]
    fig.add_trace(go.Scatter(
        x=years_x,
        y=difference,
        mode="lines",
        name="Frais cumulés",
        line=dict(dash="dot"),
        hovertemplate="Frais cumulés: %{y:,.0f} $<extra></extra>"
    ))

    fig.update_layout(
        title="Évolution du capital",
        xaxis_title="Années",
        yaxis_title="Capital ($)",
        hovermode="x unified",
        template="plotly_white",
        xaxis=dict(tick0=0, dtick=1)
    )

    return fig
