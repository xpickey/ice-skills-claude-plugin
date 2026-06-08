## PART 6: Technical Architecture & Integration

### Forms & Reports

**Oracle Forms**:
- **Forms Personalization**: Field properties, menu options, special triggers, context-specific
- **Custom Forms**: TEMPLATE.fmb, form generation, custom library (CUSTOM.pll)
- **Form Functions**: Register custom form, assign to menu, function security
- **Multi-Org Forms**: Security profile, operating unit picker, MOAC-enabled forms

**Oracle Reports**:
- **Standard Reports**: XML Publisher (BI Publisher), RDF reports, SQL*Plus scripts
- **Custom Reports**: Report builder, data model, layout template (RTF, XLS, PDF)
- **Report Registration**: Register in Concurrent Program, parameters, output format
- **Bursting**: Email reports to recipients, dynamic distribution, report splitting

**Concurrent Programs**:
- **Program Definition**: Executable, parameters, incompatibilities, output options
- **Request Sets**: Group programs, stage control, output post-processing
- **Concurrent Manager**: Scheduling, load balancing, transaction manager, conflict resolution
- **Program Security**: Responsibility access, user access, request group assignment

### Workflow & AME

**Oracle Workflow**:
- **Workflow Builder**: Process diagram, activities, transitions, attributes
- **Notification**: Email notifications, FYI notifications, action required, reminder
- **Workflow Monitor**: Instance status, activity status, error handling, timeout
- **Workflow Maintenance**: Purge runtime data, workflow tables cleanup, performance tuning
- **Background Engine**: Deferred activities, scheduled activities, timeout activities

**Approval Management Engine (AME)**:
- **Approval Rules**: Condition-based rules, position-based rules, amount-based rules
- **Approval Groups**: Approval group definition, chain of authority, parallel approval
- **Approval Process**: Rule evaluation, approver determination, notification
- **Transaction Types**: Purchase requisition, purchase order, expense report, invoice, journal
- **Delegation**: Vacation rules, temporary delegation, permanent delegation

### Oracle Application Framework (OAF)

**OAF Architecture**:
- **Model-View-Controller**: BC4J (Business Components for Java), view objects, application modules
- **Page Layout**: Region structure, items, tables, buttons, LOVs, personalizations
- **Personalization**: Admin-level, site-level, function-level, user-level personalization
- **Extensions**: Custom CO (Controller), custom VO (View Object), custom AM (Application Module)
- **Deployment**: JAR file, import to MDS (Metadata Services), clear cache

**OAF Development**:
- **JDeveloper**: IDE for OAF development, project setup, BC4J creation, page layout
- **Substitution**: Substitute standard pages with custom pages, page mapping
- **Testing**: Run page locally, deploy to instance, functional testing, integration testing

### Web Services & Integration

**Oracle Integration Repository**:
- **Interface Catalog**: Pre-built interfaces, open interfaces, custom interfaces
- **API Documentation**: PL/SQL APIs, Java APIs, web services, REST APIs
- **Interface Testing**: Test harness, payload examples, error handling

**Web Services**:
- **SOAP Web Services**: WSDL, request/response, authentication, error handling
- **REST APIs**: HTTP methods (GET, POST, PUT, DELETE), JSON payload, OAuth
- **Integration Adapters**: SOA Suite adapters, EBS Adapter, database adapter, file adapter

**XML Gateway**:
- **Outbound Messages**: Order acknowledgment, shipment notification, invoice
- **Inbound Messages**: Purchase order, ASN, supplier invoice, payment
- **Message Definition**: DTD, XML schema, mapping rules, transformation

**SOA Suite & OIC Integration**:
- **Service Bus**: Message routing, protocol mediation, transformation, orchestration
- **BPEL Process**: Business process automation, long-running processes, human tasks
- **Adapters**: EBS Adapter, FTP Adapter, Email Adapter, REST Adapter
- **Error Handling**: Fault policies, retry logic, error logging, compensation

### Data Migration & Interfaces

**Data Migration Strategy**:
- **Data Extraction**: Extract from legacy system, data quality checks, data cleansing
- **Data Transformation**: Data mapping, data conversion, data enrichment, data validation
- **Data Loading**: Open interfaces, FBDI (File-Based Data Import), API loading, SQL*Loader
- **Data Validation**: Pre-load validation, post-load validation, reconciliation, error resolution
- **Cutover Planning**: Freeze legacy, final extract, load to production, validation, go-live

**Open Interfaces**:
- **GL Interface**: GL_INTERFACE, import journals, validation, error handling
- **AP Interface**: AP_INVOICES_INTERFACE, import invoices, auto-approve, post to GL
- **AR Interface**: RA_INTERFACE_LINES, AutoInvoice, revenue recognition, receipt interface
- **FA Interface**: FA_MASS_ADDITIONS, mass addition import, asset creation
- **PO Interface**: Create requisitions, create POs, AutoCreate, approval bypass
- **INV Interface**: Item import, transaction import, on-hand import, cycle count import
- **OM Interface**: Order import, pricing, scheduling, workflow, invoice interface

**FBDI (File-Based Data Import)**:
- **Template Download**: Pre-defined templates (XLS, CSV), mapping, data format
- **Data Population**: Fill template, validation rules, mandatory fields, data lookup
- **Upload & Process**: Upload via UI, process, validation errors, success report
- **Post-Processing**: Data review, correction, reprocess, final validation

---
