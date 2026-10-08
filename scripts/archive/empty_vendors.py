import re

with open('vendors.html', 'r') as f:
    content = f.read()

# Replace the desktop and mobile tables with the empty state
table_pattern = re.compile(r'<!-- Table \(Desktop\) -->.*?(?=</div>\n          </div>)', re.DOTALL)
empty_state = """<!-- Empty State -->
            <div class="bg-surface border border-line rounded flex items-center justify-center min-h-[400px]">
              {{> list-empty-state icon="#i-users" title="No vendors found" description="You haven't added any vendors yet. Create your first vendor to start logging purchases." action_label="Add vendor" action_attr="data-drawer-target=\\"vendor-drawer\\"" }}
            </div>"""

content = re.sub(table_pattern, empty_state, content)

with open('vendors.html', 'w') as f:
    f.write(content)
