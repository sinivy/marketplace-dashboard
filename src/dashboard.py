import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Marketplace Analytics",
    page_icon="◉",
    layout="wide"
)

st.markdown("""
<style>
.block-container { padding-top: 2rem; }

div[data-testid="metric-container"]{
    background:white;
    border:1px solid #ececec;
    border-radius:18px;
    padding:20px;
    box-shadow:0 2px 10px rgba(0,0,0,.05);
}

h1 { font-weight:700; }
</style>
""", unsafe_allow_html=True)

df = pd.read_csv("data/marketplace.csv")
df["data"] = pd.to_datetime(df["data"])

st.sidebar.title("Filtros")

categorias = st.sidebar.multiselect(
    "Categoria",
    sorted(df["categoria"].dropna().unique())
)

vendedores = st.sidebar.multiselect(
    "Vendedor",
    sorted(df["vendedor"].dropna().unique())
)

df_filtrado = df.copy()

if categorias:
    df_filtrado = df_filtrado[df_filtrado["categoria"].isin(categorias)]

if vendedores:
    df_filtrado = df_filtrado[df_filtrado["vendedor"].isin(vendedores)]

concluidos = df_filtrado[df_filtrado["status"] == "Concluído"]

receita_total = concluidos["valor"].sum()
numero_vendas = len(concluidos)

ticket_medio = receita_total / numero_vendas if numero_vendas else 0

taxa_cancelamento = (
    len(df_filtrado[df_filtrado["status"] == "Cancelado"]) /
    len(df_filtrado) * 100
    if len(df_filtrado) else 0
)

melhor_vendedor = (
    concluidos.groupby("vendedor")["valor"].sum().idxmax()
    if not concluidos.empty else "—"
)

faturamento_vencedor = (
    concluidos.groupby("vendedor")["valor"].sum().max()
    if not concluidos.empty else 0
)

melhor_categoria = (
    concluidos.groupby("categoria")["valor"].sum().idxmax()
    if not concluidos.empty else "—"
)

receita_categoria = (
    concluidos.groupby("categoria")["valor"].sum().max()
    if not concluidos.empty else 0
)

st.title("Marketplace Analytics")
st.caption("Monitoramento de indicadores e desempenho operacional")
st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Receita Total", f"R$ {receita_total:,.0f}")
col2.metric("Pedidos Concluídos", numero_vendas)
col3.metric("Ticket Médio", f"R$ {ticket_medio:,.0f}")
col4.metric("Taxa Cancelamento", f"{taxa_cancelamento:.1f}%")

st.markdown("### Destaques")

d1, d2 = st.columns(2)
d1.metric("🥇 Melhor Vendedor", melhor_vendedor, f"R$ {faturamento_vencedor:,.0f}")
d2.metric("🏆 Melhor Categoria", melhor_categoria, f"R$ {receita_categoria:,.0f}")

categoria_df = (
    concluidos.groupby("categoria")["valor"]
    .sum()
    .reset_index()
    .sort_values("valor", ascending=False)
)

fig_categoria = px.bar(
    categoria_df,
    x="categoria",
    y="valor",
    title="Receita por Categoria",
    color_discrete_sequence=["#ff3d71"]
)

fig_categoria.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white",
    showlegend=False
)

status_df = (
    df_filtrado.groupby("status")
    .size()
    .reset_index(name="quantidade")
)

fig_status = px.pie(
    status_df,
    names="status",
    values="quantidade",
    hole=0.65,
    title="Distribuição dos Pedidos",
    color="status",
    color_discrete_map={
        "Concluído": "#ff3d71",
        "Cancelado": "#ff8fab",
        "Em andamento": "#d9d9d9"
    }
)

fig_status.update_layout(
    paper_bgcolor="white",
    plot_bgcolor="white",
    legend_title_text=""
)

concluidos["mes"] = concluidos["data"].dt.to_period("M").astype(str)

mensal = (
    concluidos.groupby("mes")["valor"]
    .sum()
    .reset_index()
)

fig_mensal = px.bar(
    mensal,
    x="mes",
    y="valor",
    title="Receita Mensal",
    color_discrete_sequence=["#ff3d71"]
)

fig_mensal.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white",
    showlegend=False,
    xaxis_title="",
    yaxis_title="Receita (R$)"
)

vendedor_df = (
    concluidos.groupby("vendedor")["valor"]
    .sum()
    .reset_index()
    .sort_values("valor", ascending=False)
)

fig_vendedor = px.bar(
    vendedor_df.head(5),
    x="valor",
    y="vendedor",
    orientation="h",
    title="Top 5 Vendedores",
    color_discrete_sequence=["#ff3d71"]
)

fig_vendedor.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white",
    showlegend=False
)

col_esq, col_dir = st.columns(2)

with col_esq:
    st.plotly_chart(fig_categoria, use_container_width=True)
    st.plotly_chart(fig_vendedor, use_container_width=True)

with col_dir:
    st.plotly_chart(fig_status, use_container_width=True)
    st.plotly_chart(fig_mensal, use_container_width=True)

evolucao = (
    concluidos.groupby("data")["valor"]
    .sum()
    .reset_index()
)

fig_linha = px.line(
    evolucao,
    x="data",
    y="valor",
    title="Evolução das Vendas"
)

fig_linha.update_traces(line=dict(width=4, color="#ff3d71"))

fig_linha.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white"
)

st.plotly_chart(fig_linha, use_container_width=True)

with st.expander("Visualizar dados brutos"):
    st.dataframe(df_filtrado, use_container_width=True)