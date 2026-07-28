# Article Outline — Energy Valorization of Oil Palm Residual Biomass in Magdalena, Colombia
*Working draft skeleton — v1. Language: English. Status: all figures below validated in the July 2026 working session; see cross-references to notebook sections and notes §-numbers.*

**Authors and affiliations**
- Juan Camilo Barrera-Hernandez [affiliation to be confirmed — presumably corresponding author]
- Electo Eduardo Silva Lora — NEST, Excellence Group in Thermal Power and Distributed Generation, Institute of Mechanical Engineering, Federal University of Itajubá, Av. BPS 1303, Itajubá, MG, CEP: 37500-903, Brazil
- Alexis Sagastume Gutierrez — Department of Civil Engineering, Faculty of Distance Studies, Nueva Granada Military University, Cajicá 250247, CU, Colombia
- Jesús Alberto García-Nuñez — Colombian Oil Palm Research Centre, Cenipalma, Calle 98 N° 70 - 91 Piso 14, Bogotá, Colombia

> ⚠️ **STATUS AFTER TODAY'S VALIDATION SESSION (see `Lista_de_tareas_pendientes.md` for the full
> checklist)**: the four chained corrections from the previous session (joint self-consumption/
> energy-credit cap; corrected metered demand for technology substitution; reconstructed fiber/
> shell opportunity cost; new EFB opportunity cost) have now been independently validated,
> including replacing initially invented placeholder fertilizer prices with verified Fedepalma/
> DANE-Sipsa Q1 2025 prices and adding a literature-based mineralization efficiency factor (70%,
> Budi et al. 2001; Saletes et al. 2004; Ramirez et al. 2011) to the EFB opportunity cost. The
> aggregate finding is now considered solid: Scenario 1 net benefit is USD 258,705 at its economic
> optimum (32.2% of potential) and falls to USD −6,531,746 at full deployment, with the profitable
> window being narrower than earlier drafts suggested (already negative at 40.6% of potential);
> Scenario 2 remains solidly profitable throughout its range, from USD 3,427,932 (92.3%) to USD
> 2,315,672 (100%). Tables 4 through 9, Figures 5, 6, and 8, and the plant-level and per-tCO2
> figures in the Abstract, Discussion, and Conclusions still need to be rebuilt against this
> validated front before the manuscript is finalized.

---

## Title (AGREED)

**"Beyond technical potential: profitability, robustness, and regional sustainability trade-offs in mature cogeneration pathways for palm oil mill residues"**

*Rationale: gives explicit continuity with the prior potential-quantification article on the same
biomass resource (which stops at the technical potential number), signals the "regional" and
plant-level scope, and foregrounds "mature" pathways (evidence: Cenipalma 2024 benchmarking
shows 6/23 and 7/23 surveyed Colombian mills already operate steam and biogas cogeneration
respectively). No em dashes, no explicit regulation named, no "equity" language (see keyword
note below).*

Discarded alternatives (kept for reference): "No subsidy needed..." (too CREG-explicit for
Abstract-level framing); "...equity..." variants (dropped — the paper documents empirical
profitability *disparities* across plants, not a developed energy-equity/justice framework;
using "equity" would overpromise relative to what Discussion actually delivers).

---

## Abstract (FINAL — all figures confirmed against the fully validated model)

> Prior assessments of Colombia's palm oil residual biomass have established the scale of its technical energy potential, but have stopped short of asking whether capturing it is financially sound for the mills that would invest in it. This study moves beyond potential quantification to assess profitability, robustness, and sustainability trade-offs across two mature cogeneration pathways: an extraction condensation steam turbine paired with biogas from palm oil mill effluent (Scenario 1), and a backpressure turbine paired with biogas from co-digested effluent and thermally pretreated empty fruit bunches (Scenario 2). A mixed integer optimization model covers six extraction plants in the Magdalena region, jointly assessing economic, environmental, and social outcomes.
>
> Each scenario is profitable at its own economic optimum, but the two diverge sharply beyond that point. Scenario 2 remains profitable across its entire technical range; Scenario 1's profitable window is narrow, turning negative almost immediately past its own optimum and falling substantially further toward full deployment unless supported by a capital incentive or a higher feed-in tariff. The divergence traces to conversion losses: turbine losses are several times larger than biogas losses, so Scenario 1's private optimum relies overwhelmingly on biogas, and any deployment beyond that point requires turbine expansion at a cost that quickly outweighs the added revenue. Plant level results sharpen this picture further: at full deployment, none of the six mills remain profitable under Scenario 1, against four of six under Scenario 2. Closing the gap between the private optimum and full deployment costs USD 294 per additional tonne of CO2 avoided for Scenario 1 and USD 599 for Scenario 2, far exceeding Colombia's current carbon tax. Neither route dominates: Scenario 2 is more profitable, more robust, and viable at more mills, while Scenario 1 avoids substantially more emissions in absolute terms given its larger technical potential.

*(word count to be rechecked at final typesetting)*

**CORRECTION LOG (updated today):** this abstract has been through two rounds of correction. The
original claim ("both routes profitable without subsidy even at full deployment") was found false
for Scenario 1 once turbine and biogas conversion losses were properly priced (bruta-to-neta
correction, an earlier session). A second round today found and fixed a joint-cap constraint error
plus added a literature-grounded EFB opportunity cost, narrowing Scenario 1's profitable window
much further. Current confirmed figures: Scenario 1's full-deployment net benefit is USD
−6,531,746/yr; the abatement cost is USD 294/tCO2 for Scenario 1 and USD 599/tCO2 for Scenario 2;
the carbon tax comparison uses the verified 2026 rate of USD 8.70/tCO2 (COP 29,070.49, DIAN
Resolution 000003 of 2026). Earlier figures in prior drafts (USD −908,171/yr; USD 169-593/tCO2)
are both superseded.

**Style rules locked in for the rest of the manuscript** (apply consistently from here on):
- No em/en dashes as stylistic separators; use commas, semicolons, or full clauses instead
- Short hyphens permitted only for numeric ranges (e.g., "225-392"); "to" is acceptable mid-sentence for ranges (e.g., "225 to 392") when a hyphen would be visually ambiguous
- No explicit regulation names (e.g., "CREG 174") in the Abstract; regulatory framework is described narratively and named explicitly only in Materials and Methods
- No "equity" language anywhere in the manuscript unless a dedicated energy-equity/justice theoretical framework is developed in Discussion (not currently planned); use "disparities" or "heterogeneity" instead
- Target journal: Journal of Cleaner Production (JCLEPRO) — house style to match: Cenipalma/Revista Palmas article tone (plain, formal, minimal stylistic punctuation)

Keywords (draft, to refine): palm oil mill residues; biomass valorization; mixed-integer optimization; conversion losses; profitability disparities; carbon abatement cost

---

## Nomenclature (NEW this session)

**Sets and indices**

| Symbol | Description |
|---|---|
| $i \in I$ | Plant index, $I = \{A, B, C, D, E, F\}$ |
| $j \in J_i$ | Turbine catalog option available to plant $i$ |
| $b \in B$ | Biomass fraction, $B = \{\text{fiber, shell, EFB}\}$ |
| $k = 0, \ldots, 10$ | Interval index of the epsilon-constraint sweep |

**Decision variables**

| Symbol | Description | Unit |
|---|---|---|
| $y_{i,j}$ | 1 if turbine option $j$ is selected for plant $i$, 0 otherwise | binary |
| $n_i$ | Number of 1,000 kW biogas engine modules installed at plant $i$ | integer |
| $u^{turb}_i, u^{bio}_i$ | Utilization factor of the turbine and biogas routes at plant $i$ | dimensionless, [0,1] |
| $E^{auto}_i, E^{permuta}_i, E^{bolsa}_i$ | Annual energy allocated to the self-consumption, energy-credit, and spot-market tiers at plant $i$ | kWh/yr |

**Parameters**

| Symbol | Description | Unit |
|---|---|---|
| $S_i, S_{ref}$ | Installed capacity of plant $i$'s equipment; reference capacity for cost scaling | kW or t FFB/h |
| $C_{ref}$ | Reference equipment cost at $S_{ref}$ | USD |
| $CEPCI_y$ | Chemical Engineering Plant Cost Index in year $y$ | dimensionless |
| $PVAF$ | Present value annuity factor | dimensionless |
| $r, N$ | Discount rate (10%), project lifetime (20 yr) | %, yr |
| $\alpha$ | Operating and maintenance rate (2.5% of capital cost) | %/yr |
| $p^{retail}_i$ | Plant $i$'s own weighted retail electricity price | USD/kWh |
| $p^{spot}$ | Wholesale spot market price | USD/kWh |
| $h_i$ | Annual operating hours of plant $i$ | h/yr |
| $\eta^{turb}_{net}, \eta^{bio}_{net}$ | Net conversion factors, turbine and biogas routes (mechanical, electrical, and self-consumption losses combined) | dimensionless |
| $D_i$ | Plant $i$'s own electricity demand | kWh/yr |
| $OC^{bio}_i, OC^{EFB}_i$ | Opportunity cost of fiber/shell (market value as PKS/MF) and of EFB (Net Fertilizer Replacement Value, Section 2.6) diverted from their current use at plant $i$ | USD/yr |
| $u^{EFB}_i$ | Utilization variable scaling the EFB opportunity cost; equals $u^{turb}_i$ under Scenario 1 (EFB combusted) and $u^{bio}_i$ under Scenario 2 (EFB co-digested) | dimensionless, [0,1] |
| $EF_{biomass}, EF_{biogas}, EF_{diesel}, EF_{grid}$ | Emission factors for solid biomass and biogas combustion, diesel backup, and grid displacement credit | kg CO2eq per unit |
| $c_{HH}$ | Average annual rural household electricity consumption (346) | kWh/household/yr |
| $N^{rural}$ | Total rural households in the department | households |

**Abbreviations**: CAPEX, capital expenditure; O&M, operation and maintenance; LCOE, levelized
cost of electricity; MILP, mixed-integer linear programming; FFB, fresh fruit bunches; EFB, empty
fruit bunches; POME, palm oil mill effluent; HHV, higher heating value; BMP, biochemical methane
potential.

---

## 1. Introduction (REVISED — literature strengthened this session, see audit notes below)

> Colombia's oil palm agroindustry generates large volumes of residual biomass, including empty fruit bunches, fiber, shell, and palm oil mill effluent, whose energy content is regarded as an underexploited resource for the country's renewable energy transition and for strengthening electricity access in rural, biomass-producing regions (Rocha-Meneses et al., 2023). Prior work has quantified this technical potential at the national scale from complementary angles: the author's own research group estimated a national biomass energy potential of 61,078 GWh across agriculture, agroindustry, livestock, and slaughterhouse waste using direct combustion and anaerobic digestion (Sagastume Gutierrez et al., 2020), later narrowing that assessment to the palm sector specifically and estimating between 61 and 227 MW of electricity capacity (Barrera Hernandez et al., 2024); a separate national inventory built with Fedepalma, covering 45 companies, estimated 2,762 kilotonnes of available palm biomass waste for 2023 (Alean et al., 2025). Establishing exactly how much of this technical potential can realistically be captured, and through which technological route, remains an open and consequential question.
>
> Converting technical potential into installed capacity, however, is not automatic. Bioenergy generation is a discretionary investment that sits outside the core business of a palm oil extraction plant, which is the production of crude palm oil. Committing capital to on site power generation exposes a mill to a different set of risks, including electricity market prices, regulatory conditions governing self generation and surplus exchange, and technology specific costs, none of which are relevant to the mill's primary operations. From the perspective of an individual investor, the relevant question is therefore not whether generating electricity from residual biomass is technically feasible or environmentally desirable, both of which are increasingly well established, but whether it is sufficiently and robustly profitable to justify entering an unfamiliar line of business. From a system perspective, however, more renewable generation is unambiguously beneficial: it strengthens grid robustness, displaces fossil generation, and supports national decarbonization and rural electrification targets, including the modest non-conventional renewable electricity capacity targets Colombia has struggled to meet despite ample unused potential (Cabello Eras et al., 2018) and the commitment to expand rural electrification under Colombia's 2016 peace agreement (Martinez et al., 2025), regardless of whether the private return fully reflects that value.
>
> This tension between what is privately optimal and what is technically and environmentally optimal has received limited attention in the literature on palm biomass valorization. Prior techno-economic assessments have typically reported aggregate, departmental or regional level profitability using a single representative technology: Boom-Carcamo et al. (2025) compare two aggregate deployment scenarios, steam generation and electricity generation, for a cluster of northern Colombian mills against fossil fuel alternatives using standard project-evaluation software, and Martinez et al. (2025) estimate an aggregate technical potential of nearly 3,900 MW for isolated Colombian regions across several agricultural residue types and generic Rankine and internal combustion technologies. Neither disaggregates results across individual mills or tests their robustness to electricity price uncertainty. As a result, two practically important questions remain unanswered. First, does profitability hold uniformly across mills of different sizes and operating conditions, or is it concentrated in a subset of plants, with implications for whether policy support, if any, should be broad or targeted. Second, how large is the gap between the deployment level a private investor would rationally choose and full technical deployment, and what would closing that gap cost in terms of forgone private profitability.
>
> A distinct but related literature has applied mathematical optimization, rather than scenario comparison, to palm oil biomass energy systems, though almost entirely outside Colombia. Several studies have used mixed integer linear programming (MILP) to design and operate palm biomass-to-bioenergy systems in Indonesia and Malaysia: Harahap et al. (2019) developed the first geographically explicit MILP model of the palm oil supply chain in Sumatra, and Ho et al. (2015) formulated a multiperiod MILP model for hourly scheduling of a combined biomass, biogas, and solar generation system for a palm oil eco-community. Multi-objective formulations solved via the epsilon-constraint method, the same approach adopted in this study, have been used to compare pyrolysis technologies for palm biomass (Teh et al., 2023) and to evaluate waste-to-energy deployment scenarios under a carbon tax (Aprilianto and Rau, 2025). Closer to this study's own policy question, Nair et al. (2022) used a disjunctive fuzzy MILP model to optimize the participation of multiple biomass power plants in a feed-in tariff programme, and Memari et al. (2018) compared carbon tax and cap-and-trade policies within an MILP supply chain model. None of these studies, however, is set in Colombia, nor do they jointly assess plant-level profitability, its robustness to electricity price uncertainty, and the gap between privately optimal and full technical deployment, the three elements this study brings together.
>
> This study addresses both questions using two cogeneration pathways that are technologically mature, having reached high technology readiness levels in prior comparative assessments of biomass electricity generation routes (Dovichi Filho et al., 2021), and that build on an established line of Colombian palm-to-biorefinery research (Garcia-Nunez et al., 2016): an extraction condensation steam turbine paired with biogas generation from palm oil mill effluent, and a backpressure steam turbine paired with biogas generation from co-digested effluent and thermally pretreated empty fruit bunches. A mixed integer optimization model is developed for six extraction plants in the Magdalena department, jointly assessing economic, environmental, and social outcomes under both pathways. The analysis quantifies the technical energy potential of the region's residual biomass, evaluates plant level profitability and its robustness to electricity price fluctuations, and estimates the cost, in forgone private profitability, of moving from the privately optimal deployment level to full technical deployment. In doing so, this study reframes the relevant policy question from whether this transition needs to be subsidized to which technological route policy should favor, and for which mills targeted intervention may be warranted.

**Literature audit notes (this session, not for the manuscript)**:
- Identified three claims a reviewer would likely flag as unsupported: (1) the opening
  "underexploited resource" framing had no citation; (2) only one, self-authored source
  (Barrera Hernandez et al. 2024) backed the national-potential claim; (3) most seriously, the
  central literature-gap claim in paragraph 3, which motivates the entire study, cited zero prior
  assessments by name. All three are now addressed above with real, verified sources.
- The previously noted "Guerrero et al. (2023) and Chavez et al. (2026)" placeholder for the
  "mature, already partially adopted" claim has been replaced with Dovichi Filho et al. (2021),
  since Guerrero/Chavez were already found this session to be misattributed Cenipalma cost-series
  citations unrelated to technology maturity specifically.
- **All 6 new citations independently verified this session** (full search-result confirmation of
  authors, journal, volume, DOI, and specific claims used — same rigor as the Barrera Hernandez
  and Mosquera-Montoya verifications):
  - Boom-Carcamo, E., Penabaena-Niebles, R., Alean, J. (2025). "Scenario analysis of the use of
    oil palm residual biomass for bioenergy generation: A comparison with fossil fuels." Energy,
    335, 137933. https://doi.org/10.1016/j.energy.2025.137933. **Confirmed**; one wording
    correction made (their two scenarios are steam and electricity generation separately, not
    "cogeneration" jointly — fixed in the prose above).
  - Martinez, G.L., Buritica Arboleda, C.I., Silva Lora, E.E., Castillo Santiago, Y., Almazan del
    Olmo, O.A. (2025). "Techno-economic evaluation of converting biomass to electricity in
    isolated areas of Colombia." Biofuels, Bioproducts and Biorefining, 19(4), 1059-1074.
    https://doi.org/10.1002/bbb.2768. **Confirmed**, including an exact match for the 2016 peace
    agreement / rural electrification quote used in paragraph 2.
  - Alean, J., Bastidas, M., Boom-Carcamo, E., Maya, J.C., Chejne, F., Ramirez, S., Nieto, D.,
    Ceballos, C., Saurith, A., Cordoba-Ramirez, M. (2025). "Design of a Technical Decision-Making
    Strategy to Collect Biomass Waste from the Palm Oil Industry as a Renewable Energy Source:
    Case Study in Colombia." Environments, 12(5), 165. https://doi.org/10.3390/environments12050165.
    **Confirmed**, including Fedepalma co-affiliation and the exact 2,762 kt (2023) figure used.
  - Garcia-Nunez, J.A., Rodriguez, D.T., Fontanilla, C.A., Ramirez, N.E., Silva Lora, E.E., Frear,
    C.S., Stockle, C., Amonette, J., Garcia-Perez, M. (2016). "Evaluation of alternatives for the
    evolution of palm oil mills into biorefineries." Biomass and Bioenergy, 95, 310-329.
    https://doi.org/10.1016/j.biombioe.2016.05.020. **Confirmed**, Cenipalma-authored foundational
    Colombian palm biorefinery paper.
  - Dovichi Filho, F.B., Castillo Santiago, Y., Silva Lora, E.E., Escobar Palacio, J.C., Almazan
    del Olmo, O.A. (2021). "Evaluation of the maturity level of biomass electricity generation
    technologies using the technology readiness level criteria." Journal of Cleaner Production,
    295, 126426. https://doi.org/10.1016/j.jclepro.2021.126426. **Confirmed**, 77 citations; the
    underlying finding (62.07% of surveyed experts rate Conventional Rankine Cycle at TRL 8+)
    directly strengthens the "technologically mature" claim for the steam turbine route.
  - Rocha-Meneses, L., Luna-delRisco, M., Gonzalez, C.A., Villegas Moncada, S., Moreno, A.,
    Sierra-Del Rio, J., Castillo-Meza, L.E. (2023). "An Overview of the Socio-Economic,
    Technological, and Environmental Opportunities and Challenges for Renewable Energy Generation
    from Residual Biomass: A Case Study of Biogas Production in Colombia." Energies, 16(16), 5901.
    https://doi.org/10.3390/en16165901. **Confirmed**.
- **Two additional citations found and verified this session** (identified by the user directly,
  both confirmed via search): both are by the *same research group* as Barrera Hernandez et al.
  (2024) — Sagastume Gutierrez and Cabello Eras are co-authors of both, strengthening rather than
  diluting the "prior work by the author's own group" framing by showing a sustained research
  program (2018-2024) rather than an isolated paper:
  - Sagastume Gutierrez, A., Cabello Eras, J.J., Hens, L., Vandecasteele, C. (2020). "The energy
    potential of agriculture, agroindustrial, livestock, and slaughterhouse biomass wastes
    through direct combustion and anaerobic digestion. The case of Colombia." Journal of Cleaner
    Production, 269, 122317. https://doi.org/10.1016/j.jclepro.2020.122317. **Confirmed**:
    national biomass potential of 61,078 GWh, narrower predecessor to Barrera Hernandez et al.'s
    palm-specific estimate; now cited in paragraph 1 to show the trajectory of the group's work.
  - Cabello Eras, J.J., Balbis Morejon, M., Sagastume Gutierrez, A., Pardo Garcia, A., Cabello
    Ulloa, M., Rey Martinez, F.J., Rueda-Bayona, J.G. (2018). "A look to the Electricity
    Generation from Non-Conventional Renewable Energy Sources in Colombia." International
    Journal of Energy Economics and Policy, 9(1), 15-25. https://doi.org/10.32479/ijeep.7108.
    **Confirmed**: assesses Colombia's NCRE capacity targets and Law 1715 framework; now cited in
    paragraph 2 alongside Martinez et al. (2025) for the decarbonization/policy-target framing.
- **Eight optimization-methodology citations, all independently verified this session**, added as
  a new paragraph surveying the state of the art in mathematical optimization applied to palm oil
  biomass energy systems (inserted before the final "This study addresses..." paragraph). All are
  Indonesia/Malaysia case studies; none are set in Colombia, supporting a geographic and
  methodological novelty claim for this study. Six were woven into the new paragraph directly
  (methodologically closest to this study's own MILP/epsilon-constraint approach); two
  (Yeo et al. 2020, Umar et al. 2018) were verified but not included in the paragraph itself to
  keep it concise, and may be cited elsewhere if useful:
  - Harahap, F., Leduc, S., Mesfun, S., Khatiwada, D., Kraxner, F., Silveira, S. (2019).
    "Opportunities to Optimize the Palm Oil Supply Chain in Sumatra, Indonesia." Energies, 12(3),
    420. https://doi.org/10.3390/en12030420. **Confirmed**.
  - Ho, W.S., Khor, C.S., Hashim, H., Lim, J.S., Ashina, S., Herran, D.S. (2015). "Optimal
    operation of a distributed energy generation system for a sustainable palm oil-based
    eco-community." Clean Technologies and Environmental Policy, 17, 1597-1617.
    https://doi.org/10.1007/s10098-014-0893-6. **Confirmed**.
  - Teh, K.C., Tan, J., Chew, I.M.L. (2023). "Multiple biogenic waste valorization via pyrolysis
    technologies in palm oil industry: economic and environmental multi-objective optimization
    for sustainable energy system." Process Integration and Optimization for Sustainability,
    7(4), 847-860. https://doi.org/10.1007/s41660-023-00327-w. **Confirmed**; uses the same
    epsilon-constraint method as this study.
  - Aprilianto, H.C., Rau, H. (2025). "A Multi-Objective Optimization Approach for Generating
    Energy from Palm Oil Wastes." Energies, 18(11), 2947. https://doi.org/10.3390/en18112947.
    **Confirmed**; finding that POME processing becomes viable only above a price threshold
    closely parallels this study's own price-robustness result (Section 3.4/Table 6) and may be
    worth citing there too as independent corroboration.
  - Nair, P.N.S.B., Andiappan, V., Foo, D.C.Y., Chemmangattuvalappil, N.G. (2022). "Disjunctive
    fuzzy optimisation of electricity generation by biomass power producers in a feed-in tariff
    programme." Asia-Pacific Journal of Chemical Engineering, 17(6), e2830.
    https://doi.org/10.1002/apj.2830. **Confirmed**.
  - Memari, A., Ahmad, R., Abdul Rahim, A.R. et al. (2018). "An optimization study of a palm
    oil-based regional bio-energy supply chain under carbon pricing and trading policies." Clean
    Technologies and Environmental Policy, 20, 113-125. https://doi.org/10.1007/s10098-017-1461-7.
    **Confirmed**; directly comparable to this study's Discussion 4.4 (carbon tax inadequacy) and
    worth citing there as a comparandum, since it compares carbon tax against cap-and-trade within
    an MILP framework.
  - Yeo, J.Y.J., How, B.S., Teng, S.Y., Leong, W.D., Ng, W.P.Q., Lim, C.H., Ngan, S.L., Sunarso, J.,
    Lam, H.L. (2020). "Synthesis of sustainable circular economy in palm oil industry using
    graph-theoretic method." Sustainability, 12(19), 8081. https://doi.org/10.3390/su12198081.
    **Confirmed**; uses P-graph, not MILP, so not included in the optimization-methodology
    paragraph to avoid overstating methodological overlap.
  - Umar, M.S., Urmee, T., Jennings, P. (2018). "A policy framework and industry roadmap model for
    sustainable oil palm biomass electricity generation in Malaysia." Renewable Energy, 128,
    275-284. **Confirmed**; policy/roadmap framework rather than a mathematical optimization
    model, so kept out of the optimization paragraph specifically.

**Contribution statement (fold into end of Introduction or keep as explicit list, TBD):**
(1) corrected CAPEX methodology (economies of scale, no double-counting); (2) plant-level
disaggregation revealing profitability disparities invisible in aggregate results; (3) robustness
analysis to price uncertainty; (4) technology-upgrade sensitivity for mills that already
self-generate; (5) quantification of the gap between privately optimal and fully deployed
generation, and its cost in forgone profitability

---

## 2. Materials and Methods (MERGED — user's richer v3 draft + this session's structural decisions and corrections)

**Five structural decisions locked in for this section (agreed this session), all reflected below:**
1. Governing equations consolidated in Table 3; body text is descriptive only
2. Full parameter values, cost catalogs, and detailed factor tables go to Appendix
3. Internal validation narration replaced by workflow diagram (§2.9, placeholder). *Exception: the Phase 1 "validation case" described in §2.3 is legitimate methodology (a fixed-capacity consistency check that is part of how the model is built), not this session's ad hoc debugging narrative, and is kept in prose.*
4. Regulatory framework (§2.4) concise, named once, no legal history
5. Scenario comparison diagram deferred to the end of the writing process

**Three corrections applied to the user's original draft this session (see rationale below each subsection):**
- §2.6: LCOE denominator rationale rewritten (export, not generation, per corrected model behavior)
- §2.2/2.3: continuous sterilization confirmed as Scenario 1 only (Scenario 2 lacks sufficient biomass-derived steam to meet the added demand)
- §2.5: internal cross-reference fixed twice (was "Section 2.7", then "Section 2.8"; final correct target is "Section 2.9", where the capital-side sensitivity analysis lives); also, all three regulatory instrument families are now named explicitly (CREG 174/2021, Law 1715/2014 as amended by Law 2099/2021, CREG 071/2006, and Decree 926/2017), since the paragraph explicitly claims "three families" and only one was named in an earlier draft

> This study assesses whether the deployment of residual biomass in palm oil mills is constrained by biomass availability, by market and regulatory conditions, or by the technological route selected. A multi-objective mixed-integer linear programming (MILP) model was built in Python 3 using the Pyomo algebraic modelling library and solved with the GLPK solver. The model was parameterized with primary operational data from six palm oil mills and used to generate Pareto fronts of profitability against biomass deployment; the levelized cost of electricity (LCOE), the greenhouse gas balance, and rural electricity coverage were subsequently evaluated at every point of each front. All data cleaning, modeling, and post-processing steps are implemented in openly available Jupyter notebooks (see Data availability).

### 2.1 Study area and biomass characterization (FINAL)

> This study covers six palm oil mills (Plants A to F) located in the Magdalena department, on the Caribbean coast of Colombia. Primary data were collected in the field during the authors' doctoral research and comprise process flows, steam and electricity consumption by processing stage, biomass yields, fuel use, and equipment inventories. Nominal processing capacities range from 20 to 40 tonnes of fresh fruit bunches per hour, and actual annual throughput ranges from 38,620 to 206,200 tonnes, reflecting substantial heterogeneity in scale and utilization across the sample (Table 1). Annual operating hours also vary widely, from 1,931 hours per year at Plant F to 5,920 hours per year at Plant C; this difference turns out to matter a great deal for profitability, as Section 4.2 shows.
>
> The original spreadsheets, laid out with one column per plant for ease of reading, were restructured into a tidy long format, with each row recording a single parameter, its unit, the processing stage, the plant, and the corresponding value, so that the dataset could be queried programmatically by the optimization model. Eleven processing stages were normalized across the six mills: reception, sterilization, threshing, digestion and pressing, clarification, oil recovery, storage, nut drying, nut cracking, process water heating, and the boiler house. Data quality was audited rather than assumed: a unit error in the reported lower heating value of the biomass, an analogous unit error in the CH4 emission factor applied to the valorization scenarios, and a set of process efficiencies computed by a spreadsheet formula with a broken reference were identified and corrected before modeling; in each case the affected quantities were recomputed from first principles and the reported efficiencies were treated as model outputs subject to validation rather than as inputs.
>
> The higher heating value of each biomass fraction was obtained from its ultimate analysis (Table 3, #13). Boiler efficiency was computed with the direct method of the ASME performance test code, with steam and feedwater enthalpies from the IAPWS-IF97 formulation; for the Plant A baseline this yielded 75.7%, consistent with the 54 to 76% range measured across the sector.

**Table 1 — Plant characterization and annual biomass availability**

| Plant | Capacity (t FFB/h) | Hours (h/yr) | FFB processed (t/yr) | Shell (t/yr) | Fiber (t/yr) | EFB (t/yr) | POME (m3/yr) |
|---|---|---|---|---|---|---|---|
| A | 30 | 5,105 | 153,150 | 9,189 | 18,837 | 37,215 | 91,890 |
| B | 40 | 5,155 | 206,200 | 8,496 | 25,775 | 46,395 | 123,720 |
| C | 30 | 5,920 | 177,600 | 7,992 | 22,555 | 40,670 | 106,560 |
| D | 24 | 5,496 | 131,904 | 7,519 | 16,356 | 24,534 | 79,142 |
| E | 30 | 3,147 | 94,410 | 3,444 | 12,368 | 22,979 | 56,646 |
| F | 20 | 1,931 | 38,620 | 2,703 | 4,905 | 8,245 | 23,172 |

*Sanity check passed: POME/FFB ratio ≈ 0.6 m3/t (Plant A), within the typical literature range
of 0.5 to 0.7 m3/t FFB.*

### 2.2 Current energy configuration (FINAL)

> At present, two of the six plants already operate on site power generation: Plant A meets 79.1% of its electricity demand through existing steam cogeneration, and Plant D meets 70.0% of its demand through an existing biogas system; the remaining four plants rely entirely on grid supply for electricity (Table 2). Process thermal demand, in contrast, is met entirely from each mill's own boiler in all six cases; there is no grid substitute for process steam. It is 13.5 to 26.4 times larger than electricity demand, which is typical for a process this steam intensive. This existing infrastructure is treated as a baseline condition rather than as a modeled investment in either scenario, and its implications for the marginal investment case of Plants A and D are examined separately in Section 3.5.

**Table 2 — Current (baseline) energy configuration**

| Plant | Electricity consumption (MWh/yr) | Electricity self-generation (%) | Self-generation source | Thermal demand (kWth) | Thermal energy demand (MWh_th/yr) |
|---|---|---|---|---|---|
| A | 3,083.7 | 79.1 | Steam cogeneration (existing) | 11,627.4 | 59,357.9 |
| B | 5,398.1 | 0.0 | Grid only | 14,954.1 | 77,088.2 |
| C | 2,740.9 | 0.0 | Grid only | 12,199.8 | 72,222.8 |
| D | 3,746.2 | 70.0 | Biogas (existing) | 9,180.4 | 50,455.2 |
| E | 2,281.7 | 0.0 | Grid only | 10,323.7 | 32,488.7 |
| F | 702.9 | 0.0 | Grid only | 7,436.5 | 14,360.0 |

*Sanity check passed: thermal-to-electric demand ratio ranges from 13.5x (Plant D) to 26.4x
(Plant C), consistent with the steam-intensive profile typical of palm oil extraction. Thermal
demand excludes boiler self-consumption/losses (validated against the source dataset for Plant A:
11,627.4 kWth, exact match).*

### 2.3 System boundary and scenario definitions (MERGED, CORRECTED)

> The system boundary is drawn at the mill gate. Only the incremental investment associated with energy valorization is considered: boilers, turbines, flue gas treatment, anaerobic digesters, biogas engines, and the process substitutions they require. The existing extraction plant is assumed to operate identically across all cases and is therefore excluded from both capital and operating costs, as are the revenues of the core oil extraction business, which do not change with the energy configuration. Combustion of biogenic carbon is treated as climate neutral following IPCC convention; only CH4 and N2O from combustion, together with fossil diesel use, are accounted as emissions.
>
> Three configurations are compared. The **baseline** reproduces the mills' measured current operation, in which low pressure boilers supply process steam and electricity is drawn from up to three sources: on site biomass cogeneration where it exists, the national grid, and back up diesel generation. The baseline is not a design case but a validation case, used to confirm that the model reproduces the plants' measured energy balances before either scenario is evaluated (Section 2.4).
>
> **Scenario 1 (extraction condensation route)** combusts all solid residues, fiber, shell, and mechanically pretreated empty fruit bunches, in a high pressure boiler. An extraction condensation steam turbine bleeds steam to satisfy process heat demand and expands the remainder to condensing conditions to maximize electricity output. Palm oil mill effluent is anaerobically digested and the resulting biogas fuels a gas engine; empty fruit bunches are not part of this digestion stream. Continuous sterilization replaces the conventional batch process in this scenario, avoiding the pressure spikes that batch sterilization imposes on the steam system and allowing steadier turbine operation.
>
> **Scenario 2 (backpressure route with co-digestion)** combusts only fiber and shell, in a lower pressure boiler feeding a backpressure turbine whose exhaust steam supplies the entire process heat demand. Empty fruit bunches are withdrawn from the combustion train, thermally pretreated to raise their biodegradability, and co-digested with palm oil mill effluent, so that the anaerobic route carries a substantially larger organic load than in Scenario 1. Continuous sterilization is **not** implemented in this scenario: the additional steam demand it requires could not be met by the energy available from the reduced solid biomass stream (fiber and shell only), so the conventional batch process is retained. Dynamic clarification, which does not add steam demand, replaces the conventional stage in both scenarios.
>
> Design parameters for the boilers and turbines follow operating conditions reported for comparable installations, with the Scenario 2 turbine parameters verified against Booneimsri et al. (2018). The biochemical methane potential of pretreated EFB was computed with the correlation of Thomsen et al. (2014), and the conceptual design assumptions for organic load removal, biogas yield, and CH4 content were taken from Voogt et al. (2021).

**Figures 1 to 3 — Configuration diagrams for the baseline, Scenario 1, and Scenario 2**
(one diagram each, built directly from the descriptions in this section) — **CREATED this session
(matplotlib, boxes and arrows), no notebook data required since these are conceptual process
diagrams, not data visualizations**
- Figure 1 — Baseline: fiber and shell to a low pressure boiler for process steam; electricity from
  up to three sources (on-site cogeneration at Plants A and D only, national grid, diesel backup);
  POME untreated in this configuration.
- Figure 2 — Scenario 1: fiber, shell, and pretreated EFB to a high pressure boiler feeding an
  extraction condensation turbine (bleeds for process steam, condenses the rest for electricity);
  POME to an anaerobic digester and gas engine, independent of the turbine route; continuous
  sterilization.
- Figure 3 — Scenario 2: fiber and shell only to a lower pressure boiler feeding a backpressure
  turbine (exhaust steam meets 100% of process heat); EFB withdrawn, thermally pretreated, and
  co-digested with POME; batch sterilization retained.

**Discussion angle to develop**: part of Scenario 2's higher profitability/robustness may stem
from its broader biogas feedstock (POME+EFB) rather than the turbine choice alone. Worth
isolating this effect if time allows.

### 2.4 Optimization model (MERGED, cross-reference fixed)

> The model was developed in two phases. **Phase 1 (validation)** formulates each configuration with fixed capacities and no degrees of freedom, using a dummy objective; its purpose is to confirm that the thermal balance and the electricity balance close simultaneously for each mill before any decision variable is introduced. All three configurations returned optimal status for the six mills, confirming the internal consistency of the cleaned dataset.
>
> **Phase 2 (superstructure)** releases equipment capacity as a decision variable. Two generation routes are represented independently for each mill: a steam turbine selected from a discrete commercial catalogue by binary variables, and a modular biogas engine sized as an integer number of 1,000 kW units, a modularity consistent with units reported for palm oil mill effluent to biogas installations. Each route carries its own continuous utilization factor, bounded between zero and one. Biomass availability is the binding physical constraint: no route may generate more energy than its substrate allows.
>
> Surplus electricity is not remunerated at a single price. Under the prevailing Colombian regulation for distributed and small scale self generation, each kWh is valued according to its destination: self consumption and an energy credit tier are both remunerated at the plant's own weighted retail electricity price (0.114 to 0.259 USD/kWh, computed from each mill's measured supply mix), jointly capped at the plant's own metered demand, since together they represent electricity that displaces a retail purchase rather than reaching the spot market; any generation beyond that joint cap is sold at the spot price (0.0703 USD/kWh, the eleven month average of the wholesale market, adopted because of the high volatility of the series). Because the retail-linked tiers share an identical price, the split between self consumption and the energy credit tier is immaterial to profitability and is left to the solver; only their joint cap against metered demand is economically binding (Table 3, #5).

**Table 3 — Governing equations** (formal notation, cross-referenced to the Nomenclature above;
subscripts and summations now match the notebook's implementation exactly)

| # | Component | Formula | Notes |
|---|---|---|---|
| 1 | Equipment CAPEX (six-tenths rule) | $C_i = C_{ref} \left(\dfrac{S_i}{S_{ref}}\right)^{0.6} \dfrac{CEPCI_{2026}}{CEPCI_{2019}}, \quad \forall i \in I$ | $CEPCI_{2019}=607.5$, $CEPCI_{2026}\approx873.8$ |
| 2 | Modular biogas generator CAPEX | $C^{bio}_i = n_i \, C_{unit}, \quad n_i \in \mathbb{Z}_{\geq 0}, \; \forall i \in I$ | Linear, 1,000 kW increments |
| 3 | Annualized CAPEX | $C^{ann}_i = \dfrac{C^{total}_i}{PVAF}, \quad PVAF = \dfrac{(1+r)^N - 1}{r(1+r)^N}$ | $r=10\%$, $N=20$ yr, $PVAF = 8.5136$ |
| 4 | O&M cost | $OM_i = \alpha \, C^{total}_i, \quad \alpha = 0.025$ | Applies to both variable and fixed CAPEX |
| 5 | Three-tier revenue | $R_i = p^{retail}_i \left(E^{auto}_i + E^{permuta}_i\right) + p^{spot} E^{bolsa}_i$, s.t. $E^{auto}_i + E^{permuta}_i \leq D_i$ | $p^{spot}=0.0703$ USD/kWh |
| 6 | Objective 1 (economic benefit) | $f_1 = \displaystyle\sum_{i \in I} \left[R_i - C^{ann}_i - OM_i - u^{turb}_i\,OC^{bio}_i - u^{EFB}_i\,OC^{EFB}_i\right]$ | $OC^{bio}_i$: fiber/shell opportunity cost (PKS/MF value); $OC^{EFB}_i$: EFB opportunity cost (NFRV, Section 2.6). $u^{EFB}_i = u^{turb}_i$ in Scenario 1 (EFB combusted), $u^{EFB}_i = u^{bio}_i$ in Scenario 2 (EFB co-digested) |
| 7 | Objective 2 (net generation) | $f_2 = \displaystyle\sum_{i \in I} \left[\eta^{turb}_{net} P^{turb}_i u^{turb}_i + \eta^{bio}_{net} P^{bio}_i u^{bio}_i\right] h_i$ | Net of conversion losses (Section 2.6 to 2.7); self-consumption constant across the front |
| 8 | $\epsilon$-constraint sweep | $\max f_1(x)$ s.t. $f_2(x) \geq \epsilon_k$, $\; \epsilon_k = f_2^{min} + \dfrac{k}{10}\left(f_2^{max}-f_2^{min}\right), \; k=0,\ldots,10$ | Pareto front construction |
| 9 | LCOE (export basis) | $LCOE_i = \dfrac{C^{ann}_i + OM_i}{E^{permuta}_i + E^{bolsa}_i}$ | Denominator excludes self-consumption $E^{auto}_i$ |
| 10 | HHV correlation | $HHV_b = 0.3443\,X^C_b + 1.192\,X^H_b - 0.113\,X^O_b - 0.024\,X^N_b + 0.093\,X^S_b, \; \forall b \in B$ | Elemental mass fractions, dry basis; internal consistency check only |
| 11 | Avoided emissions balance | $\Delta GHG_i = EF_{biomass}\,m^{biomass}_i + EF_{biogas}\,V^{biogas}_i + EF_{diesel}\,E^{diesel}_i - EF_{grid}\left(E^{permuta}_i + E^{bolsa}_i\right)$ | Biogenic CO2 excluded (IPCC); $EF_{diesel}=74{,}100$ kg CO2/TJ; $EF_{grid}=163.4$ g CO2/kWh |
| 12 | Rural household-equivalent | $HH_i = \min\!\left(\dfrac{E^{permuta}_i + E^{bolsa}_i}{c_{HH}}, \, N^{rural}\right)$ | $c_{HH}=346$ kWh/household/yr, 3.7 persons/household (DANE 2018); capped at 100%; non-saturating share-of-total-demand indicator reported alongside |
| 13 | Boiler efficiency (direct method) | $\eta^{boiler}_i = \dfrac{\dot{m}^{steam}_i \left(h_{steam} - h_{feedwater}\right)}{\dot{m}^{fuel}_i \, HHV_{fuel}}$ | ASME PTC direct method, IAPWS-IF97 enthalpies; Plant A baseline: 75.7%, within 54-76% sector range |

*All later subsections (2.5 to 2.9) reference this table by equation number rather than
re-deriving formulas inline, per decision #1. Equations are rendered here in LaTeX-style notation
for precision during co-author review; final typesetting will convert these to the journal's
native equation format (Word Equation Editor or LaTeX, depending on the submission template).*

### 2.5 Regulatory framework represented in the model (FINAL, concise per decision #4)

> Three families of instruments govern the economics of distributed bioenergy in Colombia, and the model represents them asymmetrically, a choice made explicit here because it conditions the interpretation of the results.
>
> CREG Resolution 174 of 2021, which governs remuneration of surplus electricity, is the only instrument embedded in the optimization itself: it acts on the marginal revenue of each additional kWh and therefore on the sizing decision, and its tariff structure is described in Section 2.4. Capital side tax incentives for non-conventional renewable sources (Law 1715 of 2014, as amended by Law 2099 of 2021) are deliberately not represented in the base case; the economic results reported in Section 3 are therefore conservative by construction, and the magnitude of this omission is quantified separately in the sensitivity analysis of Section 2.9. Two further instruments, the firm energy reliability charge (CREG Resolution 071 of 2006) and the current carbon tax (Decree 926 of 2017), are treated as context rather than embedded in the optimization; both are assessed against the model outputs in the Discussion.

### 2.6 Techno-economic parameters (MERGED)

> Capital costs are derived from supplier quotations obtained during the study, referenced to a 15 t FFB/h capacity, and escalated to 2026 USD using the Chemical Engineering Plant Cost Index (Table 3, #1). Where no quotation was available, costs were scaled from a reference capacity using the six-tenths rule (Table 3, #1; exponent 0.6), which replaces an earlier, invalid linear CAPEX assumption in which boiler cost was inadvertently double counted with turbine cost. Investments are annualized with a present value annuity factor of 8.5136, corresponding to a 10% discount rate over a 20 year lifetime (Table 3, #3), and operating and maintenance costs are taken as 2.5% of capital cost per year (Table 3, #4), applied to both fixed and variable CAPEX.
>
> A distinction is made between capital costs that respond to the sizing decision, the steam turbine and the biogas engine, and those that do not, such as the boiler, flue gas treatment, digester lagoons, and process substitutions, which are dimensioned by the plant's throughput rather than by the capacity chosen. Only the former enter the solver's objective, since the latter cannot alter the optimal solution; both, however, are included in the net benefit reported in the results, so that profitability is assessed against the full incremental investment.
>
> Diverting solid biomass toward energy generation also carries an opportunity cost, since fiber and shell have an existing market value as PKS and MF, and empty fruit bunches have an existing agronomic value as a soil amendment. The former is priced directly at PKS/MF market rates. The latter is estimated through a Net Fertilizer Replacement Value (NFRV): empty fruit bunches release plant available nutrients (N, P, K, Mg) as they decompose in the field, at rates of 7.7, 2.3, 21.7, and 3.3 kg of equivalent synthetic fertilizer per tonne of fresh EFB respectively (Caliman et al., 2001), priced at Colombian market rates for urea, diammonium phosphate, potassium chloride, and a Mg source (Fedepalma/DANE-Sipsa, Q1 2025), and converted to USD at the prevailing exchange rate. Because EFB decomposition is a microbially mediated process constrained by its high C/N ratio, unlike the immediate solubility of synthetic fertilizer, only a fraction of this theoretical nutrient value is realized within the first year; a mineralization efficiency of 70%, within the 60 to 80% range reported for field-scale EFB decomposition (Budi et al., 2001; Saletes et al., 2004; agronomic parameters for oil palm from Ramirez et al., 2011), is applied to the gross replacement value to obtain the net opportunity cost used in the model. This cost enters the objective scaled by the same utilization variable that governs solid biomass combustion in Scenario 1, and by the biogas utilization variable in Scenario 2, since EFB is co-digested rather than combusted in that configuration.

### 2.7 Sustainability indicators (MERGED, CORRECTED)

> Three indicators, the levelized cost of electricity, the greenhouse gas balance, and rural electricity coverage, are computed at every point of the Pareto front rather than at a single design point.
>
> The LCOE is calculated as annualized capital cost plus annual operating and maintenance cost, divided by the annual electricity exported rather than generated (Table 3, #9). Exported surplus, the electricity that actually leaves the mill and is remunerated or credited under the tariff structure of Section 2.4, is the economically and physically meaningful quantity for this indicator; self consumption, which is fixed by each mill's own demand and does not respond to the sizing decision, is excluded from the denominator to keep the indicator comparable across plants of different demand.
>
> The greenhouse gas balance draws on that same exported surplus. It applies IPCC default emission factors for CH4 and N2O from solid biomass and biogas combustion, an emission factor of 74,100 kg CO2/TJ for backup diesel, and a credit for the displacement of grid electricity by the exported surplus (Table 3, #11). The palm plantation itself also sequesters carbon, at a rate of 135.04 kg CO2 per tonne of fresh fruit bunches processed, consistent with the author's prior potential-quantification study of this same sector (Barrera Hernandez et al., 2024); this credit is common to both scenarios, since it depends only on the volume of fruit processed and not on which cogeneration route is chosen, and including it in the main comparison would dominate the technology-specific differences this study is designed to isolate. It is therefore excluded from the avoided-emissions figures reported throughout Results (Tables 4 to 9, Figures 8 to 9), which credit grid displacement only and are meant to compare technology routes on a like-for-like basis. A separate, more comprehensive process balance available in the notebook (`balance_emisiones_esc1`/`esc2`, `balance_neto_GEI`) nets out combustion emissions and does include this plantation credit internally; that comprehensive balance is not the source of any figure currently in Results and should be clearly labeled as distinct from the grid-displacement indicator before any future revision draws on it.
>
> **Citation correction log (this session)**: the value 135.04 kg CO2/tFFB had been attributed in
> the notebook to Ramirez-Contreras et al. (2020), whose full text was checked this session and
> does not contain that figure. Cross-referencing the project's own methodological notes traced
> the value to Barrera Hernandez, Sagastume Gutierrez, Ramirez-Contreras, Cabello Eras,
> Garcia-Nunez, Barrera Agudelo, and Silva Lora (2024), "Biomass-based energy potential from the
> oil palm agroindustry in Colombia: a path to low carbon energy transition," Journal of Cleaner
> Production, 449, 141808, https://doi.org/10.1016/j.jclepro.2024.141808, the author's own prior
> potential-quantification study of the same sector, reused here for consistency between the two
> papers. This is also the natural citation for the Introduction's opening claim that prior
> assessments have established the scale of the sector's technical potential (Section 1), closing
> two open items with one source. The exact page or table within that paper reporting 135.04 has
> not been independently re-verified against its full text this session; confirming that page
> reference before submission is a minor final check, distinct from the citation-attribution error
> itself, which is resolved.
>
> Rural electricity coverage expresses that same surplus as an equivalent number of rural households, using the departmental average rural consumption (346 kWh per household per year, derived from Cabello Eras et al. 2022) and 3.7 persons per household (DANE, CNPV 2018) (Table 3, #12). Because a single mill can exceed the aggregate rural residential demand of the entire department, the indicator is capped at 100% coverage for reporting, and a second, non-saturating indicator, the surplus as a share of total departmental electricity demand, is reported alongside it.

**CORRECTION LOG (this session, kept for internal tracking, not part of manuscript text)**: the
original LCOE rationale ("surplus approaches zero at the economic optimum") was written before
the CAPEX correction and is no longer accurate. Under the corrected model, exported surplus at
the economic optimum is 170.0 GWh (Scenario 1) and 130.7 GWh (Scenario 2), far from zero (verified
this session). The switch to an export based denominator raises reported LCOE by 11 to 13%
(Scenario 1: 0.0715 to 0.0797 USD/kWh; Scenario 2: 0.0466 to 0.0526 USD/kWh at the economic
optimum), still within typical bioenergy LCOE ranges. This change propagates to any Results table
or figure citing LCOE and must be applied before Results is drafted.

### 2.8 Multi-objective framework (MERGED)

> A preliminary structural analysis showed that the environmental and social objectives are nearly collinear with electricity generation in this system: avoided emissions scale approximately linearly with exported electricity, and rural coverage scales linearly with the surplus. The only genuine conflict is therefore between economic performance and biomass deployment, and the problem is formulated in two dimensions: **f1** (maximize annual net benefit: self consumption savings plus surplus revenue across the three regulatory tiers, minus annualized capital cost and operating cost; Table 3, #6) and **f2** (maximize annual electricity generated from biomass, a joint proxy for the environmental and social pillars and a direct answer to how much of the available potential is used; Table 3, #7). Generation, rather than exported energy, is used for f2 because self consumption is constant across the entire explored front (verified this session, §53); this does not affect any reported economic or environmental figure, all of which use exported energy directly.
>
> The Pareto front is obtained with the two step epsilon constraint method (Table 3, #8). A lexicographic payoff table first establishes the extremes of each objective; f1 is then maximized subject to a progressively increasing floor on f2, with the floor varied over 10 intervals between those extremes. The epsilon constraint method was preferred over weighted sum aggregation because it controls the number of efficient solutions, does not skip non-convex regions of the front, and avoids arbitrary normalization of objectives expressed in different units.

### 2.9 Policy instrument analysis (method only, results moved to Section 3.7)

> Two further analyses were performed on the converged model, to assess the two families of policy instruments available to Colombian policy on their own terms rather than in the abstract. Both re-solve the full optimization rather than post-processing its outputs, keeping the sizing decision free to respond.
>
> **Capital side instruments**: a generic effective reduction of capital cost (0%, 10%, 19%, and 30%) is applied to both fixed and variable CAPEX, and the epsilon constraint procedure re-run in full at each level; the 0% case reproduces the base results exactly and serves as a verification of the procedure.
>
> **Price side instruments**: the spot market tier price is swept from 0.07 to 0.25 USD/kWh in one cent steps; at each price, both the unconstrained economic optimum and the forced full deployment case are solved. Only the spot market tier price is varied; retail priced tiers, which reflect each plant's own avoided purchases, are held at their measured values.

*Both analyses required the same O&M-on-fixed-CAPEX correction applied elsewhere in this session
(§51 for the price side; the capital side analysis, formerly non-functional, was fixed and
validated this session against §19b/§51). Results reported in Section 3.7.*

### 2.10 Modeling workflow

> A single flow diagram summarizes the two-phase modeling process described throughout this
> section: data inputs feed technical sizing per plant, which determines CAPEX and O&M
> (Table 3, #1 to #4), followed by MILP optimization (#6 to #8), the resulting Pareto front,
> the sustainability indicators computed at every point of that front (#9 to #12), and finally
> the sensitivity analyses of Section 2.9.

**Figure (unnumbered, methodology overview) — Modeling workflow** — **CREATED this session**
(seven-step horizontal flow diagram, matplotlib, cross-referenced to Table 3 equation numbers)

---

## Appendix / Supplementary content list (per decision #2)
- Full per-plant biomass availability and technical parameters
- Complete CAPEX catalogs (turbine sizes, unit costs) for both scenarios
- Complete emission factor table (CH4/N2O by biomass source, GWP100 values)
- PVAF and CEPCI factor derivations
- Full Pareto front tables (all ε-constraint points, not just headline rows)
- Full price side sweep table (all one cent increments from 0.07 to 0.25 USD/kWh, both scenarios)
- Full ultimate analysis / biomass physicochemical characterization table

---

## Citations newly introduced this session (verify formatting/DOI before submission)
- **NEW this session**: Caliman, J.P. et al. (2001) — source of the EFB nutrient-equivalence
  factors (7.7, 2.3, 21.7, 3.3 kg synthetic fertilizer per t EFB). Confirmed real via a 2022
  Springer meta-analysis citing it, but the original values found there (2.60, 0.725, 6.80, 1.250
  kg/palm from a 60 t/ha application) are in different units; back-converted using a range of
  plausible planting densities (128 to 156 palms/ha), the implied kg/t figures (5.5-6.8 urea,
  1.6-1.9 phosphate, 14.5-17.7 KCl, 2.7-3.3 Mg) are the right order of magnitude and relative
  ranking but do not exactly reproduce the factors used. Locate and cite the primary Caliman et
  al. (2001) source directly, with its actual planting density assumption, before submission.
- **NEW this session**: fertilizer prices for the EFB opportunity cost — Fedepalma/DANE (Sipsa),
  "Precio promedio de insumos en el primer trimestre," 2025 edition, gives citable Q1 2025 prices
  for urea, KCl, sulfato de amonio, and fosfato diamonico (DAP) in COP per 50 kg bag. DAP is used
  as the phosphate-source proxy in place of fosfato tricalcico, since DAP is what Sipsa/DANE
  actually track for the Colombian palm sector; note this substitution explicitly in Methods.
  Kieserita (Mg source) has no equivalent Sipsa/DANE quote found and remains an unverified
  placeholder (1,600 COP/kg) pending a citable source.
- **NEW this session**: mineralization efficiency factor (70%, range 60-80%) for the EFB
  opportunity cost, attributed to Budi et al. (2001), Saletes et al. (2004), and Ramirez et al.
  (2011). None of these three have been independently verified this session; confirm full
  citations before submission.
- **NEW this session**: Fedepalma's quarterly ICPA (Indice de Costos para el Cultivo de la Palma
  de Aceite), by Mosquera-Montoya et al., confirmed as a real, citable, ongoing publication that
  tracks exactly these fertilizer inputs for the Colombian palm sector; useful as a general
  supporting citation for the fertilizer-price data source even though the specific absolute
  price table used came from the Sipsa/DANE graphic above, not from an ICPA bulletin directly.
- ~~Booneimsri et al. (2018)~~ **VERIFIED**: Booneimsri, P., Kubaha, K., Chullabodhi, C. (2018). "Increasing
  power generation with enhanced cogeneration using waste energy in palm oil mills." Energy Science &
  Engineering, 6(3), 154-173. DOI: 10.1002/ese3.196. On-topic (backpressure steam turbine cogeneration
  in palm oil mills), correctly cited for Scenario 2 turbine parameter verification.
- ~~Thomsen et al. (2014)~~ **VERIFIED**: Thomsen, S.T., Spliid, H., Østergård, H. (2014). "Statistical
  prediction of biomethane potentials based on the composition of lignocellulosic biomass." Bioresource
  Technology, 154, 80-86. DOI: 10.1016/j.biortech.2013.12.029. A general statistical BMP-prediction
  correlation for lignocellulosic biomass, correctly applied to EFB in this study.
- Voogt et al. (2021) — **STILL UNRESOLVED**: could not be located via public search. A real researcher,
  Julien Voogt (Wageningen Food & Biobased Research), works on oil palm biomass valorization projects,
  lending plausibility to a 2021 conceptual design report, but no matching publication surfaced. If the
  original PDF is available locally, share it for verification the same way Barrera Hernandez et al.
  (2024) was confirmed; otherwise this citation remains open.
- **NEW FINDING this session**: "Guerrero et al. (2023)" and "Chavez et al. (2026)" (Introduction and
  Table 7 respectively) are BOTH misattributed, the same error pattern as the original
  Ramirez-Contreras/Barrera Hernandez mixup. Both trace to Cenipalma's annual "Estudio de costos de
  producción... empresas benchmark" series (Revista Palmas), whose lead author is always
  Mosquera-Montoya, M.; Guerrero and Chavez appear only as co-authors in different yearly editions.
  Confirmed matches: Guerrero, A.E. co-authors Mosquera-Montoya et al. (2022), "Estudio de costos de
  producción 2021 para empresas benchmark del sector de la palma de aceite de Colombia," Palmas, 43(4),
  26-39, DOI: 10.56866/01212923.13911. Chavez Duarte, N. co-authors the most recent edition found,
  Mosquera-Montoya et al. (2025), "Costos de producción 2024 en la palmicultura colombiana: un análisis
  de empresas benchmark," Palmas, 46(1), 41-54, DOI: 10.56866/01212923.14473, the likely true source of
  the Table 7 cost range figures (year off by one, author misattributed). **Action item**: rename both
  citations to Mosquera-Montoya et al. with the correct year, and confirm against the actual paper that
  the specific cost range (21 to 543.3 COP/kWh) and adoption figures (6/23, 7/23 mills) appear in the
  2025 edition rather than an earlier or later one in the series.
- Ramirez-Contreras et al. (2020) is NOT the source of the 135.04 kg CO2/tFFB plantation carbon
  credit; that citation was a misattribution in the notebook. **RESOLVED this session**: traced
  to Barrera Hernandez et al. (2024), "Biomass-based energy potential from the oil palm
  agroindustry in Colombia: a path to low carbon energy transition," Journal of Cleaner
  Production, 449, 141808, https://doi.org/10.1016/j.jclepro.2024.141808, the author's own prior
  potential-quantification study, confirmed via the project's methodological notes and by author
  and topic match (Ramirez-Contreras and Cabello Eras, already cited elsewhere in this outline,
  are co-authors). Doubles as the citation for the Introduction's opening claim about prior
  potential-quantification assessments (Section 1). The exact page/table reporting 135.04 within
  that paper has not been independently re-verified against its full text; a final page check
  before submission is recommended but does not block anything else.

---

## 3. Results

### 3.1 Deployment relative to the baseline

> The scale of the change from current operation is substantial at every plant, whichever route is followed (Table 4). Under the baseline, four mills draw their electricity entirely from the grid and two already partially self-generate (Table 2); under either scenario, all six become net electricity producers at the economic optimum, generating between three and eleven times their own current consumption.
>
> Scenario 1's multiples at the economic optimum are notably uniform across plants (3.2 to 5.2 times baseline), a direct consequence of the conversion loss mechanism established in Section 2.6 to 2.7: at this point, every plant selects the smallest available turbine and relies almost entirely on POME biogas, so plant-to-plant differences in turbine sizing, which drove most of the variation in the uncorrected model, no longer apply. Scenario 2 retains a wider range at its own optimum (6.4 to 10.9 times), closer to the pattern of underlying biomass availability. Plant A illustrates the shift most clearly: with the corrected model, its multiple is smaller under Scenario 1 (3.3 times) than under Scenario 2 (7.9 times) at the optimum, the reverse of what the uncorrected model implied.
>
> Forcing deployment to its technical maximum re-introduces the variation that the economic optimum suppresses in Scenario 1: multiples widen to a 9.5 to 16.4 range, since every plant is now pushed toward a much larger turbine regardless of whether that investment is individually profitable, a pattern already visible in the negative aggregate net benefit reported in Section 3.2. Scenario 2 changes far less between its own optimum and full deployment (6.4 to 11.7 at full deployment), consistent with the narrow gap between these two points already established in Section 3.4.

**Table 4 — Generation relative to baseline electricity consumption, at the economic optimum and at full deployment**

| Plant | Baseline (MWh/yr) | Scenario 1, optimum (MWh/yr, x baseline) | Scenario 1, full deployment (MWh/yr, x baseline) | Scenario 2, optimum (MWh/yr, x baseline) | Scenario 2, full deployment (MWh/yr, x baseline) |
|---|---|---|---|---|---|
| A | 3,083.7 | 10,205.6 (3.3x) | 39,635.5 (12.9x) | 24,452.7 (7.9x) | 26,861.6 (8.7x) |
| B | 5,398.1 | 17,108.4 (3.2x) | 52,696.2 (9.8x) | 34,435.0 (6.4x) | 37,834.4 (7.0x) |
| C | 2,740.9 | 14,222.6 (5.2x) | 44,940.4 (16.4x) | 29,915.0 (10.9x) | 32,186.3 (11.7x) |
| D | 3,746.2 | 14,087.4 (3.8x) | 35,433.8 (9.5x) | 24,021.5 (6.4x) | 25,653.1 (6.8x) |
| E | 2,281.7 | 7,989.1 (3.5x) | 25,004.2 (11.0x) | 16,722.0 (7.3x) | 17,845.3 (7.8x) |
| F | 702.9 | 3,350.1 (4.8x) | 10,506.5 (14.9x) | 6,619.1 (9.4x) | 7,152.5 (10.2x) |

*Values are net electricity generated, corrected for conversion losses (Section 2.6 to 2.7). At the
economic optimum, every plant selects the smallest turbine in the Scenario 1 catalog (300 kW) and
relies almost entirely on biogas, explaining the narrow range of multiples in that column relative
to full deployment or to Scenario 2. Re-validated this session against the fully corrected model
(joint self-consumption/energy-credit cap, corrected metered demand, reconstructed fiber/shell
opportunity cost, and the validated EFB opportunity cost): the per-plant physical generation mix
is identical to an earlier draft of this table, confirming that none of today's corrections, which
affect revenue and cost, shift the underlying technical capacity choice at these two points.*

**Figure 4 — Grouped bar chart of generation as a multiple of baseline consumption, by plant**
(complements Table 4; makes the uniformity at the Scenario 1 economic optimum, and its reversal at
full deployment, visually immediate) — **rendered and reviewed this session, ready to generate in
the notebook (matplotlib, same palette as the rest of the figures)**

### 3.2 Aggregate techno-economic Pareto front

> Both scenarios are profitable at their own economic optimum, with net benefits of USD 258,705 (Scenario 1, at 32.2% of its own technical potential) and USD 3,427,932 (Scenario 2, at 92.3% of its own technical potential) per year. Scenario 2 remains solidly profitable at full technical deployment (USD 2,315,672 per year); Scenario 1 does not, and its profitable window is narrower than a first look at the optimum suggests: net benefit already turns negative one step past the optimum (USD −413,799 per year at 40.6% of potential) and worsens monotonically to USD −6,531,746 per year at full deployment, a finding examined further in Section 3.7. LCOE at the economic optimum, on an exported energy basis (Section 2.7), is 0.1488 USD/kWh for Scenario 1 and 0.0576 USD/kWh for Scenario 2; both are essentially unchanged from an earlier draft of this section (0.1472 and 0.0576 respectively), since LCOE depends on exported electricity rather than on the revenue-side corrections applied this session. Closing the gap between the private optimum and full deployment costs USD 6,790,451 per year for Scenario 1, equivalent to USD 294 per additional tonne of CO2 avoided, and USD 1,112,260 per year for Scenario 2, equivalent to USD 599 per tonne; both figures, along with the underlying model, were validated this session against a corrected treatment of self consumption and the energy credit tariff tier (previously modeled as two independent caps rather than a single joint cap against each plant's metered demand, Section 2.4) and a newly added, literature-grounded opportunity cost for empty fruit bunches diverted from agronomic use (Section 2.6), confirmed with direct, non-cached model resolutions.
>
> Figures 5 and 6 show how generation is routed from primary sources, through conversion losses, to the three revenue tiers of Section 2.4, at the economic optimum and at full deployment, for each scenario. The qualitative mechanism established earlier in this study continues to hold under the corrected model: at the economic optimum, Scenario 1 relies overwhelmingly on POME biogas (64.2 GWh/yr), with only a small turbine contribution (8.0 GWh/yr); full deployment reverses this balance, driven by a turbine expansion to 184.9 GWh/yr while biogas remains at its POME-limited ceiling. This follows from the conversion loss mechanism established in Section 2.6 to 2.7: turbine losses (about 20%) are substantially larger than biogas losses (about 6%), so the private optimum favors the cheaper-to-convert biogas route and invests in the turbine only once deployment is pushed beyond what profitability alone would choose. In Scenario 1, all exported surplus is routed to the spot market tier rather than the energy credit tier at every point checked, consistent with the finding in Section 3.4 that the joint self-consumption/energy-credit cap is filled entirely by self-consumption for this scenario. Scenario 2 shows a related but less extreme pattern: biogas remains the dominant source at both points (127.4 to 127.9 GWh/yr, nearly unchanged) while the turbine grows from 20.1 to 33.7 GWh/yr, and both the self-consumption and energy-credit tiers are used (16.8 GWh/yr each at both points), with the remainder routed to the spot market. Conversion losses, shown explicitly as their own flow, rise from 5.3 to 40.9 GWh/yr in Scenario 1 as the lossier turbine route expands, compared with a narrower 11.3 to 14.1 GWh/yr range in Scenario 2.

**Figures 5 and 6 — Sankey diagrams of generation routed through the three revenue tiers**
(energy flow only, economic figures reported in prose above; each figure combines the economic
optimum and full deployment points as panels (a) and (b), respectively) — **FINAL, validated this
session against direct model resolutions matching Table 5 and Section 3.2 exactly (all four
underlying models checked against known net benefit before the figures were generated)**
- Figure 5 — Scenario 1: (a) economic optimum, 72.2 GWh/yr gross, 67.0 GWh/yr net (8.0 turbine +
  64.2 biogas, 5.3 GWh/yr conversion losses; 19.9 GWh/yr self-consumption, 47.0 GWh/yr spot
  market, no energy-credit tier use); (b) full deployment, 249.1 GWh/yr gross, 208.2 GWh/yr net
  (184.9 turbine + 64.2 biogas, 40.9 GWh/yr conversion losses; 19.9 GWh/yr self-consumption, 188.3
  GWh/yr spot market, no energy-credit tier use).
- Figure 6 — Scenario 2: (a) economic optimum, 147.5 GWh/yr gross, 136.2 GWh/yr net (127.4 biogas
  + 20.1 turbine, 11.3 GWh/yr conversion losses; 16.8 GWh/yr self-consumption, 16.8 GWh/yr energy
  credit, 102.6 GWh/yr spot market); (b) full deployment, 161.6 GWh/yr gross, 147.5 GWh/yr net
  (127.9 biogas + 33.7 turbine, 14.1 GWh/yr conversion losses; 16.8 GWh/yr self-consumption, 16.8
  GWh/yr energy credit, 113.9 GWh/yr spot market).

**LCOE shape, confirmed this session against the fully corrected model** (Figure 8b): Scenario 1's
LCOE is U-shaped across the front, falling from 0.1488 USD/kWh at the economic optimum (32.2% of
potential) to a minimum of about 0.0940 USD/kWh near 87% of potential, then rising to 0.1033
USD/kWh at full deployment. Unlike an earlier draft of this section, the minimum-LCOE point is
**not** a profitable point under the corrected model (net benefit −$3,327,144 at 87%, Table
[to be added]); LCOE and profitability diverge even more sharply than previously described, since
Scenario 1 is only profitable very close to its own economic optimum (Section 3.2). Scenario 2
shows no U-shape: its LCOE-minimizing point coincides exactly with its economic optimum (92.3% of
potential, 0.0576 USD/kWh), so the private optimum is simultaneously the cheapest point on the
curve, unlike Scenario 1 where the privately optimal point and the cost-minimizing point diverge
and neither point is representative of the other's profitability.

### 3.3 Plant level disaggregation

> Aggregate profitability conceals substantial variation across mills, and once conversion losses and the full set of opportunity costs are properly priced, none of the six mills remain profitable under Scenario 1 at full deployment (Table 5); the two largest, highest-utilization mills, B and C, come closest, but even they turn negative once the EFB opportunity cost and the corrected demand cap are applied. Scenario 2 is far more broadly viable: four of six mills remain profitable at full deployment (B, C, D, and E), with only Plant A and Plant F unviable. Plant A's result under Scenario 2 is a notable reversal from earlier analysis in this study: despite already partially self-generating, and despite being viable across most of Scenario 2's technical range at other points on the front (Section 3.5), Plant A turns negative at full deployment once the EFB opportunity cost is included, since its capacity choice at that point routes more biomass, EFB included, to the digester than its own economics can support. Plant F remains unviable under either technology route, consistent with its low annual operating hours limiting the surplus available to cover fixed costs.

**Table 5 — Net benefit by plant at full deployment**

| Plant | Scenario 1 (USD/yr) | Scenario 2 (USD/yr) |
|---|---|---|
| A | −1,336,197 | −113,940 |
| B | −471,498 | 1,066,132 |
| C | −216,126 | 1,361,445 |
| D | −863,244 | 295,684 |
| E | −1,704,770 | 296,099 |
| F | −1,939,911 | −589,748 |
| **Total** | **−6,531,746** | **2,315,672** |

*Validated this session against the fully corrected model: joint self-consumption/energy-credit
cap, corrected metered demand for technology substitution, reconstructed fiber/shell opportunity
cost, and the new EFB opportunity cost (Net Fertilizer Replacement Value, Section 2.6), all
confirmed with direct, non-cached model resolutions; per-plant sums match the aggregate net
benefit reported in Section 3.2 exactly.*

### 3.4 Robustness to electricity price

> The breakeven wholesale price, the price below which full deployment stops being profitable, differs sharply between scenarios (Table 6). At the aggregate level, Scenario 1 requires the spot price to hold at or above 0.1050 USD/kWh, about 49% above the current price; Scenario 2 remains profitable down to 0.0500 USD/kWh, a 29% drop from the current price. Both thresholds rose substantially once the EFB opportunity cost was properly included in the model (Scenario 1 from 0.0757 to 0.1050, Scenario 2 from 0.0234 to 0.0500), narrowing the robustness gap between the two routes without closing it. The same asymmetry holds plant by plant, with Plant F the least robust under either scenario (breakeven of 0.2697 USD/kWh under Scenario 1, 0.1703 under Scenario 2) and Plant C the most robust under Scenario 2 specifically (0.0148 USD/kWh).
>
> This gap is not because Scenario 2 depends less on the spot market; if anything, a majority of its exported surplus is sold there rather than at the fixed retail-linked tiers (Section 2.4). The reason is volume: Scenario 2's spot-exposed surplus at full deployment is large enough that even a moderate price generates enough revenue to close what would otherwise be a substantial shortfall at a low spot price. Scenario 1 needs a higher price for the same mechanism to work, because its cost structure, dominated by a larger turbine investment and now also by the EFB opportunity cost, leaves a bigger gap to close per unit of spot-exposed volume. Robustness, in other words, comes from having a lot of low-priced surplus to sell, not from needing the spot market less. A price threshold below which biomass valorization becomes uneconomical is not unique to this study's context: in an independent multi-objective optimization of palm oil waste-to-energy scenarios in Indonesia, Aprilianto and Rau (2025) similarly find that POME-based processing is infeasible below the government-set electricity price and becomes viable only once prices exceed that threshold, a structurally similar breakeven mechanism to the one identified here.

**Table 6 — Breakeven spot price by plant and in aggregate (current price: 0.0703 USD/kWh)**

| Plant | Scenario 1 (USD/kWh) | Scenario 2 (USD/kWh) |
|---|---|---|
| A | 0.1083 | 0.0762 |
| B | 0.0800 | 0.0363 |
| C | 0.0757 | 0.0148 |
| D | 0.0970 | 0.0558 |
| E | 0.1472 | 0.0468 |
| F | 0.2697 | 0.1703 |
| **Aggregate** | **0.1050** | **0.0500** |

*Fully validated this session against the corrected model, including the EFB opportunity cost:
per-plant current-price net benefit matches Table 5 exactly, and the aggregate breakeven for
Scenario 1 (0.1050) matches the independently derived value from the full front's zero-crossing
in Section 3.2. An intermediate version of this analysis, which reconstructed the split between
the energy-credit and spot-market tiers via an approximation (`min(excedente, autoconsumo)`)
rather than using the model's own solved allocation, gave a materially wrong result (Scenario 1
aggregate net benefit at full deployment of −$3,789,300 instead of the correct −$6,531,746); the
model's own `excedente_permuta_kWh` and `excedente_bolsa_kWh` columns should always be used
directly rather than reconstructed, since the joint self-consumption/energy-credit cap (Section
2.4) means the solver is free to allocate the entire tier to either label with no economic
consequence, and any approximation of that split independent of the model's own solution will
generally not match it.*

**Figure 11 — Robustness of full deployment to the spot market price**
(aggregate net benefit at full deployment, both scenarios, as a function of the spot price, with
the current spot price and each scenario's breakeven marked) — **FINAL, validated this session**
- **Caption**: Aggregate net benefit at full deployment as a function of the spot market price,
  for Scenario 1 and Scenario 2. The vertical line marks the current spot price (0.0703 USD/kWh);
  each curve crosses zero at that scenario's aggregate breakeven price (Table 6).

> Figure 9 shows the same asymmetry from a policy angle: the cost of closing the gap between the
> private optimum and full deployment, and what that cost implies per tonne of CO2 avoided,
> against Colombia's current carbon tax. Scenario 1's gap costs less in absolute terms (USD 3.89
> million per year against USD 1.10 million for Scenario 2) but Scenario 1 already deploys a
> smaller share of its own potential at the optimum, so the same absolute gap represents 130% of
> its own optimal net benefit, against 17% for Scenario 2. Per tonne of CO2, the ordering reverses:
> Scenario 1's marginal abatement is cheaper (USD 169/tCO2) than Scenario 2's (USD 593/tCO2), since
> Scenario 1 has more low-hanging technical potential left to capture. Both figures sit far above
> the carbon tax (USD 8.70/tCO2), a comparison developed further in Section 4.4.

**Figure 9 — Cost of closing the gap between the private optimum and full deployment, and implicit
marginal abatement cost against the current carbon tax**
(two panels: (a) cost of deploying the full 100% in MUSD/yr, labeled with the share of each
scenario's own optimal net benefit; (b) implicit cost per additional tCO2 avoided, with a
reference line at the current carbon tax) — **FINAL, validated this session (values match
`correr_frente`'s 0% incentive row and the independently confirmed USD 169/593 per tCO2 figures
exactly); carbon tax value verified against DIAN Resolution 000003 of 2026**
- **Caption**: Cost of deploying the full technical potential beyond each scenario's private
  optimum (a), and the implicit cost per additional tonne of CO2 avoided by doing so (b), compared
  against Colombia's current carbon tax (DIAN Resolution 000003 of 2026, COP 29,070.49/tCO2eq).

> At current prices, however, neither scenario's economic optimum reaches full deployment (Section 3.2): the profit maximizing choice stops at 32.2% of exportable potential in Scenario 1 and 92.3% in Scenario 2 (Table 9, confirmed against the corrected model). Forcing deployment the rest of the way costs USD 3,891,631 per year in forgone net benefit for Scenario 1 and USD 1,101,918 per year for Scenario 2, equivalent to USD 169 and USD 593 per additional tonne of CO2 avoided respectively (both confirmed this session against `correr_frente`'s output). Both figures substantially exceed Colombia's current carbon tax, a comparison developed further in Section 4.4.

### 3.5 Sensitivity of self-generating plants to technology upgrade decisions

> Plants A and D already generate part of their own electricity, so the value of investing further depends on how their existing infrastructure is priced, a quantity for which no single reliable estimate exists (Section 2.6 in the notes; not reproduced in Methods). Table 7 and Figure 7 report the outcome across the full cost range reported by Cenipalma's 2024 sector-wide benchmarking study of Colombian palm oil mills (21 to 543.3 COP/kWh for steam cogeneration, from a sample of 6 mills; 180 to 465.1 COP/kWh for biogas, from a sample of 7 mills), for both plants, both scenarios, and both the economic optimum and full deployment, with the EFB opportunity cost now included throughout.
>
> The picture changes substantially once this cost is properly priced. Under Scenario 1, Plant A is unprofitable across the *entire* observed cost range, at both deployment levels, including at the upper extreme of the range (543.3 COP/kWh); an earlier draft of this analysis, run before the EFB opportunity cost was validated, found Plant A becoming profitable at that upper extreme, but that result does not survive the correction. Plant D fares only marginally better under Scenario 1: also unprofitable across the entire range at both deployment levels. Under Scenario 2, the picture is more mixed than previously reported: Plant D remains profitable across the entire cost range at both deployment levels, but Plant A is only profitable from roughly the average reported cost upward, turning negative at the low end of the range; this is consistent with Plant A's own negative result at full deployment under Scenario 2 at the current price point (Table 5), which is no longer an outlier but part of a broader pattern across much of Plant A's plausible cost range.

**Table 7 — Net benefit for Plants A and D across the empirically observed cost range of their existing infrastructure**

| Plant | Scenario | Point | Min | Average | Current | Max |
|---|---|---|---|---|---|---|
| A | 1 | Optimum | −1,064,239 | −923,458 | −866,505 | −561,861 |
| A | 1 | Full deployment | −1,534,022 | −1,393,241 | −1,336,287 | −1,030,969 |
| A | 2 | Optimum | −237,769 | 1,326 | 98,053 | 616,591 |
| A | 2 | Full deployment | −449,916 | −210,821 | −114,094 | 404,444 |
| D | 1 | Optimum | −541,778 | −476,436 | −289,502 | −331,385 |
| D | 1 | Full deployment | −1,115,521 | −1,050,179 | −863,244 | −905,128 |
| D | 2 | Optimum | 45,761 | 158,107 | 479,513 | 407,501 |
| D | 2 | Full deployment | −138,069 | −25,723 | 295,684 | 223,671 |

*Cost range for Plant A (steam cogeneration): 21 (min) to 543.3 (max) COP/kWh, average 204.8
COP/kWh across 6 mills. Cost range for Plant D (biogas): 180 (min) to 465.1 (max) COP/kWh, average
306.3 COP/kWh across 7 mills. Both from Mosquera-Montoya et al. (2025), Cenipalma's 2024
sector-wide benchmarking of Colombian palm oil mills (see bibliography note: exact edition still
to be reconfirmed). Fully validated this session against the corrected model, including the EFB
opportunity cost: Plant A and Plant D's values at the "Current" price
point match Table 5 exactly for both scenarios. **Note on Plant D's current price**: at 0.153
USD/kWh (approximately 511 COP/kWh), Plant D's own measured cost falls above the maximum of the
Cenipalma benchmarking range (465.1 COP/kWh); since that range describes seven other mills'
biogas costs rather than Plant D's own installation specifically, this is not necessarily an
inconsistency, but simply indicates that Plant D's existing biogas infrastructure is costlier
than the sampled sector range. This should still be confirmed against the original field data
before submission, to rule out a transcription error, but is not treated as a data quality
problem by default. Unlike Plant A, no independent fraction of Plant D's price attributable to
biomass versus grid supply was available this session, so Plant D's range was converted from
COP/kWh using a simple exchange-rate conversion rather than the weighted formula used for Plant A;
this difference in methodology between the two plants should be reconciled or explicitly
documented before finalizing this table.*

**Figure 7 — Sensitivity range chart, net benefit for Plants A and D across the observed cost range**
(horizontal range bars, colored by scenario, with a marker for the current cost estimate and a
zero reference line; makes visually immediate which combinations are robust and which are
genuinely uncertain) — rendered and reviewed this session, ready to generate in the notebook

### 3.6 Environmental and social indicators

> Avoided emissions scale with deployment (Section 3.2), and the implicit cost of the last increment of deployment, from the economic optimum to full technical deployment, is USD 294 per tonne of CO2 for Scenario 1 and USD 599 per tonne for Scenario 2, as confirmed this session with a direct, non-cached recomputation of the full front for both scenarios.
>
> Rural electricity coverage exceeds the aggregate residential demand of the department's rural population from the economic optimum onward in both scenarios, a consequence of Magdalena's unusually low rural electricity consumption (Cabello Eras et al., 2022) rather than of an implausibly large surplus; this specific indicator has not yet been individually rechecked against today's corrections and should be treated as provisional, though the closely related non-saturating share of total departmental electricity demand (Section 2.7) has been confirmed via Figure 8c, since both depend on the same, largely unchanged exported surplus.
>
> Figure 8 summarizes three indicators together across the full Pareto front of each scenario, normalized to each scenario's own technical potential: net benefit, LCOE, and avoided emissions paired with departmental demand share on a shared panel with dual vertical axes, since both grow linearly with exported surplus for the same underlying reason. Net benefit (panel a) and LCOE (panel b) both show Scenario 1 in unfavorable territory across nearly its entire range, consistent with the narrow profitable window established in Section 3.2, while avoided emissions and departmental demand share (panel c) continue to grow linearly with deployment regardless of profitability, since they depend only on exported electricity, not on cost. This visually separates the two questions the study asks: how much of the potential is worth capturing privately, and how much of it exists physically, which only coincide for Scenario 2.

**Figure 8 — Sustainability indicators across the full Pareto front, Scenario 1 vs. Scenario 2**
(three panels: net benefit, LCOE, and avoided emissions paired with departmental demand share on
a dual-axis panel, each plotted against percent of each scenario's own technical potential, with a
star marking each scenario's private optimum) — **FINAL, generated and validated this session
against the fully corrected model (LCOE at the economic optimum confirmed 0.1488/0.0576 USD/kWh,
matching Section 3.2 exactly)**
- **Caption**: Net benefit (a), LCOE (b), and avoided emissions paired with departmental demand
  share (c) across the full Pareto front of each scenario, as a share of each scenario's own
  technical potential. Stars mark the private optimum of each scenario.

### 3.7 Policy instrument sensitivity (results for the method described in Section 2.9)

> The two policy instruments available to Colombian regulators no longer tell the same story once conversion losses and the EFB opportunity cost are properly priced. Scenario 2 remains profitable at every incentive level and at both the economic optimum and full deployment, requiring no capital support at all. Scenario 1 does not: at full deployment with no capital incentive, its net benefit is negative (Table 8), consistent with the aggregate finding of Section 3.2. Even a capital cost reduction of 30%, at the upper end of what is available under current tax incentives for non-conventional renewable sources (Section 2.5), is not enough to restore profitability at full deployment for Scenario 1, though it comes close (−USD 697,660 per year at 30%, against −USD 6,531,746 at 0%). Scenario 2 remains ahead of Scenario 1 at every incentive level tested, but the gap narrows as the incentive rises.

**Table 8 — Capital incentive sensitivity**

| Incentive | Scenario | Net benefit at economic optimum (USD/yr) | Net benefit at full deployment (USD/yr) |
|---|---|---|---|
| 0% | 1 | 258,705 | −6,531,746 |
| 0% | 2 | 3,427,932 | 2,315,672 |
| 10% | 1 | 958,500 | −4,587,051 |
| 10% | 2 | 4,115,171 | 3,134,918 |
| 19% | 1 | 1,588,315 | −2,836,825 |
| 19% | 2 | 4,733,687 | 3,872,240 |
| 30% | 1 | 2,358,090 | −697,660 |
| 30% | 2 | 5,489,650 | 4,773,412 |

*Fully validated this session against the corrected model (0% row matches Table 5 exactly for
both scenarios). Notably, Scenario 1's economic optimum stays fixed at 67.0 GWh/yr (32.2% of its
own technical potential) across every incentive level tested: the capital incentive raises the
profitability of that same deployment level rather than shifting where the peak occurs. What does
grow with the incentive is the breakeven deployment level, the furthest point along the front that
remains profitable at that incentive: 35.4% of potential at 0% incentive, 50.6% at 10%, 75.7% at
19%, and 96.4% at 30%, still short of full deployment even at the highest incentive level tested.
Scenario 2's own optimum stays close to its technical ceiling (92.3% of potential) across the
entire incentive range, since it was already close to full deployment at 0%.*

> The response to the spot market price tells a related story from the demand side, and confirms the capital-incentive finding from another angle: at the current price, Scenario 1's private optimum falls far short of full deployment (32.2%), while Scenario 2's optimum is already close to it (92.3%). Scenario 1 requires the spot price to rise to USD 0.105/kWh, about 49% above the current price, before forced full deployment stops losing money; within the full range tested (up to USD 0.25/kWh, more than three times the current price), Scenario 1's freely chosen deployment plateaus at 96.1% and never reaches 100%, so the incentive-compatible feed-in tariff (the price at which the mill would freely choose full deployment) lies above USD 0.25/kWh and was not identified within this study's tested range. Scenario 2 needs no price support at all: full deployment is already profitable at the current price, and the mill's own optimum tracks close to its technical ceiling throughout the range tested.

**Table 9 — Deployment freely chosen at each spot market price**

| Spot price (USD/kWh) | Scenario 1, share of exportable potential | Scenario 2, share of exportable potential |
|---|---|---|
| 0.07 (current) | 32.2% | 92.3% |
| 0.10 | 64.0% | 92.3% |
| 0.13 | 88.0% | 93.8% |
| 0.16 | 96.1% | 98.1% |
| 0.20 | 96.1% | 98.5% |
| 0.25 | 96.1% | 98.9% |

*Confirmed this session against the fully corrected model (joint self-consumption/energy-credit
cap, corrected metered demand, reconstructed fiber/shell opportunity cost, and the validated EFB
opportunity cost). Scenario 1's breakeven feed-in tariff (the price at which forced full
deployment stops losing money) is USD 0.105/kWh, up from an earlier draft's USD 0.080/kWh; its
incentive-compatible feed-in tariff (the price at which the mill freely chooses full deployment)
was not reached within the USD 0.07 to 0.25/kWh range tested, since freely chosen deployment
plateaus at 96.1% from USD 0.16/kWh onward. Scenario 2 needs no feed-in tariff: it is already
profitable at full deployment at the current price (Section 3.2), and its own optimum stays
within a few points of its technical ceiling across the entire range tested. Full one cent
increment table in Appendix.*

---

## 4. Discussion

### 4.1 Reframing the policy question, and quantifying the privately-optimal-vs-full-deployment gap

> The central practical question this study set out to answer was not whether biomass valorization is profitable, since it demonstrably is at the private optimum of both routes, but which of two mature, already partially adopted pathways policy should favor, and for whom. Neither route dominates outright. Scenario 2 is more profitable, more robust to a falling spot price, and viable at more mills; Scenario 1 avoids substantially more emissions in absolute terms, since its technical potential is larger. This trade-off, not a subsidy gap, is the more useful frame for policy attention.
>
> A second, related tension runs through the results: at current prices, neither scenario's private optimum reaches full technical deployment (32.2% for Scenario 1, 92.3% for Scenario 2). For Scenario 1, that gap is wider than it first appears, since profitability turns negative almost immediately past the optimum rather than only near full deployment. Closing the gap costs USD 294 per additional tonne of CO2 avoided for Scenario 1 and USD 599 for Scenario 2 (Section 3.2), in each case the forgone private profitability of pushing deployment beyond what a rational investor would choose. This connects to Section 3.7's capital incentive and feed-in tariff findings: even a 30% capital cost reduction, at the upper end of what current tax incentives make available, is not enough to make full deployment profitable for Scenario 1, though it substantially narrows the gap; within the price range tested, no feed-in tariff level was identified at which Scenario 1 would freely choose full deployment either. Scenario 2 needs neither instrument.

### 4.2 Profitability disparities across mills

> Aggregate profitability, on its own, obscures how unevenly it is distributed, and in the case of Scenario 1, it obscures that no mill is actually profitable at full deployment once the full set of opportunity costs is priced correctly. The two largest, highest-utilization mills, B and C, come closest to breaking even, and would likely be the first candidates for any partial or phased deployment strategy, but even they are negative at full deployment under Scenario 1. Scenario 2 is far more broadly viable, with four of six mills profitable at full deployment; only Plant F is unviable under either technology route, and Plant A, despite already partially self-generating, turns negative under Scenario 2 specifically at full deployment, a reversal examined further in Section 4.3. This pattern is invisible in departmental-aggregate assessments, which report only the sector-wide total, and is one of this study's central contributions: profitability at the plant level depends on operating hours at least as much as on technology choice, since a mill running under 2,000 hours a year, like Plant F, cannot generate enough surplus to cover the fixed costs of either pathway.
>
> The policy implication follows directly, and is sharper than an aggregate view suggests. A uniform subsidy or feed-in tariff, sized to the sector average, would understate what Scenario 1 actually needs to become viable at any mill, and would overcompensate the mills that are already profitable under Scenario 2. Plant F, specifically, is not a pricing problem that a higher tariff would solve; it is a scale problem, better addressed through the kind of centralized, shared infrastructure discussed under future work, than through instruments that treat all six mills as interchangeable.

*Framing note (not for the manuscript): presented throughout as an empirical disparity finding,
not as an energy-equity or energy-justice analysis, since no such theoretical framework is
developed in this study (see style rules above).*

### 4.3 Existing infrastructure changes the investment calculus

> A more counterintuitive finding concerns the two mills that already partially self-generate. Because the model prices new investment against each mill's own avoided cost, cheaper existing infrastructure reduces, rather than strengthens, the marginal case for expanding it: a mill that already captures the low-cost part of its own energy needs has less headroom left to gain from investing further. This is visible in Section 3.5's sensitivity analysis, and it is sharper than an earlier round of this analysis suggested: once the EFB opportunity cost is properly priced, Plant A is unprofitable across its *entire* empirically observed cost range under Scenario 1, not just for most of it, and Plant D fares only marginally better, also unprofitable throughout under that scenario. Under Scenario 2, Plant D remains profitable across its entire range, but Plant A is profitable only from roughly the average reported cost upward, turning negative at the low end; Plant A's negative result at full deployment under Scenario 2 at the current price (Table 5) is therefore not an isolated result but part of a broader pattern across much of its plausible cost range.
>
> This is a mechanism that a study using a single reference grid price for all mills, rather than each mill's own measured energy matrix, would not surface at all. It is also a caution against treating existing self-generation as a straightforward advantage: for the marginal investment decision this study models, it can just as easily be the opposite, and Plant A illustrates that this can hold even under the more broadly favorable Scenario 2, not only under Scenario 1.

### 4.4 Carbon tax inadequacy, robustly confirmed

> Colombia's carbon tax, at its currently verified rate of USD 8.70 per tonne of CO2 (DIAN Resolution 000003 of 2026), covers only a small fraction of the implicit cost of closing the gap between private and full deployment: about one thirty-fourth of that cost for Scenario 1 and one sixty-ninth for Scenario 2. This gap is robust to the corrections applied throughout this study; if anything, it widened further with today's validated model, since Scenario 1's implicit abatement cost rose from USD 169 to USD 294 per tonne. On the tax alone, there is little reason to expect it to move deployment meaningfully beyond the private optimum. **[Memari et al. (2018) compare a carbon tax against a cap-and-trade scheme within an MILP model of a Malaysian palm biomass supply chain and could be a useful comparandum here, but their specific finding on which instrument moves deployment more was not confirmed this session and should be checked directly before citing a result, not just the comparison itself.]**
>
> A second, unmodeled channel may matter more. Colombian regulation allows entities liable for the carbon tax to offset up to half of it by purchasing and retiring carbon credits from verified domestic emission-reduction projects, a mechanism that creates demand for credits independent of the tax rate itself. A biomass valorization project that displaces grid electricity is exactly the kind of project that could generate credits sellable into that market, an income stream this study's model does not represent, since it credits avoided emissions physically rather than monetarily. Quantifying that channel would require assumptions about credit pricing and market access beyond this study's scope, but it is a more promising avenue than the tax rate itself for closing Scenario 1's marginal gap, and is flagged here as unexplored policy space rather than modeled. A pending tax reform bill proposes raising the tax rate itself to COP 42,609/tCO2; this is not yet in force and should be noted as a limitation if it advances before submission.

### 4.5 Limitations

> This study's results depend on modeling assumptions that are standard for a techno-economic pre-feasibility analysis but are not measured at each of the six plants individually. Turbine and biogas generator conversion efficiencies, reducing gross output by about 20% and 6% respectively, are taken from manufacturer catalogs and published references rather than measured on site; these efficiencies were central to this study's main finding once properly applied (Section 2.6 to 2.7), and a plant whose equipment performs differently would see its own profitability shift accordingly, particularly under Scenario 1, where the turbine's larger loss makes it the more sensitive route. A related point: because conversion losses separate gross generation from net exportable electricity, the two are easily conflated in similar studies that report gross figures without noting the difference; this study tracks net, exported electricity throughout. A further source of variation this study does not capture is biomass composition itself: fiber, shell, and effluent characteristics vary with fruit ripeness, season, and milling practice, all of which affect the actual thermal and biogas potential of a given tonne of biomass, in ways the fixed reference values used here cannot represent.
>
> Operating and maintenance costs are modeled as a fixed 2.5% of installed capital cost across all equipment, when actual O&M varies by technology and manufacturer. Biogas generation under both scenarios, including EFB co-digestion under Scenario 2, uses published digestion parameters and a conceptual design reference (Voogt et al., 2021) rather than plant-level performance data, since none of the six mills currently operates that configuration. The turbine catalog itself is discretized into standard sizes rather than continuously sized, which is why several points along the Pareto front collapse onto the same capacity choice (Section 3.2 to 3.7); and both CAPEX and market prices are held static over the project's economic life, without a technology cost-decline curve or price escalation. Together, these assumptions make the reported figures a defensible approximation under current best-available parameters, not a precise prediction; a mill considering this investment would still need its own equipment quotes and site data.
>
> The empty fruit bunch opportunity cost (Section 2.6) carries a similar caveat. It rests on two literature-based parameters rather than site measurement: nutrient equivalence factors for the fertilizer value of EFB (Caliman et al., 2001) and a 70% mineralization efficiency drawn from a 60 to 80% range reported for field-scale EFB decomposition elsewhere. Actual nutrient release depends on local soil type, rainfall, and application practice, none of which is specific to the six mills studied here, so the true opportunity cost at any given mill could differ from the value used. Because this cost was found to materially affect plant-level profitability (Section 3.3, 3.5), it is one of the more consequential simplifications in this study and a natural target for refinement with local agronomic data.
>
> Two further limitations concern scope. Scenario 2's economic optimum and technical maximum lie close together, which could reflect a genuine cost advantage of co-digestion or unmodeled scale constraints on biogas capacity; distinguishing between the two would require testing a wider range of module sizes. The rural demand baseline behind the social indicator, while externally validated (Section 2.7), reflects Magdalena's unusually low rural consumption and should not be generalized without recalculating it for other departments.
>
> Finally, the avoided-emissions indicator used throughout, including Figure 8c, credits only grid displacement; it does not net out non-CO2 process emissions from biomass and biogas combustion or diesel backup, which are computed elsewhere but only at full deployment. An approximate scaling suggests this overstates avoided emissions by roughly 10 to 12% at the economic optimum and 17 to 21% at full deployment, growing with deployment under Scenario 1 as more turbine use burns more solid biomass. This does not change the comparison between scenarios, but the absolute figures reported should be read as an upper bound.

### 4.6 Bioenergy generation as a discretionary business decision, separate from the core business

> The tension this study documents, between what is privately optimal and what is technically and environmentally optimal, is easiest to understand once bioenergy generation is placed correctly within a mill's overall business. Committing capital to on site power generation is a secondary line of business for a palm oil extraction plant, entirely separate from its core activity of producing crude palm oil, and it carries a distinct set of risks: electricity market prices, regulatory conditions governing self generation and surplus exchange, and technology specific costs that have nothing to do with the mill's primary operations.
>
> This framing explains, causally, why the robustness findings of Sections 3.4 and 3.7 matter as much as the headline profitability figures. An investor evaluating an unfamiliar line of business should reasonably weight downside price scenarios more heavily than they would for a marginal expansion of a familiar one, since there is no existing operational buffer to absorb a bad year. Scenario 2's advantage, then, is not only that it is more profitable at the private optimum; it is that it asks less of an investor already uncertain about a business they do not otherwise run.

---

## 5. Conclusions

> This study finds that both mature cogeneration pathways for palm oil mill residues are profitable at their own economic optimum, but that profitability alone is an incomplete basis for choosing between them. Scenario 2, a backpressure turbine paired with biogas from co-digested effluent and empty fruit bunches, remains profitable across its entire technical range and requires no external support to reach full deployment. Scenario 1, an extraction condensation turbine paired with POME biogas, is profitable only in a narrow window close to its own optimum, at 32.2% of its technical potential; profitability turns negative almost immediately beyond that point and falls substantially further toward full deployment, where even a 30% capital cost reduction, at the upper end of what current tax incentives make available, is not enough to restore profitability.
>
> This divergence reframes the policy question. Rather than asking how much subsidy either route requires, given that Scenario 2 requires none, the more useful question is which route to favor, and the answer depends on what is weighed most heavily: Scenario 2 is more profitable, more robust to a falling electricity price, and viable at more mills, while Scenario 1 avoids substantially more emissions in absolute terms because its technical potential is larger. Neither route dominates the other outright.
>
> Plant level results sharpen this picture further: at full deployment, none of the six mills remain profitable under Scenario 1, against four of six under Scenario 2, and even mills that already partially self-generate are not spared, turning negative under one or both scenarios once the full set of opportunity costs, including the value of empty fruit bunches as a soil amendment, is properly priced. Colombia's current carbon tax covers only a small fraction of the cost of closing the gap between the private optimum and full deployment for either scenario, about one thirty-fourth for Scenario 1 and one sixty-ninth for Scenario 2, indicating that carbon pricing alone is unlikely to move deployment meaningfully beyond what mills would choose on their own.

## Future work

> Two extensions follow directly from these findings. The smallest and lowest-utilization mills, unprofitable under either scenario at full deployment, appear to face a scale problem rather than a pricing one; a centralized biomass processing hub serving several extraction plants is now a regulatory possibility in Colombia under CREG Resolution 101-99 of 2026, which allows a generator to supply users at different connection points, provided they share economic linkage, an arrangement well suited to plants under common ownership. Testing whether shared infrastructure changes the smaller mills' investment case in a way plant-level analysis cannot capture is a natural next step. Separately, Plant A's sensitivity to its own existing cogeneration cost was tested only at the full deployment point in this study; extending that sensitivity analysis across the full Pareto front would confirm whether the same conclusion holds at intermediate deployment levels.

---

## Open items before finalizing text (do not block outline, but flag before submission)
1. ~~Plant A cogeneration cost — confirm sensitivity-range framing survives Section 25 re-optimization~~ **RESOLVED**: full re-optimization at all 4 price points confirms Plant A's optimal capacity (300 kW turbine, 2,000 kW biogas) is unchanged across the entire cost range; the fixed-capacity approximation in Table 7 is exact, validated within 0.01%
2. ~~Numbering collision between old (pre-correction) and new notes sections~~ **RESOLVED**: cross-checked against the user's own `Notas_metodologicas_articulo.md`, `Notas_ADENDA_correcciones.md`, and `Estado_proyecto_continuidad.md`; everything still valid from those documents (CAPEX six-tenths rule, POME via Rahayu, opportunity cost, Pareto discretization gaps, rural coverage denominator, Plant A cost range) is already correctly incorporated, and everything invalidated by this session's bruta-to-neta correction has already been replaced in this outline
3. ~~Section 21 (capital incentive sensitivity) fix pasted into notebook this session but not yet re-run/confirmed by user~~ **RESOLVED**: re-run and validated this session, 0% row reproduces §19b exactly (Table 8)

---

## Section → Notebook cross-reference (for internal use, not for the manuscript)
| Article section | Notebook section(s) | Notes §§ |
|---|---|---|
| 3.1 Deployment relative to baseline | 19, 19bis, 20 (punto 0 per-plant generation) | df_pareto_plantas / df_pareto_plantas_e2, punto 0 |
| 3.2 Aggregate Pareto front | 19, 19bis, 19c, 20 | continuity doc "RESULTADOS DEFINITIVOS" |
| 3.3 Plant disaggregation | 23 (new) | §50 |
| 3.4 Robustness | 24 (new), barrido_fit (corrected) | §51, §51.1 |
| 3.5 Technology-upgrade sensitivity | 25 (to run) | §52 |
| 3.6 Environmental/social | balance_emisiones_esc1/2, viviendas_rurales_beneficiadas | §53, §54 |
| 3.7 Policy instrument sensitivity | correr_frente (corrected), barrido_fit (corrected) | §21, §51/§51.1 |
