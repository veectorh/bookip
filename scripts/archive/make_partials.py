import os

os.makedirs('src/partials', exist_ok=True)

with open('src/partials/editor-item-desktop.html', 'w') as f:
    f.write("""                        <tr>
                          <td class="px-3 border-b border-line h-11"><div class="flex items-center h-7 px-2 bg-surface border border-line-strong rounded text-[13px] focus-within:border-indigo focus-within:ring-[3px] focus-within:ring-indigo-line"><select class="bg-transparent border-0 outline-none w-full"><option>{{name}}</option></select></div></td>
                          <td class="px-3 border-b border-line h-11"><div class="flex items-center h-7 px-2 bg-surface border border-line-strong rounded text-[13px] focus-within:border-indigo focus-within:ring-[3px] focus-within:ring-indigo-line"><select class="bg-transparent border-0 outline-none w-full"><option>{{tax}}</option><option>None</option></select></div></td>
                          <td class="px-3 border-b border-line h-11 text-right font-variant-numeric:tabular-nums"><div class="flex items-center h-7 px-2 bg-surface border border-line-strong rounded text-[13px] focus-within:border-indigo focus-within:ring-[3px] focus-within:ring-indigo-line"><input type="text" class="bg-transparent border-0 outline-none w-full text-right" value="{{qty}}"></div></td>
                          <td class="px-3 border-b border-line h-11 text-right font-variant-numeric:tabular-nums"><div class="flex items-center h-7 px-2 bg-surface border border-line-strong rounded text-[13px] focus-within:border-indigo focus-within:ring-[3px] focus-within:ring-indigo-line"><input type="text" class="bg-transparent border-0 outline-none w-full text-right" value="{{price}}"></div></td>
                          <td class="px-3 border-b border-line h-11 text-right font-variant-numeric:tabular-nums">{{amount}}</td>
                          <td class="px-3 border-b border-line h-11"><button class="w-[26px] h-[26px] rounded flex items-center justify-center text-muted hover:bg-th hover:border-line-strong hover:text-ink border border-transparent"><svg class="w-4 h-4 stroke-[1.75]" aria-hidden="true"><use href="#i-trash-2"/></svg></button></td>
                        </tr>""")

with open('src/partials/editor-item-mobile.html', 'w') as f:
    f.write("""                    <div class="flex flex-col border border-line-strong rounded p-3 bg-canvas">
                      <div class="flex items-start justify-between">
                        <div>
                          <div class="font-medium text-ink">{{name}}</div>
                          <div class="text-xs text-muted mt-0.5">{{qty}} x {{price}} • {{tax}}</div>
                        </div>
                        <div class="text-right">
                          <div class="font-medium font-variant-numeric:tabular-nums text-ink">{{amount}}</div>
                          <button class="mt-2 text-muted hover:text-[#B4372A]"><svg class="w-4 h-4 stroke-[1.75] ml-auto"><use href="#i-trash-2"/></svg></button>
                        </div>
                      </div>
                    </div>""")
