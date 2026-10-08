import re

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
                      <tfoot class="border-t border-line bg-surface">
                        <tr>
                          <td colspan="2" class="px-3 py-3">
                            <button class="inline-flex items-center gap-1.5 h-control px-3 rounded border border-line-strong text-[13px] font-medium bg-surface hover:bg-th"><svg class="w-4 h-4 stroke-[1.75]" aria-hidden="true"><use href="#i-plus"/></svg> Add item</button>
                          </td>
                          <td colspan="2" class="px-3 py-1.5 text-right font-medium">Subtotal</td>
                          <td class="px-3 py-1.5 text-right font-variant-numeric:tabular-nums">450,000.00</td>
                          <td></td>
                        </tr>
                        <tr>
                          <td colspan="2"></td>
                          <td colspan="2" class="px-3 py-1.5 text-right text-muted">Tax</td>
                          <td class="px-3 py-1.5 text-right font-variant-numeric:tabular-nums text-muted">0.00</td>
                          <td></td>
                        </tr>
                        <tr>
                          <td colspan="2"></td>
                          <td colspan="2" class="px-3 py-1.5 text-right text-muted">Discount</td>
                          <td class="px-3 py-1.5 text-right font-variant-numeric:tabular-nums text-muted">0.00</td>
                          <td></td>
                        </tr>
                        <tr>
                          <td colspan="2"></td>
                          <td colspan="2" class="px-3 py-3 text-right font-semibold text-[15px]">Total</td>
                          <td class="px-3 py-3 text-right font-semibold text-[15px] font-variant-numeric:tabular-nums">₦ 450,000.00</td>
                          <td></td>
                        </tr>
                      </tfoot>
                    </table>
                  </div>

                  <!-- Mobile Items List -->
                  <div class="block md:hidden p-3 flex flex-col gap-2 border-b border-line">
                    <div class="flex flex-col border border-line-strong rounded p-3 bg-canvas">
                      <div class="flex items-start justify-between">
                        <div>
                          <div class="font-medium text-ink">Design services</div>
                          <div class="text-xs text-muted mt-0.5">1 x 450,000.00 • None</div>
                        </div>
                        <div class="text-right">
                          <div class="font-medium font-variant-numeric:tabular-nums text-ink">450,000.00</div>
                          <button class="mt-2 text-muted hover:text-[#B4372A]"><svg class="w-4 h-4 stroke-[1.75] ml-auto"><use href="#i-trash-2"/></svg></button>
                        </div>
                      </div>
                      <!-- Expanded state mockup -->
                      <div class="hidden flex-col gap-3 mt-3 pt-3 border-t border-line-strong">
                         <div class="flex items-center h-control px-2 bg-surface border border-line-strong rounded text-[13px]"><select class="bg-transparent border-0 outline-none w-full"><option>Design services</option></select></div>
                         <div class="flex gap-2">
                           <div class="flex-1 flex items-center h-control px-2 bg-surface border border-line-strong rounded text-[13px]"><input type="text" class="bg-transparent border-0 outline-none w-full text-right" value="450,000.00"></div>
                           <div class="w-16 flex items-center h-control px-2 bg-surface border border-line-strong rounded text-[13px]"><input type="text" class="bg-transparent border-0 outline-none w-full text-right" value="1"></div>
                         </div>
                         <button class="h-control rounded bg-th font-medium">Done</button>
                      </div>
                    </div>
                  </div>
                  
                  <!-- Mobile Footer -->
                  <div class="block md:hidden px-3.5 py-3">
                    <button class="inline-flex items-center gap-1.5 w-full justify-center h-control px-3 rounded border border-line-strong text-[13px] font-medium bg-surface hover:bg-th mt-1 mb-3"><svg class="w-4 h-4 stroke-[1.75]" aria-hidden="true"><use href="#i-plus"/></svg> Add item</button>
                    <div class="flex flex-col gap-1.5 text-[13px]">
                      <div class="flex justify-between py-1 border-b border-line"><span>Subtotal</span><span class="font-variant-numeric:tabular-nums">450,000.00</span></div>
                      <div class="flex justify-between py-1 border-b border-line text-muted"><span>Tax</span><span class="font-variant-numeric:tabular-nums">0.00</span></div>
                      <div class="flex justify-between py-1 border-b border-line text-muted"><span>Discount</span><span class="font-variant-numeric:tabular-nums">0.00</span></div>
                      <div class="flex justify-between pt-1.5 font-semibold text-[15px]"><span>Total</span><span class="font-variant-numeric:tabular-nums">₦ 450,000.00</span></div>
                    </div>
                  </div>
"""

with open('quotations.html', 'r') as f:
    content = f.read()

pattern = re.compile(r'                  <div class="hidden md:block p-0 overflow-x-auto">.*?</div>\n                    </div>\n                  </div>', re.DOTALL)
content = pattern.sub(desktop_table_quotation, content)

with open('quotations.html', 'w') as f:
    f.write(content)
