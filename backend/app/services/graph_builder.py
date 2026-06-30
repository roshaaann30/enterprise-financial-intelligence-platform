class GraphBuilder:

    def build_company_graph(self, company_name: str):

        nodes = [
            {"id": company_name, "type": "company"},
            {"id": "CEO", "type": "executive"},
            {"id": "Technology", "type": "industry"},
            {"id": "USA", "type": "country"},
            {"id": "Microsoft", "type": "competitor"},
            {"id": "Google", "type": "competitor"},
            {"id": "iPhone", "type": "product"},
            {"id": "MacBook", "type": "product"},
        ]

        links = [
            {"source": company_name, "target": "CEO", "relation": "CEO"},
            {"source": company_name, "target": "Technology", "relation": "INDUSTRY"},
            {"source": company_name, "target": "USA", "relation": "COUNTRY"},
            {"source": company_name, "target": "Microsoft", "relation": "COMPETITOR"},
            {"source": company_name, "target": "Google", "relation": "COMPETITOR"},
            {"source": company_name, "target": "iPhone", "relation": "PRODUCT"},
            {"source": company_name, "target": "MacBook", "relation": "PRODUCT"},
        ]

        return {
            "nodes": nodes,
            "links": links,
        }