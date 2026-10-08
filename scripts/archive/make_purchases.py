with open('purchases.html', 'r') as f:
    content = f.read()

# Topbar active link
content = content.replace('href="index.html" class="flex items-center gap-3 px-3 py-1.5 rounded-md text-[13px] font-medium bg-th text-ink"',
                          'href="index.html" class="flex items-center gap-3 px-3 py-1.5 rounded-md text-[13px] font-medium text-muted hover:text-ink hover:bg-th"')
content = content.replace('href="purchases.html" class="flex items-center gap-3 px-3 py-1.5 rounded-md text-[13px] font-medium text-muted hover:text-ink hover:bg-th"',
                          'href="purchases.html" class="flex items-center gap-3 px-3 py-1.5 rounded-md text-[13px] font-medium bg-th text-ink"')

# Titles and counts
content = content.replace('Invoices', 'Purchases')
content = content.replace('invoices', 'purchases')
content = content.replace('New invoice', 'New purchase')
content = content.replace('New Invoice', 'New purchase')
content = content.replace('View invoice', 'View purchase')
content = content.replace('Cancel invoice', 'Cancel purchase')

# Table Headers
content = content.replace('<th class="px-3.5 py-2.5 text-left border-b border-line whitespace-nowrap font-medium">Number</th>', '<th class="px-3.5 py-2.5 text-left border-b border-line whitespace-nowrap font-medium">Bill Number</th>')
content = content.replace('<th class="px-3.5 py-2.5 text-left border-b border-line whitespace-nowrap font-medium">Customer</th>', '<th class="px-3.5 py-2.5 text-left border-b border-line whitespace-nowrap font-medium">Vendor</th>')
content = content.replace('<th class="px-3.5 py-2.5 text-left border-b border-line whitespace-nowrap font-medium">Issued</th>', '<th class="px-3.5 py-2.5 text-left border-b border-line whitespace-nowrap font-medium">Purchase Date</th>')

# Data replacements
content = content.replace('INV-', 'BILL-')
content = content.replace('Customer', 'Vendor')
content = content.replace('customer', 'vendor')

# Editor
content = content.replace('Invoice date', 'Purchase date')
content = content.replace('Issue and send', 'Save purchase')

# Add Footer to Editor (Purchases Brief says: Notes, Footer)
# Find the Notes section and append Footer
notes_section = """                    <label class="block text-xs font-medium text-muted mb-1.25">Notes</label>
                    <div class="flex items-center gap-2 h-auto py-2 px-2.5 bg-surface border border-line-strong rounded text-[13px] focus-within:border-indigo focus-within:ring-[3px] focus-within:ring-indigo-line">
                      <input type="text" class="bg-transparent border-0 outline-none w-full placeholder-muted" placeholder="Shown on the purchase">
                    </div>"""
new_notes_section = """                    <label class="block text-xs font-medium text-muted mb-1.25">Notes</label>
                    <div class="flex items-center gap-2 h-auto py-2 px-2.5 bg-surface border border-line-strong rounded text-[13px] focus-within:border-indigo focus-within:ring-[3px] focus-within:ring-indigo-line mb-3">
                      <input type="text" class="bg-transparent border-0 outline-none w-full placeholder-muted" placeholder="Shown on the purchase">
                    </div>
                    <label class="block text-xs font-medium text-muted mb-1.25">Footer</label>
                    <div class="flex items-center gap-2 h-auto py-2 px-2.5 bg-surface border border-line-strong rounded text-[13px] focus-within:border-indigo focus-within:ring-[3px] focus-within:ring-indigo-line">
                      <input type="text" class="bg-transparent border-0 outline-none w-full placeholder-muted" placeholder="Terms and conditions">
                    </div>"""
content = content.replace(notes_section, new_notes_section)
content = content.replace('Shown on the invoice', 'Shown on the purchase')


with open('purchases.html', 'w') as f:
    f.write(content)

