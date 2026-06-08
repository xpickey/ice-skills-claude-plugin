#!/usr/bin/env python3
"""
MD050 Configuration Workbook Generator for Oracle EBS
Generates standardized configuration documentation templates
"""

import json
from datetime import datetime

def generate_gl_md050():
    """Generate General Ledger MD050 configuration workbook"""
    workbook = {
        "Module": "General Ledger",
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Sections": [
            {
                "Section": "Chart of Accounts",
                "Fields": [
                    {"Field": "Segment Structure", "Value": "", "Notes": "Define segments (Company, Dept, Account, etc.)"},
                    {"Field": "Number of Segments", "Value": "", "Notes": "Typically 4-8 segments"},
                    {"Field": "Separator", "Value": "-", "Notes": "Segment separator character"},
                ]
            },
            {
                "Section": "Ledger Setup",
                "Fields": [
                    {"Field": "Ledger Name", "Value": "", "Notes": "Primary ledger name"},
                    {"Field": "Chart of Accounts", "Value": "", "Notes": "Assigned COA"},
                    {"Field": "Currency", "Value": "THB", "Notes": "Functional currency"},
                    {"Field": "Calendar", "Value": "", "Notes": "Accounting calendar"},
                ]
            },
            {
                "Section": "Period Setup",
                "Fields": [
                    {"Field": "Period Type", "Value": "Month", "Notes": "Period granularity"},
                    {"Field": "First Period", "Value": "", "Notes": "First fiscal period"},
                    {"Field": "Adjustment Periods", "Value": "13", "Notes": "Year-end adjustment period"},
                ]
            },
        ]
    }
    return workbook

def generate_ap_md050():
    """Generate Accounts Payable MD050 configuration workbook"""
    workbook = {
        "Module": "Accounts Payable",
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Sections": [
            {
                "Section": "Invoice Matching",
                "Fields": [
                    {"Field": "Match Type", "Value": "3-Way", "Notes": "PO-Receipt-Invoice"},
                    {"Field": "Price Tolerance (%)", "Value": "5", "Notes": "Percentage variance allowed"},
                    {"Field": "Quantity Tolerance (%)", "Value": "2", "Notes": "Quantity variance allowed"},
                    {"Field": "Amount Threshold", "Value": "10000", "Notes": "Auto-hold if variance exceeds"},
                ]
            },
            {
                "Section": "Payment Processing",
                "Fields": [
                    {"Field": "Payment Method", "Value": "Electronic", "Notes": "Check, Wire, ACH, etc."},
                    {"Field": "Payment Format", "Value": "", "Notes": "Bank-specific format"},
                    {"Field": "Payment Terms", "Value": "Net 30", "Notes": "Default payment terms"},
                ]
            },
        ]
    }
    return workbook

def export_to_json(workbook, filename):
    """Export MD050 workbook to JSON format"""
    with open(filename, 'w') as f:
        json.dump(workbook, f, indent=2)
    print(f"MD050 workbook exported to {filename}")

def export_to_csv(workbook, filename):
    """Export MD050 workbook to CSV format"""
    import csv
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Module', workbook['Module']])
        writer.writerow(['Date', workbook['Date']])
        writer.writerow([])
        
        for section in workbook['Sections']:
            writer.writerow(['Section', section['Section']])
            writer.writerow(['Field', 'Value', 'Notes'])
            for field in section['Fields']:
                writer.writerow([field['Field'], field['Value'], field['Notes']])
            writer.writerow([])
    
    print(f"MD050 workbook exported to {filename}")

if __name__ == "__main__":
    # Example usage
    gl_workbook = generate_gl_md050()
    ap_workbook = generate_ap_md050()
    
    # Export to JSON
    export_to_json(gl_workbook, "GL_MD050.json")
    export_to_json(ap_workbook, "AP_MD050.json")
    
    # Export to CSV
    export_to_csv(gl_workbook, "GL_MD050.csv")
    export_to_csv(ap_workbook, "AP_MD050.csv")
    
    print("\nMD050 templates generated successfully!")
