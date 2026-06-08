#!/usr/bin/env python3
"""
Chart of Accounts (COA) Design Validator for Oracle EBS
Validates COA structure against best practices
"""

def validate_coa_design(coa_structure):
    """
    Validate Chart of Accounts structure
    
    Args:
        coa_structure: Dictionary containing COA definition
        
    Returns:
        List of validation messages (warnings and errors)
    """
    messages = []
    
    # Check number of segments
    num_segments = coa_structure.get('num_segments', 0)
    if num_segments < 3:
        messages.append("ERROR: Minimum 3 segments required (Company, Account, Cost Center)")
    elif num_segments > 30:
        messages.append("ERROR: Maximum 30 segments allowed by Oracle")
    elif num_segments > 10:
        messages.append("WARNING: More than 10 segments may impact performance")
    
    # Check segment naming
    segments = coa_structure.get('segments', [])
    required_qualifiers = ['GL_BALANCING', 'GL_ACCOUNT']
    
    for qualifier in required_qualifiers:
        if not any(seg.get('qualifier') == qualifier for seg in segments):
            messages.append(f"ERROR: Missing required qualifier: {qualifier}")
    
    # Check segment sizes
    for seg in segments:
        size = seg.get('size', 0)
        if size < 2:
            messages.append(f"WARNING: Segment '{seg.get('name')}' size {size} is very small")
        if size > 30:
            messages.append(f"ERROR: Segment '{seg.get('name')}' exceeds maximum size of 30")
    
    # Check for Future segments
    future_segments = [s for s in segments if 'FUTURE' in s.get('name', '').upper()]
    if len(future_segments) < 2:
        messages.append("WARNING: Consider adding 2+ FUTURE segments for flexibility")
    
    # Check separator
    separator = coa_structure.get('separator', '')
    if separator not in ['-', '.', '_']:
        messages.append("WARNING: Unusual separator. Common separators: '-', '.', '_'")
    
    # Check dynamic insertion
    if not coa_structure.get('allow_dynamic_insert', False):
        messages.append("INFO: Dynamic insertion disabled - new combinations must be pre-defined")
    
    return messages

def suggest_coa_structure(business_requirements):
    """
    Suggest COA structure based on business requirements
    
    Args:
        business_requirements: Dictionary with business needs
        
    Returns:
        Suggested COA structure
    """
    suggested = {
        'num_segments': 0,
        'segments': [],
        'separator': '-'
    }
    
    # Core segments
    suggested['segments'].append({
        'name': 'Company',
        'size': 3,
        'qualifier': 'GL_BALANCING',
        'description': 'Legal entity / Operating unit'
    })
    
    suggested['segments'].append({
        'name': 'Cost_Center',
        'size': 4,
        'qualifier': None,
        'description': 'Department / Cost center'
    })
    
    suggested['segments'].append({
        'name': 'Account',
        'size': 6,
        'qualifier': 'GL_ACCOUNT',
        'description': 'Natural account'
    })
    
    # Optional segments based on requirements
    if business_requirements.get('needs_product_tracking'):
        suggested['segments'].append({
            'name': 'Product',
            'size': 4,
            'qualifier': None,
            'description': 'Product line / Brand'
        })
    
    if business_requirements.get('needs_project_tracking'):
        suggested['segments'].append({
            'name': 'Project',
            'size': 6,
            'qualifier': None,
            'description': 'Project / Job number'
        })
    
    if business_requirements.get('needs_intercompany'):
        suggested['segments'].append({
            'name': 'Intercompany',
            'size': 3,
            'qualifier': 'GL_INTERCOMPANY',
            'description': 'Intercompany transactions'
        })
    
    if business_requirements.get('needs_location_tracking'):
        suggested['segments'].append({
            'name': 'Location',
            'size': 3,
            'qualifier': None,
            'description': 'Geographic location'
        })
    
    # Add Future segments
    for i in range(1, 3):
        suggested['segments'].append({
            'name': f'Future{i}',
            'size': 3,
            'qualifier': None,
            'description': f'Reserved for future use {i}'
        })
    
    suggested['num_segments'] = len(suggested['segments'])
    
    return suggested

def format_coa_display(coa_structure):
    """Format COA structure for display"""
    separator = coa_structure.get('separator', '-')
    segments = coa_structure.get('segments', [])
    
    display = []
    display.append("Chart of Accounts Structure")
    display.append("=" * 80)
    display.append(f"Number of Segments: {len(segments)}")
    display.append(f"Separator: '{separator}'")
    display.append("")
    display.append("Segments:")
    display.append("-" * 80)
    
    for i, seg in enumerate(segments, 1):
        name = seg.get('name', 'Unknown')
        size = seg.get('size', 0)
        qual = seg.get('qualifier', 'None')
        desc = seg.get('description', '')
        
        display.append(f"{i}. {name:15} | Size: {size:2} | Qualifier: {qual:20} | {desc}")
    
    display.append("-" * 80)
    
    # Show example
    example_parts = []
    for seg in segments:
        example_parts.append("X" * seg.get('size', 3))
    
    example = separator.join(example_parts)
    display.append(f"\nExample Account: {example}")
    display.append(f"Total Length: {len(example)} characters")
    
    return "\n".join(display)

# Example usage
if __name__ == "__main__":
    # Example COA structure
    example_coa = {
        'num_segments': 7,
        'separator': '-',
        'allow_dynamic_insert': True,
        'segments': [
            {'name': 'Company', 'size': 3, 'qualifier': 'GL_BALANCING', 'description': 'Legal entity'},
            {'name': 'Department', 'size': 4, 'qualifier': None, 'description': 'Cost center'},
            {'name': 'Account', 'size': 6, 'qualifier': 'GL_ACCOUNT', 'description': 'Natural account'},
            {'name': 'Product', 'size': 4, 'qualifier': None, 'description': 'Product line'},
            {'name': 'Project', 'size': 6, 'qualifier': None, 'description': 'Project code'},
            {'name': 'Future1', 'size': 3, 'qualifier': None, 'description': 'Future use 1'},
            {'name': 'Future2', 'size': 3, 'qualifier': None, 'description': 'Future use 2'},
        ]
    }
    
    # Validate
    print("Validating COA structure...")
    validation_messages = validate_coa_design(example_coa)
    
    if validation_messages:
        print("\nValidation Results:")
        for msg in validation_messages:
            print(f"  {msg}")
    else:
        print("\n✓ COA structure is valid!")
    
    # Display structure
    print("\n" + format_coa_display(example_coa))
    
    # Suggest structure based on requirements
    print("\n\nSuggesting COA based on requirements...")
    requirements = {
        'needs_product_tracking': True,
        'needs_project_tracking': True,
        'needs_intercompany': True,
        'needs_location_tracking': False
    }
    
    suggested_coa = suggest_coa_structure(requirements)
    print(format_coa_display(suggested_coa))
