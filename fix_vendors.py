with open('vendors.html', 'r') as f:
    content = f.read()

# Text replacements
content = content.replace('Customers', 'Vendors')
content = content.replace('Customer', 'Vendor')
content = content.replace('customer', 'vendor')
content = content.replace('active_customers=true', 'active_vendors=true')
content = content.replace('{{> list-desktop-filters new_button_label="New Vendor" }}', '{{> list-desktop-filters new_button_label="New vendor" }}')
content = content.replace('data-drawer-target="vendor-drawer"', 'data-drawer-target="vendor-drawer"')

with open('vendors.html', 'w') as f:
    f.write(content)
