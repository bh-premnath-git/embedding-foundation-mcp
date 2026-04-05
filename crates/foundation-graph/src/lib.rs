use petgraph::graph::DiGraph;

pub fn empty_dag() -> DiGraph<&'static str, ()> {
    DiGraph::new()
}
