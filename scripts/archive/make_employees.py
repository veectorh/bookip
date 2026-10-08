import re

content = """<!DOCTYPE html>
<html lang="en">
{{> head title="Employees" }}
<body class="bg-canvas text-ink font-sans antialiased selection:bg-indigo-light">
  {{> icons}}

  <div id="app" class="flex h-screen overflow-hidden" data-layout="rail">
    {{> sidebar active_employees=true}}

    <div class="flex-1 flex flex-col min-w-0">
      {{> topbar title="Employees"}}

      <main class="flex-1 overflow-y-auto overflow-x-hidden relative">
        <div id="screens">
          <!-- Content: List -->
          <div id="s-list" class="p-4 md:p-6 pb-24 md:pb-6" data-screen="list">
            
            <div class="flex gap-2 mb-2.5 flex-wrap hidden md:flex">
              <div class="flex-1 min-w-[200px] flex items-center gap-2 h-control px-2.5 bg-surface border border-line-strong rounded text-[13px] focus-within:border-indigo focus-within:ring-[3px] focus-within:ring-indigo-line">
                <svg class="w-4 h-4 stroke-[1.75] text-muted shrink-0" aria-hidden="true"><use href="#i-search"/></svg>
                <input type="text" placeholder="Search employees" class="bg-transparent border-0 outline-none w-full placeholder-muted">
              </div>
              <div class="flex items-center h-control px-2.5 bg-surface border border-line-strong rounded text-[13px] focus-within:border-indigo focus-within:ring-[3px] focus-within:ring-indigo-line">
                <select class="bg-transparent border-0 outline-none w-full"><option>All departments</option></select>
              </div>
              <div class="ml-auto flex gap-2 hidden md:flex">
                <button class="inline-flex items-center gap-1.5 h-control px-3 rounded border border-line-strong text-[13px] font-medium bg-surface hover:bg-th"><svg class="w-4 h-4 stroke-[1.75]" aria-hidden="true"><use href="#i-download"/></svg> Export</button>
                <button class="inline-flex items-center gap-1.5 h-control px-3 rounded border border-transparent text-[13px] font-medium bg-indigo text-white hover:bg-indigo-hover" data-goto="editor"><svg class="w-4 h-4 stroke-[1.75]" aria-hidden="true"><use href="#i-plus"/></svg> New employee</button>
              </div>
            </div>
            
            {{> list-mobile-filters }}

            <!-- Table (Desktop) -->
            <div class="bg-surface border border-line rounded overflow-x-auto hidden md:block">
              <table class="w-full border-collapse text-[13px] min-w-[700px]">
                <thead>
                  <tr class="bg-th text-muted font-medium text-xs">
                    <th class="px-3.5 py-2.5 text-left border-b border-line whitespace-nowrap font-medium">Employee ID</th>
                    <th class="px-3.5 py-2.5 text-left border-b border-line whitespace-nowrap font-medium">Name</th>
                    <th class="px-3.5 py-2.5 text-left border-b border-line whitespace-nowrap font-medium">Department</th>
                    <th class="px-3.5 py-2.5 text-left border-b border-line whitespace-nowrap font-medium">Designation</th>
                    <th class="px-3.5 py-2.5 text-right border-b border-line whitespace-nowrap font-medium font-variant-numeric:tabular-nums">Basic Salary</th>
                    <th class="px-3.5 py-2.5 border-b border-line w-9"></th>
                  </tr>
                </thead>
                <tbody class="[&_tr:last-child_td]:border-b-0">
                  <tr class="hover:bg-[#FAFBFD] group transition-colors cursor-pointer" data-goto="profile">
                    <td class="px-3.5 py-3 border-b border-line whitespace-nowrap font-medium">EMP-001</td>
                    <td class="px-3.5 py-3 border-b border-line whitespace-nowrap flex items-center gap-2">
                       <div class="w-6 h-6 rounded-full bg-indigo/10 text-indigo flex items-center justify-center text-[10px] font-bold">JD</div>
                       John Doe
                    </td>
                    <td class="px-3.5 py-3 border-b border-line whitespace-nowrap">Engineering</td>
                    <td class="px-3.5 py-3 border-b border-line whitespace-nowrap">Senior Developer</td>
                    <td class="px-3.5 py-3 border-b border-line whitespace-nowrap text-right font-medium" style="font-variant-numeric: tabular-nums;">450,000.00</td>
                    <td class="px-3.5 py-3 border-b border-line whitespace-nowrap" onclick="event.stopPropagation()"><button class="w-[26px] h-[26px] rounded flex items-center justify-center text-muted hover:bg-th hover:border-line-strong hover:text-ink border border-transparent"><svg class="w-4 h-4 stroke-[1.75]" aria-hidden="true"><use href="#i-more-horizontal"/></svg></button></td>
                  </tr>
                </tbody>
              </table>
              <div class="flex items-center gap-3 px-3.5 py-2.5 border-t border-line text-xs text-muted bg-surface">
                <span>1 employee</span>
              </div>
            </div>

            <!-- List (Mobile) -->
            <div class="block md:hidden">
              <div class="bg-surface border border-line rounded overflow-hidden">
                <button class="w-full text-left bg-transparent border-0 border-b border-line px-3 py-2.5 flex items-center gap-3 min-h-row-mob last:border-b-0 active:bg-th" data-goto="profile">
                  <div class="w-8 h-8 rounded-full bg-indigo/10 text-indigo flex items-center justify-center text-[12px] font-bold shrink-0">JD</div>
                  <div class="flex-1 min-w-0">
                    <div class="font-medium text-ink truncate">John Doe</div>
                    <div class="text-xs text-muted truncate">EMP-001 · Senior Developer</div>
                  </div>
                  <div class="text-right shrink-0">
                    <div class="font-medium text-ink font-variant-numeric:tabular-nums">450,000.00</div>
                  </div>
                </button>
              </div>
              <div class="sticky bottom-3 flex justify-end mt-3 pointer-events-none">
                <button class="pointer-events-auto inline-flex items-center gap-1.5 h-[44px] px-[18px] rounded-pill border border-transparent text-[13px] font-medium bg-indigo text-white shadow-[0_6px_18px_rgba(67,83,224,0.35)]" data-goto="editor">
                  <svg class="w-4 h-4 stroke-[1.75]" aria-hidden="true"><use href="#i-plus"/></svg> New employee
                </button>
              </div>
            </div>
          </div>

          <!-- Content: Editor -->
          <div id="s-editor" class="hidden p-4 md:p-6 pb-24 md:pb-6" data-screen="editor">
            
            <div class="flex items-center gap-3 mb-4">
              <button class="inline-flex items-center justify-center w-control h-control rounded bg-transparent text-muted hover:bg-th hover:text-ink" data-goto="list"><svg class="w-4 h-4 stroke-[1.75]" aria-hidden="true"><use href="#i-arrow-left"/></svg></button>
              <h1 class="m-0 text-xl font-semibold tracking-tight">New employee</h1>
              <div class="ml-auto flex gap-2 hidden md:flex">
                <button class="inline-flex items-center gap-1.5 h-control px-3 rounded border border-line-strong text-[13px] font-medium bg-surface hover:bg-th" data-goto="list">Cancel</button>
                <button class="inline-flex items-center gap-1.5 h-control px-3 rounded border border-transparent text-[13px] font-medium bg-indigo text-white hover:bg-indigo-hover" data-goto="list"><svg class="w-4 h-4 stroke-[1.75]" aria-hidden="true"><use href="#i-save"/></svg> Save employee</button>
              </div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-[1fr_280px] gap-3.5 items-start">
              
              <!-- Left Panel -->
              <div class="flex flex-col gap-3.5">
                
                <!-- Personal Info -->
                <div class="bg-surface border border-line rounded p-4">
                  <h3 class="text-[13px] font-semibold mb-3 border-b border-line pb-2">Personal Information</h3>
                  <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                    <div>
                      <label class="block text-xs font-medium text-muted mb-1.25">First Name <span class="text-[#B4372A]">*</span></label>
                      <input type="text" class="w-full h-control px-2.5 bg-surface border border-line-strong rounded text-[13px] focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none">
                    </div>
                    <div>
                      <label class="block text-xs font-medium text-muted mb-1.25">Last Name <span class="text-[#B4372A]">*</span></label>
                      <input type="text" class="w-full h-control px-2.5 bg-surface border border-line-strong rounded text-[13px] focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none">
                    </div>
                    <div>
                      <label class="block text-xs font-medium text-muted mb-1.25">Email</label>
                      <input type="email" class="w-full h-control px-2.5 bg-surface border border-line-strong rounded text-[13px] focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none">
                    </div>
                    <div>
                      <label class="block text-xs font-medium text-muted mb-1.25">Phone</label>
                      <input type="tel" class="w-full h-control px-2.5 bg-surface border border-line-strong rounded text-[13px] focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none">
                    </div>
                    <div>
                      <label class="block text-xs font-medium text-muted mb-1.25">Date of Birth</label>
                      <input type="date" class="w-full h-control px-2.5 bg-surface border border-line-strong rounded text-[13px] focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none text-ink">
                    </div>
                    <div>
                      <label class="block text-xs font-medium text-muted mb-1.25">City / State</label>
                      <input type="text" class="w-full h-control px-2.5 bg-surface border border-line-strong rounded text-[13px] focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none">
                    </div>
                  </div>
                </div>

                <!-- Job Info -->
                <div class="bg-surface border border-line rounded p-4">
                  <h3 class="text-[13px] font-semibold mb-3 border-b border-line pb-2">Employment Details</h3>
                  <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                    <div>
                      <label class="block text-xs font-medium text-muted mb-1.25">Employee ID <span class="text-[#B4372A]">*</span></label>
                      <input type="text" class="w-full h-control px-2.5 bg-surface border border-line-strong rounded text-[13px] focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none">
                    </div>
                    <div>
                      <label class="block text-xs font-medium text-muted mb-1.25">Department</label>
                      <select class="w-full h-control px-2 bg-surface border border-line-strong rounded text-[13px] focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none"><option>Select...</option></select>
                    </div>
                    <div>
                      <label class="block text-xs font-medium text-muted mb-1.25">Designation</label>
                      <select class="w-full h-control px-2 bg-surface border border-line-strong rounded text-[13px] focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none"><option>Select...</option></select>
                    </div>
                    <div>
                      <label class="block text-xs font-medium text-muted mb-1.25">Salary Scale</label>
                      <select class="w-full h-control px-2 bg-surface border border-line-strong rounded text-[13px] focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none"><option>Select...</option></select>
                    </div>
                    <div>
                      <label class="block text-xs font-medium text-muted mb-1.25">Joining Date</label>
                      <input type="date" class="w-full h-control px-2.5 bg-surface border border-line-strong rounded text-[13px] focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none text-ink">
                    </div>
                  </div>
                </div>

                <!-- Bank Info -->
                <div class="bg-surface border border-line rounded p-4">
                  <h3 class="text-[13px] font-semibold mb-3 border-b border-line pb-2">Bank Details</h3>
                  <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                    <div>
                      <label class="block text-xs font-medium text-muted mb-1.25">Account Name</label>
                      <input type="text" class="w-full h-control px-2.5 bg-surface border border-line-strong rounded text-[13px] focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none">
                    </div>
                    <div>
                      <label class="block text-xs font-medium text-muted mb-1.25">Account Number</label>
                      <input type="text" class="w-full h-control px-2.5 bg-surface border border-line-strong rounded text-[13px] focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none">
                    </div>
                    <div>
                      <label class="block text-xs font-medium text-muted mb-1.25">Bank Name</label>
                      <input type="text" class="w-full h-control px-2.5 bg-surface border border-line-strong rounded text-[13px] focus:border-indigo focus:ring-[3px] focus:ring-indigo-line outline-none">
                    </div>
                  </div>
                </div>
              </div>

              <!-- Right Panel -->
              <div class="bg-surface border border-line rounded p-3.5 flex flex-col items-center">
                <div class="w-24 h-24 rounded-full border-2 border-dashed border-line-strong flex flex-col items-center justify-center text-muted hover:border-indigo hover:text-indigo cursor-pointer transition-colors mb-3">
                  <svg class="w-6 h-6 stroke-[1.5] mb-1"><use href="#i-user"/></svg>
                  <span class="text-[10px] font-medium">Upload</span>
                </div>
                <p class="text-xs text-muted text-center leading-relaxed">Allowed file types: png, jpg, jpeg.<br>Max size: 2MB</p>
                <hr class="border-0 border-t border-line my-3 w-full">
                <button class="w-full inline-flex items-center justify-center gap-1.5 h-control px-3 rounded border border-transparent text-[13px] font-medium bg-indigo text-white hover:bg-indigo-hover mb-2"><svg class="w-4 h-4 stroke-[1.75]" aria-hidden="true"><use href="#i-save"/></svg> Save employee</button>
                <button class="w-full inline-flex items-center justify-center gap-1.5 h-control px-3 rounded border border-line-strong text-[13px] font-medium bg-surface hover:bg-th" data-goto="list">Cancel</button>
              </div>

            </div>
          </div>

          <!-- Content: Profile (Read-Only) -->
          <div id="s-profile" class="hidden p-4 md:p-6 pb-24 md:pb-6" data-screen="profile">
            <div class="flex items-center gap-3 mb-4">
              <button class="inline-flex items-center justify-center w-control h-control rounded bg-transparent text-muted hover:bg-th hover:text-ink" data-goto="list"><svg class="w-4 h-4 stroke-[1.75]" aria-hidden="true"><use href="#i-arrow-left"/></svg></button>
              <h1 class="m-0 text-xl font-semibold tracking-tight">John Doe</h1>
              <div class="ml-auto flex gap-2">
                <button class="inline-flex items-center gap-1.5 h-control px-3 rounded border border-line-strong text-[13px] font-medium bg-surface hover:bg-th" data-goto="editor"><svg class="w-4 h-4 stroke-[1.75]" aria-hidden="true"><use href="#i-edit-2"/></svg> Edit profile</button>
              </div>
            </div>

            <div class="bg-surface border border-line rounded overflow-hidden">
              <div class="h-24 bg-th"></div>
              <div class="px-6 pb-6 relative">
                <div class="w-20 h-20 rounded-full border-4 border-surface bg-indigo/10 text-indigo flex items-center justify-center text-2xl font-bold -mt-10 mb-3 absolute">JD</div>
                <div class="pt-12">
                  <h2 class="text-xl font-semibold text-ink">John Doe</h2>
                  <p class="text-[13px] text-muted mb-4">Senior Developer • EMP-001</p>
                  
                  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 text-[13px]">
                    <div>
                      <div class="text-xs text-muted mb-1">Department</div>
                      <div class="font-medium">Engineering</div>
                    </div>
                    <div>
                      <div class="text-xs text-muted mb-1">Email</div>
                      <div class="font-medium">john.doe@example.com</div>
                    </div>
                    <div>
                      <div class="text-xs text-muted mb-1">Phone</div>
                      <div class="font-medium">+234 800 000 0000</div>
                    </div>
                    <div>
                      <div class="text-xs text-muted mb-1">Joining Date</div>
                      <div class="font-medium">12 Jan 2024</div>
                    </div>
                    <div>
                      <div class="text-xs text-muted mb-1">Basic Salary</div>
                      <div class="font-medium">₦ 450,000.00</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </main>
    </div>
  </div>

  {{> scripts}}
  
  <script>
    document.querySelectorAll('[data-goto]').forEach(b => {
      b.addEventListener('click', e => {
        // e.preventDefault();
        const target = b.dataset.goto;
        document.getElementById('s-list').classList.toggle('hidden', target !== 'list');
        document.getElementById('s-editor').classList.toggle('hidden', target !== 'editor');
        document.getElementById('s-profile').classList.toggle('hidden', target !== 'profile');
      });
    });
  </script>
</body>
</html>
"""

with open('employees.html', 'w') as f:
    f.write(content)
