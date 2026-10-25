import pandas as pd
from datetime import datetime

def run_access_reconciliation(hr_db_path, active_systems_path):
    print("=== Access Reconciliation Compliance Audit ===")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Load authoritative HR database and active system access logs
    hr_df = pd.read_csv(hr_db_path)
    systems_df = pd.read_csv(active_systems_path)

    # Filter terminated employees from HR records
    terminated = hr_df[hr_df['status'].str.lower() == 'terminated']['email'].tolist()
    
    # Identify orphaned accounts (terminated individuals still active on systems)
    orphaned = systems_df[systems_df['email'].isin(terminated)]
    
    print(f"Total Accounts Scanned: {len(systems_df)}")
    print(f"Orphaned Accounts Found: {len(orphaned)}\n")
    
    if not orphaned.empty:
        print(orphaned[['username', 'email', 'system_name', 'last_login_date']])
        
        # Save audit report
        report_name = f"access_audit_report_{datetime.now().strftime('%Y%m%d')}.csv"
        orphaned.to_csv(report_name, index=False)
        print(f"\n[SUCCESS] Report saved: {report_name}")
    else:
        print("\n[SUCCESS] No orphaned accounts detected.")

if __name__ == "__main__":
    # Example usage:
    # run_access_reconciliation("hr_database.csv", "active_systems.csv")
    pass