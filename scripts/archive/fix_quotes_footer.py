import re

with open('quotations.html', 'r') as f:
    content = f.read()

# The dangling footer to remove:
dangling = """                    <div class="px-3.5 py-3">
                      <button class="inline-flex items-center gap-1.5 h-control px-3 rounded border border-line-strong text-[13px] font-medium bg-surface hover:bg-th mt-2.5"><svg class="w-4 h-4 stroke-[1.75]" aria-hidden="true"><use href="#i-plus"/></svg> Add item</button>
                      <div class="ml-auto w-[280px] [&[data-layout=mob]_&]:w-full [&[data-layout=tablet]_&]:w-full text-[13px] mt-3.5">
                        <div class="flex justify-between py-1.75 border-b border-line"><span>Subtotal</span><span class="font-variant-numeric:tabular-nums">450,000.00</span></div>
                        <div class="flex justify-between py-1.75 border-b border-line"><span>Tax</span><span class="font-variant-numeric:tabular-nums">0.00</span></div>
                        <div class="flex justify-between py-1.75 border-b border-line"><span>Discount</span><span class="font-variant-numeric:tabular-nums">0.00</span></div>
                        <div class="flex justify-between pt-2.5 font-semibold text-[15px]"><span>Total</span><span class="font-variant-numeric:tabular-nums">₦ 450,000.00</span></div>
                      </div>
                    </div>"""

content = content.replace(dangling, "")

with open('quotations.html', 'w') as f:
    f.write(content)
