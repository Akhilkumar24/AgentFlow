class DomainKnowledge:
    """Provides high-quality category-specific knowledge for various industry domains."""
    
    # Detailed category-specific fallback datasets
    KNOWLEDGE = {
        "ev": {
            "market_share": "The competitive landscape is led by three major incumbents holding over 60% of the market. Leading manufacturers are focusing on vertically integrated supply chains, while new entrants are disrupting the entry-level segment with low-cost platforms.",
            "market_size": "Current industry valuation is estimated at $150 billion with a projected CAGR of 22% through 2030. The growth is primarily fueled by shifting consumer preferences and the decreasing cost of lithium-ion battery packs.",
            "trends": "Key innovations include solid-state battery testing, 800V fast-charging architectures, and the integration of autonomous driving software. OEMs are increasingly investing in software-defined vehicle architectures.",
            "policies": "Government actions involve direct purchase subsidies (e.g., FAME-II, IRA tax credits) and strict emission mandates. Many regions have announced bans on internal combustion engine sales by 2035."
        },
        "finance": {
            "market_share": "The banking sector is seeing consolidation among top-tier institutions, with the top 5 banks controlling 45% of retail deposits. Fintech disruptors are capturing 15% of the payment processing volume.",
            "market_size": "Global assets under management (AUM) have reached $110 trillion, with alternative investments growing at a CAGR of 12%. Digital banking adoption is at an all-time high of 78% in developed economies.",
            "trends": "Generative AI is being deployed for fraud detection and algorithmic trading. Open banking APIs are allowing third-party providers to build integrated financial ecosystems for SMEs.",
            "policies": "Regulations like Basel III capital requirements and GDPR data privacy rules are shaping operational strategies. Central banks are exploring CBDCs to modernize payment rails."
        },
        "blockchain": {
            "market_share": "The ecosystem is bifurcated between Layer 1 protocols and Layer 2 scaling solutions. Ethereum continues to lead with 70% of total value locked (TVL) in DeFi applications.",
            "market_size": "The total crypto market capitalization fluctuates between $1T and $3T. The enterprise blockchain market is growing at a CAGR of 35% as logistics companies adopt DLT for transparency.",
            "trends": "Zero-knowledge proofs (ZKP) are becoming the standard for privacy. Real-world asset (RWA) tokenization is bridging traditional finance with decentralized rails.",
            "policies": "Global regulatory clarity is emerging with frameworks like MiCA in Europe. Standardized KYC/AML requirements are being enforced for centralized exchanges to combat illicit flows."
        },
        "energy": {
            "market_share": "Renewables have surpassed 30% of global electricity generation. Solar PV manufacturers in East Asia dominate the supply chain, while wind turbine technology is led by European engineering firms.",
            "market_size": "Investment in clean energy has reached $1.7 trillion annually. Hydrogen economy infrastructure is projected to grow at a CAGR of 40% as industrial heavy-emitters transition.",
            "trends": "Long-duration energy storage (LDES) and green hydrogen electrolysis are the primary tech frontiers. Microgrid technology is improving rural electrification rates in emerging markets.",
            "policies": "Carbon pricing mechanisms and 'Green Deal' investment packages are the primary drivers. Subsidies for offshore wind and grid-modernization tax credits are being expanded globally."
        },
        "general": {
            "market_share": "Industry leaders are maintaining dominance through aggressive M&A strategies. Middle-market players are focusing on niche specialization to avoid direct competition with giants.",
            "market_size": "Sector valuation is showing steady growth with a CAGR of 8%. Inflationary pressures are being mitigated through digital-first operational efficiencies.",
            "trends": "Digital transformation and the adoption of IoT sensors are the biggest trends. Predictive maintenance is reducing operational costs by an average of 15% across the board.",
            "policies": "Trade regulations and supply chain near-shoring policies are becoming critical. ESG reporting mandates are now a standard requirement for publicly listed companies."
        }
    }

    @staticmethod
    def get(domain: str, category: str) -> str:
        domain_data = DomainKnowledge.KNOWLEDGE.get(domain, DomainKnowledge.KNOWLEDGE["general"])
        # Use category to get specific insight, or default to general overview
        return domain_data.get(category, "The sector continues to evolve with significant capital inflows and technological advancements.")
