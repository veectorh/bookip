import re

desktop_table_invoice = """                  <div class="hidden md:block p-0 overflow-x-auto">
                    <table class="w-full border-collapse text-[13px] min-w-[600px]">
                      <thead>
                        <tr class="bg-th text-xs text-muted font-medium">
                          <th class="px-3 font-medium text-left w-[38%]">Item</th>
                          <th class="px-3 font-medium text-left w-[18%]">Tax</th>
                          <th class="px-3 font-medium text-right w-[12%]">Qty</th>
                          <th class="px-3 font-medium text-right w-[16%]">Price</th>
                          <th class="px-3 font-medium text-right w-[16%]">Amount</th>
                          <th class="px-3 font-medium w-9"></th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td class="px-3 border-b border-line h-11"><div class="flex items-center h-7 px-2 bg-surface border border-line-strong rounded text-[13px] focus-within:border-indigo focus-within:ring-[3px] focus-within:ring-indigo-line"><select class="bg-transparent border-0 outline-none w-full"><option>Website retainer</option></select></div></td>
                          <td class="px-3 border-b border-line h-11"><div class="flex items-center h-7 px-2 bg-surface border border-line-strong rounded text-[13px] focus-within:border-indigo focus-within:ring-[3px] focus-within:ring-indigo-line"><select class="bg-transparent border-0 outline-none w-full"><option>VAT 7.5%</option><option>None</option></select></div></td>
                          <td class="px-3 border-b border-line h-11 text-right font-variant-numeric:tabular-nums"><div class="flex items-center h-7 px-2 bg-surface border border-line-strong rounded text-[13px] focus-within:border-indigo focus-within:ring-[3px] focus-within:ring-indigo-line"><input type="text" class="bg-transparent border-0 outline-none w-full text-right" value="1"></div></td>
                          <td class="px-3 border-b border-line h-11 text-right font-variant-numeric:tabular-nums"><div class="flex items-center h-7 px-2 bg-surface border border-line-strong rounded text-[13px] focus-within:border-indigo focus-within:ring-[3px] focus-within:ring-indigo-line"><input type="text" class="bg-transparent border-0 outline-none w-full text-right" value="150,000.00"></div></td>
                          <td class="px-3 border-b border-line h-11 text-right font-variant-numeric:tabular-nums">161,250.00</td>
                          <td class="px-3 border-b border-line h-11"><button class="w-[26px] h-[26px] rounded flex items-center justify-center text-muted hover:bg-th hover:border-line-strong hover:text-ink border border-transparent"><svg class="w-4 h-4 stroke-[1.75]" aria-hidden="true"><use href="#i-trash-2"/></svg></button></td>
                        </tr>
                        <tr>
                          <td class="px-3 border-b border-line h-11"><div class="flex items-center h-7 px-2 bg-surface border border-line-strong rounded text-[13px] focus-within:border-indigo focus-within:ring-[3px] focus-within:ring-indigo-line"><select class="bg-transparent border-0 outline-none w-full"><option>Hosting — 12 months</option></select></div></td>
                          <td class="px-3 border-b border-line h-11"><div class="flex items-center h-7 px-2 bg-surface border border-line-strong rounded text-[13px] focus-within:border-indigo focus-within:ring-[3px] focus-within:ring-indigo-line"><select class="bg-transparent border-0 outline-none w-full"><option>None</option><option>VAT 7.5%</option></select></div></td>
                          <td class="px-3 border-b border-line h-11 text-right font-variant-numeric:tabular-nums"><div class="flex items-center h-7 px-2 bg-surface border border-line-strong rounded text-[13px] focus-within:border-indigo focus-within:ring-[3px] focus-within:ring-indigo-line"><input type="text" class="bg-transparent border-0 outline-none w-full text-right" value="1"></div></td>
                          <td class="px-3 border-b border-line h-11 text-right font-variant-numeric:tabular-nums"><div class="flex items-center h-7 px-2 bg-surface border border-line-strong rounded text-[13px] focus-within:border-indigo focus-within:ring-[3px] focus-within:ring-indigo-line"><input type="text" class="bg-transparent border-0 outline-none w-full text-right" value="45,000.00"></div></td>
                          <td class="px-3 border-b border-line h-11 text-right font-variant-numeric:tabular-nums">45,000.00</td>
                          <td class="px-3 border-b border-line h-11"><button class="w-[26px] h-[26px] rounded flex items-center justify-center text-muted hover:bg-th hover:border-line-strong hover:text-ink border border-transparent"><svg class="w-4 h-4 stroke-[1.75]" aria-hidden="true"><use href="#i-trash-2"/></svg></button></td>
                        </tr>
                      </tbody>
                    </table>
                  </div>

                  <!-- Mobile Items List -->
                  <div class="block md:hidden p-3 flex flex-col gap-2 border-b border-line">
                    <div class="flex items-start justify-between border border-line-strong rounded p-3 bg-canvas">
                      <div>
                        <div class="font-medium text-ink">Website retainer</div>
                        <div class="text-xs text-muted mt-0.5">1 x 150,000.00 • VAT 7.5%</div>
                      </div>
                      <div class="text-right">
                        <div class="font-medium font-variant-numeric:tabular-nums text-ink">161,250.00</div>
                        <button class="mt-2 text-muted hover:text-[#B4372A]"><svg class="w-4 h-4 stroke-[1.75] ml-auto"><use href="#i-trash-2"/></svg></button>
                      </div>
                    </div>
                    <div class="flex items-start justify-between border border-line-strong rounded p-3 bg-canvas">
                      <div>
                        <div class="font-medium text-ink">Hosting — 12 months</div>
                        <div class="text-xs text-muted mt-0.5">1 x 45,000.00 • None</div>
                      </div>
                      <div class="text-right">
                        <div class="font-medium font-variant-numeric:tabular-nums text-ink">45,000.00</div>
                        <button class="mt-2 text-muted hover:text-[#B4372A]"><svg class="w-4 h-4 stroke-[1.75] ml-auto"><use href="#i-trash-2"/></svg></button>
                      </div>
                    </div>
                  </div>
"""

desktop_table_quotation = """                  <div class="hidden md:block p-0 overflow-x-auto">
                    <table class="w-full border-collapse text-[13px] min-w-[600px]">
                      <thead>
                        <tr class="bg-th text-xs text-muted font-medium">
                          <th class="px-3 font-medium text-left w-[38%]">Item</th>
                          <th class="px-3 font-medium text-left w-[18%]">Tax</th>
                          <th class="px-3 font-medium text-right w-[12%]">Qty</th>
                          <th class="px-3 font-medium text-right w-[16%]">Price</th>
                          <th class="px-3 font-medium text-right w-[16%]">Amount</th>
                          <th class="px-3 font-medium w-9"></th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td class="px-3 border-b border-line h-11"><div class="flex items-center h-7 px-2 bg-surface border border-line-strong rounded text-[13px] focus-within:border-indigo focus-within:ring-[3px] focus-within:ring-indigo-line"><select class="bg-transparent border-0 outline-none w-full"><option>Design services</option></select></div></td>
                          <td class="px-3 border-b border-line h-11"><div class="flex items-center h-7 px-2 bg-surface border border-line-strong rounded text-[13px] focus-within:border-indigo focus-within:ring-[3px] focus-within:ring-indigo-line"><select class="bg-transparent border-0 outline-none w-full"><option>None</option></select></div></td>
                          <td class="px-3 border-b border-line h-11 text-right font-variant-numeric:tabular-nums"><div class="flex items-center h-7 px-2 bg-surface border border-line-strong rounded text-[13px] focus-within:border-indigo focus-within:ring-[3px] focus-within:ring-indigo-line"><input type="text" class="bg-transparent border-0 outline-none w-full text-right" value="1"></div></td>
                          <td class="px-3 border-b border-line h-11 text-right font-variant-numeric:tabular-nums"><div class="flex items-center h-7 px-2 bg-surface border border-line-strong rounded text-[13px] focus-within:border-indigo focus-within:ring-[3px] focus-within:ring-indigo-line"><input type="text" class="bg-transparent border-0 outline-none w-full text-right" value="450,000.00"></div></td>
                          <td class="px-3 border-b border-line h-11 text-right font-variant-numeric:tabular-nums">450,000.00</td>
                          <td class="px-3 border-b border-line h-11"><button class="w-[26px] h-[26px] rounded flex items-center justify-center text-muted hover:bg-th hover:border-line-strong hover:text-ink border border-transparent"><svg class="w-4 h-4 stroke-[1.75]" aria-hidden="true"><use href="#i-trash-2"/></svg></button></td>
                        </tr>
                      </tbody>
                    </table>
                  </div>

                  <!-- Mobile Items List -->
                  <div class="block md:hidden p-3 flex flex-col gap-2 border-b border-line">
                    <div class="flex items-start justify-between border border-line-strong rounded p-3 bg-canvas">
                      <div>
                        <div class="font-medium text-ink">Design services</div>
                        <div class="text-xs text-muted mt-0.5">1 x 450,000.00 • None</div>
                      </div>
                      <div class="text-right">
                        <div class="font-medium font-variant-numeric:tabular-nums text-ink">450,000.00</div>
                        <button class="mt-2 text-muted hover:text-[#B4372A]"><svg class="w-4 h-4 stroke-[1.75] ml-auto"><use href="#i-trash-2"/></svg></button>
                      </div>
                    </div>
                  </div>
"""

with open('index.html', 'r') as f:
    content = f.read()

pattern = re.compile(r'                  <div class="p-0 overflow-x-auto">\n                    <table class="w-full border-collapse text-\[13px\] min-w-\[600px\]">.*?</table>\n                  </div>', re.DOTALL)
content = pattern.sub(desktop_table_invoice, content)

with open('index.html', 'w') as f:
    f.write(content)

with open('quotations.html', 'r') as f:
    content = f.read()

content = pattern.sub(desktop_table_quotation, content)

with open('quotations.html', 'w') as f:
    f.write(content)
