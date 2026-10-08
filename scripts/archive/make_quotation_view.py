import re

with open('quotations.html', 'r') as f:
    content = f.read()

view_screen = """
          <!-- Content: View (Read-Only) -->
          <div id="s-view" class="hidden flex-col h-full absolute inset-0" data-screen="view">
            <div class="flex items-center gap-3 p-4 md:px-6 shrink-0 bg-canvas border-b border-line">
              <button class="inline-flex items-center justify-center w-control h-control rounded bg-transparent text-muted hover:bg-th hover:text-ink" data-goto="list"><svg class="w-4 h-4 stroke-[1.75]" aria-hidden="true"><use href="#i-arrow-left"/></svg></button>
              <h1 class="m-0 text-lg font-semibold tracking-tight">QUO-0011</h1>
              <span class="inline-flex items-center gap-1.5 h-[22px] px-2 rounded-[3px] text-xs font-medium whitespace-nowrap bg-status-draft-bg text-status-draft-text border border-status-draft-border before:content-[''] before:w-1.5 before:h-1.5 before:rounded-full before:bg-status-draft-dot before:shrink-0">Draft</span>
              
              <div class="ml-auto flex gap-2">
                <button class="inline-flex items-center gap-1.5 h-control px-3 rounded border border-line-strong text-[13px] font-medium bg-surface hover:bg-th" data-goto="editor"><svg class="w-4 h-4 stroke-[1.75]" aria-hidden="true"><use href="#i-edit-2"/></svg> Edit</button>
                <button class="inline-flex items-center gap-1.5 h-control px-3 rounded border border-transparent text-[13px] font-medium bg-indigo text-white hover:bg-indigo-hover hidden md:inline-flex"><svg class="w-4 h-4 stroke-[1.75]" aria-hidden="true"><use href="#i-send"/></svg> Send to customer</button>
                <button class="inline-flex items-center justify-center w-control h-control rounded border border-line-strong text-muted bg-surface hover:bg-th hover:text-ink"><svg class="w-4 h-4 stroke-[1.75]" aria-hidden="true"><use href="#i-more-horizontal"/></svg></button>
              </div>
            </div>
            
            <div class="flex-1 overflow-auto p-4 md:p-8 bg-[#FAFBFD] flex justify-center">
              <!-- A4 Document -->
              <div class="w-full max-w-[800px] bg-white border border-line shadow-sm rounded-lg p-8 md:p-12 text-[13px] text-ink flex flex-col gap-10 shrink-0 h-max">
                
                <!-- Header -->
                <div class="flex justify-between items-start">
                  <div>
                    <h2 class="text-3xl font-bold text-ink tracking-tight mb-2">QUOTATION</h2>
                    <div class="text-muted">QUO-0011</div>
                  </div>
                  <div class="text-right">
                    <div class="font-bold text-lg text-ink mb-1">Your Company Ltd</div>
                    <div class="text-muted text-[13px] leading-relaxed">
                      123 Business Avenue<br>
                      Lagos, Nigeria<br>
                      contact@yourcompany.com
                    </div>
                  </div>
                </div>

                <!-- Meta & Customer -->
                <div class="flex justify-between items-start border-t border-b border-line py-6">
                  <div class="flex gap-12">
                    <div>
                      <div class="text-[11px] font-bold text-muted uppercase tracking-wider mb-1">Quotation Date</div>
                      <div class="font-medium">10 Jul 2026</div>
                    </div>
                    <div>
                      <div class="text-[11px] font-bold text-muted uppercase tracking-wider mb-1">Valid Until</div>
                      <div class="font-medium">10 Aug 2026</div>
                    </div>
                  </div>
                  <div class="text-right max-w-[250px]">
                    <div class="text-[11px] font-bold text-muted uppercase tracking-wider mb-1">Quoted To</div>
                    <div class="font-bold text-[14px] text-ink mb-0.5">Charles Business LLC</div>
                    <div class="text-muted text-[13px] leading-relaxed">
                      charles@example.com<br>
                      +234 800 123 4567
                    </div>
                  </div>
                </div>

                <!-- Items Table -->
                <div>
                  <table class="w-full border-collapse">
                    <thead>
                      <tr class="border-b border-line">
                        <th class="py-3 text-left font-bold text-[11px] text-muted uppercase tracking-wider w-[50%]">Item Description</th>
                        <th class="py-3 text-right font-bold text-[11px] text-muted uppercase tracking-wider">Qty</th>
                        <th class="py-3 text-right font-bold text-[11px] text-muted uppercase tracking-wider">Price</th>
                        <th class="py-3 text-right font-bold text-[11px] text-muted uppercase tracking-wider">Amount</th>
                      </tr>
                    </thead>
                    <tbody class="[&_tr]:border-b [&_tr]:border-line-light">
                      <tr>
                        <td class="py-4">
                          <div class="font-medium text-ink mb-0.5">Design services</div>
                        </td>
                        <td class="py-4 text-right">1</td>
                        <td class="py-4 text-right font-variant-numeric:tabular-nums">450,000.00</td>
                        <td class="py-4 text-right font-medium font-variant-numeric:tabular-nums">450,000.00</td>
                      </tr>
                    </tbody>
                  </table>

                  <!-- Totals -->
                  <div class="flex justify-end mt-4">
                    <div class="w-full max-w-[280px]">
                      <div class="flex justify-between py-2 text-muted">
                        <span>Subtotal</span>
                        <span class="font-variant-numeric:tabular-nums">450,000.00</span>
                      </div>
                      <div class="flex justify-between py-2 text-muted">
                        <span>Tax</span>
                        <span class="font-variant-numeric:tabular-nums">0.00</span>
                      </div>
                      <div class="flex justify-between py-2 text-muted">
                        <span>Discount</span>
                        <span class="font-variant-numeric:tabular-nums">0.00</span>
                      </div>
                      <div class="flex justify-between py-3 mt-1 border-t border-line text-[16px] font-bold text-ink">
                        <span>Total</span>
                        <span class="font-variant-numeric:tabular-nums">₦ 450,000.00</span>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Footer & Notes -->
                <div class="mt-8 pt-8 border-t border-line text-muted">
                  <div class="mb-4">
                    <div class="font-medium text-ink text-xs mb-1">Notes</div>
                    <p>Prices are valid for 30 days.</p>
                  </div>
                </div>

              </div>
            </div>
          </div>
"""

content = content.replace('        </div>\n      </main>', view_screen + '\n        </div>\n      </main>')
content = content.replace("document.getElementById('s-editor').classList.toggle('hidden', target !== 'editor');", "document.getElementById('s-editor').classList.toggle('hidden', target !== 'editor');\n        const v = document.getElementById('s-view'); if(v) v.classList.toggle('hidden', target !== 'view');")
content = content.replace('class="hover:bg-[#FAFBFD] group transition-colors cursor-pointer" data-goto="editor"', 'class="hover:bg-[#FAFBFD] group transition-colors cursor-pointer" data-goto="view"')
content = content.replace('active:bg-th" data-goto="editor"', 'active:bg-th" data-goto="view"')

with open('quotations.html', 'w') as f:
    f.write(content)
