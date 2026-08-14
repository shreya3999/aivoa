from langgraph.graph import (
    StateGraph,
    START,
    END
)


from app.graph.state import ComplaintState


from app.graph.nodes import (

    extract_complaint,

    check_completeness,

    assess_risk,

    generate_recommendations

)


def create_workflow():

    graph = StateGraph(
        ComplaintState
    )


    # Add nodes

    graph.add_node(
        "extract_complaint",
        extract_complaint
    )


    graph.add_node(
        "check_completeness",
        check_completeness
    )


    graph.add_node(
        "assess_risk",
        assess_risk
    )


    graph.add_node(
        "generate_recommendations",
        generate_recommendations
    )


    # Connect nodes

    graph.add_edge(
        START,
        "extract_complaint"
    )


    graph.add_edge(
        "extract_complaint",
        "check_completeness"
    )


    graph.add_edge(
        "check_completeness",
        "assess_risk"
    )


    graph.add_edge(
        "assess_risk",
        "generate_recommendations"
    )


    graph.add_edge(
        "generate_recommendations",
        END
    )


    return graph.compile()


workflow = create_workflow()