
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="G6PD-Insight",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 G6PD-Insight")
st.subheader("Integrated Bioinformatics Platform for G6PD Variant Analysis")

st.write(
    "Explore G6PD variants using variant information, "
    "functional prediction records, and evidence-based prioritization."
)

st.sidebar.header("Navigation")
page = st.sidebar.radio(
    "Choose an analysis",
    [
        "Dashboard",
        "Variant Analysis",
        "Compare Variants",
        "About"
    ]
)

variants = pd.DataFrame({
    "Variant": [
        "p.Gly163Ser",
        "p.Val68Met",
        "p.Glu317Lys",
        "p.Cys385Arg",
        "p.Arg463Leu"
    ],
    "Gene": ["G6PD"] * 5,
    "Protein Position": [163, 68, 317, 385, 463],
    "Clinical Evidence": [
        "Pathogenic / likely pathogenic",
        "Pathogenic / likely pathogenic",
        "Pathogenic / likely pathogenic",
        "Pathogenic / likely pathogenic",
        "Pathogenic"
    ]
})

if page == "Dashboard":
    st.header("Analysis Dashboard")

    a, b, c = st.columns(3)
    a.metric("Gene", "G6PD")
    b.metric("Example variants", len(variants))
    c.metric("Analysis modules", "3")

    st.info(
        "This initial demo uses example records. "
        "It does not perform live database searches or "
        "run SIFT/PolyPhen-2 predictions."
    )

    st.subheader("Example variant records")
    st.dataframe(variants, use_container_width=True)

elif page == "Variant Analysis":
    st.header("Individual Variant Analysis")

    choice = st.selectbox(
        "Select a variant",
        variants["Variant"].tolist()
    )

    result = variants[variants["Variant"] == choice].iloc[0]

    st.write("### Variant details")
    st.write("**Gene:**", result["Gene"])
    st.write("**Protein change:**", result["Variant"])
    st.write("**Protein position:**", result["Protein Position"])
    st.write("**Clinical evidence:**", result["Clinical Evidence"])

    st.warning(
        "Confirm the transcript and current ClinVar record "
        "before interpreting or reporting a variant."
    )

elif page == "Compare Variants":
    st.header("Variant Comparison")

    selected = st.multiselect(
        "Choose variants to compare",
        variants["Variant"].tolist(),
        default=variants["Variant"].tolist()[:3]
    )

    if selected:
        comparison = variants[
            variants["Variant"].isin(selected)
        ]
        st.dataframe(comparison, use_container_width=True)

        st.bar_chart(
            comparison.set_index("Variant")["Protein Position"]
        )

elif page == "About":
    st.header("About G6PD-Insight")

    st.write("""
    G6PD-Insight is a prototype for organizing and comparing
    G6PD genetic variant evidence.

    Planned analyses:
    1. Variant information and clinical evidence
    2. Sequence conservation and functional predictions
    3. Comparative variant prioritization

    Predictions and clinical interpretations must be validated
    using reliable biological databases and analysis tools.
    """)
