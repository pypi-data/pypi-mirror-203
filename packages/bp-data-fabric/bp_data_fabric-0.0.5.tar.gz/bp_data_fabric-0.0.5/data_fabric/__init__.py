from typing import List
import query_tool as qt
import data_grid as dg
import data_visualization as dv

def data_fabric(
    query: str = "",
    query_tool_title: str = "",
    data_grid_title: str = "",
    data_visualization_title: str = "",
    databases: List[str] = [],
    tables: List[dict] = [],
    columns: List[dict] = [],
    on_database_change=None,
    on_table_change=None,
    on_generate_query=None,
    on_copy_query=None,
    data={},
):
    
    qt.query_tool(
        query=query,
        title=query_tool_title,
        databases=databases,
        tables=tables,
        columns=columns,
        on_database_change=on_database_change,
        on_table_change=on_table_change,
        on_generate_query=on_generate_query,
        on_copy_query=on_copy_query,
        key="query_builder",
    )

    dg.data_grid(
        title=data_grid_title,
        rows=data.get("rows", []),
        columns=data.get("columns", []),
        key="data_grid",
    )

    dv.data_visualizer(
        data=data.get("rows", []),
        key="data_visualizer",
    )
