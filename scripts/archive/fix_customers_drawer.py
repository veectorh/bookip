import re

with open('customers.html', 'r') as f:
    content = f.read()

# Replace the giant Javascript string injected drawer with the Handlebars partial in HTML
slide_over_content = """        </div>
      </main>
    </div>
  </div>

  {{> slide-over id="customer-drawer" title="Add Customer" save_label="Save customer" }}
    <!-- Basic Info -->
    <div>
      <div class="text-xs font-semibold text-muted uppercase tracking-wider mb-3">Basic Info</div>
      <div class="flex flex-col gap-3">
        <div class="flex items-center gap-3">
          <div class="w-12 h-12 rounded-full bg-canvas border border-line-strong flex items-center justify-center text-muted"><svg class="w-5 h-5 stroke-[1.5]"><use href="#i-user"/></svg></div>
          <button class="text-indigo font-medium hover:underline underline-offset-2">Upload picture</button>
        </div>
        <div>
          <label class="block text-xs font-medium text-muted mb-1.25">Name <span class="text-[#B4372A]">*</span></label>
          <input type="text" class="w-full h-control px-2.5 bg-surface border border-line-strong rounded focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none">
        </div>
        <div>
          <label class="block text-xs font-medium text-muted mb-1.25">Company Name</label>
          <input type="text" class="w-full h-control px-2.5 bg-surface border border-line-strong rounded focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none">
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-medium text-muted mb-1.25">Email</label>
            <input type="email" class="w-full h-control px-2.5 bg-surface border border-line-strong rounded focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none">
          </div>
          <div>
            <label class="block text-xs font-medium text-muted mb-1.25">Mobile</label>
            <input type="tel" class="w-full h-control px-2.5 bg-surface border border-line-strong rounded focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none">
          </div>
        </div>
      </div>
    </div>

    <hr class="border-0 border-t border-line my-1">
    
    <!-- Billing Details -->
    <div>
      <div class="text-xs font-semibold text-muted uppercase tracking-wider mb-3">Billing Details</div>
      <div class="flex flex-col gap-3">
        <div>
          <label class="block text-xs font-medium text-muted mb-1.25">Currency</label>
          <select class="w-full h-control px-2.5 bg-surface border border-line-strong rounded focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none">
            <option>NGN (Naira)</option>
            <option>USD (US Dollar)</option>
          </select>
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-medium text-muted mb-1.25">VAT ID</label>
            <input type="text" class="w-full h-control px-2.5 bg-surface border border-line-strong rounded focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none">
          </div>
          <div>
            <label class="block text-xs font-medium text-muted mb-1.25">Reg No</label>
            <input type="text" class="w-full h-control px-2.5 bg-surface border border-line-strong rounded focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none">
          </div>
        </div>
      </div>
    </div>

    <hr class="border-0 border-t border-line my-1">
    
    <!-- Address -->
    <div>
      <div class="text-xs font-semibold text-muted uppercase tracking-wider mb-3">Address</div>
      <div class="flex flex-col gap-3">
        <div>
          <label class="block text-xs font-medium text-muted mb-1.25">Street Address</label>
          <input type="text" class="w-full h-control px-2.5 bg-surface border border-line-strong rounded focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none">
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-medium text-muted mb-1.25">City</label>
            <input type="text" class="w-full h-control px-2.5 bg-surface border border-line-strong rounded focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none">
          </div>
          <div>
            <label class="block text-xs font-medium text-muted mb-1.25">State</label>
            <input type="text" class="w-full h-control px-2.5 bg-surface border border-line-strong rounded focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none">
          </div>
          <div>
            <label class="block text-xs font-medium text-muted mb-1.25">ZIP / Postal Code</label>
            <input type="text" class="w-full h-control px-2.5 bg-surface border border-line-strong rounded focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none">
          </div>
          <div>
            <label class="block text-xs font-medium text-muted mb-1.25">Country</label>
            <select class="w-full h-control px-2.5 bg-surface border border-line-strong rounded focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none">
              <option>Nigeria</option>
              <option>Ghana</option>
            </select>
          </div>
        </div>
      </div>
    </div>
    
    <hr class="border-0 border-t border-line my-1">
    
    <!-- Other -->
    <div>
      <div class="flex flex-col gap-3">
        <div>
          <label class="block text-xs font-medium text-muted mb-1.25">Remarks</label>
          <textarea class="w-full p-2.5 bg-surface border border-line-strong rounded focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none min-h-[80px] resize-y" placeholder="Internal notes about this customer"></textarea>
        </div>
      </div>
    </div>
  {{/slide-over}}

  {{> scripts}}"""

# Remove the JS function
content = re.sub(r'      function openCustomerDrawer\(\) \{.*?\n      \}\n', '', content, flags=re.DOTALL)
content = content.replace('onclick="openCustomerDrawer()"', 'data-drawer-target="customer-drawer"')
content = re.sub(r'        </div>\n      </main>\n    </div>\n  </div>\n\n  \{\{> scripts\}\}', slide_over_content, content, flags=re.DOTALL)

with open('customers.html', 'w') as f:
    f.write(content)
