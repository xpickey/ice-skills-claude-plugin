## PART 4: Oracle EBS Manufacturing

### Discrete Manufacturing

**Bills of Material (BOM)**:
- **BOM Structure**: Parent-component relationship, quantity per assembly, effectivity dates
- **BOM Types**: Manufacturing BOM, engineering BOM, planning BOM, costing BOM
- **Phantom Assemblies**: Transient sub-assembly, no inventory tracking
- **Alternate BOMs**: Alternate material, alternate routing, make vs. buy decision
- **BOM Revisions**: Engineering change orders, revision effectivity, mass changes
- **Component Attributes**: Component item, quantity, yield, scrap factor, supply type

**Routing & Work Centers**:
- **Routing Definition**: Sequence of operations, operation description, work center
- **Work Centers**: Department, resource, capacity, utilization, efficiency factor
- **Operation Resources**: Labor, machine, space, setup time, run time
- **Routing Revisions**: Engineering changes, routing alternatives, effectivity control
- **Alternate Routings**: Alternate work centers, alternate operations, routing preferences

**Work in Process (WIP)**:
- **Job Types**: Discrete job, repetitive schedule, flow schedule, lot-based job
- **Job Creation**: Manual, MRP/MPS-generated, ERP-generated, flow schedule
- **Job Release**: Release to shop floor, material allocation, resource reservation
- **Material Issue**: Backflush, manual issue, issue to job, return from job
- **Resource Transactions**: Labor booking, machine time, move transactions
- **Job Completion**: Assembly completion, by-product completion, close job
- **Job Costing**: Standard cost, actual cost, cost variance analysis, WIP valuation

**Production Scheduling**:
- **Capacity Planning**: Rough-cut capacity planning, capacity requirements planning
- **Shop Floor Control**: Dispatch list, job priority, operation status, queue time
- **Finite Scheduling**: Constrained-based scheduling, resource leveling, what-if analysis
- **Job Tracking**: Job status, operation completion %, material consumed, actual vs. standard

### Process Manufacturing (OPM)

**Formula & Recipe Management**:
- **Formula Definition**: Ingredient list, product yield, co-products, by-products
- **Recipe**: Formula + routing + processing parameters, product-specific recipes
- **Scale**: Formula scaling, recipe scaling, ingredient substitution
- **Recipe Versions**: Multiple versions, effectivity dates, preferred recipe
- **Quality Attributes**: Ingredient quality, product specification, test methods

**Process Execution**:
- **Batch Creation**: Planned batch, unplanned batch, batch from formula, recipe-driven
- **Batch Release**: Material reservation, resource allocation, release to production
- **Batch Transactions**: Material issue, material receipt, step completion, batch completion
- **Batch Status**: Pending, WIP, completed, closed, cancelled
- **Process Loss**: Theoretical yield vs. actual yield, process efficiency, variance analysis

**Product Costing (OPM)**:
- **Cost Components**: Material, resources, overhead, process loss
- **Cost Rollup**: Roll up cost from ingredients to finished product
- **Actual Costing**: Capture actual costs, variance analysis, cost allocation

**Quality Management (OPM)**:
- **Quality Specifications**: Specification limits, test methods, sampling plans
- **Quality Tests**: Lab tests, in-process tests, final product tests
- **Test Results**: Pass/fail, out-of-spec handling, certificate of analysis (COA)
- **Quality Hold**: Hold batch/lot pending quality approval, release after approval

---
