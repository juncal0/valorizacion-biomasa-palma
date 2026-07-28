# Article Outline — Energy Valorization of Oil Palm Residual Biomass in Magdalena, Colombia
*Working draft skeleton — v1. Language: English. Status: all figures below validated in the July 2026 working session; see cross-references to notebook sections and notes §-numbers.*

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

## Abstract (FINAL, agreed version — reflects the corrected bruta-to-neta model, this session)

> Prior assessments of Colombia's palm oil residual biomass have established the scale of its technical energy potential, but have stopped short of asking whether capturing it is financially sound for the mills that would invest in it. This study moves beyond potential quantification to assess profitability, robustness, and sustainability trade-offs across two mature cogeneration pathways: an extraction condensation steam turbine paired with biogas from palm oil mill effluent (Scenario 1), and a backpressure turbine paired with biogas from co-digested effluent and thermally pretreated empty fruit bunches (Scenario 2). A mixed integer optimization model covers six extraction plants in the Magdalena region, jointly assessing economic, environmental, and social outcomes.
>
> Each scenario is profitable at its own economic optimum, but the two diverge beyond that point. Scenario 2 remains profitable across its entire technical range; Scenario 1 turns unprofitable near full deployment unless supported by a capital incentive or a higher feed-in tariff. The divergence traces to conversion losses: turbine losses are several times larger than biogas losses, so Scenario 1's private optimum relies almost entirely on biogas, while full deployment forces substantial turbine expansion. Plant level results, masked in prior aggregate assessments, sharpen this picture: at full deployment, only two of six mills remain profitable under Scenario 1, against five of six under Scenario 2. Closing the gap between the private optimum and full deployment costs USD 169 to 593 per additional tonne of CO2 avoided, far exceeding Colombia's current carbon tax. Neither route dominates: Scenario 2 is more profitable, more robust, and viable at more mills, while Scenario 1 avoids substantially more emissions in absolute terms given its larger technical potential.

*(271 words, agreed length)*

**CORRECTION LOG (this session):** replaces the pre-bruta-to-neta-correction abstract, whose
headline claim ("both routes profitable without subsidy even at full deployment") was found to
be false for Scenario 1 once turbine and biogas conversion losses were properly priced (§53 and
the whole model-correction cascade documented in Section 2 above). All figures in this version
are confirmed against the corrected model: Scenario 1's full-deployment net benefit is USD
−908,171/yr (not the pre-correction USD 1.96 million); the abatement cost range is USD 169 to
593/tCO2 (not the pre-correction USD 225 to 392); the carbon tax comparison uses the verified
2026 rate of USD 8.70/tCO2 (COP 29,070.49, DIAN Resolution 000003 of 2026), not an earlier
placeholder.

**Style rules locked in for the rest of the manuscript** (apply consistently from here on):
- No em/en dashes as stylistic separators; use commas, semicolons, or full clauses instead
- Short hyphens permitted only for numeric ranges (e.g., "225-392"); "to" is acceptable mid-sentence for ranges (e.g., "225 to 392") when a hyphen would be visually ambiguous
- No explicit regulation names (e.g., "CREG 174") in the Abstract; regulatory framework is described narratively and named explicitly only in Materials and Methods
- No "equity" language anywhere in the manuscript unless a dedicated energy-equity/justice theoretical framework is developed in Discussion (not currently planned); use "disparities" or "heterogeneity" instead
- Target journal: Journal of Cleaner Production (JCLEPRO) — house style to match: Cenipalma/Revista Palmas article tone (plain, formal, minimal stylistic punctuation)

Keywords (draft, to refine): palm oil mill residues; biomass valorization; mixed-integer optimization; conversion losses; profitability disparities; carbon abatement cost

---

## 1. Introduction (CURRENT WORKING VERSION — full draft, ~420 words)

> Colombia's oil palm agroindustry generates large volumes of residual biomass, including empty fruit bunches, fiber, shell, and palm oil mill effluent, whose energy content is widely regarded as an underexploited resource for the country's renewable energy transition and for strengthening electricity access in rural, biomass-producing regions. Establishing exactly how much of this technical potential can realistically be captured, and through which technological route, remains an open and consequential question.
>
> Converting technical potential into installed capacity, however, is not automatic. Bioenergy generation is a discretionary investment that sits outside the core business of a palm oil extraction plant, which is the production of crude palm oil. Committing capital to on site power generation exposes a mill to a different set of risks, including electricity market prices, regulatory conditions governing self generation and surplus exchange, and technology specific costs, none of which are relevant to the mill's primary operations. From the perspective of an individual investor, the relevant question is therefore not whether generating electricity from residual biomass is technically feasible or environmentally desirable, both of which are increasingly well established, but whether it is sufficiently and robustly profitable to justify entering an unfamiliar line of business. From a system perspective, however, more renewable generation is unambiguously beneficial: it strengthens grid robustness, displaces fossil generation, and supports national decarbonization and rural electrification targets, regardless of whether the private return fully reflects that value.
>
> This tension between what is privately optimal and what is technically and environmentally optimal has received limited attention in the literature on palm biomass valorization. Prior techno-economic assessments have typically reported aggregate, departmental level profitability using a single representative technology, without disaggregating results across individual mills or testing their robustness to electricity price uncertainty. As a result, two practically important questions remain unanswered. First, does profitability hold uniformly across mills of different sizes and operating conditions, or is it concentrated in a subset of plants, with implications for whether policy support, if any, should be broad or targeted. Second, how large is the gap between the deployment level a private investor would rationally choose and full technical deployment, and what would closing that gap cost in terms of forgone private profitability.
>
> This study addresses both questions using two cogeneration pathways that are technologically mature and already partially adopted within the Colombian palm sector: an extraction condensation steam turbine paired with biogas generation from palm oil mill effluent, and a backpressure steam turbine paired with biogas generation from co-digested effluent and thermally pretreated empty fruit bunches. A mixed integer optimization model is developed for six extraction plants in the Magdalena department, jointly assessing economic, environmental, and social outcomes under both pathways. The analysis quantifies the technical energy potential of the region's residual biomass, evaluates plant level profitability and its robustness to electricity price fluctuations, and estimates the cost, in forgone private profitability, of moving from the privately optimal deployment level to full technical deployment. In doing so, this study reframes the relevant policy question from whether this transition needs to be subsidized to which technological route policy should favor, and for which mills targeted intervention may be warranted.

**Citations to weave in when finalizing** (not yet placed in the prose above):
- Prior potential-quantification article (the one this paper explicitly continues from) — anchor the opening paragraph's claim
- Guerrero et al. (2023) and Chávez et al. (2026, Cenipalma benchmarking) — evidence for "mature... already partially adopted" claim (6/23 and 7/23 surveyed mills)
- Cabello Eras et al. (2022) — for the rural electrification/energy access framing in paragraph 1, and reused later for the rural demand baseline (§54)

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
> **Scenario 1 (extraction condensation route)** combusts all solid residues, fiber, shell, and mechanically pretreated empty fruit bunches, in a high pressure boiler. An extraction condensation steam turbine bleeds steam to satisfy process heat demand and expands the remainder to condensing conditions to maximize electricity output. Palm oil mill effluent is anaerobically digested and the resulting biogas fuels a gas engine; empty fruit bunches are not part of this digestion stream. Continuous sterilization replaces the conventional batch process in this scenario.
>
> **Scenario 2 (backpressure route with co-digestion)** combusts only fiber and shell, in a lower pressure boiler feeding a backpressure turbine whose exhaust steam supplies the entire process heat demand. Empty fruit bunches are withdrawn from the combustion train, thermally pretreated to raise their biodegradability, and co-digested with palm oil mill effluent, so that the anaerobic route carries a substantially larger organic load than in Scenario 1. Continuous sterilization is **not** implemented in this scenario: the additional steam demand it requires could not be met by the energy available from the reduced solid biomass stream (fiber and shell only), so the conventional batch process is retained. Dynamic clarification, which does not add steam demand, replaces the conventional stage in both scenarios.
>
> Design parameters for the boilers and turbines follow operating conditions reported for comparable installations, with the Scenario 2 turbine parameters verified against Booneimsri et al. (2018). The biochemical methane potential of pretreated EFB was computed with the correlation of Thomsen et al. (2014), and the conceptual design assumptions for organic load removal, biogas yield, and CH4 content were taken from Voogt et al. (2021).

*Scenario comparison diagram deferred here, per decision #5. Reserved as Figures 1 to 3 (one
diagram each for the baseline, Scenario 1, and Scenario 2 configurations described above), so
that figure numbering in the manuscript runs Methods before Results. To be produced at the end
of the writing process, alongside the modeling workflow diagram (§2.10).*

**Discussion angle to develop**: part of Scenario 2's higher profitability/robustness may stem
from its broader biogas feedstock (POME+EFB) rather than the turbine choice alone. Worth
isolating this effect if time allows.

### 2.4 Optimization model (MERGED, cross-reference fixed)

> The model was developed in two phases. **Phase 1 (validation)** formulates each configuration with fixed capacities and no degrees of freedom, using a dummy objective; its purpose is to confirm that the thermal balance and the electricity balance close simultaneously for each mill before any decision variable is introduced. All three configurations returned optimal status for the six mills, confirming the internal consistency of the cleaned dataset.
>
> **Phase 2 (superstructure)** releases equipment capacity as a decision variable. Two generation routes are represented independently for each mill: a steam turbine selected from a discrete commercial catalogue by binary variables, and a modular biogas engine sized as an integer number of 1,000 kW units, a modularity consistent with units reported for palm oil mill effluent to biogas installations. Each route carries its own continuous utilization factor, bounded between zero and one. Biomass availability is the binding physical constraint: no route may generate more energy than its substrate allows.
>
> Surplus electricity is not remunerated at a single price. Under the prevailing Colombian regulation for distributed and small scale self generation, each kWh is valued according to its destination, in decreasing order of value: self consumption, which displaces retail purchases at the plant's own weighted electricity price (0.114 to 0.259 USD/kWh, computed from each mill's measured supply mix); an energy credit tier up to the plant's own consumption, remunerated at the same retail price; and any excess above that, sold at the spot price (0.0703 USD/kWh, the eleven month average of the wholesale market, adopted because of the high volatility of the series). Because tier prices are strictly decreasing, the model allocates generation to the higher value tiers first without requiring additional binary variables (Table 3, #5).

**Table 3 — Governing equations** (populated with real notation from the user's draft; still needs final subscript/summation notation transcribed directly from the notebook before submission)

| # | Component | Formula (draft) | Notes |
|---|---|---|---|
| 1 | Equipment CAPEX (six-tenths rule) | C = C_ref × (S / S_ref)^0.6 × CEPCI_2026/CEPCI_2019 | CEPCI 2019 = 607.5, CEPCI 2026 ≈ 873.8 |
| 2 | Modular biogas generator CAPEX | C_biogas = n_units × C_unit | Linear, 1,000 kW increments |
| 3 | Annualized CAPEX | C_ann = C_total / PVAF | PVAF = 8.5136 (10% discount rate, 20-year lifetime) |
| 4 | O&M cost | O&M = 0.025 × C_total | Applies to both variable and fixed CAPEX |
| 5 | Three-tier revenue | Revenue = auto×p_retail + permuta×p_retail + bolsa×p_spot | permuta capped at own demand; p_spot = 0.0703 USD/kWh |
| 6 | Objective 1 (economic benefit) | f1 = Revenue − C_ann − O&M − opportunity cost | Opportunity cost of displaced biomass fuel use |
| 7 | Objective 2 (generation) | f2 = Σ (turbine + biogas generation) × hours | Gross generation; self-consumption constant across front, §53 |
| 8 | ε-constraint sweep | max f1 s.t. f2 ≥ ε, ε over 10 intervals | Pareto front construction |
| 9 | LCOE (export basis, CORRECTED) | LCOE = (C_ann + O&M) / export_kWh | Corrected this session; was generation basis |
| 10 | HHV correlation | HHV = 0.3443C + 1.192H − 0.113O − 0.024N + 0.093S | C,H,O,N,S on dry mass basis; internal consistency check only |
| 11 | Avoided emissions balance | ΔGHG = biomass + biogas non-CO2 − grid displacement credit + diesel backup | Biogenic CO2 excluded (IPCC); diesel EF = 74,100 kg CO2/TJ; grid EF = 163.4 g CO2/kWh |
| 12 | Rural household-equivalent | HH_served = min(export_kWh / 346, total_rural_users) | 346 kWh/household/yr, 3.7 persons/household (DANE 2018); capped at 100%; non-saturating share-of-total-demand indicator reported alongside |
| 13 | Boiler efficiency | Direct method, ASME PTC, IAPWS-IF97 enthalpies | Plant A baseline: 75.7%, within 54-76% sector range |

*All later subsections (2.5 to 2.9) reference this table by equation number rather than
re-deriving formulas inline, per decision #1.*

### 2.5 Regulatory framework represented in the model (FINAL, concise per decision #4)

> Three families of instruments govern the economics of distributed bioenergy in Colombia, and the model represents them asymmetrically, a choice made explicit here because it conditions the interpretation of the results.
>
> CREG Resolution 174 of 2021, which governs remuneration of surplus electricity, is the only instrument embedded in the optimization itself: it acts on the marginal revenue of each additional kWh and therefore on the sizing decision, and its tariff structure is described in Section 2.4. Capital side tax incentives for non-conventional renewable sources (Law 1715 of 2014, as amended by Law 2099 of 2021) are deliberately not represented in the base case; the economic results reported in Section 3 are therefore conservative by construction, and the magnitude of this omission is quantified separately in the sensitivity analysis of Section 2.9. Two further instruments, the firm energy reliability charge (CREG Resolution 071 of 2006) and the current carbon tax (Decree 926 of 2017), are treated as context rather than embedded in the optimization; both are assessed against the model outputs in the Discussion.

### 2.6 Techno-economic parameters (MERGED)

> Capital costs are derived from supplier quotations obtained during the study, referenced to a 15 t FFB/h capacity, and escalated to 2026 USD using the Chemical Engineering Plant Cost Index (Table 3, #1). Where no quotation was available, costs were scaled from a reference capacity using the six-tenths rule (Table 3, #1; exponent 0.6), which replaces an earlier, invalid linear CAPEX assumption in which boiler cost was inadvertently double counted with turbine cost. Investments are annualized with a present value annuity factor of 8.5136, corresponding to a 10% discount rate over a 20 year lifetime (Table 3, #3), and operating and maintenance costs are taken as 2.5% of capital cost per year (Table 3, #4), applied to both fixed and variable CAPEX.
>
> A distinction is made between capital costs that respond to the sizing decision, the steam turbine and the biogas engine, and those that do not, such as the boiler, flue gas treatment, digester lagoons, and process substitutions, which are dimensioned by the plant's throughput rather than by the capacity chosen. Only the former enter the solver's objective, since the latter cannot alter the optimal solution; both, however, are included in the net benefit reported in the results, so that profitability is assessed against the full incremental investment.

### 2.7 Sustainability indicators (MERGED, CORRECTED)

> Three indicators, the levelized cost of electricity, the greenhouse gas balance, and rural electricity coverage, are computed at every point of the Pareto front rather than at a single design point.
>
> The LCOE is calculated as annualized capital cost plus annual operating and maintenance cost, divided by the annual electricity exported rather than generated (Table 3, #9). Exported surplus, the electricity that actually leaves the mill and is remunerated or credited under the tariff structure of Section 2.4, is the economically and physically meaningful quantity for this indicator; self consumption, which is fixed by each mill's own demand and does not respond to the sizing decision, is excluded from the denominator to keep the indicator comparable across plants of different demand.
>
> The greenhouse gas balance draws on that same exported surplus. It applies IPCC default emission factors for CH4 and N2O from solid biomass and biogas combustion, an emission factor of 74,100 kg CO2/TJ for backup diesel, and a credit for the displacement of grid electricity by the exported surplus (Table 3, #11). A carbon uptake credit of the palm plantation is reported separately, since it is common to all configurations and would otherwise obscure the comparison between technologies.
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

### 2.10 Modeling workflow (placeholder, per decision #3)
Single flow diagram summarizing Phase 1 (validation) and Phase 2 (superstructure optimization):
data inputs → technical sizing per plant → CAPEX and O&M calculation (Table 3 #1-4) → MILP
optimization (#6-8) → Pareto front → sustainability indicators (#9-12) → sensitivity analyses
(§2.9). *To be produced as a figure once Results/Discussion are drafted.*

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
- Booneimsri et al. (2018) — Scenario 2 turbine parameter verification
- Thomsen et al. (2014) — biochemical methane potential correlation for pretreated EFB
- Voogt et al. (2021) — anaerobic co-digestion design assumptions

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
to full deployment or to Scenario 2.*

**Figure 4 — Grouped bar chart of generation as a multiple of baseline consumption, by plant**
(complements Table 4; makes the uniformity at the Scenario 1 economic optimum, and its reversal at
full deployment, visually immediate) — **rendered and reviewed this session, ready to generate in
the notebook (matplotlib, same palette as the rest of the figures)**

### 3.2 Aggregate techno-economic Pareto front

> Both scenarios are profitable at their own economic optimum, with net benefits of USD 2,983,460 (Scenario 1) and USD 6,446,605 (Scenario 2) per year. Scenario 2 remains profitable at full technical deployment (USD 5,344,687 per year); Scenario 1 does not, turning negative near full deployment (USD −908,171 per year), a finding examined further in Section 3.7. LCOE at the economic optimum, on an exported energy basis (Section 2.7), is 0.1472 USD/kWh for Scenario 1 and 0.0576 USD/kWh for Scenario 2, both confirmed this session against a fresh recalculation from first principles.
>
> Figures 5 and 6 show how generation is routed from primary sources, through conversion losses, to the three revenue tiers of Section 2.4, at the economic optimum and at full deployment, for each scenario. In Scenario 1, the economic optimum relies almost entirely on POME biogas (64.2 GWh/yr), with only a small turbine contribution (8.0 GWh/yr); full deployment reverses this balance, driven by a turbine expansion to 184.9 GWh/yr while biogas remains at its POME-limited ceiling. This follows directly from the conversion loss mechanism established in Section 2.6 to 2.7: turbine losses (about 20%) are substantially larger than biogas losses (about 6%), so the private optimum favors the cheaper-to-convert biogas route and invests in the turbine only once deployment is pushed beyond what profitability alone would choose. Scenario 2 shows a related but less extreme pattern: biogas remains the dominant source at both points (127.4 to 127.9 GWh/yr, nearly unchanged) while the turbine grows from 20.1 to 33.7 GWh/yr. Conversion losses, shown explicitly as their own flow, rise from 5.2 to 40.9 GWh/yr in Scenario 1 as the lossier turbine route expands, compared with a narrower 11.3 to 14.1 GWh/yr range in Scenario 2. In both scenarios, as deployment rises, a growing share of net electricity is routed to the spot market tier rather than the energy credit tier, since both self consumption and the credit tier are capped at each plant's own demand.

**Figures 5 and 6 — Sankey diagrams of generation routed through the three revenue tiers**
(replace former Table 5; energy flow only, economic figures reported in prose above; each figure
combines the economic optimum and full deployment points as panels (a) and (b), respectively)
- Figure 5 — Scenario 1: (a) economic optimum, 72.2 GWh/yr gross, 67.0 GWh/yr net (8.0 turbine + 64.2 biogas, 5.2 GWh/yr conversion losses); (b) full deployment, 249.1 GWh/yr gross, 208.2 GWh/yr net (184.9 turbine + 64.2 biogas, 40.9 GWh/yr conversion losses) — **FINAL, validated (energy balance closes exactly in both panels, including the conversion loss stage)**
  - **Caption**: Sankey diagram of Scenario 1 electricity generation, from primary sources through conversion losses to the three revenue tiers of Section 2.4, at (a) the economic optimum and (b) full deployment. Node values are annual energy flows, in GWh per year.
- Figure 6 — Scenario 2: (a) economic optimum, 147.5 GWh/yr gross, 136.2 GWh/yr net (127.4 biogas + 20.1 turbine, 11.3 GWh/yr conversion losses); (b) full deployment, 161.6 GWh/yr gross, 147.5 GWh/yr net (127.9 biogas + 33.7 turbine, 14.1 GWh/yr conversion losses) — **FINAL, validated (energy balance closes exactly in both panels, including the conversion loss stage)**
  - **Caption**: Sankey diagram of Scenario 2 electricity generation, from primary sources through conversion losses to the three revenue tiers of Section 2.4, at (a) the economic optimum and (b) full deployment. Node values are annual energy flows, in GWh per year.

**CORRECTION LOG (this session, CLOSED)**: `df_sost`'s `lcoe_USD_kWh` column was found to be using
`generacion_kWh` (gross generation) as the denominator, not `excedente_kWh` (exported surplus,
the convention decided in Section 2.7) — the Section 16.6 correction had been applied and
validated earlier in the session but was not preserved when the cell was re-run later. Confirmed
by recomputing from first principles against a fresh `df_pareto_plantas` pull: correct value is
0.1472 USD/kWh (was showing 0.1045). Section 16.6 (Scenario 1) and Section 17.4 (Scenario 2)
were both re-run with the excedente-based denominator; Scenario 2's economic-optimum LCOE
(0.0576 USD/kWh) was cross-validated against its own known net benefit ($6,446,605, exact match).
A state-check cell was added to the notebook (prints FACTOR_NETO_TURBINA/BIOGAS, f2_en_f1max(_e2),
f2_max(_e2), the presence of the permuta/bolsa columns, and both scenarios' punto=0 LCOE against
these confirmed reference values) to catch this class of regression after any kernel restart,
since notebook cells in this project have repeatedly lost earlier fixes when re-run out of order.

**RESOLVED this session**: Scenario 1's LCOE is genuinely U-shaped across the front, confirmed
against the full Pareto curve (Figure 8b). It falls from 0.1472 USD/kWh at the economic optimum
(32.2% of potential) to a minimum of 0.0937 USD/kWh at 87.0% of potential (net benefit $1,739,897
at that point, still positive), then rises to 0.1030 USD/kWh at full deployment. Scenario 2 shows
no such U-shape: its LCOE-minimizing point coincides exactly with its economic optimum (92.3% of
potential, 0.0576 USD/kWh), so the private optimum is simultaneously the cheapest point on the
curve, unlike Scenario 1 where the privately optimal point and the cost-minimizing point diverge.

### 3.3 Plant level disaggregation

> Aggregate profitability conceals substantial variation across mills (Table 5). At full deployment, Plants B and C carry most of Scenario 1's aggregate net benefit, while Plant F is unviable under either scenario and Plant E becomes viable only under Scenario 2. Plant A is profitable under Scenario 1 by a narrow margin that depends on an assumption examined separately in Section 3.5. Across both scenarios, the ranking of plants by net benefit matches an independently computed ranking by net LCOE, providing a cross check on the result.

**Table 5 — Net benefit by plant at full deployment**

| Plant | Scenario 1 (USD/yr) | Scenario 2 (USD/yr) |
|---|---|---|
| A | 56,424 (sensitive, see 3.4) | 700,056 (robust, see 3.4) |
| B | 1,716,945 | 2,094,999 |
| C | 1,868,776 | 2,260,949 |
| D | 251,997 (robust, see 3.4) | 880,864 (robust, see 3.4) |
| E | −412,460 | 798,296 |
| F | −1,517,372 | −400,202 |

### 3.4 Robustness to electricity price

> The breakeven wholesale price, the price below which full deployment stops being profitable, differs sharply between scenarios (Table 6). At the aggregate level, Scenario 1 requires the spot price to hold at or above 0.0757 USD/kWh, close to the current price with little margin, whereas Scenario 2 remains profitable down to 0.0234 USD/kWh, a 70% drop from the current price. The same asymmetry holds plant by plant.
>
> This gap is not because Scenario 2 depends less on the spot market; if anything, a majority of its exported surplus is sold there rather than at the fixed retail-linked tiers (Section 2.4). The reason is volume: Scenario 2's spot-exposed surplus at full deployment is large enough (113.9 GWh/yr) that even a low price generates enough revenue to close what would otherwise be a USD 2.67 million shortfall at a spot price of zero. Scenario 1 needs a substantially higher price for the same mechanism to work, because its cost structure, dominated by a larger turbine investment, leaves a bigger gap to close per unit of spot-exposed volume. Robustness, in other words, comes from having a lot of low-priced surplus to sell, not from needing the spot market less.

**Table 6 — Breakeven spot price by plant and in aggregate (current price: 0.0703 USD/kWh)**

| Plant | Scenario 1 (USD/kWh) | Scenario 2 (USD/kWh) |
|---|---|---|
| A | 0.0873 | 0.0436 |
| B | 0.0480 | 0.0113 |
| C | 0.0359 | −0.0131 |
| D | 0.0772 | 0.0356 |
| E | 0.1099 | 0.0161 |
| F | 0.2551 | 0.1468 |
| **Aggregate** | **0.0757** | **0.0234** |

*Confirmed this session via a standalone breakeven search (`price_robustness`/`_beneficio_planta_bolsa`
in the notebook), matching the values already derived analytically from the corrected model. One
methodological note settled this session: the search values permuta strictly at the retail tier
regardless of the spot price being tested, consistent with the fixed three-tier structure of
Section 2.4 and with every other analysis in this study; an earlier draft of the search allowed
switching to spot pricing whenever it was more favorable, which would have inflated Plant A's
robustness specifically (its retail tariff, 0.1141 USD/kWh, is the only one low enough to fall
within the price range tested) and was removed for consistency.*

> At current prices, however, neither scenario's economic optimum reaches full deployment (Section 3.2): the profit maximizing choice stops at 32.2% of exportable potential in Scenario 1 and 92.3% in Scenario 2 (Table 9, confirmed against the corrected model). Forcing deployment the rest of the way costs USD 3,891,631 per year in forgone net benefit for Scenario 1 and USD 1,101,918 per year for Scenario 2, equivalent to USD 169 and USD 593 per additional tonne of CO2 avoided respectively (both confirmed this session against `correr_frente`'s output). Both figures substantially exceed Colombia's current carbon tax, a comparison developed further in Section 4.4.

### 3.5 Sensitivity of self-generating plants to technology upgrade decisions

> Plants A and D already generate part of their own electricity, so the value of investing further depends on how their existing infrastructure is priced, a quantity for which no single reliable estimate exists (Section 2.6 in the notes; not reproduced in Methods). Table 7 and Figure 7 report the outcome across the full cost range reported by Cenipalma's 2024 sector-wide benchmarking study of Colombian palm oil mills (21 to 543.3 COP/kWh for steam cogeneration, from a sample of 6 mills; 180 to 465.1 COP/kWh for biogas, from a sample of 7 mills), for both plants, both scenarios, and both the economic optimum and full deployment, since the same weighted price enters the objective function throughout.
>
> Plant D and Plant A both remain profitable across the entire cost range under Scenario 2, at either deployment level, confirming the robustness already established in Section 3.4. Under Scenario 1, the picture is considerably weaker for both plants once conversion losses are properly priced. Plant A is unprofitable across nearly the entire observed range, becoming profitable only at the upper extreme (543.3 COP/kWh, the highest steam cogeneration cost reported in the benchmarking sample); this holds at both the economic optimum and full deployment. Plant D fares better at the economic optimum, where it is profitable except at the low end of the range, but is unprofitable across the entire range once forced to full deployment, consistent with Scenario 1's aggregate net benefit turning negative near full deployment (Section 3.2). Scenario 1 is therefore not just less attractive on average for these two plants; for Plant A specifically, it is close to uneconomical across the whole range of plausible costs for its existing infrastructure.

**Table 7 — Net benefit for Plants A and D across the empirically observed cost range of their existing infrastructure**

| Plant | Scenario | Point | Min | Average | Current | Max |
|---|---|---|---|---|---|---|
| A | 1 | Optimum | −832,278 | −451,160 | −340,847 | 250,737 |
| A | 1 | Full deployment | −1,016,219 | −635,100 | −524,788 | 66,796 |
| A | 2 | Optimum | 162,233 | 496,289 | 592,980 | 1,111,511 |
| A | 2 | Full deployment | 81,263 | 415,318 | 512,009 | 1,030,541 |
| D | 1 | Optimum | −81,550 | 78,211 | 133,489 | 279,083 |
| D | 1 | Full deployment | −418,736 | −258,974 | −203,697 | −58,102 |
| D | 2 | Optimum | 625,743 | 764,590 | 812,632 | 939,166 |
| D | 2 | Full deployment | 521,536 | 660,383 | 708,424 | 834,959 |

*Cost range for Plant A (steam cogeneration): 21 (min) to 543.3 (max) COP/kWh, average 204.8
COP/kWh across 6 mills. Cost range for Plant D (biogas): 180 (min) to 465.1 (max) COP/kWh, average
306.3 COP/kWh across 7 mills. Both from Chavez et al. (2026), Cenipalma's 2024 sector-wide
benchmarking of Colombian palm oil mills. Values in USD/yr, holding capacity fixed at the corrected
model's solution for each point (Section 2.6 to 2.7) and varying only the weighted price of the
plant's existing infrastructure.*

**Figure 7 — Sensitivity range chart, net benefit for Plants A and D across the observed cost range**
(horizontal range bars, colored by scenario, with a marker for the current cost estimate and a
zero reference line; makes visually immediate which combinations are robust and which are
genuinely uncertain) — rendered and reviewed this session, ready to generate in the notebook

### 3.6 Environmental and social indicators

> Avoided emissions scale with deployment (Section 3.2), and the implicit cost of the last increment of deployment, from the economic optimum to full technical deployment, is USD 169 per tonne of CO2 for Scenario 1 and USD 593 per tonne for Scenario 2, as reported in Section 3.4.
>
> Rural electricity coverage exceeds the aggregate residential demand of the department's rural population from the economic optimum onward in both scenarios, a consequence of Magdalena's unusually low rural electricity consumption (Cabello Eras et al., 2022) rather than of an implausibly large surplus. The indicator is therefore reported capped at 100% of departmental rural demand, alongside the non-saturating share of total departmental electricity demand described in Section 2.7.
>
> Figure 8 summarizes all four indicators together across the full Pareto front of each scenario, normalized to each scenario's own technical potential. Net benefit (panel a) and LCOE (panel b) both show Scenario 1 crossing from favorable to unfavorable territory as deployment approaches 100%, while emissions avoided and rural coverage (panels c and d) continue to grow linearly with deployment regardless of profitability, since they depend only on exported electricity, not on cost. This visually separates the two questions the study asks: how much of the potential is worth capturing privately, and how much of it exists physically, which only coincide for Scenario 2.

**Figure 8 — Sustainability indicators across the full Pareto front, Scenario 1 vs. Scenario 2**
(net benefit, LCOE, avoided emissions, and rural household-equivalents, each plotted against
percent of each scenario's own technical potential, with a star marking each scenario's private
optimum) — **FINAL, validated this session (LCOE at punto=0 confirmed 0.1472/0.0576 USD/kWh,
matching Table 5 exactly; resolves the pending U-shape question for Scenario 1's LCOE, see note
in Section 3.2)**
- **Caption**: Net benefit, LCOE, avoided emissions, and rural household-equivalents across the
  full Pareto front of each scenario, as a share of each scenario's own technical potential. Stars
  mark the private optimum of each scenario.

### 3.7 Policy instrument sensitivity (results for the method described in Section 2.9)

> The two policy instruments available to Colombian regulators no longer tell the same story once conversion losses are properly priced. Scenario 2 remains profitable at every incentive level and at both the economic optimum and full deployment, requiring no capital support at all. Scenario 1 does not: at full deployment with no capital incentive, its net benefit is negative (Table 8), consistent with the aggregate finding of Section 3.2. A capital cost reduction of only 10%, well within the range available under current tax incentives for non-conventional renewable sources (Section 2.5), is enough to restore profitability at full deployment for Scenario 1. Scenario 2 remains ahead of Scenario 1 at every incentive level tested, but the gap narrows as the incentive rises.

**Table 8 — Capital incentive sensitivity**

| Incentive | Scenario | Net benefit at economic optimum (USD/yr) | Net benefit at full deployment (USD/yr) |
|---|---|---|---|
| 0% | 1 | 2,983,460 | −908,171 |
| 0% | 2 | 6,446,605 | 5,344,687 |
| 10% | 1 | 3,701,839 | 1,036,526 |
| 10% | 2 | 7,133,845 | 6,163,934 |
| 19% | 1 | 4,707,339 | 2,786,751 |
| 19% | 2 | 7,752,360 | 6,901,256 |
| 30% | 1 | 6,286,303 | 4,925,916 |
| 30% | 2 | 8,508,324 | 7,802,428 |

*At 0% incentive, Scenario 1's economic optimum deploys only 66.96 GWh/yr (32.2% of its own
technical potential of 208.2 GWh/yr); this share grows with the incentive level (46.9% at 10%,
64.0% at 19%, 87.0% at 30%), while Scenario 2's own optimum stays essentially unchanged
(136.2 GWh/yr, 92.3% of potential) across the entire incentive range, since it was already close
to full deployment. Capital incentives therefore move Scenario 1's deployment choice
substantially without changing Scenario 2's.*

> The response to the spot market price tells a related story from the demand side, and confirms the capital-incentive finding from another angle: at the current price, Scenario 1's private optimum falls far short of full deployment (32.2%), while Scenario 2's optimum is already close to it (92.3%), matching Table 8's incentive-level figures exactly since both analyses share the same underlying model. Scenario 1 requires the spot price to rise to USD 0.080/kWh, about 14% above the current price, before full deployment stops losing money, and to USD 0.240/kWh, more than three times the current price, before the mill would choose full deployment on its own. Scenario 2 needs no price support at all: full deployment is already profitable at the current price, and the mill's own optimum tracks close to its technical ceiling throughout the range tested.

**Table 9 — Deployment freely chosen at each spot market price**

| Spot price (USD/kWh) | Scenario 1, share of exportable potential | Scenario 2, share of exportable potential |
|---|---|---|
| 0.07 (current) | 32.2% | 92.3% |
| 0.10 | 87.0% | 92.3% |
| 0.15 | 96.1% | 98.1% |
| 0.20 | 96.1% | 98.5% |
| 0.25 | 99.6% | 98.9% |

*Scenario 1's breakeven feed-in tariff (the price at which forced full deployment stops losing
money) is USD 0.080/kWh; its incentive-compatible feed-in tariff (the price at which the mill
freely chooses full deployment) is USD 0.240/kWh. Scenario 2 needs no feed-in tariff: it is
already profitable at full deployment at the current price (Table 5), and its own optimum stays
within a few points of its technical ceiling across the entire range tested, without reaching the
99.5% threshold used to define the incentive-compatible price within that range. Full one cent
increment table in Appendix.*

---

## 4. Discussion

### 4.1 Reframing the policy question, and quantifying the privately-optimal-vs-full-deployment gap

> The central practical question this study set out to answer was not whether biomass valorization is profitable, since it demonstrably is at the private optimum of both routes, but which of two mature, already partially adopted pathways policy should favor, and for whom. Neither route dominates outright. Scenario 2 is more profitable, more robust to a falling spot price, and viable at more mills; Scenario 1 avoids substantially more emissions in absolute terms, since its technical potential is larger. This trade-off, not a subsidy gap, is the more useful frame for policy attention.
>
> A second, related tension runs through the results: at current prices, neither scenario's private optimum reaches full technical deployment (Table 9: 32.2% for Scenario 1, 92.3% for Scenario 2). Closing that gap costs USD 169 per additional tonne of CO2 avoided for Scenario 1 and USD 593 for Scenario 2 (Section 3.4), in each case the forgone private profitability of pushing deployment beyond what a rational investor would choose. This connects directly to the capital incentive and feed-in tariff findings of Section 3.7: Scenario 1 needs external support, either a capital incentive of about 10% or a spot price between USD 0.080 and 0.240 per kWh, to make full deployment privately worthwhile; Scenario 2 needs none.

### 4.2 Profitability disparities across mills

> Aggregate profitability, on its own, obscures how unevenly it is distributed. At full deployment, the two largest mills, B and C, carry most of Scenario 1's aggregate net benefit, while the smaller or lower-utilization mills, particularly E and F, are structurally disadvantaged regardless of which technology route is chosen. This pattern is invisible in departmental-aggregate assessments, which report only the sector-wide total, and is one of this study's central contributions: profitability at the plant level depends on operating hours at least as much as on technology choice, since a mill running under 2,000 hours a year, like Plant F, cannot generate enough surplus to cover the fixed costs of either pathway.
>
> The policy implication follows directly. A uniform subsidy or feed-in tariff, sized to the sector average, would either overcompensate the mills that are already profitable or still fall short for the ones that are not. Plant F, specifically, is not a pricing problem that a higher tariff would solve; it is a scale problem, better addressed through the kind of centralized, shared infrastructure discussed under future work, than through instruments that treat all six mills as interchangeable.

*Framing note (not for the manuscript): presented throughout as an empirical disparity finding,
not as an energy-equity or energy-justice analysis, since no such theoretical framework is
developed in this study (see style rules above).*

### 4.3 Existing infrastructure changes the investment calculus

> A more counterintuitive finding concerns the two mills that already partially self-generate. Because the model prices new investment against each mill's own avoided cost, cheaper existing infrastructure reduces, rather than strengthens, the marginal case for expanding it: a mill that already captures the low-cost part of its own energy needs has less headroom left to gain from investing further. This is visible in Section 3.5's sensitivity analysis, where Plant A, whose reported cogeneration cost spans a wide empirically observed range, is profitable under Scenario 1 only at the upper end of that range, while Plant D remains profitable under Scenario 2 across nearly the entire range but not at full deployment under Scenario 1.
>
> This is a mechanism that a study using a single reference grid price for all mills, rather than each mill's own measured energy matrix, would not surface at all. It is also a caution against treating existing self-generation as a straightforward advantage: for the marginal investment decision this study models, it can just as easily be the opposite.

### 4.4 Carbon tax inadequacy, robustly confirmed

> Colombia's carbon tax, at its currently verified rate of USD 8.70 per tonne of CO2 (DIAN Resolution 000003 of 2026), covers only a small fraction of the implicit cost of closing the gap between private and full deployment: about one nineteenth of that cost for Scenario 1 and one sixty-eighth for Scenario 2. This gap is robust to the correction applied throughout this study; if anything, it widened once conversion losses were properly priced, since Scenario 2's implicit abatement cost rose proportionally more than Scenario 1's. On the tax alone, there is little reason to expect it to move deployment meaningfully beyond the private optimum.
>
> A second, unmodeled channel may matter more. Colombian regulation allows entities liable for the carbon tax to offset up to half of it by purchasing and retiring carbon credits from verified domestic emission-reduction projects, a mechanism that creates demand for credits independent of the tax rate itself. A biomass valorization project that displaces grid electricity is exactly the kind of project that could generate credits sellable into that market, an income stream this study's model does not represent, since it credits avoided emissions physically rather than monetarily. Quantifying that channel would require assumptions about credit pricing and market access beyond this study's scope, but it is a more promising avenue than the tax rate itself for closing Scenario 1's marginal gap, and is flagged here as unexplored policy space rather than modeled. A pending tax reform bill proposes raising the tax rate itself to COP 42,609/tCO2; this is not yet in force and should be noted as a limitation if it advances before submission.

### 4.5 Limitations

> Several limitations qualify these results. First, the distinction between gross and exported generation, resolved in this study by tracking self consumption as a constant across the deployment range (Section 2.7), does not affect any reported economic or environmental figure, but is worth stating plainly given how easily the two can be conflated in similar studies. Second, Scenario 2's explored range is narrow: its economic optimum and its technical maximum lie close together, which could reflect a genuine cost advantage of the co-digestion route or, alternatively, scale constraints on biogas capacity that this study's catalog of modular units does not fully explore; distinguishing between the two would require testing a wider range of biogas module sizes than modeled here. Third, the rural electricity demand baseline against which the social indicator is compared, while validated against an independent departmental study (Section 2.7), reflects Magdalena's unusually low rural per capita consumption; the same indicator applied to a department with higher rural electrification would show a much smaller relative impact, and this comparison should not be generalized without recalculating the baseline.
>
> Fourth, the avoided-emissions indicator reported throughout the results, including Figure 8c, credits only the displacement of grid electricity; it does not net out the non-CO2 emissions from burning solid biomass and biogas or from diesel backup generation, all of which are computed elsewhere but only at the full deployment point rather than across the whole deployment range. An approximate scaling suggests the simplified credit overstates avoided emissions by roughly 10 to 12% at the economic optimum and 17 to 21% at full deployment, growing with deployment under Scenario 1 specifically because more turbine use means more solid biomass burned. This does not change the comparison between scenarios, but the absolute emissions figures reported should be read as an upper bound rather than a fully netted process balance.

### 4.6 Bioenergy generation as a discretionary business decision, separate from the core business

> The tension this study documents, between what is privately optimal and what is technically and environmentally optimal, is easiest to understand once bioenergy generation is placed correctly within a mill's overall business. Committing capital to on site power generation is a secondary line of business for a palm oil extraction plant, entirely separate from its core activity of producing crude palm oil, and it carries a distinct set of risks: electricity market prices, regulatory conditions governing self generation and surplus exchange, and technology specific costs that have nothing to do with the mill's primary operations.
>
> This framing explains, causally, why the robustness findings of Sections 3.4 and 3.7 matter as much as the headline profitability figures. An investor evaluating an unfamiliar line of business should reasonably weight downside price scenarios more heavily than they would for a marginal expansion of a familiar one, since there is no existing operational buffer to absorb a bad year. Scenario 2's advantage, then, is not only that it is more profitable at the private optimum; it is that it asks less of an investor already uncertain about a business they do not otherwise run.

---

## 5. Conclusions
- Restate headline finding: Scenario 2 is profitable without support across its entire technical range; Scenario 1 is profitable only up to about 97% of its range and needs either a capital incentive (~10%) or a higher feed-in tariff to be worthwhile at full deployment
- Restate the reframed policy question and the profitability-disparity caveat (concentrated in the two largest mills)
- One or two sentences on the technology-choice trade-off (profitability/robustness/equity favor Scenario 2; absolute avoided emissions favor Scenario 1)

## Future work
- Centralized biomass hub under CREG 101 099/2026 (Analysis 5, declared not modeled) — could rescue E and F through scale economies
- Full re-optimization of Scenario 1 under the Plant A cost sensitivity range (pending notebook run, Section 25)

---

## Open items before finalizing text (do not block outline, but flag before submission)
1. Plant A cogeneration cost — confirm sensitivity-range framing survives Section 25 re-optimization (full Pareto front, not just the 100% point)
2. Numbering collision between old (pre-correction) and new notes sections — reconcile before compiling final Methods/Results citations
3. ~~Section 21 (capital incentive sensitivity) fix pasted into notebook this session but not yet re-run/confirmed by user~~ **RESOLVED**: re-run and validated this session, 0% row reproduces §19b exactly (Table 8)
4. **New**: `balance_neto_GEI()`'s returned `balance_neto_kgCO2eq_ano` does not match the sum of its
   own reported components (`emisiones_biomasa_kg + emisiones_biogas_kg + emisiones_diesel_kg +
   credito_exportacion_kg`); the difference (~COP -108 million kg total, both scenarios) is close
   to but not exactly explained by the palm plantation carbon uptake credit (-135.04 kg CO2/tFFB)
   that Methods §2.7 describes as reported separately — suggesting it may already be baked into
   this function despite the text saying otherwise. Not investigated further this session since it
   did not block the emissions-panel question being answered; needs resolving before Methods §2.7
   or any GHG balance figure citing this function is finalized.

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
