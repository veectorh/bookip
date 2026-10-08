with open('vendors.html', 'r') as f:
    content = f.read()

# Topbar active link
content = content.replace('href="customers.html" class="flex items-center gap-3 px-3 py-1.5 rounded-md text-[13px] font-medium bg-th text-ink"',
                          'href="customers.html" class="flex items-center gap-3 px-3 py-1.5 rounded-md text-[13px] font-medium text-muted hover:text-ink hover:bg-th"')
content = content.replace('href="vendors.html" class="flex items-center gap-3 px-3 py-1.5 rounded-md text-[13px] font-medium text-muted hover:text-ink hover:bg-th"',
                          'href="vendors.html" class="flex items-center gap-3 px-3 py-1.5 rounded-md text-[13px] font-medium bg-th text-ink"')

content = content.replace('Customers', 'Vendors')
content = content.replace('customers', 'vendors')
content = content.replace('Customer', 'Vendor')
content = content.replace('customer', 'vendor')

with open('vendors.html', 'w') as f:
    f.write(content)
